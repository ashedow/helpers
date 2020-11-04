# Vault

> Vault is a complex system that has many different pieces. To help both users and developers of Vault build a mental model of how it works, this page documents the system architecture.

> Vault is a service to manage secrets. It provides an API that gives access to secrets based on policies. Any user of the API needs to authenticate and only sees the secrets for which he is authorized. Vault encrypts data using 256-bit AES with GCM. It can store data in various backends (files, Amazon DynamoDB, Consul, etcd and much more). The other key aspect is that Vault never stores a key in a persistent location. Starting/restarting Vault always requires one or more operators to unseal Vault. However let’s start with the basics first.

## Glossary:

* Storage Backend - A storage backend is responsible for durable storage of encrypted data. Backends are not trusted by Vault and are only expected to provide durability. The storage backend is configured when starting the Vault server.

* Barrier - The barrier is cryptographic steel and concrete around the Vault. All data that flows between Vault and the storage backend passes through the barrier. The barrier ensures that only encrypted data is written out, and that data is verified and decrypted on the way in. Much like a bank vault, the barrier must be "unsealed" before anything inside can be accessed.

* Secrets Engine - A secrets engine is responsible for managing secrets. Simple secrets engines like the "kv" secrets engine simply return the same secret when queried. Some secrets engines support using policies to dynamically generate a secret each time they are queried. This allows for unique secrets to be used which allows Vault to do fine-grained revocation and policy updates. As an example, a MySQL secrets engine could be configured with a "web" policy. When the "web" secret is read, a new MySQL user/password pair will be generated with a limited set of privileges for the web server.

* Audit Device - An audit device is responsible for managing audit logs. Every request to Vault and response from Vault goes through the configured audit devices. This provides a simple way to integrate Vault with multiple audit logging destinations of different types.

* Auth Method - An auth method is used to authenticate users or applications which are connecting to Vault. Once authenticated, the auth method returns the list of applicable policies which should be applied. Vault takes an authenticated user and returns a client token that can be used for future requests. As an example, the userpass auth method uses a username and password to authenticate the user. Alternatively, the github auth method allows users to authenticate via GitHub.

* Client Token - A client token (aka "Vault Token") is conceptually similar to a session cookie on a web site. Once a user authenticates, Vault returns a client token which is used for future requests. The token is used by Vault to verify the identity of the client and to enforce the applicable ACL policies. This token is passed via HTTP headers.

* Secret - A secret is the term for anything returned by Vault which contains confidential or cryptographic material. Not everything returned by Vault is a secret, for example system configuration, status information, or policies are not considered secrets. Secrets always have an associated lease. This means clients cannot assume that the secret contents can be used indefinitely. Vault will revoke a secret at the end of the lease, and an operator may intervene to revoke the secret before the lease is over. This contract between Vault and its clients is critical, as it allows for changes in keys and policies without manual intervention.

* Server - Vault depends on a long-running instance which operates as a server. The Vault server provides an API which clients interact with and manages the interaction between all the secrets engines, ACL enforcement, and secret lease revocation. Having a server based architecture decouples clients from the security keys and policies, enables centralized audit logging and simplifies administration for operators.

## Overview

![](./vault_layers.png)

Once started, the Vault is in a sealed state. Before any operation can be performed on the Vault it must be unsealed. This is done by providing the unseal keys. When the Vault is initialized it generates an encryption key which is used to protect all the data. That key is protected by a master key. By default, Vault uses a technique known as [Shamir's secret sharing algorithm](https://en.wikipedia.org/wiki/Shamir's_Secret_Sharing) to split the master key into 5 shares, any 3 of which are required to reconstruct the master key.

![](vault-shamir-secret-sharing.svg)

When a client first connects to Vault, it needs to authenticate. Vault provides configurable auth methods providing flexibility in the authentication mechanism used. Human friendly mechanisms such as username/password or GitHub might be used for operators, while applications may use public/private keys or tokens to authenticate. An authentication request flows through core and into an auth method, which determines if the request is valid and returns a list of associated policies.

## Links 

https://www.vaultproject.io/
https://spring.io/blog/2016/06/24/managing-secrets-with-vault - owerview and start configurtion
https://www.hashicorp.com/resources/adopting-hashicorp-vault