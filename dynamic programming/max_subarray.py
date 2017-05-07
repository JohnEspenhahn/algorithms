# Most intuitive (to me) verion
def max_subarray_verbose(A):
	max_upto = [0]*len(A)
	max_upto_k_starts = [0]*len(A)
	max_upto_k_ends = [0]*len(A)

	max_upto[0] = A[0]
	max_upto_k_starts[0] = 0
	max_upto_k_ends[0] = 0

	max_ending_at = [0]*len(A)
	max_ending_at_k_starts = [0]*len(A)

	max_ending_at[0] = A[0]
	max_ending_at_k_starts[0] = 0

	for k in range(1,len(A)):
		if (max_ending_at[k-1]+A[k] > A[k]):
			# Best is max subarray ending at k-1 plus k
			max_ending_at[k] = max_ending_at[k-1]+A[k]
			max_ending_at_k_starts[k] = max_ending_at_k_starts[k-1]
		else:
			# Best is to restart with k
			max_ending_at[k] = A[k]
			max_ending_at_k_starts[k] = k
			

		if (max_ending_at[k] > max_upto[k-1]):
			# Found new global best
			max_upto[k] = max_ending_at[k]
			max_upto_k_starts[k] = max_ending_at_k_starts[k]
			max_upto_k_ends[k] = k
		else:
			# Global best is same as previous step
			max_upto[k] = max_upto[k-1]
			max_upto_k_starts[k] = max_upto_k_starts[k-1]
			max_upto_k_ends[k] = max_upto_k_ends[k-1]

	end = len(A)-1
	print(max_ending_at)
	print(max_upto)
	print("Best " + str(max_upto[end]) + ": " + str(max_upto_k_starts[end]) + "..." + str(max_upto_k_ends[end]));
#
# First optimization step
#   remove keeping track of global best at every step (it is global so only need at current step)
#
def max_subarray_onemax(A):
	max_val = A[0]
	max_start = 0
	max_end = 0

	max_ending_at = [0]*len(A)
	max_ending_at_k_starts = [0]*len(A)

	max_ending_at[0] = A[0]
	max_ending_at_k_starts[0] = 0

	for k in range(1,len(A)):
		if (max_ending_at[k-1]+A[k] > A[k]):
			# Best is max subarray ending at k-1 plus k
			max_ending_at[k] = max_ending_at[k-1]+A[k]
			max_ending_at_k_starts[k] = max_ending_at_k_starts[k-1]
		else:
			# Best is to restart with k
			max_ending_at[k] = A[k]
			max_ending_at_k_starts[k] = k
			
		if (max_ending_at[k] > max_val):
			# Found new global best
			max_val = max_ending_at[k]
			max_start = max_ending_at_k_starts[k]
			max_end = k

	print("Best " + str(max_val) + ": " + str(max_start) + "..." + str(max_end));

#
# Second optimization step
#   only need to save last step
#
def max_subarray(A):
	max_val = A[0]
	max_start = 0
	max_end = 0

	max_ending_here = A[0]
	max_ending_here_starts = 0

	for k in range(1,len(A)):
		if (max_ending_here+A[k] > A[k]):
			# Best is max subarray ending at k-1 plus k
			max_ending_here += A[k]
		else:
			# Best is to restart with k
			max_ending_here = A[k]
			max_ending_here_starts = k
			
		if (max_ending_here > max_val):
			# Found new global best
			max_val = max_ending_here
			max_start = max_ending_here_starts
			max_end = k

	print("Best " + str(max_val) + ": " + str(max_start) + "..." + str(max_end));

max_subarray([ -2, 1, -3, 4, -1, 2, 1, -5, 4 ])

