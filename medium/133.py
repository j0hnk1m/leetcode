class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

import collections

if not node:
    return 

ncopy = Node(node.val, [])
graph = {node: ncopy}
q = collections.deque([node])
while q:
    node = q.popleft()
    for i in node.neighbors:
        if i not in graph:  # neighbor is not visited
            graph[i] = Node(i.val, [])
            q.append(i)
        graph[node].neighbors.append(graph[i])
return ncopy
