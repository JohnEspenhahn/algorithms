import csv
import math

class MinHeap:
  def __init__(self):
    self.arr = []

  def insert(self, n):
    self.arr.append(n)
    idx = len(self.arr)-1
    p = self.parent(idx)
    # Bubble up (while still has parent)
    while idx > 0 and self.arr[idx].getValue() < self.arr[p].getValue():
      temp = self.arr[idx]
      self.arr[idx] = self.arr[p]
      self.arr[p] = temp

      idx = p
      p = self.parent(idx)

  def parent(self, idx):
    return math.ceil(idx/2)-1

  def left(self, idx):
    return 2*idx+1

  def right(self, idx):
    return 2*idx+2

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

  def heapify(self, idx):
    min_idx = self.min_child_idx(idx)
    # Bubble down (while still has a child)
    while self.left(idx) < len(self.arr) and self.get(min_idx) < self.get(idx):
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

    left_val = self.get(left_idx)
    right_val = self.get(right_idx)
    if (left_val < right_val):
      return left_idx
    else:
      return right_idx

class Edge:
  def __init__(self, cost, next):
    self.cost = cost
    self.next = next;

  def getValue():
    return self.cost

class Node:
  def __init__(self):
    self.edges = MinHeap()

  def addEdge(cost, next):
    self.edges.insert(Edge(cost, next))

adj_list = None
with open('connectivity_matrix.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    if (adj_list == None):
      adj_list = 