#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import zipfile
import rarfile


if sys.argv[1].endswith("zip"):
    print "unzip File " + sys.argv[1]
    file=zipfile.ZipFile(sys.argv[1],"r");
    for name in file.namelist():
        utf8name=name.decode('gbk')
        print "Extracting " + utf8name
        pathname = os.path.dirname(utf8name)
        if not os.path.exists(pathname) and pathname!= "":
            os.makedirs(pathname)
        data = file.read(name)
        if not os.path.exists(utf8name):
            fo = open(utf8name, "w")
            fo.write(data)
            fo.close
    file.close()
elif sys.argv[1].endswith("rar"):
    print "unrar File " + sys.argv[1];
    rar_file = rarfile.RarFile(sys.argv[1]);
    dir_name = sys.argv[1].decode('gbk').replace('.rar','')
    if os.path.isdir(dir_name):
        pass
    else:
        os.mkdir(dir_name)
    rar_file.extractall()
    rar_file.close()
else:
    print "Unsupported File Type"
