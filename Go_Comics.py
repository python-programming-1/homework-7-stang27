import requests
from bs4 import BeautifulSoup
import os
from time import sleep

# 1. GET THE MAIN WEBSITE

url = 'https://www.gocomics.com/pearlsbeforeswine/2019/08/21'
for i in range(10):
	res = requests.get(url)
	res.raise_for_status()

	soup = BeautifulSoup(res.text)

	# 2. Find the Comic in the inspect
	comic_div = soup.select('div .item-comic-image')

	# 3. Find the image URL

	image_url = comic_div[0].contents[0].attrs['src']
	image_res = requests.get(image_url)
	image_res.raise_for_status()
	#print(image_url)

	# 4. Save the Image URL

	image_file = open(os.path.basename(image_url),'wb')
	for chunk in image_res.iter_content(100000):
		image_file.write(chunk)
	image_file.close()

	# 5. Get previous URL
	prev_link_div = soup.select('div .gc-calendar-nav__previous')
	prev_link = prev_link_div[0].contents[3].attrs['href']

	url = 'https://www.gocomics.com' + prev_link

	print(url)


