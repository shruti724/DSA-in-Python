class Solution:

    def isClose(self, s: str) -> bool:
        stack = []
        hashMap = {")": "(", "]": "[", "}": "{"}

        for b in s:
            if b in hashMap:
                if stack and stack[-1] == hashMap[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return True if not stack else False


s1 = Solution()
s = "()["
print(s1.isClose(s))
