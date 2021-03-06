#! /usr/bin/python3

from PIL import Image
import os
import sys
import shutil

try:
    direct = sys.argv[1]
except IndexError:
    print('You need to enter an input and output folder')
    exit(0)

outtxt = open(direct + '_out.txt', 'w+')
fileid = 0
for file in os.listdir(direct):
    outtxt.write('{},{},{}\n'.format(direct, str(fileid), file))
    shutil.move(direct + '/' + file, direct + '/' + str(fileid) + '_' + direct + '.jpg')
    fileid += 1
