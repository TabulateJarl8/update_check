import requests
import hashlib
import urllib.request
import logging
from tqdm import tqdm

def isUpToDate(fileName, url):
	with open(fileName, "r") as f:
		file = f.read()
	hash = hashlib.sha256((file).encode('utf-8')).hexdigest()

	urlcode = requests.get(url).text
	urlhash = hashlib.sha256((urlcode).encode('utf-8')).hexdigest()
	
	if hash == urlhash:
		return True
	else:
		return False

def update(path, url):
	#put __file__ in path to update current file
	for i in tqdm(range(1), desc="Downloading Updates..."):
		urllib.request.urlretrieve(url, path)

def checkForUpdates(path, url):
	if isUpToDate(path, url) == False:
		update(path, url)
		return True
	else:
		return False