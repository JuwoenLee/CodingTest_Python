from collections import deque
import sys
input = sys.stdin.readline

def preO(tree, node) :
    if node == '.' :
        return 
    
    print(node, end='')
    preO(tree, tree[node][0])
    preO(tree, tree[node][1])

def inO(tree, node) :
    if node == '.' :
        return
    
    inO(tree, tree[node][0])
    print(node, end='')
    inO(tree, tree[node][1])

def postO(tree, node) :
    if node == '.' :
        return
    
    postO(tree, tree[node][0])
    postO(tree, tree[node][1])
    print(node, end='')

n = int(input())
tree = {}

for _ in range(n) :
    parent, left, right = input().split()
    tree[parent] = (left, right)

preO(tree, 'A')
print()

inO(tree, 'A')
print()

postO(tree, 'A')
print()