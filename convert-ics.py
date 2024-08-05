#!/usr/bin/python3


from ics import Calendar, Event
import sys

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
current_month = 0
events = {}

with open(sys.argv[1]) as calendar_file:
	calendar = Calendar(calendar_file.read())

for event in list(calendar.timeline):
	date = event.begin.format('YYYY-MM-DD').split('-')
	time = event.begin.format('HH:mm') + ' - ' + event.end.format('HH:mm')
	
	if current_month != date[0] + '-' + date[1]:
		current_month = date[0] + '-' + date[1]
		events[current_month] = {}
	

	events[current_month][date[2] + event.name]= {}
	events[current_month][date[2] + event.name]['date'] = date[2]
	events[current_month][date[2] + event.name]['name'] = event.name
	events[current_month][date[2] + event.name]['time'] = time
	events[current_month][date[2] + event.name]['location'] = event.location
		

for month in events:
	data = ''
	data += month_names[int(month.split('-')[1]) - 1] + ' ' + month.split('-')[0] + '\n'

	for day in events[month]:
		data += events[month][day]['date'] + ':\n'
		data += '\t' + events[month][day]['name'] + '\n\t'

		if events[month][day]['time'] != '00:00 - 00:00':
			data += events[month][day]['time'] + '\\\\\\\\'
		details = events[month][day]['location']
		if details == None:
			data += '~\n'
		else:
			data+= '; '.join(details.split('\n')) + '\n'

	with open(month + '.cal', 'w') as file:
		file.write(data)
