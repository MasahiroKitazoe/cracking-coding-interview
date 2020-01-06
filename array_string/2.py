STRING1 = "abcdef"
STRING2 = "acdebf"


def main(s1, s2):
	return sorted(s1) == sorted(s2)

if __name__ == "__main__":
	print(main(STRING1, STRING2))

