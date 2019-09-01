class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return address.replace('.', '[.]')
        return '[.]'.join(address.split('.'))