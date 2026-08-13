class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(d) for d in digits] 
        integer = ''.join(digits)
        integer_plus_one = str(int(integer) + 1)
        return [d for d in integer_plus_one]