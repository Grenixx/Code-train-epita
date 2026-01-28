nums1 = [-1,0,0,2,5,1,0,5,0]
m = 8
nums2 = [3,2,1,0,0,0]
n = 3
def merge(nums1, m, nums2, n):
    while len(nums1) != m:
        nums1.pop(m) 
    while len(nums2) != n:
        nums2.pop(n) 
    nums1.extend(nums2)
    nums1.sort()

merge(nums1, m, nums2, n)
print(nums1)


