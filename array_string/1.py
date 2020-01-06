def main(string):
	found = {}
	for s in string:
		if found.get(s):
			return False
		else:
			found[s] = True
	return True


if __name__ == "__main__":
	print(main("test"))

