import os
import hashlib
import fnmatch
from functools import partial

#Don't walk into this dirs
ignoreddirs = [".git", ".svn"]
#Don't check this files
ignoredfiles = []
#Truncate hash file at every launch? 1/0 = yes/no
truncatehash = "1"

def md5sum(filename):
	with open(filename, mode='rb') as f:
		d = hashlib.md5()
		for buf in iter(partial(f.read, 128), b''):
			d.update(buf)
	return d.hexdigest()

hashfile = open('images.txt', 'a+')
if truncatehash == "1":
	hashfile.truncate(0)

for dirname, dirnames, filenames in os.walk('images'):

	for ignoredfile in ignoredfiles:
		for ignoredfile in fnmatch.filter(filenames, ignoredfile):
			filenames.remove(ignoredfile)

	for ignoreddir in ignoreddirs:
		for ignoreddir in fnmatch.filter(dirnames, ignoreddir):
			dirnames.remove(ignoreddir)		

	for subdirname in dirnames:
		print(os.path.join(dirname, subdirname))
	
	for filename in filenames:
		img = os.path.join(dirname, filename)
		imgsizebefore = os.path.getsize(img)
		imghash = md5sum(img)
		print(imghash, imgsizebefore, img, sep = " ")
		hashfile.write(imghash + " " + img + "\n")

hashfile.close