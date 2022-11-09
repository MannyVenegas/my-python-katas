
import re
def count_smileys(arr):
    return len(re.findall(r"[:;][-~]?[)D]","".join(arr)))
    print (len(re.findall(r"[:;][-~]?[)D]","".join(arr))))
count_smileys([':D',':~)',';~D',':)'])
