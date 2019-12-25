matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

prev = None
for i in matrix:
    if prev:
        if i[1:] != prev:
            return False
    prev = i[:-1]
return True
