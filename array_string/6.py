import sys


def main(string):
	compressed = ""
	count = 1
	target = string[0]

	for i in range(1, len(string)):
		if string[i] == string[i-1]:
			count += 1
		else:
			compressed += string[i-1] + str(count)
			count = 1
	compressed += string[-1] + str(count)
	return compressed if len(compressed) < len(string) else string


if __name__ == "__main__":
	print(main(sys.argv[1]))

