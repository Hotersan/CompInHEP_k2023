SRC = $(basename $(wildcard *.tex))

all:
	$(MAKE) -i tex
	$(MAKE) dvips
tex:
	latex $(SRC)
	pdflatex $(SRC)
dvips:
	dvips $(SRC) -o

RM = $(sort $(wildcard *.dvi *.log *.aux triangle_loop* *~))
clean:
	rm -r $(RM)

cleanAll:
	$(MAKE) clean
	rm -rf *.ps

test:
	echo $(SRC)
