#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, ConfigParser
conf_file="./generate_utf8.conf"
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
if "first_fixed" in conf_vars:
    string+=conf_vars["first_fixed"]
if "first_var" in conf_vars:
    string+=conf_vars["first_var"][random.randint(0,len(conf_vars["first_var"])-1)]
    string+=" "
if "second_var" in conf_vars:
    string+=conf_vars["second_var"][random.randint(0,len(conf_vars["second_var"])-1)]
if "second_fixed" in conf_vars:
    string+=conf_vars["second_fixed"]
if "third_var" in conf_vars:
    string+=conf_vars["third_var"][random.randint(0,len(conf_vars["third_var"])-1)]
if "third_fixed" in conf_vars:
    string+=conf_vars["third_fixed"]
if "fourth_var" in conf_vars:
    string+=conf_vars["fourth_var"][random.randint(0,len(conf_vars["fourth_var"])-1)]
    string+=" "
if "fifth_var" in conf_vars:
    string+=conf_vars["fifth_var"][random.randint(0,len(conf_vars["fifth_var"])-1)]
if "fouth_fixed" in conf_vars:
    string+=conf_vars["fouth_fixed"]
if "sixth_var" in conf_vars:
    string+=conf_vars["sixth_var"][random.randint(0,len(conf_vars["sixth_var"])-1)]
    string+="\n"
if "finish" in conf_vars:
    string+=conf_vars["finish"]

print "-> Generated string : %s " % string
