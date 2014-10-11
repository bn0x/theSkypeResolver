import json
import urllib2

userName = raw_input('Username: ')

apiURL = urllib2.urlopen('http://yourserver:8080/api/%s' % (userName))
for index in json.load(apiURL):
	print index['public'], index['local']
