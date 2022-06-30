# O(n+m)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a = len(nums1)
        b = len(nums2)
        total = a + b
        # e.g. 5 + 5 = 10
        # idx = 6
        idx = total // 2 + 1
        even = total % 2 == 0
        
        # current and previous
        num1 = num2 = j = k = 0

        for i in range(idx):
            num2 = num1
            if j < a and k < b:
                if nums1[j] > nums2[k]:
                    num1 =  nums2[k]
                    k += 1
                else:
                    num1 =  nums1[j]
                    j += 1
            else:
                if j < a:
                    num1 = nums1[j]
                    j += 1
                else:
                    num1 = nums2[k]
                    k += 1

        if even:         
            return (num1 + num2) / 2
        else:
            return num1
