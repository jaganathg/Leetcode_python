from collections import Counter

def intersect( nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    c1 = Counter(nums1)
    c2 = Counter(nums2)
    
    for i in c1:
        if i in c2:
            min_count = min(c2[i], c1[i])
            res.extend([i] * min_count)
    return res


if __name__=="__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(intersect(nums1, nums2))
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersect(nums1, nums2))
   