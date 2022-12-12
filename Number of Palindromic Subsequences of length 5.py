Given a binary string that consists of only '1's and '0's.
Find the number of palindromic substring that has a length of 5.
Goldman Sachs OAs

https://jtuto.com/number-of-palindromic-subsequences-of-length-5-in-binary-string/
  
def getPalindromesCount(s):
    counter = Counter([''])
    res = 0

    for char in s:
        for substring, count in list(counter.items()):
            substring += char

            if len(substring) < 5:
                counter[substring] += count
                continue

            if substring == substring[::-1]:
                res += count
    
    return res
