dir_hw = src
dir_check = tools

hw01:
	g++ -std=c++11 $(dir_hw)/$@/main.cpp -o $(dir_hw)/$@/main

hw01c: hw01 
	python ./$(dir_check)/check01.py

