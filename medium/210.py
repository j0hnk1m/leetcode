numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

# graph (prereq -> course) + dfs + stack
import collections
adj_list = collections.defaultdict(list)
for c, pre in prerequisites:
    adj_list[pre].append(c)

stack = []
cycle = False
added = {k: 0 for k in range(numCourses)}  # 0 = not seen, 1 = visited, 2 = added to stack
def dfs(node):
    global cycle
    if cycle:
        return
    
    added[node] = 1
    if node in adj_list:
        for neighbor in adj_list[node]:
            if added[neighbor] == 0:
                dfs(neighbor)
            elif added[neighbor] == 1:
                cycle = True
    added[node] = 2
    stack.append(node)

for i in range(numCourses):
    if added[i] == 0:
        dfs(i)

if cycle:
    return []
return stack[::-1]
