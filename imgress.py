import os
import hashlib
from functools import partial

#Don't walk into this dirs
ignoreddirs = [".git", ".svn"]
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

	for rf in ignoreddirs:
		if rf in dirnames:
			dirnames.remove(rf)

	for subdirname in dirnames:
		print(os.path.join(dirname, subdirname))
	
	for filename in filenames:
		img = os.path.join(dirname, filename)
		imgsizebefore = os.path.getsize(img)
		imghash = md5sum(img)
		print(imghash, imgsizebefore, img, sep = " ")
		hashfile.write(imghash + " " + img + "\n")

hashfile.close