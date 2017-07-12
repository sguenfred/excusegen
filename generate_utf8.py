#!/usr/bin/env python
# -*- coding: utf-8 -*-
#é#
import random, ConfigParser
conf_file="./generate_utf8.conf"

configParser = ConfigParser.RawConfigParser()
configFilePath = r"%s" % conf_file
configParser.read(configFilePath)
prelude = eval(configParser.get("config", "prelude"))
first_fixed = eval(configParser.get("config", "first_fixed"))
first_var = eval(configParser.get("config", "first_var"))
second_var = eval(configParser.get("config", "second_var"))
second_fixed = eval(configParser.get("config", "second_fixed"))
third_var = eval(configParser.get("config", "third_var"))
third_fixed = eval(configParser.get("config", "third_fixed"))
fourth_var = eval(configParser.get("config", "fourth_var"))
fifth_var = eval(configParser.get("config", "fifth_var"))
fouth_fixed = eval(configParser.get("config", "fouth_fixed"))
sixth_var = eval(configParser.get("config", "sixth_var"))
finish = eval(configParser.get("config", "finish"))

string=prelude
string+="\n"
string+=first_fixed
string+=first_var[random.randint(0,len(first_var)-1)]
string+=" "
string+=second_var[random.randint(0,len(second_var)-1)]
string+=second_fixed
string+=third_var[random.randint(0,len(third_var)-1)]
string+=third_fixed
string+=fourth_var[random.randint(0,len(fourth_var)-1)]
string+=" "
string+=fifth_var[random.randint(0,len(fifth_var)-1)]
string+=fouth_fixed
string+=sixth_var[random.randint(0,len(sixth_var)-1)]
string+="\n"
string+=finish

print "-> Generated string : %s " % string


