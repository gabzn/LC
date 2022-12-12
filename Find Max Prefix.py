arr = [-6,3,4,-10]

def find_max_pos_prefix(arr):
    arr.sort(reverse=True)
    running_sum = 0
    res = 0

    for num in arr:
        running_sum += num
        if running_sum > 0:
            res += 1
        else:
            break

    return res

print(find_max_pos_prefix(arr))
