class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        mappings = {3: 'Fizz', 5: 'Buzz'}
        out = []
        for i in range(1, n+1):
            add = ""
            for j in mappings:
                if i % j == 0:
                    add += mappings[j]
            if not add:
                add = str(i)
            out.append(add)
        
        return out