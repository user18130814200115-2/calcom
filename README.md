# Calcom

Convert your calendars into beatiful pdfs using LaTeX.

Calcom can generate pdfs from `ics` files or from its custom human-readable syntax.


## Usage

`calcom FILES` where FILES is a list containing ics files or files using
`calcom` custom syntax as described below. You can mix the two syntaxes.

`calcom home.ics work.ics custom.cal`

All processed PDFs will be merged at the end. Single month PDFs will be
available in the `.compile/` directory.

## Syntax
Each month has its own text file with the following syntax:

```
Month Year

day:
  Name
  [Details]
  [...]

---
Month Year

day:
	...

```

And example may be:

```
December 2022

9:
	GitHub release
	Release version 1 of calcom

2:
	Details are Optional

---
January 2023

1:
	Event with many details
	Time
	Location
	Summary
```

calcom's calendar syntax also has support for recurring events. The syntax is
as follows:

```
every [frequency][type][number] [starting day]:
	[Details]
	[Details]
```
[frequency] is a number determining how many instances of [type] need to pass
before the event repeats. `7days5` will repeat every 7 days for example.

[type] can be one of 'd', 'm', 'y', 'days', 'months', 'years' and determines
what needs to pass before the event repeats.

[number] is the number of repetitions. 1 Repetition will result in 2 events,
the original and the repetition.

For example:
```
August 2022

every 7days5 1:
	This event will repeat every 7 days starting from the 1st of August
	This will happen 5 times
  
every 1d3 5:
	This event will repeat every day starting from the 5th of August
	This will happpen 3 times

every 1m4 6:
	This event repeats every month on the 6th starting in August
	This will happen 6 times

every 1mmonths4 6:
	This event repeats every month on the 6th starting in August
	This will happen 6 times
---
September 2022

every 1years5 10:
	This event repeats every year on the 10th of September
	This will happen 5 times.
	
```

This can also be used to generate empty calendars, or to ensure the presence of
pages for months with no events.

```
January 2024
every 1months12:
	~
	~
```
Generates a full calendar for 2024

## Requirements
- Python 3
- Arrow
- multiprocessing (optional)
- ics (optional)
- pypdf (optional)


# Licences and attribution

The LaTeX calendar style is not my own. It is licenced under [CC BY-NC-SA
3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) credit goes to Evan A.
Sultanik.
