import math

def insert(heap, d, val):
  heap.append(val)

  i = len(heap)-1
  p = parent(i,d)
  while (i > 0 and heap[i] >= heap[p]):
    temp = heap[i]
    heap[i] = heap[p]
    heap[p] = temp
    i = p
    p = parent(i,d)

def parent(i, d):
  return math.ceil(i/d) - 1

def extract_max(heap, d):
  if (len(heap) < 1):
    raise "Underflow"

  max = heap[0]
  if (len(heap) > 1):
    heap[0] = heap.pop()
    heapify(0, heap, d)
  else:
    heap.pop();

  return max

def heapify(i, heap, d):
  max_idx, max_val = max_child(i, heap, d)
  if (max_val > heap[i]):
    # Swap
    temp = heap[i]
    heap[i] = max_val
    heap[max_idx] = temp
    # Recurse (can turn tail-recursion into iteration, see MinHeap.heapify in dijkstra for example)
    heapify(max_idx, heap, d)

def max_child(i, heap, d):
  max_val = -1
  max_idx = -1
  # for each child, check if larger
  for j in range(1, d+1):
    idx = i*d + j
    if (idx >= len(heap)):
      break
    elif (heap[idx] > max_val):
      max_val = heap[idx]
      max_idx = idx

  return max_idx, max_val