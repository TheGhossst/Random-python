class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            print(f"\nright -> {right}")
            print(f"s[right] - > {s[right]}")
            
            if s[right] in char_index_map:
                left = max(left, char_index_map[s[right]] + 1)
                print(f"left -> {left}")
                
            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
            
            print(f"left -> {left}")
            print(f"max_len -> {max_length}")
            print(f"char_map -> {char_index_map}")

        return max_length
    
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("acbdeac"))