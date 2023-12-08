import os 

CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARD_VALS = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
def read_file(file_name: str):
	# cwd: str = os.path.dirname(os.path.realpath)
	file_path = os.getcwd() + "\\tests" + "\\" + file_name
	f = open(file_path, "r")
	return f

def get_hand_score(hand):
	card_counts = dict.fromkeys(CARDS, 0)
	for c in hand:
		card_counts[c] += 1
	score_of_current_card = []
	for c in hand:
		if card_counts[c] == 5:
			score_of_current_card.append(7)
		elif card_counts[c] == 4:
			score_of_current_card.append(6)
		elif card_counts[c] == 3:
			# Full house
			if len(set(hand)) == 2:
				score_of_current_card.append(5)
			# Three of a kind
			elif len(set(hand)) == 3:
				score_of_current_card.append(4)
		elif card_counts[c] == 2:
			# Two pair 
			if len(set(hand)) == 3:
				score_of_current_card.append(3)
			# One pair
			elif len(set(hand)) == 4:
				score_of_current_card.append(2)
		else:
			score_of_current_card.append(1)
	return max(score_of_current_card)

def main():
	file = read_file("second.txt")
	# 1. Determine the rank of each hand
	# 	a. Determine type 
	keys = []
	cards = {}
	for line in file:
		key = line[:line.find(" ")]
		keys.append(key)
		cards[key] = line[line.find(" ")+1:].rstrip()

	cards = dict(sorted(cards.items())) # sort list in ascending order
	#print(get_hand_score('T55J5'))
	
	# Iterate backwards and swap card positions
	hand_list = list(cards.keys())
	crnt_idx = len(hand_list) - 1
	
	for i in range(crnt_idx, 0, -1):
		temp = None
		if get_hand_score(hand_list[i]) == get_hand_score(hand_list[i-1]):
			#print(hand_list[i], hand_list[i-1])
			# Iterate through each hand and find the first difference
			x, y = 0, 0
			while hand_list[i][x] == hand_list[i-1][y]:
				x += 1
				y += 1
			#print(hand_list[i][x], hand_list[i-1][y])
			if CARD_VALS[hand_list[i][x]] < CARD_VALS[hand_list[i-1][y]]:
				#print(hand_list[i-1])
				temp = hand_list[i]
				hand_list[i] = hand_list[i-1]
				hand_list[i-1] = temp
			else:
				#print(hand_list[i])
				temp = hand_list[i-1]
				hand_list[i-1] = hand_list[i]
				hand_list[i] = temp
	print(hand_list)
	total = 0
	card_len = len(cards)
	i = 1
	for hand in hand_list:
		total += int(cards[hand]) * i
		i += 1
	print(total)
	
if __name__ == "__main__":
	main()