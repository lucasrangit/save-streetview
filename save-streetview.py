#!/usr/bin/env python
#
# Save Google Street View images
#
# Based on: https://andrewpwheeler.wordpress.com/2015/12/28/using-python-to-grab-google-street-view-imagery/
#

import urllib, os, datetime
import secrets

myloc = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
key = "&key=" + secrets.api_key

def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&location="
  MyUrl = base + Add + key
  fi = Add + ".jpg"
  try:
    os.makedirs(SaveLoc)
  except OSError, e:
    if e.errno != 17:
      raise # not EEXISTS
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))
  if fi not in Sizes:
    return
  for size in Sizes[fi]:
    if os.path.getsize(os.path.join(SaveLoc, fi)) == size:
      os.remove(os.path.join(SaveLoc, fi))
      return

Tests = ["34.0543543,-118.2586675",
	 "34.0542833,-118.2587341"]

Sizes = dict()

# get sizes of recent images
for subdir, dirs, files in os.walk(os.getcwd()):
  for file in files:
    if not file.endswith(".jpg"):
      continue
    if file not in Sizes:
      Sizes[file] = list()
    Sizes[file].append(os.path.getsize(os.path.join(subdir, file)))


for i in Tests:
  GetStreet(Add=i,SaveLoc=myloc)

# remove empty directories
if len(os.listdir(myloc)) == 0:
  os.rmdir(myloc)

