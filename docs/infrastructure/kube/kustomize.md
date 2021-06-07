# Kustomize

Kustomize is an open-source configuration management tool developed to help address these concerns.
**Kustomize** is a *standalone tool* to *customize Kubernetes objects* through a kustomization *file*.

Since 1.14, Kubectl also supports the management of Kubernetes objects using a kustomization file. To view Resources found in a directory containing a kustomization file, run the following command:
```bash
kubectl kustomize <kustomization_directory>
```
To apply those Resources, run kubectl apply with `--kustomize` or `-k` flag:
```bash
kubectl apply -k <kustomization_directory>
```


It has the following features to manage application configuration files:
* [generating resources](##Generating-Resources) from other sources
* [setting cross-cutting fields](##setting-cross-cutting-fields) for resources
* [composing and customizing collections of resources](##Composing-and-Customizing-Resources)


## Generating Resources

ConfigMaps and Secrets hold configuration or sensitive data that are used by other Kubernetes objects, such as Pods. 
The source of truth of ConfigMaps or Secrets are usually external to a cluster, such as a `.properties` file or an SSH keyfile. 
Kustomize has secretGenerator and configMapGenerator, which generate Secret and ConfigMap from files or literals.

## Setting cross-cutting fields

It is quite common to set cross-cutting fields for all Kubernetes resources in a project. Some use cases for setting cross-cutting fields:
* setting the same namespace for all Resources
* adding the same name prefix or suffix
* adding the same set of labels
* adding the same set of annotations

Run `kubectl kustomize ./` to view those fields are all set in the Deployment Resource:

## Composing and Customizing Resources 

It is common to *compose a set of Resources* in a project and *manage them inside the same file or directory*. 
Kustomize offers composing Resources from different files and applying patches or other customization to them.

### Composing 
Kustomize supports composition of different resources. The resources field, in the `kustomization.yaml` file, defines the list of resources to include in a configuration. Set the path to a resource's configuration file in the resources list.

The Resources from `kubectl kustomize ./` contain both the Deployment and the Service objects.

### Customizing

Patches can be used to apply different customizations to Resources. 
Kustomize supports different patching mechanisms through `patchesStrategicMerge` and `patchesJson6902`. 
`patchesStrategicMerge` is a list of file paths. Each file should be resolved to a strategic merge patch. The names inside the patches must match Resource names that are already loaded. Small patches that do one thing are recommended. For example, create one patch for increasing the deployment replica number and another patch for setting the memory limit.

Not all Resources or fields support strategic merge patches. To support modifying arbitrary fields in arbitrary Resources, Kustomize offers applying JSON patch through `patchesJson6902`. To find the correct Resource for a Json patch, the group, version, kind and name of that Resource need to be specified in `kustomization.yaml`. For example, increasing the replica number of a Deployment object can also be done through `patchesJson6902`.





## Links

> https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/

> https://www.digitalocean.com/community/tutorials/how-to-manage-your-kubernetes-configurations-with-kustomize