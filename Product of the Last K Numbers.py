https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    def __init__(self):
        self.s = [1]        

    def add(self, num: int) -> None:
        # If we see any 0, discard everything except for the very first 1
        if num == 0:
            while len(self.s) > 1:
                self.s.pop()
        else:
            # Prefix-product
            if len(self.s) == 1:
                self.s.append(num)
            else:
                self.s.append(self.s[-1] * num)

    def getProduct(self, k: int) -> int:
        size = len(self.s)
        if size == 1 or k > size - 1:
            return 0

        i = size - k
        last = self.s[-1]
        return last // self.s[i - 1]

# [1, 2, 10, 3, 4, 2]
# [1, 2, 20, 60, 240, 480]
# size - k = i
# [-1] / [i - 1] = product of last k
