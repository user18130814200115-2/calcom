#!/usr/bin/python3

import arrow
from ics import Calendar, Event
import sys

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
current_month = 0
index = 0
events = {}

with open(sys.argv[1]) as calendar_file:
	calendar = Calendar(calendar_file.read())

for event in list(calendar.timeline):
	date = event.begin.format('YYYY-MM-DD').split('-')
	time = event.begin.format('HH:mm') + ' - ' + event.end.format('HH:mm')
	
	if current_month != date[0] + '-' + date[1]:
		current_month = date[0] + '-' + date[1]
		events[current_month] = {}
	
	index += 1

	events[current_month][index]= {}
	events[current_month][index]['day'] = date[2]
	events[current_month][index]['name'] = event.name
	events[current_month][index]['time'] = time
	events[current_month][index]['location'] = event.location
	events[current_month][index]['description'] = event.description
		

for month in events:
	data = ''
	data += arrow.get(month).format('YYYY MMMM\n')

	for day in events[month]:
		data += events[month][day]['day'] + ':\n\t'
		data += events[month][day]['name'] + '\n\t'

		if events[month][day]['time'] != '00:00 - 00:00':
			data += events[month][day]['time']

		if events[month][day]['location'] != None:
			data+= '\n\t' + '; '.join(events[month][day]['location'].split('\n'))

		if events[month][day]['description'] != None:
			data+= '\n\t' + '; '.join(events[month][day]['description'].split('\n'))

		data += '\n'

	with open(month + '.cal', 'w') as file:
		file.write(data)
