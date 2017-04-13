import csv
import math
import random


class MinHeap:
  def __init__(self, arr = []):
    self.arr = arr
    self.build_heap()

  def insert(self, n): # ! n must have a function "getCost()"
    self.arr.append(n)
    idx = len(self.arr)-1
    self.bubbleUp(idx)

  def decrease_key(self, idx, new_cost):
    if next_cost > self.arr[idx].getCost():
      raise "Increased key in decrease_key!"

    self.arr[idx].setCost(new_cost)
    self.bubbleUp(idx)

  def find_idx(self, targ): # ! n must have a function "getCost()"
    idx = 0
    node = self.arr[idx]
    while True: # Assume it is in the heap
      if (node == targ):
        return idx

      if (node.getCost() > targ.getCost()):
        idx = self.right(idx)
        node = self.arr[idx]
      else:
        idx = self.left(idx)
        node = self.arr[idx]


  def extract_min(self):
    if (len(self.arr) < 1):
      raise "Underflow"

    min = self.arr[0]
    
    # Maintain heap propety
    if (len(self.arr) > 1):
      self.arr[0] = self.arr.pop()
      self.heapify(0)
    else:
      self.arr.pop()

    return min

  def bubbleUp(self, idx):
    p = self.parent(idx)
    # Bubble up (while still has parent)
    while idx > 0 and self.arr[idx].getCost() < self.arr[p].getCost():
      temp = self.arr[idx]
      self.arr[idx] = self.arr[p]
      self.arr[p] = temp

      idx = p
      p = self.parent(idx)

  def build_heap(self):
    for idx in range(math.floor(len(self.arr)/2)-1,0,-1):
      self.heapify(idx)

  def parent(self, idx):
    return math.ceil(idx/2)-1

  def left(self, idx):
    return 2*idx+1

  def right(self, idx):
    return 2*idx+2

  def heapify(self, idx):
    min_idx = self.min_child_idx(idx)
    # Bubble down (while still has a child)
    while self.left(idx) < len(self.arr) and self.arr[min_idx].getCost() < self.get[idx].getCost():
      # Move the actual object
      temp = self.arr[idx]
      self.arr[idx] = self.arr[min_idx]
      self.arr[min_idx] = temp

      idx = min_idx
      min_idx = self.min_child_idx(idx)

  def min_child_idx(self, idx):
    left_idx = self.left(idx)
    if (left_idx >= len(self.arr)):
      raise "Index out of bounds"

    right_idx = self.right(idx)
    if (right_idx >= len(self.arr)): 
      return left_idx

    left_val = self.arr[left_idx].getCost()
    right_val = self.arr[right_idx].getCost()
    if (left_val < right_val):
      return left_idx
    else:
      return right_idx

class Edge:
  def __init__(self, cost, next):
    self.cost = cost
    self.next = next;

  def getCost(self):
    return self.cost

class Node:
  def __init__(self, idx, cost=math.inf):
    self.idx = idx
    self.edges = []
    self.cost = cost

    self.visited = False
    self.previous = None

  def getIdx(self):
    return self.idx

  def addEdge(self, edge):
    self.edges.append(edge)

  def getCost(self):
    return self.cost

  def setCode(self, cost):
    self.cost = cost

  def setPrevious(self, prev):
    self.previous = prev

  def setVisited(self):
    self.visited = True

  def isVisited(self):
    return self.visited

# Load adjacency list
def load_heap(start_idx):
  adj_list = None
  with open('connectivity_matrix.csv', 'r') as file:
    row_idx = 0
    reader = csv.reader(file)
    for cols in reader:
      # Init
      if (adj_list == None):
        adj_list = [] # Use to add edges
        for idx in range(0,len(cols)):
          # Generate a random number if not start to try and get a sorta balanced tree
          cost = (0.0 if (idx == start_idx) else float(2**20 + random.randint(1,15000000)))
          adj_list.append(Node(idx, cost))

      for col_idx, c in enumerate(cols):
        cost = float(c)
        if (cost <= 1e-10): continue;

        adj_list[row_idx].addEdge(Edge(cost, adj_list[col_idx]))
        
      row_idx += 1

    return MinHeap(adj_list)

# Dijkstra
def dijkstra(heap, start_idx, end_idx):
  node = heap.extract_min()
  start_node = node
  if (start_node.getIdx() != start_idx):
    raise "Incorrect setup!"  # Start must have cost set to 0 before calling

  end_node = None
  while True:
    node.setVisited()
    for edge in node.edges:
      next = edge.next
      if next.isVisited(): continue

      # Update cost
      if (node.getCost() + edge.getCost() < next.getCost()):
        next.setPrevious(node)
        idx = heap.find_idx(next)
        new_cost = node.getCost() + edge.getCost()
        heap.decrease_key(idx, new_cost)

    # If visited end, we're done
    if (node.getIdx() == end_idx):
      end_node = node
      break
    else:
      node = heap.extract_min()

  res = [ start_node.getIdx() ]

  node = start_node
  while (node.next != end_node):
    node = node.next
    res.append(node.getIdx())

  res.append(end_node.getIdx())

  return res

# Execute
start_node = 61
end_node = 151

start_idx = start_node-1
end_idx = end_node-1
print(dijkstra(load_heap(start_idx), start_idx, end_idx))