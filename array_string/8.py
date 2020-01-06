MATRIX = [
	[1,0,3,4],
	[5,6,7,8],
	[9,10,11,0]
]


def main():
	zero_columns = {i: False for i in range(len(MATRIX[0]))}
	for row in MATRIX:
		is_zero_row = False
		for i, val in enumerate(row):
			if zero_columns[i]:
				continue
			if val == 0 and not zero_columns[i]:
				is_zero_row = True
				zero_columns[i] = True
		if is_zero_row:
			for i in range(len(row)):
				row[i] = 0
	for col_i in range(len(MATRIX[0])):
		if zero_columns[col_i]:
			for row in MATRIX:
				row[col_i] = 0


if __name__ == "__main__":
	main()
	print(MATRIX)

