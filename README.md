# Hitchhikers Guide to OBS services

## Overview

1. [Create a new service locally](#create_service)
   1. [Required Files](#1.1-Required-Files)
   2. [Testing xml file](#test_xml_file)
   3. [Testing service via osc](#test_via_osc)
2. [Prepare for OBS-Appliance](#prepare_obs_appliance)
   1. [Create a new rpm package for your service](#create_testing_vm)
      1. [Kanku](#create_testing_vm_kanku)
      2. [Other](#create_testing_vm_other)
   2. [Test service in a obs-server Appliance](#)
3. [Prepare service container](#prepare_service_container)
   1. [Branch obs-source-service-podman](#branch_service_container)
   2. [Add service](#add_service_to_container)
   3. [Test your service running in the container](#test_service_container)
4. [Deployment on https://build.opensuse.org](#deployment_oo)
   1. [Create a audit bug in bugzilla.opensuse.org](#create_audit_bug)
   2. [Create "Submit Request" to OBS:Server:Unstable](#create_sr)


All the osc commands can be done via the WebUI - 
but using cli commands makes documentation so much easier ;-).

Before you create a rpm package for your service you may want to branch the container,
this create a repo named `home:<username>:branches:OBS:Server:Unstable` if it 
not already exists.

In this OBS project you can easily create your new package (e.g. `obs-service-example`).


## <a name=create_service>1. Create a new service locally</a>

You should create a new public git repository (preferable in https://github.com/openSUSE)


### 1.1 Required Files


Each service contains at least 2 files:

* A executable file which will be executed (e.g. example)
  * An option `--outdir` is required
* A xml service description (`<script_name>.service`)


### <a name=test_xml_file>1.2 Test your xml file</a>


```
xmllint --relaxng service.rng example.service
```


### <a name=test_via_osc>1.3 Test service via osc</a>

If you create a test package including a `_service` to run this service, you can easily 
test while development.


## <a name=prepare_obs_appliance>2. Prepare OBS-Appliance</a>

### <a name=create_testing_vm>2.1 Create you own testing VM</a>

#### <a name=create_testing_vm_kanku>2.1.1 Kanku</a>

```
git clone https://github.com/openSUSE/open-build-service/
cd open-build-service
kanku up
```


#### <a name=create_testing_vm_other>2.1.2 Other virtualization solutions</a>

Choose the image for your preferred virtualization solution at [openbuildservice.org](https://openbuildservice.org/download/other/)
and create your own running OBS instance.


## <a name=prepare_service_container>3. Prepare service container</a>

### <a name=branch_service_container>3.1 Branch [obs-source-service-podman](https://build.opensuse.org/package/show/OBS:Server:Unstable/obs-source-service-podman)</a>


```
osc branch OBS:Server:Unstable/obs-source-service-podman
```

### <a name=add_service_to_container>3.2 Add your service to the branched container</a>

You need to add a `<package name="obs-service-example"/>` entry to the kiwi file


### <a name=test_service_container>3.3 Test your service running in the container</a>

FIXME: explain how to trigger service run


### 3.4 Network access for containers

The default is to run services without network access. If your new service needs
network access you need to enhance the [call-service-in-container](https://github.com/openSUSE/open-build-service/blob/master/src/backend/call-service-in-container#L72)
(The line number may change in future, search for `WITH_NET="1"`).

To get it into production systems please open an issue 
(containing a link to the bugzilla audit request) and a pull request in the [open-build-service github repository](https://github.com/openSUSE/open-build-service/)


## <a name=deployment_oo>4. Deployment on https://build.opensuse.org</a>


### <a name=create_audit_bug>4.1 Create a audit bug in bugzilla.opensuse.org</a>

To run your service on https://build.opensuse.org a security audit has to be done
by the SUSE security team. You can simply open an audit request on 
https://bugzilla.opensuse.org. 


### <a name=create_sr>4.2 Create "Submit Request" to OBS:Server:Unstable</a>

Once your audit bug gets closed (successfully) you can create a submit request
for your new service package and the container to
[OBS:Server:Unstable](https://build.opensuse.org/project/show/OBS:Server:Unstable)
