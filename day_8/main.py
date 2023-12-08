import os 
import queue

queue = queue.Queue()

directions = {}

L = 0
R = 1

def refill_queue(q, data):
	for d in data:
		q.put(d)

def read_file(file_name: str):
	# cwd: str = os.path.dirname(os.path.realpath)
	file_path = os.getcwd() + "\\tests" + "\\" + file_name
	f = open(file_path, "r")
	return f

def main():
	file_name = input("Enter file name: ")
	file = read_file(file_name)
	# Start at AAA, end at ZZZ
	rules = file.readline().strip()
	refill_queue(queue, rules)

	# Process directions into mapping
	for line in file:
		if len(line.strip()) == 0:
			continue
		else:
			line = line.strip()
		key, value = line.split("=")
		key = key.strip()
		l, r = value.split(",")
		l = "".join(c for c in l if c.isalpha())
		r = "".join(c for c in r if c.isalpha())
		directions[key] = (l, r)
	
	crnt = 'AAA'
	di = -1
	file = read_file(file_name)
	moves = 0
	while crnt != 'ZZZ':
		if queue.empty():
			#print("refill queue")
			refill_queue(queue, rules)
		direction = queue.get()
		if direction == 'L':
			di = 0
		else:
			di = 1
		crnt = directions[crnt][di]
		moves += 1
	print(moves)
	
if __name__ == "__main__":
	main()