class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        
        used = {}
        window_start = 0
        window_end = 0
        ans = 0

        while window_start != len(s) and window_end != len(s):
            if s[window_end] not in used:
                used[s[window_end]] = window_end
                window_end += 1
                if window_end - window_start > ans:
                    ans = window_end - window_start
            else:
                del used[s[window_start]]
                window_start += 1 

        return ans