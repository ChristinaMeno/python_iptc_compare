import sys
import hashlib

pyexiv_caption = iptcdata_caption = pil_caption = None
pyexiv_hash = iptcdata_hash = pil_hash = None
import pyexiv2
image = pyexiv2.Image(sys.argv[1])
image.readMetadata()
#print  image.iptcKeys()
if 'Iptc.Application2.Caption' in image.iptcKeys():
    pyexiv_caption =  image['Iptc.Application2.Caption']
    pyexiv_hash = hashlib.sha1(pyexiv_caption).hexdigest() 

import iptcdata
f = iptcdata.open(sys.argv[1])
for x in f.datasets:
    if 'Caption/Abstract' == x.title:
        iptcdata_caption = x.value 
        iptcdata_hash = hashlib.sha1(iptcdata_caption).hexdigest() 


import Image, TiffImagePlugin, JpegImagePlugin, IptcImagePlugin
import StringIO


im = Image.open(sys.argv[1])
info = IptcImagePlugin.getiptcinfo(im)
if info:
    # extract caption
    pil_caption = info.get((2, 120))
    pil_hash = hashlib.sha1(pil_caption).hexdigest()
    # print all available fields
    '''
    for k, v in info.items():
        print "  %s %s" % (k, repr(v))
    '''


if len(set((pyexiv_hash, iptcdata_hash, pil_hash))) > 1:
    print 'differing output for %s' % (sys.argv[1]) 
    print 'pyexiv2  says %s' % pyexiv_caption
    print 'iptcdata says %s' % iptcdata_caption
    print 'PIL      says %s' % pil_caption

    print 'pyexiv2  hash %s' % pyexiv_hash
    print 'iptcdata hash %s' % iptcdata_hash
    print 'PIL      hash %s' % pil_hash
