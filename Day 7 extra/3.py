def strStr( haystack, needle):
        str_len = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            word = haystack[i:i+len(needle)]
            if word == needle:
                return i
        return -1

haystack = "sad"
needle = "ssadbutsad"

print(strStr(haystack, needle)) # Output: -1

# haystack , needle = list(haystack , needle)
# print("Haystack : ", haystack)
# print("Needle  : ", needle)
# # for i in haystack:
# #     if  haystack.index(i) == needle.index(i):
# #         print("Found needle at position", haystack.index(i))

# x = haystack.index(needle)

# print(x)

