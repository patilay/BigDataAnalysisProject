#!/usr/bin/env python
import sys
import csv

f = csv.reader(sys.stdin)
for line in f:
    missingAttr = (line[3] == -9999 or line[4] == 'P')
    tminTmaxAttr = (line[2] == 'TMIN' or line[2] == 'TMAX')
    qualityReading = (line[5] == '')
    sourceCheck = (line[6] != '')
    if (not missingAttr and tminTmaxAttr and qualityReading and sourceCheck):
        print '%s\t%s\t%s\t%s' % (line[1], line[0], line[2], line[3])