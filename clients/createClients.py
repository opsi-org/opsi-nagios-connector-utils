#!/usr/bin/env python

from OPSI.Backend.BackendManager import *

template = '''
define host {
	use		opsi-client-tmpl
	host_name	%hostId%
	hostgroups	opsi-clients
	alias		%hostId%
	address		%hostId%
	}
'''

backend = BackendManager(
             dispatchConfigFile = u'/etc/opsi/backendManager/dispatch.conf',
             backendConfigDir   = u'/etc/opsi/backends',
             extensionConfigDir = u'/etc/opsi/backendManager/extend.d',
                        )


hosts = backend.host_getObjects(type="OpsiClient")

for host in hosts:
	filename = "%s.cfg" % host.id
	entry = template.replace("%hostId%",host.id)
	f = open(filename, 'w')
	f.write(entry)
	f.close()
