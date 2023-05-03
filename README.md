# glesys

A Python library to interact with the [Glesys.com API](https://github.com/glesys/API) endpoints.<br>
It's also a CLI tool to access a subset of all those features as well as housing a LetsEncrypt  [certbot](https://github.com/certbot/certbot) Authenticator plugin.

*Small Disclaimer: I have no affiliation with Glesys, I just appreciate their API and services*

# Installation

```
$ pip install glesys
```

# Usage

:information_source: This assumes a valid `glesys.toml` configuration.

## List all domains

```
$ glesys dns --all-domains
```

## List all records for hvornum.se

```
$ glesys dns --all-records hvornum.se
```

## LetsEncrypt challenge

:warning: This assumes you have installed this library locally on the machine before running the `certbot` utility. This is because `certbot` will use plugin-discovery via [Entry points for plugins](https://setuptools.pypa.io/en/latest/userguide/entry_point.html#entry-points-for-plugins). This also requires a valid `glesys.toml`.

### Single certificate for all domains

```
$ sudo glesys lets-encrypt --all-domains
```

This will generate certificates for all domains hosted under the Glesys DNS server. This would be eqivilant of running certbot manually for `hvornum.se` and `archlinux.life`:

```
certbot -v certonly --non-interactive --authenticator dns-glesys --preferred-challenges dns --dry-run --server https://acme-staging-v02.api.letsencrypt.org/directory --work-dir /home/anton/github/python-glesys/certbot --logs-dir /home/anton/github/python-glesys/certbot --config-dir /home/anton/github/python-glesys/certbot --text --agree-tos --email anton@hvornum.se --expand --renew-by-default -d '*.hvornum.se,hvornum.se,*.archlinux.life,archlinux.life'
```

By default it will run against LetsEncrypt staging environment. Use `--production` to target `glesys lets-encrypt` against the production endpoint of LetsEncrypt and to remove the dryrun.

### Separate certificate for all domains

TBD!

```
$ sudo glesys lets-encrypt --all-domains --individual
```

### Separate certificate for selected domains

TBD!

```
$ sudo glesys lets-encrypt --individual --hostname '*.hvornum.se' --hostname 'hvornum.se'
```

# Supported API Endpoints

As of 2023-05-03 [API Doc Spec](https://github.com/GleSYS/API/wiki/API-Documentation).

 * [x] https://api.glesys.com/server/list
 * [x] https://api.glesys.com/server/details
 * [x] https://api.glesys.com/server/networkadapters
 * [ ] https://api.glesys.com/server/backup
 * [ ] https://api.glesys.com/server/status
 * [ ] https://api.glesys.com/server/reboot
 * [ ] https://api.glesys.com/server/reset
 * [ ] https://api.glesys.com/server/stop
 * [ ] https://api.glesys.com/server/start
 * [ ] https://api.glesys.com/server/create
 * [ ] https://api.glesys.com/server/createfrombackup
 * [ ] https://api.glesys.com/server/createmanualbackup
 * [ ] https://api.glesys.com/server/deletemanualbackup
 * [ ] https://api.glesys.com/server/destroy
 * [ ] https://api.glesys.com/server/edit
 * [ ] https://api.glesys.com/server/clone
 * [x] https://api.glesys.com/server/limits
 * [ ] https://api.glesys.com/server/resetlimit
 * [ ] https://api.glesys.com/server/listbackups
 * [ ] https://api.glesys.com/server/console
 * [ ] https://api.glesys.com/server/resetpassword
 * [ ] https://api.glesys.com/server/templates
 * [ ] https://api.glesys.com/server/allowedarguments
 * [ ] https://api.glesys.com/server/resourceusage
 * [x] https://api.glesys.com/server/costs
 * [ ] https://api.glesys.com/server/listiso
 * [ ] https://api.glesys.com/server/mountiso
 * [ ] https://api.glesys.com/server/estimatedcost
 * [ ] https://api.glesys.com/server/previewcloudconfig
 * [x] https://api.glesys.com/ip/listfree
 * [ ] https://api.glesys.com/ip/listown
 * [ ] https://api.glesys.com/ip/details
 * [ ] https://api.glesys.com/ip/take
 * [ ] https://api.glesys.com/ip/release
 * [ ] https://api.glesys.com/ip/add
 * [ ] https://api.glesys.com/ip/remove
 * [ ] https://api.glesys.com/ip/setptr
 * [ ] https://api.glesys.com/ip/resetptr
 * [x] https://api.glesys.com/domain/list
 * [ ] https://api.glesys.com/domain/add
 * [ ] https://api.glesys.com/domain/register
 * [ ] https://api.glesys.com/domain/transfer
 * [ ] https://api.glesys.com/domain/renew
 * [ ] https://api.glesys.com/domain/setautorenew
 * [ ] https://api.glesys.com/domain/details
 * [ ] https://api.glesys.com/domain/export
 * [ ] https://api.glesys.com/domain/available
 * [ ] https://api.glesys.com/domain/pricelist
 * [ ] https://api.glesys.com/domain/edit
 * [ ] https://api.glesys.com/domain/delete
 * [ ] https://api.glesys.com/domain/updaterecord
 * [ ] https://api.glesys.com/domain/listrecords
 * [x] https://api.glesys.com/domain/addrecord
 * [x] https://api.glesys.com/domain/deleterecord
 * [ ] https://api.glesys.com/domain/allowedarguments
 * [ ] https://api.glesys.com/domain/changenameservers
 * [ ] https://api.glesys.com/domain/legacywebhosting
 * [ ] https://api.glesys.com/archive/details
 * [ ] https://api.glesys.com/archive/delete
 * [ ] https://api.glesys.com/archive/list
 * [ ] https://api.glesys.com/archive/create
 * [ ] https://api.glesys.com/archive/changepassword
 * [ ] https://api.glesys.com/archive/resize
 * [ ] https://api.glesys.com/archive/changedescription
 * [ ] https://api.glesys.com/archive/allowedarguments
 * [ ] https://api.glesys.com/email/overview
 * [ ] https://api.glesys.com/email/list
 * [ ] https://api.glesys.com/email/editaccount
 * [ ] https://api.glesys.com/email/delete
 * [ ] https://api.glesys.com/email/createaccount
 * [ ] https://api.glesys.com/email/quota
 * [ ] https://api.glesys.com/email/createalias
 * [ ] https://api.glesys.com/email/editalias
 * [ ] https://api.glesys.com/email/costs
 * [ ] https://api.glesys.com/email/resetpassword
 * [ ] https://api.glesys.com/invoice/list
 * [ ] https://api.glesys.com/invoice/next
 * [ ] https://api.glesys.com/invoice/paybypaypal
 * [ ] https://api.glesys.com/country/list
 * [ ] https://api.glesys.com/customer/settings
 * [ ] https://api.glesys.com/customer/listcollaborators
 * [ ] https://api.glesys.com/customer/listprojects
 * [ ] https://api.glesys.com/customer/editcollaborator
 * [ ] https://api.glesys.com/customer/removecollaborator
 * [ ] https://api.glesys.com/customer/createproject
 * [ ] https://api.glesys.com/account/info
 * [ ] https://api.glesys.com/paymentcard/add
 * [ ] https://api.glesys.com/vpn/listusers
 * [ ] https://api.glesys.com/vpn/createuser
 * [ ] https://api.glesys.com/vpn/deleteuser
 * [ ] https://api.glesys.com/vpn/edituser
 * [ ] https://api.glesys.com/loadbalancer/list
 * [ ] https://api.glesys.com/loadbalancer/details
 * [ ] https://api.glesys.com/loadbalancer/create
 * [ ] https://api.glesys.com/loadbalancer/edit
 * [ ] https://api.glesys.com/loadbalancer/destroy
 * [ ] https://api.glesys.com/loadbalancer/addfrontend
 * [ ] https://api.glesys.com/loadbalancer/editfrontend
 * [ ] https://api.glesys.com/loadbalancer/removefrontend
 * [ ] https://api.glesys.com/loadbalancer/addbackend
 * [ ] https://api.glesys.com/loadbalancer/editbackend
 * [ ] https://api.glesys.com/loadbalancer/removebackend
 * [ ] https://api.glesys.com/loadbalancer/addtarget
 * [ ] https://api.glesys.com/loadbalancer/edittarget
 * [ ] https://api.glesys.com/loadbalancer/enabletarget
 * [ ] https://api.glesys.com/loadbalancer/disabletarget
 * [ ] https://api.glesys.com/loadbalancer/removetarget
 * [ ] https://api.glesys.com/loadbalancer/addcertificate
 * [ ] https://api.glesys.com/loadbalancer/listcertificate
 * [ ] https://api.glesys.com/loadbalancer/removecertificate
 * [ ] https://api.glesys.com/loadbalancer/errors
 * [ ] https://api.glesys.com/loadbalancer/addtoblocklist
 * [ ] https://api.glesys.com/loadbalancer/removefromblocklist
 * [ ] https://api.glesys.com/user/createorganization
 * [ ] https://api.glesys.com/user/details
 * [ ] https://api.glesys.com/user/edit
 * [ ] https://api.glesys.com/user/login
 * [ ] https://api.glesys.com/user/logout
 * [ ] https://api.glesys.com/user/enabletwofactor
 * [ ] https://api.glesys.com/user/disabletwofactor
 * [ ] https://api.glesys.com/user/changepassword
 * [ ] https://api.glesys.com/user/listorganizations
 * [ ] https://api.glesys.com/user/searchdata
 * [ ] https://api.glesys.com/user/signup
 * [ ] https://api.glesys.com/user/supportchallenge
 * [ ] https://api.glesys.com/user/initiatesupportchallenge
 * [ ] https://api.glesys.com/user/confirm
 * [ ] https://api.glesys.com/api/maintenance
 * [ ] https://api.glesys.com/api/serviceinfo
 * [ ] https://api.glesys.com/api/listfunctions
 * [ ] https://api.glesys.com/sshkey/add
 * [ ] https://api.glesys.com/sshkey/list
 * [ ] https://api.glesys.com/sshkey/remove
 * [ ] https://api.glesys.com/networkadapter/create
 * [ ] https://api.glesys.com/networkadapter/details
 * [ ] https://api.glesys.com/networkadapter/edit
 * [ ] https://api.glesys.com/networkadapter/delete
 * [ ] https://api.glesys.com/network/list
 * [ ] https://api.glesys.com/network/details
 * [ ] https://api.glesys.com/network/create
 * [ ] https://api.glesys.com/network/delete
 * [ ] https://api.glesys.com/network/edit
 * [ ] https://api.glesys.com/filestorage/createvolume
 * [ ] https://api.glesys.com/filestorage/listvolumes
 * [ ] https://api.glesys.com/filestorage/volumedetails
 * [ ] https://api.glesys.com/filestorage/editvolume
 * [ ] https://api.glesys.com/filestorage/deletevolume
 * [ ] https://api.glesys.com/filestorage/resourceusage
 * [ ] https://api.glesys.com/filestorage/listplans
 * [ ] https://api.glesys.com/project/edit
 * [ ] https://api.glesys.com/project/rename
 * [ ] https://api.glesys.com/project/delete
 * [ ] https://api.glesys.com/objectstorage/instancedetails
 * [ ] https://api.glesys.com/objectstorage/listinstances
 * [ ] https://api.glesys.com/objectstorage/createinstance
 * [ ] https://api.glesys.com/objectstorage/editinstance
 * [ ] https://api.glesys.com/objectstorage/deleteinstance
 * [ ] https://api.glesys.com/objectstorage/createcredential
 * [ ] https://api.glesys.com/objectstorage/deletecredential
 * [ ] https://api.glesys.com/objectstorage/estimatedcost