import os
import hashlib
from functools import partial

def md5sum(filename):
	with open(filename, mode='rb') as f:
		d = hashlib.md5()
		for buf in iter(partial(f.read, 128), b''):
			d.update(buf)
	return d.hexdigest()

hashfile = open('images.txt', 'w')

for dirname, dirnames, filenames in os.walk('images'):

	for subdirname in dirnames:
		print(os.path.join(dirname, subdirname))

	for filename in filenames:
		img = os.path.join(dirname, filename)
		imghash = md5sum(img)
		print(imghash, img, sep = " ")
		hashfile.write(imghash + " " + img + "\n")

hashfile.close