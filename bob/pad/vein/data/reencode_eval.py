#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Re-encodes eval scores as originally available

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
    filename = filename.rsplit('.', 1)[0]
    bits = filename.split('_')
    if len(bits) == 4:
      source = 'pa'
    else:
      source = 'bf'
    f = db.query(File).join(Finger,Client).filter(
    File.size==size, #full or cropped
    File.source==source, #bf or pa
    File.session==bits[2],
    Client.id==int(bits[0]),
    Finger.side==bits[1],
    ).one()
    if source == 'pa':
      print('%s attack/%s %s %s' % (f.finger.unique_name, f.finger.unique_name,
        f.path, score))
    else:
      print('%s %s %s %s' % (f.finger.unique_name, f.finger.unique_name,
        f.path, score))
