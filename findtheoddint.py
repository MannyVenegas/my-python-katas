#Given an array of integers, find the one that appears an odd number of times.
#[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time
#(which is odd).
def find_oddint(arr):
    for i in arr:
        if arr.count(i) % 2 != 0:
            result = i
        else:
            continue
    return result

find_oddint([1,1,2,-2,5,2,4,4,-1,-2,5])