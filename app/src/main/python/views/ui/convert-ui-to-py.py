#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

# Convert ui file to py file in directory

for filename in os.listdir("."):
    if filename.endswith(".ui"):
        filename_py = os.path.splitext(filename)[0] + ".py"
        cmd = f"pyside2-uic {filename} -o {filename_py}"

        print(cmd)
        os.system(cmd)
