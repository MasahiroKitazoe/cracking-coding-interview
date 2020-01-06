MATRIX = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
]


def main():	
	def helper(row_idx, col_idx, value, count, matrix_len):
		if count == matrix_len:
			return
		next_row_idx = col_idx
		next_col_idx = (row_idx * -1) - 1
		tmp = MATRIX[next_row_idx][next_col_idx]
		MATRIX[next_row_idx][next_col_idx] = value
		count += 1
		helper(next_row_idx, next_col_idx, tmp, count, matrix_len)
	
	n = len(MATRIX)
	for i in range(n//2):
		for j in range(i, n-1-i):
			helper(i, j, MATRIX[i][j], 0, n)
		

if __name__ == "__main__":
	main()
	for row in MATRIX:
		print(row)

