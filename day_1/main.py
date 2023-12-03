import os

def read_file(file_name: str):
	# cwd: str = os.path.dirname(os.path.realpath)
	file_path = os.getcwd() + "\\tests" + "\\" + file_name
	f = open(file_path, "r")
	return f

# Part one
def find_cal_sum(f):
	sum_cal = 0
	for line in f:
		cal_val = ""
		f_i = 0
		l_i = len(line) - 1
		while f_i <= l_i:
			if line[f_i].isnumeric():
				cal_val += line[f_i]
				break
			f_i += 1
		while l_i >= f_i:
			if line[l_i].isnumeric():
				cal_val += line[l_i]
				break
			l_i -= 1
		sum_cal += int(cal_val)
	return sum_cal

def main():
	file = read_file("one.txt")
	print(find_cal_sum(file))

if __name__ == "__main__":
	main()