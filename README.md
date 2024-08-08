# Calcom

Convert your calendars into beatiful pdfs using LaTeX.

Calcom can generate pdfs from ics files or from its custom human-readable synax.


## Usage

`calcom FILES` where FILES is a lost containing ics files or files using `calcom`
custom syntax as described below. You can mix the two syntaxes.

All processed PDFs will be merged at the end into one combined one.

## Syntax
Each month has its own text file with the following syntax:

```
Month Year

day:
  Name
  [Details]
  [...]

```

And example may be:

```
December 2022

9:
  GitHub release
  Release version 1 of calcom

2:
  Details are Optional

10:
	Event with many details
	Time
	Location
	Summary
```
# Currently unsupported (regression)

`calcom` also has support for recurring tasks, though for now they cannot span
months or years, as each file defines just one month.
The syntax is as follows:

```
every [frequency]d[number] [starting]:
  Name
  Details

```

For example:
```
every 7d5 1:
  Weekly task
  For entire month
  
every 1d3 5:
  Daily task
  Between 5th and 8th
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
