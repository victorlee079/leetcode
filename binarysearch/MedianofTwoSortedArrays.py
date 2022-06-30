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
        
    # O(log(n+m))
    def findMedianSortedArraysBS(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        # when total length is odd, the median is the middle
        if (len1 + len2) % 2 != 0:
            return self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
        else:
        # when total length is even, the median is the average of the middle 2
            middle1 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
            middle2 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2-1)
            return (middle1 + middle2) / 2

    def get_kth(self, nums1, nums2, start1, end1, start2, end2, k):
        if start1 > end1:
            return nums2[k-start1]
        if start2 > end2:
            return nums1[k-start2]
        
        middle1 = (start1 + end1) // 2
        middle2 = (start2 + end2) // 2
        middle1_value = nums1[middle1]
        middle2_value = nums2[middle2]
        
        # if sum of two median's indicies is smaller than k
        if (middle1 + middle2) < k:
            # if nums1 median value bigger than nums2, then nums2's first half will always be positioned before nums1's median, so k would never be in num2's first half
            if middle1_value > middle2_value:
                return self.get_kth(nums1, nums2, start1, end1, middle2+1, end2, k)
            else:
                return self.get_kth(nums1, nums2, middle1+1, end1, start2, end2, k)
        # if sum of two median's indicies is bigger than k
        else:
            # if nums1 median value bigger than nums2, then nums2's first half would be merged before nums1's first half, thus k always come before nums1's median, then nums1's second half would never include k
            if middle1_value > middle2_value:
                return self.get_kth(nums1, nums2, start1, middle1-1, start2, end2, k)
            else:
                return self.get_kth(nums1, nums2, start1, end1, start2, middle2-1, k)
