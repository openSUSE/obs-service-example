# Hitchhikers Guide to OBS services

## Required Files

Each service contains at least 2 files:

* A executable file which will be executed (e.g. example)
  * An option `--outdir` is required
* A xml service description (`<script_name>.service`)

## Test your xml file

### XMLlint


```
xmllint --relaxng service.rng example.service
```


## Production systems

On production systems (like https://build.opensuse.org) we recommend to run your
services in containers. `obs-service` therefore uses the script configured in 
`BS_Config.pm` as `our $service_wrapper = ...;`.

To run your service on https://build.opensuse.org a security audit has to be done
by the SUSE security team. You can simply open an audit request on 
https://bugzilla.opensuse.org.


### Network access in production

The default is to run services without network access. If your new service needs
network access you need to enhance the [call-service-in-container](https://github.com/openSUSE/open-build-service/blob/master/src/backend/call-service-in-container#L72)
(The line number may change in future, search for `WITH_NET="1"`).

To get it into production systems please open an issue 
(containing a link to the bugzilla audit request) and a pull request in the [open-build-service github repository](https://github.com/openSUSE/open-build-service/)
