#!/usr/bin/python

# Copyright (c) 2016 Datera, Inc.  All rights reserved.
# Datera, Inc. Confidential and Proprietary.

# Script to create INIT file


import json
import uuid


INIT_TEMPLATE = '''
{
	"adminPassword" : "password",
	"autoJoin" : true,
	"debug" : 1,
        "cabalSize" : 3,
	"name" : "DateraVM",
        "statsSize" : "104857600",
        "ntp":
        [
            "0.pool.ntp.org", "1.pool.ntp.org"
        ],
        "dns":
        [
            "8.8.8.8", "8.8.4.4"
        ],
	"network" : 
	[
		{
			"addr" : 
			{
				"mtu" : 1500,
				"network" : 24,
				"range" : 50,
                                "server" : "172.16.211.170",
				"vlan" : 0
			},
			"ident" : 
			[
				"netA1"
			],
			"net" : "ext1"
		},
                {
                        "addr": 
                        {
                                "mtu": 1500,
                                "network": 24,
                                "range": 50,
                                "server": "172.17.211.170",
                                "vlan": 0
                        },
                        "ident": 
                        [
                                "netA2"
                        ],
                        "net": "ext2"
                },
                {
                        "addr" :
                        {
                                "mtu" : 1500,
                                "network" : 24,
                                "range" : 50,
				"server" : "192.168.100.2",
                                "vlan" : 0
                        },
                        "ident" :
                        [
                                "netB1"
                        ],
                        "net" : "int1"
                },
                {
                        "addr":
                        {
                                "mtu": 1500,
                                "network": 24,
                                "range": 50,
                                "server": "192.168.110.2",
                                "vlan": 0
                        },
                        "ident":
                        [
                                "netB2"
                        ],
                        "net": "int2"
                },
		{
			"addr" : 
			{
				"gateway" : "",
				"mtu" : 1500,
				"network" : 24,
				"range" : 0,
				"vlan" : 0,
				"server" : ""
			},
			"ident" : 
			[
				"mgt1"
			],
			"net" : "mgmt1"
		},
                {
                        "addr": 
                        {
                                "gateway": "",
                                "mtu": 1500,
                                "network": 24,
                                "range": 50,
				"vlan" : 0,
                                "server": "172.16.211.170"
                        },
                        "ident": 
                        [
                                "netA1"
                        ],
                        "net": "ext1iscsi"
                },
                {
                        "addr":
                        {
                                "gateway": "",
                                "mtu": 1500,
                                "network": 24,
                                "range": 50,
				"vlan" : 0,
                                "server": "172.17.211.170"
                        },
                        "ident":
                        [
                                "netA2"
                        ],
                        "net": "ext2iscsi"
                }
	],
	"timezone" : "US/Pacific",
	"useRDMA" : false,
	"uuid" : "9a3162f0-d581-48ed-a8d6-2d7cefd91de0"
}
'''

def parse_netinfo(net_path):
    gateway = None
    serverIp = None
    with open(net_path) as data_file:
        info = json.load(data_file)
        serverIp = info['addr'].split("/")[0]
        _g = info['gateways'].split(".")
        _g.pop()
        _g.append('254')
        gateway = ".".join(_g)
    return (gateway, serverIp)


class InitCreate(object):
    def __init__(self):
        self.gateway = None
        self.serverIp = None
	self.uuid = uuid.uuid4().urn[9:]
        (self.gateway, self.serverIp) = \
            parse_netinfo("/var/datera/datera-net-dhcplease-mgt1.json")
        self.generateInitFile()

    def generateInitFile(self):
        temp_init = json.loads(INIT_TEMPLATE)
        temp_init['uuid'] = self.uuid
        temp_init['network'][4]['addr']['server'] = self.serverIp
        #temp_init['network'][5]['addr']['server'] = self.serverIp
        temp_init['network'][4]['addr']['gateway'] = self.gateway
        #temp_init['network'][5]['addr']['gateway'] = self.gateway
	f = open("/var/datera/INIT", "wb")
	f.write(unicode(json.dumps(temp_init, ensure_ascii=False)))

if __name__ == "__main__":
    ic = InitCreate()
