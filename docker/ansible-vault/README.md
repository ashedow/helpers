# Dockerfile for run ansible-vault 

Example encrypt the secret file:
```sh
docker run -rm ashedow/ansible-vault encrypt <path_to_secret>
Vault password:
Decryption successful
```

Example decrypt the secret file:
```sh
docker run -rm ashedow/ansible-vault decrypt <path_to_secret>
```