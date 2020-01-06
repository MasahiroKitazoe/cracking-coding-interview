STRING = "Mr John Smith "

def main(string):
	new_str = []
	for s in string:
		if s == " ":
			new_str.append("%20")
		else:
			new_str.append(s)
	return "".join(new_str)


if __name__ == "__main__":
	print(main(STRING))

