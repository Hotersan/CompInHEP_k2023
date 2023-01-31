SRC = $(basename $(wildcard *.cpp))

all:
	$(MAKE) cpp
cpp:
	g++ $(SRC).cpp -o $(SRC).out

RM = $(sort $(wildcard *.out ))
clean:
	rm -r $(RM)

cleanAll:
	$(MAKE) clean
	rm -rf *.out

test:
	echo $(SRC)
