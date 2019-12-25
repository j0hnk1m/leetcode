input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"

max_len = 0
lvl = {-1: 0}

for line in input.split('\n'):
    depth = line.count('\t')
    lvl[depth] = lvl[depth - 1] + len(line) - depth

    if '.' in line:
        max_len = max(max_len, lvl[depth] + depth)

return max_len
