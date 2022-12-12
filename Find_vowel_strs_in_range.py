Given a list of string, sArr, and a list of query, queries.
Find the number of string that starts with a vowel and ends with a vowel in a given range in queries.  

def find_vowel_strs_in_range(sArr, queries):
    vowels_set = set('aeiou')
    answer = []

    # Go through each string to check if it starts with a vowel and ends with a vowel.
    is_vowel = [0] * len(sArr) 
    for ind, s in enumerate(sArr):
        if s[0] in vowels_set and s[-1] in vowels_set:
            is_vowel[ind] = 1
    print(is_vowel)

    # Build the prefix sum of is_vowel for range search.
    # A given index in prefix_sum_list tells us the sum of all the previous values including the current index.
    prefix_sum_list = [is_vowel[0] for i in range(len(is_vowel))]
    for ind in range(1, len(prefix_sum_list)):
        prefix_sum_list[ind] = prefix_sum_list[ind-1] + is_vowel[ind]  
    print(prefix_sum_list)

    # Go through each query to find the answer.
    for query in queries:
        query = query.split('-')
        start, end = int(query[0]) - 1, int(query[1]) - 1

        if start != 0:
            answer.append(prefix_sum_list[end] - prefix_sum_list[start-1])
        else:
            answer.append(prefix_sum_list[end])

    return answer
    
    # [1,      0,     1,     1,    1,    0,     0,     1,     0,     1,    1,     0,     0,    0,    1]
s = ['aba', 'bcb', 'ece', 'aa', 'e', 'asd', 'fxs', 'aoe', 'fjs', 'iau', 'eie', 'diu', 'ni', 'sb', 'iou']    
print(find_vowel_strs_in_range(s, ['1-3', '2-5', '2-2', '1-12', '10-10', '13-15']))
