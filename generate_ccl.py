#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, ConfigParser
conf_file="./generate.conf"
conf_vars=dict()

configParser = ConfigParser.RawConfigParser()
configFilePath = r"%s" % conf_file
configParser.read(configFilePath)
conf_list = configParser.items("ccl")

for element in conf_list:
    conf_vars[element[0]] = eval(element[1])

if "prelude" in conf_vars:
    string=conf_vars["prelude"]
    string+="\n"
if "first" in conf_vars:
    string+=conf_vars["first"]

if random.randint(0,1) == 0:
    if "entity" in conf_vars:
        string+=conf_vars["entity"][random.randint(0,len(conf_vars["entity"])-1)]
        string+=" "
    if "entity_fail" in conf_vars:
        string+=conf_vars["entity_fail"][random.randint(0,len(conf_vars["entity_fail"])-1)]
        string+=" "
else:
    if "person" in conf_vars:
        string+=conf_vars["person"][random.randint(0,len(conf_vars["person"])-1)]
        string+=" "
    if "person_fail" in conf_vars:
        string+=conf_vars["person_fail"][random.randint(0,len(conf_vars["person_fail"])-1)]
        string+=" "

if "second" in conf_vars:
    string+=conf_vars["second"]

rand = random.randint(0,1)
if rand == 0:
    if "entity" in conf_vars:
        string+=conf_vars["entity"][random.randint(0,len(conf_vars["entity"])-1)]
        string+=" "
else:
    if "person" in conf_vars:
        string+=conf_vars["person"][random.randint(0,len(conf_vars["person"])-1)]
        string+=" "

if rand == 0:
    if "entity_fail" in conf_vars:
        string+=conf_vars["entity_fail"][random.randint(0,len(conf_vars["entity_fail"])-1)]
        string+=" "
else:
    if "person_fail" in conf_vars:
        string+=conf_vars["person_fail"][random.randint(0,len(conf_vars["person_fail"])-1)]
        string+=" "

if "finish" in conf_vars:
    string+=conf_vars["finish"]

print "-> Generated string : %s " % string
