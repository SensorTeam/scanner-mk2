import sys
sys.path.append('../')

import config

import requests as req

# Functions
# ------------------------------

def get_image_list():
	# Returns a list of all the files currently on the SD card
	res = req.get(
		'{}/command.cgi'.format(config.URL_SERVER),
		params={
			'op': 100,
			'DIR': '/' + config.PATH_SERVER
		}
	)
	images = []
	lines = res.text.split('\n')
	for line in lines[1:]:
		values = line.split(',')
		if len(values) > 2:
			image = values[1].strip()
			images.append(image)
	return images

def download(url, to):
	# Downloads a file from the specified `url`
	res = req.get(url, stream=True)
	if res.status_code == 200:
		with open(to, 'wb') as file:
			for chunk in res:
				file.write(chunk)

def is_connected():
	# Checks if the SD card server is still alive
	res = req.get(config.URL_SERVER)
	if res.status_code == 200:
		return True
	else:
		return False

def download_latest_image():
	# Downloads two files (raw and jpg) from the SD card
	image_list = get_image_list()
	raw, jpg = image_list[-1], image_list[-2]
	url = config.URL_SERVER + '/' + config.PATH_SERVER + '/'
	download(url + raw, config.PATH_DOWNLOADS + '/' + raw)
	download(url + jpg, config.PATH_DOWNLOADS + '/' + jpg)
	return config.PATH_DOWNLOADS + '/'+ raw[:-4]

def download_image(index):
	# Downloads two files (raw and jpg) given an index from the SD card
	image_list = get_image_list()
	raw, jpg = image_list[index-1], image_list[index-2]
	url = config.URL_SERVER + '/' + config.PATH_SERVER + '/'
	download(url + raw, config.PATH_DOWNLOADS + '/' + raw)
	download(url + jpg, config.PATH_DOWNLOADS + '/' + jpg)
	return config.PATH_DOWNLOADS + '/'+ raw[:-4]

def download_latest_jpg(index):
	# Downloads the latest jpg given an index from the SD card
	image_list = get_image_list()
	jpg = image_list[index-1]
	url = config.URL_SERVER + '/' + config.PATH_SERVER + '/'
	download(url + jpg, config.PATH_DOWNLOADS + '/' + jpg)
	return config.PATH_DOWNLOADS + '/'+ jpg[:-4]