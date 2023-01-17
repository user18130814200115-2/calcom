CAL := $(wildcard *.cal)
PDF := $(patsubst %.cal, %.pdf, $(CAL))

all:
	$(MAKE) -s months
	$(MAKE) -s combine

combine: all.pdf
all.pdf: $(PDF)
	@pdfunite $(PDF) all.pdf

months: $(PDF)
%.pdf: %.cal
	calcom $< 

