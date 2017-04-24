class Node:
  def __init__(self, name):
    self.name = name
    self.edges = []
    self.color = -1

  def addEdge(self, node):
    self.edges.append(node)

  def startVisiting(self):
    self.color = 0

  def finishVisiting(self):
    self.color = 1

  def isWhite(self):
    return self.color == -1

def graphify(al):
  g = dict()
  for n in al.keys():
    g[n] = Node(n)
  for n,es in al.items():
    for e in sorted(es):
      g[n].addEdge(g[e])
  return g

def dfs(root, finish_cb):
  print('Visit ', root.name)
  root.startVisiting()
  for n in root.edges:
    if (not n.isWhite()): continue
    dfs(n, finish_cb)
  root.finishVisiting()
  print('Finish ', root.name)
  finish_cb(root)

def topo_sort(al, node_order):
  ll = []
  g = graphify(al)
  for n_name in node_order:
    n = g[n_name]
    if (n.isWhite()):
      dfs(n, lambda fn: ll.insert(0,fn.name))
  return ll

"""
print(topo_sort({
    'socks': [ 'shoes' ],
    'watch':  [  ],
    'shoes': [ ],
    'undershorts': [ 'shoes', 'pants' ],
    'pants': [ 'belt', 'shoes' ],
    'belt': [ 'jacket' ],
    'shirt': [ 'tie', 'belt' ],
    'tie': [ 'jacket' ],
    'jacket': [ ]
  }, [ 'shirt', 'watch', 'undershorts', 'socks' ]))
"""
"""
print(topo_sort({
    'm': [ 'x', 'q', 'r' ],
    'n': [ 'q', 'u', 'o' ],
    'o': [ 'r', 's', 'v' ],
    'p': [ 'o', 's', 'z' ],
    'q': [ 't' ],
    'r': [ 'u', 'y' ],
    's': [ 'r' ],
    't': [ ],
    'u': [ 't' ],
    'v': [ 'w', 'x' ],
    'w': [ 'z' ],
    'x': [ ],
    'y': [ 'v' ],
    'z': [ ]
  }, sorted([ 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ])))
  """

print(topo_sort({
    'a': [ 'b' ],
    'b': [ 'c', 'e', 'f' ],
    'c': [ 'd', 'g' ],
    'd': [ 'c', 'h' ],
    'e': [ 'a', 'f' ],
    'f': [ 'g' ],
    'g': [ 'f', 'h' ],
    'h': [ 'h' ]
  }, ['a','b','c','d','e','f','g','h']))