project_name: test-task
version: "1.0"

services:  # list of services like web, database, cach etc
    redis: # service name
        image: redis  # image name for service
        restart: always  # always
        command: redis-server /usr/local/etc/redis/redis.conf --appendonly yes
        networks:
          - app-network
        volumes:
          - redis-data:/data
          - /opt/redis/conf/redis.conf:/usr/local/etc/redis/redis.conf
        deploy:
          mode: replicated
          replicas: 1

    postgres:
        container_name: postgres
        image: "postgres:12.2"
        volumes:
            - postgres-data:/var/lib/postgresql/data
            - /opt/postgres/conf/postgres.conf:/etc/postgresql/postgresql.conf
        environment:
            POSTGRES_PASSWORD_FILE: /run/secrets/pwd-root
            PGDATA: /var/lib/postgresql/data
         deploy:
            mode: replicated
            replicas: 1
        restart: always
        environment:
            DB_ROOT_PASSWORD: "${DB_ROOT_PASSWORD}"
            DB_NAME: "${DB_NAME}"
            DB_USER: "${DB_USER}"
            DB_PASSWORD: "${DB_PASSWORD}"
        networks:
            - app-network
        ports:
            - "5432:5432"
        command: -c 'config_file=/etc/postgresql/postgresql.conf'

    wordpress:
        depends_on:
            - postgres
            - redis
        image: wordpress:5.1.1-fpm-alpine
        container_name: wordpress
        ports:
            - "8000:80"
        restart: always
        links:
            - redis
        environment:
            WORDPRESS_DB_HOST: postgres:5439
            DB_USER: "${DB_USER}"
            DB_NAME: "${DB_NAME}"
            DB_PASSWORD: "${DB_PASSWORD}"
            WP_TABLE_PREFIX: wp_
        volumes:
            - wordpress:/var/www/html
        networks:
            - app-network
        healthcheck:
            test: ["CMD", "php-fpm", "-f"]
            interval: 3m
    nginx:
        depends_on:
            wordpress:
                condition: service_healthy
        image: "nginx:1.16"
        container_name: "${PROJECT_NAME}_nginx"
        environment:
            NGINX_STATIC_OPEN_FILE_CACHE: "off"
            NGINX_ERROR_LOG_LEVEL: info
            NGINX_BACKEND_HOST: wordpress
            NGINX_VHOST_PRESET: wordpress
        ports:
            - 80:80
            - 443:443
        restart: always
        volumes:
            - wordpress:/var/www/html
            - ./nginx-conf:/etc/nginx/conf.d
            - certbot-etc:/etc/letsencrypt
        networks:
            - app-network
        labels:
            - "traefik.http.routers.${PROJECT_NAME}_nginx.rule=Host(`${PROJECT_BASE_URL}`)"

    traefik:
        image: traefik:v2.0
        container_name: "${PROJECT_NAME}_traefik"
        command: --api.insecure=true --providers.docker
        ports:
            - 80:80
            - 443:443
        volumes:
            - /var/run/docker.sock:/var/run/docker.sock
        restart: always
        networks:
            - app-network
        labels:
            - traefik.frontend.rule=Host:traefik.${DOMAIN}
            - traefik.port=8008
            - traefik.acme.domains=traefik.${DOMAIN}
        volumes:
            - /var/run/docker.sock:/var/run/docker.sock:ro  
            - ./traefik.toml:/traefik.toml
            - ./acme.json:/acme.json
            - traefik-tmp-data:/tmp

    certbot:
        depends_on:
            - nginx
        image: certbot/certbot
        container_name: certbot
        volumes:
            - certbot-etc:/etc/letsencrypt
            - wordpress:/var/www/html
        command: certonly --webroot --webroot-path=/var/www/html --email sammy@example.com --agree-tos --no-eff-email --staging -d example.com -d www.example.com
            
volumes:
    certbot-etc:
    wordpress:
    postgres-data:
    redis-data:
    traefik-tmp-data:
    
networks:
    app-network:
    driver: bridge  
