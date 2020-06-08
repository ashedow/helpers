# Dockerfile for run ansible-vault 

Create image 
```bash
docker build -t ansible-vault .
```

Example encrypt the secret file:
```sh
docker run -rm ansible-vault encrypt <path_to_secret>
Vault password:
Decryption successful
```

Example decrypt the secret file:
```sh
docker run -rm ansible-vault decrypt <path_to_secret>
```



decrypt /home/ya/bekitzur/zypmedia/devops/helm/envs/dev/deployments.yaml