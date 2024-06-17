"""
идея
"""


def removeDuplicates(nums) -> int:
    if bool(nums) is False or len(nums) == 1:
        return len(nums)
    
    insert_idx = 1
    for idx in range(1, len(nums)):
        if nums[idx] != nums[idx-1]:
            nums[insert_idx] = nums[idx]
            insert_idx += 1
    return insert_idx
                
print(removeDuplicates(nums=[1,1]))