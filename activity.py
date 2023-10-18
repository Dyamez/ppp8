"""
V (list) : The nodes that have been visited, in visitation order.
S (stack): The nodes to be visited, in the order that they were discovered. 
     Recall that a stack is a FILO data structure.
M (set): The nodes that have been visited, or that are marked to be visited. 
     This is the union of the nodes in V and S.
"""

"""
Depth-first search

S.add(root)
M.add(root)

while not isempty(S):
	cur = S.pop()
	if cur == to_find:
    	return True #we have found what we were looking for
          
	V.append(cur)
	for child in cur.children:
		if child not in M:
	    	S.add(child)
			M.add(child)

return False #element is not in tree
"""

from collections import deque


class Node:
    def __init__(self, key):
        if key == 'null':
            self.data = None
        else:
            self.data = key
        self.left = None
        self.right = None

def level_max(root):
    
    Q = deque()
    V = []
    M = set()
    levels = []

    Q.appendleft(root)

    while len(Q) != 0:
        level = 0
        for el in range(len(Q)):
            cur = Q.pop()
            V.append(cur)

            if cur.data > level:
                level = cur.data
            for child in [cur.left, cur.right]:
                if child not in M and child  != None:
                    Q.appendleft(child)
                    M.add(child)
            levels.append(level)
        return levels






       
def max_levels(arr):
    levels = 0
    for i in range(10):
        if len(arr) == 2 ** i - 1:
            levels = i + 1
            break

    root = Node(arr[0])
    root.left = Node(arr[1])
    root.right = Node(arr[2])
    root.left.left = Node(arr[3])
    root.left.right = Node(arr[4])
    root.right.left = Node(arr[5])
    root.right.right = Node(arr[6])

    print(level_max(root))

max_levels([5, 3, 8, 2, 4, 'null', 9])
