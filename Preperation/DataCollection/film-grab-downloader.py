import urllib.request
import urllib.error
import sys


if len(sys.argv) != 6:
	raise Exception('Please give year, month, start id, end id, and iteration value.')

year = sys.argv[1]
month = sys.argv[2]

start_id = sys.argv[3]
end_id = sys.argv[4]
if len(start_id) != len(end_id):
	raise Exception('Length of start and end id do not equal.')
id_length = len(start_id)

# ittr_val is the number which is changing per picture
ittr_val = 10 ** (len(sys.argv[5]) - 1)


url_list = []
num_itteration = (int(end_id) - int(start_id))//(ittr_val)

base_url = 'https://film-grab.com/wp-content/uploads/'+ year +'/'+ month + '/'

for i in range(0,num_itteration):
	curr_id = int(start_id) + (i*ittr_val)
	curr_id = str(curr_id)
	curr_id = ('0' * (id_length - len(curr_id)) + curr_id)

	url_list.append((base_url + curr_id + '.jpg', curr_id)) # has a url & the unique iq

for x in range(0,len(url_list)):
	try:
		new_fn = './Data/UnsortedFG/' + year + month + url_list[x][1] + '.jpg'
		filepath, response = urllib.request.urlretrieve(url_list[x][0], new_fn) 
		print('saved at: ', filepath)
	except urllib.error.URLError as err:
		print('URLError: ', err)
	except urllib.error.HTTPError as err:
		print('HTTPError: ', err)


print('Done')


# general form: https://film-grab.com/wp-content/uploads/{2014}/{01}/{128}.jpg

# urllib.request.urlretrieve('url','file.jpg')