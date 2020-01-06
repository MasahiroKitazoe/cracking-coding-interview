STRING = "tes"

def main(string):
	string = sorted(string)
	for i in range(1, len(string)):
		if string[i] == string[i-1]:
			return False
	return True


if __name__ == "__main__":
	print(main(STRING))

