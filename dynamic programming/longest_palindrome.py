def find_longest(s):
	"""
	:type s: str
	:rtype: int
	"""
	p = [[0]*len(s) for i in range(len(s))]
	max_lng = 0
	max_start = 0
	max_end = 0

	for lng in range(0,len(s)):
		for i in range(0,len(s)-lng):
		    j = i + lng
		    if (lng == 0):
		        p[i][j] = True
		    elif (lng == 1):
		        p[i][j] = (s[i] == s[j])
		    else:
		        p[i][j] = (s[i] == s[j] and p[i+1][j-1])
		        
		    if p[i][j] and lng > max_lng:
		        max_lng = lng
		        max_start = i
		        max_end = j
		
	return s[max_start:max_end+1]


print(find_longest("cbbd"))
