# Calcom

```
! Currently in first working release !
```

This is my personal calendar system using a simple human-readable syntax file, with the power of LaTeX behind it.

The LaTeX calendar.sty file is not my own. It is licenced under [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) credit goes to Evan A. Sultanik.


# Usage

`calcom FILE` for single month files.

If you have your files named alphabetically, EG. `YYYY-MM.cal`, you can also use `make` with the Included Makefile to automatically generate a PDF of every month called `all.pdf`

## Syntax
Each month has its own text file with the following syntax:

```
Month Year

day:
  Name
  Details
  
day:
  Name
  Details
```

And example may be:

```
December 2022

9:
  GitHub release
  Release version 1 of calcom

2:
  Details are Optional

```

`calcom` also has support for recurring tasks, though for now they cannot span months or years, as each file defines just one month.
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
- Gnu Coreutils
  + Almost everything is POSIX, but `date` is not
- A working (xe)latex instance
- A Posix Shell
- calendar.sty

Optional:
- make
