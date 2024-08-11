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

A `calcom` file input file must be written according to the following syntax.

### Comments

Lines starting with a `#` are ignored, so are empty lines.

### Starting a month

The first line (aside from empty or comment lines)  must be the name of a month
followed by the year.
```
August 2023
```

A new month can be started by writing at least 3 dashes (-) and putting the
Month on the following line
```
August 2023

---
September 2023

-------------------------------------------
June 1984
```

### Static Events

Regular events are defined by first putting the day number on which they occur.
The following lines **must be indented with tabs, not spaces** and contain
first the name, followed by an arbitrary number of lines with details.
```
August 2023

# Event on the first of august
1:
	Name
	Details

2:
	Name
	Details
	Details
	Details
```

### Recurring events

Recurring events are started with the keyword `every`. This keyword is followed
by the frequency, type, and number of repetitions. Finally, the starting day is
put, followed by a colon. The type can be any of: days, weeks,  months, years.

```
August 2023

# Event on the first of August
1:
	Name
	Details
	...

# Reccuring event starting on the second of August
every 2 days 5 2:
	Name
	Details
	...
```
You can also have events on specific weekdays every month, such as the first
Monday, or second Friday.
```
# every 1st Monday for the next 5 months
every 1 Monday 5 1:
	Name
	Details
	....

# Every 2nd Friday for the next 5 months
every 2 Friday 5 9:
	Name
	Details
	...

```


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
