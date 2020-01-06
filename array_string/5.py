def main(string1, string2):
	longer, shorter = (string1, string2) if len(string1) >= len(string2) else (string2, string1)
	len_l = len(longer)
	len_s = len(shorter)
	diff = 0
	l = 0
	s = 0
	while l < len_l and s < len_s:
		if longer[l] == shorter[s]:
			l += 1
			s += 1
		else:
			diff += 1
			if diff == 2:
				return False
			if len_l == len_s:
				l+= 1
				s += 1
			else:
				l += 1
	return True


if __name__ == "__main__":
	print(main("pale", "ple"))
	print(main("pales", "pale"))
	print(main("pale", "bale"))
	print(main("pale", "bake"))
	print(main("pale", "elap"))
	print(main("ple", "pale"))
