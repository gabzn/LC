https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for part in parts:
            # print(part)
            if part == "..":
                if stack:
                    stack.pop()
                continue

            if part and not (len(part) == 1 and part[0] == "."):
                stack.append(part)

        return "/" + "/".join(stack)
