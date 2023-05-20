class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Integer limitation
        in other static languages 3^19 as it
        is the max possible 3 power just before max int value
        should be divisible by other 3^x
        """
        return n > 0 and 1162261467 % n == 0
