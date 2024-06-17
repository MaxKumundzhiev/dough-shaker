def rotate(nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]


print(rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
print(rotate(nums=[-1, -100, 3, 99], k=2))


def moveZeroes(nums) -> None:
        if bool(nums) is False:
            return nums
        elif len(nums) == 1:
            return nums
        elif set(nums) == {0}:
            return nums
        
        # [4,2,4] + [3,0,5,1,0] + [0, 0]
        
        # [4,2,4,3,0,5,1,0,0,0]
        iteration, idx = 0, 0
        try:
            while iteration < len(nums) - 1:
                if nums[idx] != 0:
                    iteration += 1
                    idx += 1
                else:
                    if nums[idx+1] != 0:
                        nums.append(nums.pop(idx))
                        iteration += 1
                    else:
                        boundary = idx + 1
                        counter = 1
                        while True:
                            if nums[boundary] == 0:
                                boundary += 1
                                counter += 1
                            else:
                                nums[:] = nums[:idx] + nums[boundary:] + [0]*counter
                                iteration += counter
        except IndexError:
            return nums
                        
        return nums


print(moveZeroes(nums=[4,2,4,0,0,3,0,5,1,0]))
