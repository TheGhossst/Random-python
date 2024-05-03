class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        for word in words:
            if word not in d.keys():
                d[word] = 1
            else:
                d[word] += 1
        sorted_items = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        print(sorted_items)
        top_k_words = [item[0] for item in sorted_items[:k]]

        return top_k_words

if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    solution = Solution()
    result = solution.topKFrequent(words, k)
    print(result)