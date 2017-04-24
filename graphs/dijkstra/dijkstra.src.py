import csv
import math
import random
import time
from collections import deque

class MinHeap:
  def __init__(self, arr = []):
    self.arr = arr
    self.build_heap() # build from an array
    # self.print()

  def insert(self, n): # ! n must be Node
    self.arr.append(n)
    
    idx = len(self.arr)-1
    n.setHeapIdx(idx)

    self.bubbleUp(idx)

  def decrease_key(self, idx, new_cost):
    if new_cost > self.arr[idx].getCost():
      raise Exception("Increased key in decrease_key!")

    self.arr[idx].setCost(new_cost)
    self.bubbleUp(idx)

  def extract_min(self):
    if (len(self.arr) < 1):
      raise Exception("Underflow")

    min = self.arr[0]
    
    # Maintain heap propety
    if (len(self.arr) > 1):
      self.arr[0] = self.arr.pop().setHeapIdx(0)
      self.heapify(0)
    else:
      self.arr.pop() # If array will be empty, cannot heapify

    return min

  def bubbleUp(self, idx):
    p = self.parent(idx)
    # Bubble up (while still has parent)
    while idx > 0 and self.arr[idx].getCost() < self.arr[p].getCost():
      temp = self.arr[idx]
      self.arr[idx] = self.arr[p].setHeapIdx(idx)
      self.arr[p] = temp.setHeapIdx(p)

      idx = p
      p = self.parent(idx)

  def build_heap(self):
    for idx, node in enumerate(self.arr):
      node.setHeapIdx(idx)

    for idx in range(math.floor(len(self.arr)/2)-1,-1,-1):
      self.heapify(idx)

  def parent(self, idx):
    return math.ceil(idx/2)-1

  def left(self, idx):
    return 2*idx+1

  def right(self, idx):
    return 2*idx+2

  def heapify(self, idx):
    # Bubble down (while still has a child)
    while self.left(idx) < len(self.arr):
      min_idx = self.min_child_idx(idx)

      if self.arr[min_idx].getCost() < self.arr[idx].getCost():
        # Move the actual object
        temp = self.arr[idx]
        self.arr[idx] = self.arr[min_idx].setHeapIdx(idx)
        self.arr[min_idx] = temp.setHeapIdx(min_idx)
        idx = min_idx
      else:
        break

  def min_child_idx(self, idx):
    left_idx = self.left(idx)
    if (left_idx >= len(self.arr)):
      raise Exception("Index out of bounds")

    # Might not have right child
    right_idx = self.right(idx)
    if (right_idx >= len(self.arr)): 
      return left_idx

    left_val = self.arr[left_idx].getCost()
    right_val = self.arr[right_idx].getCost()
    if (left_val < right_val):
      return left_idx
    else:
      return right_idx

  def print(self):
    print(",".join(map((lambda n: str(n)), self.arr)))

class Edge:
  def __init__(self, cost, start, end):
    self.cost = cost
    self.start = start
    self.end = end

  def getCost(self):
    return self.cost

  def __str__(self):
    return str(self.end.getNodeIdx()+1)

class Node:
  def __init__(self, nodeIdx, cost=math.inf):
    self.nodeIdx = nodeIdx
    self.heapIdx = -1
    self.edges = []
    self.cost = cost

    self.visited = False
    self.previous = None

  def getNodeIdx(self):
    return self.nodeIdx

  def getHeapIdx(self):
    return self.heapIdx

  # Keep track of this node's position in the heap to avoid searching in decrease_key
  def setHeapIdx(self, heap_idx):
    self.heapIdx = heap_idx
    return self # Return self for easier linking

  def addEdge(self, edge):
    self.edges.append(edge)

  def getCost(self):
    return self.cost

  def setCost(self, cost):
    self.cost = cost

  # For reconstructing shortest path
  def setInEdge(self, prev):
    self.previous = prev

  # For reconstructing shortest path
  def getInEdge(self):
    return self.previous

  def setVisited(self):
    self.visited = True

  def isVisited(self):
    return self.visited

  def print(self):
    print(str(self.getNodeIdx()+1) + " -> " + (",".join(map((lambda e: str(e)), self.edges))))

  def __str__(self):
    return "%s(%s:%s)" % (self.getNodeIdx()+1,self.getHeapIdx(),self.getCost())

# Load adjacency list
def load_heap(start_idx):
  # print("Loading with start idx %s" % start_idx)

  adj_list = None
  with open('connectivity_matrix.csv', 'r') as file:
    row_idx = 0
    reader = csv.reader(file)
    for cols in reader:
      # Init
      if (adj_list == None):
        adj_list = [] # Use to add edges
        for nodeIdx in range(0,len(cols)):
          # Generate a random number if not start to try and get a sorta balanced tree
          cost = (0.0 if (nodeIdx == start_idx) else 1000000)
          adj_list.append(Node(nodeIdx, cost))

      # Read all edges for this node (row)
      for col_idx, c in enumerate(cols):
        cost = float(c)
        if (cost <= 1e-10): continue;

        start = adj_list[row_idx]
        start.addEdge(Edge(cost, start, adj_list[col_idx]))

      row_idx += 1

    return MinHeap(adj_list)

# Dijkstra
def dijkstra(heap, start_idx, end_idx):
  time_dijkstra = time.time() # Timing

  node = heap.extract_min()
  start_node = node
  if (start_node.getNodeIdx() != start_idx):
    raise Exception("Incorrect setup!")  # Start must have cost set to 0 before calling

  end_node = None
  while True:
    node.setVisited() # make black
    for edge in node.edges:
      next = edge.end
      if next.isVisited(): continue

      # Relax
      if (node.getCost() + edge.getCost() < next.getCost()):
        next.setInEdge(edge) # Keep track of the shortest path
        heap_idx = next.getHeapIdx()
        new_cost = node.getCost() + edge.getCost()
        heap.decrease_key(heap_idx, new_cost)

    # If visited end, we're done
    if (node.getNodeIdx() == end_idx):
      end_node = node
      break
    else:
      node = heap.extract_min()

  # Rebuild the shortest path using "inEdge" starting at the dest node
  cost = 0
  res = deque()
  
  edge = end_node.getInEdge()
  res.appendleft(end_node.getNodeIdx()+1)
  while (edge.start != start_node):
    cost += edge.getCost()
    res.appendleft(edge.start.getNodeIdx()+1) # Convert from idx to number
    edge = edge.start.getInEdge()
  cost += edge.getCost()
  res.appendleft(start_node.getNodeIdx()+1) # Convert from idx to number

  # Time
  end_dijkstra = time.time()
  # print("Elapsed time for just dijkstra was %g seconds" % (end_dijkstra - time_dijkstra))
  
  print("Cost = %s" % cost)
  return res

# Execute
start_node = int(input("Start node: "))
end_node = int(input("End node: "))

start_idx = start_node-1
end_idx = end_node-1

start_time = time.time()
if (start_node == end_node):
  print([ start_node ])
else:
  print(dijkstra(load_heap(start_idx), start_idx, end_idx))

end_time = time.time()
# print("Elapsed time was %g seconds" % (end_time - start_time))