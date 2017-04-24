class Item:
	def __init__(self, weight, value):
		self.weight = weight
		self.value = value

	def __str__(self):
		return str((self.weight, self.value))

class Path:
	def __init__(self, idx, value, previous):
		self.idx = idx
		self.value = value
		self.previous = previous
EmptyPath = Path(-1,0,None)
		

# Recursive solution O(2^n)
def recurse(weight, items, n):
	# print('Items ' + ' '.join(str(x) for x in items) + '; Weight ' + str(weight))

	val = 0
	for idx in range(n):
		item = items[idx]
		if (item.weight > weight): continue # Not enough room
		val = max(val, item.value + recurse(weight-item.weight, items, n-1))
	# print('Value ' + str(val))
	return val

# O(max_weight * ||items||)
def dynamic(max_weight, items):
	saved = [ [EmptyPath]*(len(items)+1) for _ in range(max_weight+2) ]

	# weight is avaliable weight in the sack (need to include max_weight)
	bestpath = EmptyPath
	for weight in range(1,max_weight+1):
		# n is number of items
		# Start with just one item, then one step at a time add another item
		for n in range(1,len(items)):
			idx = n-1
			item = items[idx] # item being added
			if (item.weight > weight): 
				saved[weight][n] = saved[weight][n-1] # Can't add item because it's too heavy
			else: 
				# Decide if should add
				skip = saved[weight][n-1]
				add = saved[weight-item.weight][n-1]
	
				if (skip.value > item.value + add.value):
					saved[weight][n] = skip
				else:
					path = Path(idx, item.value + add.value, add)
					saved[weight][n] = path
					if (path.value > bestpath.value):
						bestpath = path
			# print2d(saved)

	# Recreate path
	res_val = bestpath.value
	res_arr = [ ]
	while bestpath.previous != None:
		res_arr.append(bestpath.idx)
		bestpath = bestpath.previous

	return (res_val, res_arr)
	
			

def print2d(A):
	for row in A:
		for val in row:
		    print '{:4}'.format(val),
		print
	print('------')

W = 5
S = [ Item(5,6), Item(3,4), Item(2,3), Item(4,5) ]
print(recurse(W,S,len(S)))

val, arr = dynamic(W,S)
print(val)
print(arr)
