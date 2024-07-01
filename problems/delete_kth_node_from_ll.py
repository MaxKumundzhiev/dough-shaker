# class Solution:
#     def getLength(self, head) -> int:
#         current = head
#         if head.next is None:
#             return 1
#         counter = 1
#         while current is not None:
#             current = current.next
#             counter += 1
#         return counter
    
#     def removeNthFromEnd(self, head, n):
        
#         if n == 1:
#             head = None
#             return head
            
#         idx, current = 1, head
        
#         length = self.getLength(head=current)
#         idx_to_delete = (length - n) + 1
        
#         while current is not None and idx+1 != idx_to_delete:
#             current = current.next
#             idx += 1
        
#         # if node is at the end
#         if current.next.next is None:
#             current.next = None
#         # if node is at the middle
#         else:
#             rest = current.next.next
#             current.next = rest
#         return head

# Solution.removeNthFromEnd()


from typing import List

class Solution:
    def countProduct(self, idx, iterable) -> int:
        product = 1
        for i, element in enumerate(iterable):
            if i != idx:
                product *= element
            else:
                continue
        return product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        s = 1,  2,  3,  4    # product = 1 * 2 * 3 * 4 = 24
        a = 24  12  8   6
        """
        if bool(nums) is False:
            return []
        elif len(nums) == 1:
            return nums
        elif len(set(nums)) == 1:
            result = nums[0]*(len(nums)-1)
            return [result for _ in range(len(nums))]

        answer = []
        idx = 0
        while idx < len(nums):
            product = self.countProduct(idx=idx, iterable=nums)
            answer.append(product)
            idx += 1
        return answer
        
Solution().productExceptSelf(nums=[0, 0])




def countAverage(window: List[int]) -> float:
        sum_ = 0
        for element in window:
            sum_ += element
        return sum_ / len(window)

def findMaxAverage(nums: List[int], k: int) -> float:
    maximum = countAverage(window=nums[0:k])
    left, right = 1, k+1

    while right <= len(nums):
        average = countAverage(window=nums[left:right])
        if average > maximum:
            maximum = average
        left += 1
        right += 1
    
    return maximum


print(findMaxAverage(nums=[0,1,1,3,3], k=4))