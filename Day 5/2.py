class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        i = 0
        res = ""
        while i < len(strs[0]):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
            i += 1

        return res
    

strs = ["ab", "a"]
print(longestCommonPrefix(strs)) 
