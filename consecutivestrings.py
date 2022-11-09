#You are given an array(list) strarr of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array
def longest_consec(strarr,k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""

    result = ""
    if k > 0 and len(strarr) >= k:
        for i in range(len(strarr) - k + 1):
            s = "".join(strarr[i:i+k])
        if len(s) > len(result):
            result = s
    return result
