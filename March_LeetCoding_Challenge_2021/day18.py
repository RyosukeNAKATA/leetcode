l = [1, 2, 3, 4, 5]
for j in range(4):
    print(j)
    if l[j] == 3:
        l.pop(j)

print(l)

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        output = 0
        def posistive(nums: list[int], n):
            diff = nums[n+1] - nums[n]
            if diff > 0:
                output += 1
                negative(nums, n+1)
            else:
                nums.pop(n+1)
                posistive(nums, n)

        def negative(nums: list[int], n):
            diff = nums[n+1] - nums[n]
            if diff < 0:
                output += 1
                posistive(nums, n+1)
            else:
                nums.pop(n+1)
                negative(nums, n)
        
        k = 0
        num = nums[k] - nums[k+1]
        for _ in range(len(nums)):
            if num > 0:
                output += 1
                posistive(num, k+1)
                break
            elif num < 0:
                output += 1
                negative(num, k+1)
                break
            else:
                nums.pop(k+1)
                k += 1

        return output