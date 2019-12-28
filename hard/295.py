from heapq import *

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []  # maxheap
        self.large = []  # minheap
        
    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(-self.small[0] + self.large[0]) / 2
        return float(self.large[0])

