K = 2
A = [[0,0,0,0],[0,0,1,0],[1,0,0,1]]
# A = [[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]]

# memo keeps track of empty plots that are within K distance to at least 1 house
# each plot in memo contains a hashmap where keys are house IDs that are within K distance
memo = {}

def dfs(i, j, dist_left, house_id):
    # check first if valid plot
    if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or dist_left < 0:
        return
    
    # if plot is empty, mark it in memo
    if A[i][j] == 0:
        if (i, j) in memo:
            if house_id not in memo[(i, j)]:
                memo[(i, j)][house_id] = 0
        else:
            memo[(i, j)] = {house_id: 0}
    
    # run dfs on neighboring plots
    dfs(i+1, j, dist_left-1, house_id)
    dfs(i-1, j, dist_left-1, house_id)
    dfs(i, j+1, dist_left-1, house_id)
    dfs(i, j-1, dist_left-1, house_id)
    return


house_count = 0
for r in range(len(A)):
    for c in range(len(A[0])):
        if A[r][c] == 1:
            dfs(r, c, K, (r, c))
            house_count += 1

valid_stores = 0
for plot in memo:
    if len(memo[plot]) == house_count:
        valid_stores += 1
return valid_stores








A = [[15,1,5],[16,3,8],[2,6,4]]

squares = {}
for r in range(len(A)):
    for c in range(len(A[0])):
        squares[(r, c)] = A[r][c]

squares = {k: v for k, v in sorted(squares.items(), key=lambda item: item[1], reverse=True)}





min_cheermote_amount = 1
valid_cheermotes = ['cheer']
messages = 'cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000, cheer4'

res = []
cheermotes = {i: 0 for i in valid_cheermotes}
prev = cheermotes.copy()
msgs = messages.split(',')

for msg in msgs:
    words = msg.strip().split(' ')
    is_valid = True
    total_bits = 0
    
    for word in words:
        cheer = ''
        bits = ''
        for i in range(len(word)):
            if word[i].isdigit():
                bits = word[i:]
                break
            else:
                cheer += word[i]

        if cheer in cheermotes and bits.isdigit():
            cheermotes[cheer] += int(bits)
            total_bits += int(bits)
            if int(bits) < min_cheermote_amount or int(bits) > 10000 or total_bits > 100000:
                # any message which contains one or more Cheers of greater than 10,000 bits should be discarded
                is_valid = False
                
    # if entire message was valid, then we can keep curent log of cheermotes. otherwise, revert back to latest valid one
    if is_valid:
        prev = cheermotes.copy()
    else:
        cheermotes = prev.copy()

# filter out cheers with 0 bits or more than 100,000 bits
cheermotes = {c: b for c, b in sorted(cheermotes.items(), key=lambda item: item[1], reverse=True)}
for c, b in cheermotes.items():
    if b > 0:
        res.append(f'{c}{b}')   

if not res:
    return ['NO_CHEERS']
return res