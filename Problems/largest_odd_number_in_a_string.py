class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        if int(num) % 2 == 1:
            return num
        if not num:
            return ""
        
        for i in range(len(num) - 1, -1 , -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]

        return ""

if __name__ == "__main__":
    s = Solution()
    print(s.largestOddNumber("154896370")) 