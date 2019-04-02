#!/usr/bin/env python

import shutil
import sys
import os

with open(sys.argv[1]) as f:
    bvals = f.read().split(' ')
    bvals = [x for x in bvals if x != '']
    bvals = [x for x in bvals if x != '\n']
    bvals = [x for x in bvals if x != ' ']

with open('dwi.bvals','w') as f:
    for bval in bvals:
        bval = bval.replace('\n','')
	bval = round(float(bval),-2)
        f.write("%s " %bval)

shutil.move(os.path.join(os.getcwd(),'dwi.bvals'), sys.argv[1])
