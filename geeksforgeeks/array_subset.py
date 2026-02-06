# https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1

def isSubset( a1, a2, n, m):
    from collections import Counter
    c1 = Counter(a1)
    c2 = Counter(a2)
    
    for k, v in c2.items():
        if c1[k] < v:
            return "No"
    return "Yes"
