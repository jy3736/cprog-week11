dir_hw = src
dir_check = tools

hw01:
	g++ -std=c++11 $(dir_hw)/$@/main.cpp -o $(dir_hw)/$@/main

hw02:
	g++ -std=c++11 $(dir_hw)/$@/main.cpp -o $(dir_hw)/$@/main

hw03:
	g++ -std=c++11 $(dir_hw)/$@/main.cpp -o $(dir_hw)/$@/main

hw04:
	g++ -std=c++11 $(dir_hw)/$@/main.cpp -o $(dir_hw)/$@/main


hw01c: hw01 
	python ./$(dir_check)/check01.py

hw02c: hw02
	python ./$(dir_check)/check02.py

hw03c: hw03
	python ./$(dir_check)/check03.py

hw04c: hw04
	python ./$(dir_check)/check04.py

