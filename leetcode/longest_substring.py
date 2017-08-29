class Solution(object):
    def noRepeating(self, s):
        return len(set(s)) == len(s)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        max_substring = 1

        ptr_one = 0
        ptr_two = 1

        while ptr_two <= len(s):
            sub_string = s[ptr_one:ptr_two]
            if self.noRepeating(sub_string):
                if len(sub_string) > max_substring:
                    max_substring = len(sub_string)
                ptr_two += 1
            else:
                ptr_one += 1

        return max_substring

sol = Solution()

print(sol.lengthOfLongestSubstring("au"))