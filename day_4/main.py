import os
import re

GAMES = {}

def init_games_dict(f):
	for line in f:
		key = line[:line.find(":")]
		game_number = int(re.findall(r'\d+', key)[0])
		GAMES[game_number] = 1 # start with original copy of the card

def read_file(file_name: str):
	# cwd: str = os.path.dirname(os.path.realpath)
	file_path = os.getcwd() + "\\tests" + "\\" + file_name
	f = open(file_path, "r")
	return f

def binary_search(alist: list[str], item: str) -> bool:
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        pos = 0
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            pos = midpoint
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def part_one(f) -> int:
	total = 0
	# Points = 2^(winning numbers-1)
	# 1. Count the number of winnings items
		# 0 : 0
		# > 0
	for line in f:
		w = 0
		line = line[line.find(":")+1:]
		sp = line.split("|")
		nums = []
		for s in sp:
			nums.append(s.split())
			
		# for each element in numbers have, search for in winning numbers
		winning = sorted(nums[0])
		have = sorted(nums[1])
		for h in have:
			res = binary_search(winning, h)
			if res:
				w += 1
		if (w == 0):
			total += 0
		else:
			total += 2**(int(w-1))
	return total

def count_winnings(game):
	w = 0
	game = game[game.find(":")+1:]
	sp = game.split("|")
	nums = []
	for s in sp:
		nums.append(s.split())	
	# for each element in numbers have, search for in winning numbers
	winning = sorted(nums[0])
	have = sorted(nums[1])
	for h in have:
		res = binary_search(winning, h)
		if res:
			w += 1
	return (len(winning), w)
		

def main():
	file = read_file("two.txt")
	#assert(part_one(file) == 26346)
	init_games_dict(file)
	
	file = read_file("two.txt")
	for line in file:
		key = line[:line.find(":")]
		game_number = int(re.findall(r'\d+', key)[0])
		win_nums = count_winnings(line)
		max_winnings = win_nums[0]
		winnings = win_nums[1]

		number_of_next_copies = 0
		if game_number + max_winnings > max(GAMES.keys()):
			number_of_next_copies = max_winnings - game_number
		else:
			number_of_next_copies = game_number+winnings+1
		# spilling past table
		for i in range(game_number+1, number_of_next_copies):
			print(i)
			GAMES[i] += 1
	total = 0
	for key in GAMES.keys():
		#print(GAMES[key])
		pass
	


if __name__ == "__main__":
	main()