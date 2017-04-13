# Recursive Programming Example
def rodcutting(P):
  CUT = [0]*len(P)
  VAL = [0]*len(P)
  for i in range(1,len(P)):
    VAL[i] = P[i]
    CUT[i] = i
    for j in range(1,i):
      temp = VAL[j] + VAL[i-j];
      if temp > VAL[i]:
        CUT[i] = j
        VAL[i] = temp
  return CUT

print(rodcutting([ -1, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30 ]))