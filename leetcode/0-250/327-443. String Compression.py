# 443. String Compression
class Solution:
    def compress(self, chars) -> int:
        i = j = 0
        
        while j < len(chars):
            if chars[i] != chars[j]:
                if j-i > 1:
                    for c in str(j-i).split():
                        chars[i+1] = c
                        i += 1
                    chars = chars[:i+1] + chars[j:]
                    j = i+1
                i = j
            j += 1
        
        if j-i > 1:
            for c in str(j-i).split():
                chars[i+1] = c
                i += 1
            chars = chars[:i+1] + chars[j:]
        
        print(chars)
        
        return len(chars)

    def compress(self, chars) -> int:
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while i+1 < len(chars) and char == chars[i+1]:
                length, i = length+1, i+1
            chars[left] = char
            if length > 1:
                lenStr = str(length)
                chars[left+1 : left+1+len(lenStr)] = lenStr
                left += len(lenStr)
            left, i = left+1, i+1
        return left

print(Solution().compress(["a","a","b","b","c","c","c"]))