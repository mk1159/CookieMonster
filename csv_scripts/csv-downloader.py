import csv
import urllib.request
import urllib.error
import time

start_index = 0
end_index = 50000

url_list = []

with open('./IMDb-Face.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for x in range(0, end_index):
		row = reader.__next__()
		if x < start_index:
			continue

		url_list.append(row['url'])

		x += 1;
		if x > 50000:
			break

for x in range(0,len(url_list)):
	try:
		new_fn = './Data/UnsortedIMDB/' + f"{x+start_index:07d}" + '.jpg'
		filepath, response = urllib.request.urlretrieve(url_list[x], new_fn) 
		print('saved at: ', filepath)
	except urllib.error.URLError as err:
		print('URLError: ', err)
	except urllib.error.HTTPError as err:
		print('HTTPError: ', err)

	# time.sleep(.001)

print('Done')


# urllib.request.urlretrieve('url','file.jpg')
# print(row['name'],row['index'],row['image'],row['rect'],row['height'] row['width'],row['url'])
# Cite these people: https://arxiv.org/abs/1807.11649