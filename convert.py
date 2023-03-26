#!/usr/bin/env python3
# coding: utf-8
import re
import datetime

file = "list.txt"
OUT = "data.js"

convdict = {}
scriptlike = {}
with open(file, "r") as f:
    for line in f:
        #print(line)
        elems = line.strip().split(";")[0].split("\t")
        if len(elems) <= 1:
            continue
        convdict[elems[0]] = list(elems[1])
        scriptlike[elems[0]] = list(elems[1])
        if len(elems) >= 3:
            if elems[2]:
                scriptlike[elems[0]] = list(elems[2])

#timestamp
now = datetime.datetime.now().isoformat()
jscode = "const lastupdate='{}';\n".format(now)

dictelems = []
for key in convdict:
    dictelems.append("'"+key+"':["+ ",".join(map(lambda x: "'{}'".format(x), convdict[key])) +"]")
jscode += "const convdict={" + ",".join(dictelems) + "};\n"

scriptlikeelems = []
for key in scriptlike:
    scriptlikeelems.append("'"+key+"':["+ ",".join(map(lambda x: "'{}'".format(x), scriptlike[key])) +"]")
jscode += "const scriptlike={" + ",".join(scriptlikeelems) + "};\n"

with open(OUT, "w") as w:
    w.write(jscode)
print(jscode)