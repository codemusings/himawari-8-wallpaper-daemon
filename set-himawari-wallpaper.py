#!/usr/bin/env python

# Thanks to Michael Pote for figuring this out!
# https://gist.github.com/MichaelPote/92fa6e65eacf26219022

from datetime import datetime, timedelta
from urllib import urlretrieve
import Image
from gi.repository import Gio

tiles = 4
level = str(tiles) + "d"
tile_size = 550

url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/"
url += level + "/"
url += str(tile_size) + "/"

gmt_offset = -1
# use 30 minute offset (to leave time for the
# processing of the latest images I guess)
time = datetime.now() + timedelta(hours=gmt_offset,minutes=-30)
# only multiples of ten are valid minute marks apparently 
time += timedelta(minutes=-(time.time().minute % 10))
# only multiples of ten for second marks as well?
url += time.strftime("%Y/%m/%d/%H%M00")

exit(0)

img = Image.new("RGB", (4 * tile_size, 4 * tile_size))
for x in xrange(tiles):
    for y in xrange(tiles):
        print "Processing Tile " + str(x) + ", " + str(y)
        tile_url = url + "_" + str(x) + "_" + str(y) + ".png"
        tile_file = "/tmp/tile_" + str(x) + "_" + str(y) + ".png"
        urlretrieve(tile_url, tile_file)
        tile = Image.open(tile_file)
        img.paste(tile, (x * tile_size, y * tile_size))

print "Saving image..."
img.save("/tmp/earth.png")

print "Setting background..."
gsettings = Gio.Settings.new("org.gnome.desktop.background")
gsettings.set_string("picture-uri", "file:///tmp/earth.png")
gsettings.set_string("picture-options", "scaled")
