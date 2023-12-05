import os 

def read_file(file_name: str):
	# cwd: str = os.path.dirname(os.path.realpath)
	file_path = os.getcwd() + "\\tests" + "\\" + file_name
	f = open(file_path, "r")
	return f

def main():
	file = read_file("zero.txt")
	seeds = []
	for line in file:
		if line.startswith("seeds:"):
			line = line[line.find(":")+1:]
			seeds = line.split()
		# delete plz
		if line.startswith("seed-to-soil"):
			#(soil, seed, range)



if __name__ == "__main__":
	main()