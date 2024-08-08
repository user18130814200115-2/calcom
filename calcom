#!/usr/bin/python3

import sys
import os
import arrow

def printv(verbose):
	pass

def ParseCAL(filename, CalEvents):
	printv("Parsing " + filename +  " as a calcom file")

	with open(filename) as file:
		for index, line in enumerate(file):
			if index != 0:
				if line != '\n': # Discard Empty lines
					if line[0] != '\t': # Non-indented lines are day keys
						day = int(line[:-2])
						CalEvents[month][day]['amount'] += 1
						CalEvents[month][day][CalEvents[month][day]['amount']] = []
					else:
						CalEvents[month][day][CalEvents[month][day]['amount']].append(line[1:-1])
			else:
				month = line[:-1]
				if month not in CalEvents:
					CalEvents[month] = CalEventsInit(month)
	return CalEvents	

def ParseICS(filename, CalEvents):
	printv("Parsing " + filename +  " as an ICS file")

	from ics import Calendar, Event

	with open(filename) as file:
		calendar = Calendar(file.read())
	
	for event in calendar.events:
		month = event.begin.format('MMMM YYYY')
		day = int(event.begin.format('DD'))
		time = event.begin.format('HH:mm') + ' - ' + event.end.format('HH.mm')
		if month not in CalEvents:
			CalEvents[month] = CalEventsInit(month)
		CalEvents[month][day]['amount'] += 1
		CalEvents[month][day][CalEvents[month][day]['amount']] = []
		CalEvents[month][day][CalEvents[month][day]['amount']].append(event.name)
		if time != '00:00 - 00:00':
			CalEvents[month][day][CalEvents[month][day]['amount']].append(time)
		if event.location != None:
			CalEvents[month][day][CalEvents[month][day]['amount']].append('; '.join(event.location.split('\n')))
		if event.description != None:
			CalEvents[month][day][CalEvents[month][day]['amount']].append('; '.join(event.description.split('\n')))

	return CalEvents

def CalEventsInit(header):
	firstDay = int(arrow.get(header, 'MMMM YYYY').format('d'))
	lastArrow = arrow.get(header, 'MMMM YYYY').dehumanize('in a month').dehumanize('1 days ago')
	lastDay = int(lastArrow.format('d'))
	maxDays = int(lastArrow.format('DD'))

	CalEvents = {}
	CalEvents['metadata'] = {}
	CalEvents['metadata']['title'] = header
	CalEvents['metadata']['firstDay'] = firstDay
	CalEvents['metadata']['lastDay'] = lastDay
	CalEvents['metadata']['maxDays'] = maxDays

	for day in range(1,maxDays+1):
		CalEvents[day] = {}
		CalEvents[day]['amount'] = 0
	
	return CalEvents

def OutputTEX(CalEvents):
	data = "\\documentclass[11pt]{article}\n\\usepackage{calendar}\n\\usepackage[landscape, paperwidth=25.2cm, paperheight=35.64cm, margin=0.4cm]{geometry}\n\\usepackage{palatino}\n\\begin{document}\n\\hoffset=-0.85in\n\\voffset=-0.75in\n\\setbox0\\hbox{\\begin{minipage}{\\textwidth}\\pagestyle{empty}\n\\setlength{\\parindent}{0pt}\n\\StartingDayNumber=2\n\\begin{center}\n"
	for index,day in enumerate(CalEvents):
		if index == 0:
			data += '\\textsc{\\LARGE ' + CalEvents['metadata']['title'].split(' ')[0] + '}\n\\textsc{\\large ' + CalEvents['metadata']['title'].split(' ')[1] + '}\n'
			data += '\\end{center}\n\\begin{calendar}{\\textwidth}\n'
			data += '\\BlankDay\n' * (CalEvents['metadata']['firstDay'] - 1)
			data += '\\setcounter{calendardate}{1}\n'
		else:
			data += '\\day{'
			for event in range(1, CalEvents[day]['amount'] + 1):
				if event == 1:
					data += (CalEvents[day][event][0] + '}{~' + '\\\\~'.join(CalEvents[day][event][1:])).translate(str.maketrans({"&":  r"\&", "$":  r"\$"}))
				else:
					data += ('\\eventskip \\dayheader{' + CalEvents[day][event][0] + '}{}\\eventskip ' + '\\\\~'.join(CalEvents[day][event][1:])).translate(str.maketrans({"&":  r"\&", "$":  r"\$"}))
			if CalEvents[day]['amount'] == 0:
				data += '~}{~'
			data += '}\n'
	data += '\\BlankDay\n' * (7 - CalEvents['metadata']['lastDay'])
	data += "\\finishCalendar\n\\end{calendar}\n\\end{minipage}}\n\\pdfpageheight=\\dimexpr\\ht0+\\dp0+0.75in\\relax\\shipout\\box0\\stop"

	return data

def main():
	CalEvents = {}
	for input_file in sys.argv[1:]:
		if input_file[-3:] == 'ics':
			CalEvents = ParseICS(input_file, CalEvents)
		else:
			CalEvents = ParseCAL(input_file, CalEvents)
	
	compileDirectory = '.compile/'
	if not os.path.exists(compileDirectory):
		os.makedirs(compileDirectory)

	for month in CalEvents:
		TexData = OutputTEX(CalEvents[month])
		outputFileName = compileDirectory + arrow.get(month, 'MMMM YYYY').format('YYYY-MM') + '.tex'
		with open(outputFileName, 'w') as outputFile:
			outputFile.write(TexData)
		os.system('xelatex -output-directory=' + compileDirectory + ' ' + outputFileName)
			
			

main()
