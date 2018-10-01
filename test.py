from main import *

def test():
	# Downloads the latest images from the SD card
	count = 0

	if is_connected():
		count = len(get_image_list())

	while is_connected():
		new_count = len(get_image_list())
		print(get_image_list())
		while new_count > count:
			count = count + 2
			print('📸 NEW IMAGE DETECTED')
			latest_image = download_image(count)
			print('⬇️ NEW IMAGE TRANSFERRED', latest_image)


if __name__ == '__main__':
	test()