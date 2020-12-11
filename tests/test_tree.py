import sys
sys.path.append('src')
from tree import *

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]

tree = Tree(edges)

tree.build_from_edges()

print("Testing that Tree class works...")
assert tree.root.value == 'e'
assert [node.value for node in tree.root.children]==['g', 'i', 'a']
assert [node.value for node in tree.root.children[0].children]==['b']
assert [node.value for node in tree.root.children[1].children]==[]
assert [node.value for node in tree.root.children[2].children]==['c', 'd']
assert [node.value for node in tree.root.children[0].children[0].children]==[]
assert [node.value for node in tree.root.children[2].children[0].children]==['k']
assert [node.value for node in tree.root.children[2].children[1].children]==['f', 'j']
assert [node.value for node in tree.root.children[2].children[0].children[0].children]==[]
assert [node.value for node in tree.root.children[2].children[1].children[0].children]==['h']
assert [node.value for node in tree.root.children[2].children[1].children[1].children]==[]
assert [node.value for node in tree.root.children[2].children[1].children[0].children[0].children]==[]
print("PASSED")
