#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Re-encodes dev scores as originally available

$ ./<prog> eval-file full|cropped
'''


import sys
import os
from bob.db.verafinger import *

db = Database()
size = sys.argv[2]

with open(sys.argv[1], 'rt') as f:
  for line in f:
    filename, score = line.strip().split()
    bits = filename.split('/')
    if bits[1] == 'real':
      source = 'bf'
    else:
      source = 'pa'
    bits[3] = bits[3].rsplit('.', 1)[0]
    details = bits[3].split('_')
    f = db.query(File).join(Finger,Client).filter(
    File.size==size, #full or cropped
    File.source==source, #bf or pa
    File.session==details[2],
    Client.id==int(details[0]),
    Finger.side==details[1],
    ).one()
    if source == 'pa':
      print('%s attack/%s %s %s' % (f.finger.unique_name, f.finger.unique_name,
        f.path, score))
    else:
      print('%s %s %s %s' % (f.finger.unique_name, f.finger.unique_name,
        f.path, score))
