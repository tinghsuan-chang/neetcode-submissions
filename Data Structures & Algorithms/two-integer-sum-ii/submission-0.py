class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        one, two = 0, n-1
        sum_ = numbers[one] + numbers[two]

        while sum_ != target:
            if sum_ > target:
                two -= 1
            else:
                one += 1
            sum_ = numbers[one] + numbers[two]

        return [one+1, two+1]

# Time: O(n)
# Space: O(1)





