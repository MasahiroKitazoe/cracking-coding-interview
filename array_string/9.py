import sys


def isSubstring(string1, string2):
	s_len = len(string1)
	if s_len != len(string2):
		return False
	
	i = 0
	first_s1 = string1[0]
	while i < s_len:
		if string2[i] != first_s1:
			i += 1
			continue
		is_substring = True
		for str1_idx, str2_idx in enumerate(range(i-s_len, i)):
			if string1[str1_idx] != string2[str2_idx]:
				is_substring = False
				break
		if is_substring:
			return is_substring
		else:
			i += 1
	return False


if __name__ == "__main__":
	print(isSubstring(sys.argv[1], sys.argv[2]))

