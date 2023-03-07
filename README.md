# Hitchhikers Guide to OBS services

## Preamble

All the osc commands can be done via the WebUI -
but using cli commands makes documentation so much easier ;-).

**TIP:**
Before you create a rpm package for your service you may want to branch the container,
this create a repo named `home:<username>:branches:OBS:Server:Unstable` if it
not already exists.

In this OBS project you can easily create your new package (e.g. `obs-service-example`)
and include it later on in your own services container.


## 1. Create a new service locally

You should create a new public git repository (preferable in https://github.com/openSUSE)


### 1.1 Required Files


Each service contains at least 2 files:

* A executable file which will be executed (e.g. example)
  * An option `--outdir` is required
* A xml service description (`<script_name>.service`)


### 1.2 Test your xml file


```
xmllint --relaxng service.rng example.service
```


### 1.3 Test service via osc

If you create a test package including a `_service` to run this service, you can easily
test while development.


## 2. Prepare OBS-Appliance

### 2.1 Create you own testing VM

#### 2.1.1 Kanku

```
git clone https://github.com/openSUSE/open-build-service/
cd open-build-service
kanku up
```


#### 2.1.2 Other virtualization solutions

Choose the image for your preferred virtualization solution at [openbuildservice.org](https://openbuildservice.org/download/other/)
and create your own running OBS instance.


## 3. Prepare service container

### 3.1 Branch [obs-source-service-podman](https://build.opensuse.org/package/show/OBS:Server:Unstable/obs-source-service-podman)


```
osc branch OBS:Server:Unstable/obs-source-service-podman
```

### 3.2 Add your service to the branched container

You need to add a `<package name="obs-service-example"/>` entry to the kiwi file


### 3.3 Test your service running in the container

* Create a new test package with a `_service` file containing your `example` service.
* Commit it to your test OBS instance
* Run `osc service rr` to trigger the service


### 3.4 Network access for containers

The default is to run services without network access. If your new service needs
network access you need to enhance the [call-service-in-container](https://github.com/openSUSE/open-build-service/blob/master/src/backend/call-service-in-container#L72)
(The line number may change in future, search for `WITH_NET="1"`).

To get it into production systems please open an issue
(containing a link to the bugzilla audit request) and a pull request in the [open-build-service github repository](https://github.com/openSUSE/open-build-service/)


## 4. Deployment on https://build.opensuse.org

You can't deploy service on [build.opensuse.org](https://build.opensuse.org) by yourself,
but you can start a review process by doing the following:


### 4.1 Create a audit bug in bugzilla.opensuse.org

To run your service on https://build.opensuse.org a security audit has to be done
by the SUSE security team. You can simply open an audit request on
https://bugzilla.opensuse.org.


### 4.2 Create "Submit Request" to OBS:Server:Unstable

Once your audit bug gets closed (successfully) you can create a submit request
for your new service package and the container to
[OBS:Server:Unstable](https://build.opensuse.org/project/show/OBS:Server:Unstable)
