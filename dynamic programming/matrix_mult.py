from __future__ import print_function

# [ 100x10 10x50 50x20 20x5 ]
# [ 100, 10, 50, 20, 5 ]
# [ R1, R2, R3, ..., Ri, Ci ]
def matrix_mult(M):
	num_matrix = len(M)-1
	cost = [ [float('inf')]*len(M) for i in range(len(M)) ]
	splits = [ [0]*len(M) for i in range(len(M)) ]

	for i in range(len(cost)): # self mult is free
		cost[i][i] = 0

	for d in range(1, num_matrix): # distance
		for s in range(1, num_matrix-d+1): # start
			e = s+d
			for k in range(s, s+d): # split position
				# printrange(s,k)
				# printrange(k+1,e)
				# print()
				
				old = cost[s][e]
				new = cost[s][k] + cost[k+1][e] + M[s-1]*M[k]*M[e]
				if (new < old):
					cost[s][e] = new
					splits[s][e] = k

	# print("Cost")
	# print_m(cost)

	# print_m(splits)

	print("cost = ", cost[1][num_matrix])

	print_parens(splits, 1, num_matrix)
	print()

to_print = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' ];
def print_parens(splits, x, y):
	if (x != y):
		print('(',end='')
		print_parens(splits, x, splits[x][y])
		print_parens(splits, splits[x][y]+1, y)
		print(')',end='')
	else:
		print(to_print[x-1],end='')


def print_m(A):
	print(' \tA\tB\tC\tD')
	for row in A:
		for val in row:
			print('{:4}\t'.format(val), end='')
		print()


def printrange(s, e):
	print('(', end='')
	for i in range(s-1,e):
		print(to_print[i], end='')
	print(')', end='')
				

matrix_mult([ 10, 100, 20, 5, 80 ])

