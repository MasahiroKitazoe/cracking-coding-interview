def main(string):
	words = {}
	for s in string:
		if s == " ":
			continue
		words.setdefault(s, 0)
		words[s] += 1

	odds = 0
	for s in string:
		if s == " ":
			continue
		if words[s] % 2 != 0:
			odds += 1

	return odds in [0, 1]


if __name__ == "__main__":
	res = main("")
	print(res)

