import os
import re

games = {}

def read_file(file_name: str):
	# cwd: str = os.path.dirname(os.path.realpath)
	file_path = os.getcwd() + "\\tests" + "\\" + file_name
	f = open(file_path, "r")
	return f

def init_games_dict(f):
	for line in f:
		key = line[:line.find(":")]
		games[key] = {"r": 0, "g": 0, "b": 0}

def main():
	file = read_file("one.txt")
	init_games_dict(file)
	file = read_file("one.txt")
	'''
	for line in file:
		#rounds = line.count(";") + 1 
		rounds = line.split(";")
		r = len(rounds)
		for i in range(r):
			if "red" in rounds[i] or "green" in rounds[i] or "blue" in rounds[i]:
				games[line:8][i] = {"r": , "g": , "b": }

		for i in range(rounds):
			games[line[:8]][i] = {'r':, 'g': 'b':}
	'''
	#s = "Game 1: 1 blue, 3 green; 2 green, 1 blue, 1 red; 1 red, 3 green"
	for line in file:
		key = line[:line.find(":")]
		line = line[line.find(":")+1:]
		rounds = line.split(";")
		r_len = len(rounds)
		for j in range(r_len):
			c = rounds[j].split(",")
			c_len = len(c)
			for i in range(c_len):
				col = c[i]
				col_len = len(col)
				for x in range(col_len):
					if col[x].isnumeric():
						games[key][col[x+2]] = col[x]

					
	print(games['Game 1'])

if __name__ == "__main__":
	main()