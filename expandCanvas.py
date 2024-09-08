#!/usr/bin/env python3

import os
import pathlib
import subprocess

if __name__ == "__main__":
    outPathName = 'icons/src/cursors/bitmaps/32x32'
    pathlib.Path(outPathName).mkdir(exist_ok=True)

    originalPath = 'icons/src/cursors/bitmaps/24x24'

    for file in os.listdir(originalPath):
        # print(os.path.abspath(originalPath + '/' + file))
        command = f"convert {originalPath + '/' + file} -colorspace RGB -background none -alpha on -flatten -gravity NorthWest -extent 32x32 -background none {outPathName}/{file}"
        subprocess.run(command, shell=True)

    print("Done")
