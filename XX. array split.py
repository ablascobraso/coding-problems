from typing import List


class Solution:
    def splitArray(self, arr: List[int], integer: int) -> int:
        integer_count = 0
        for i in range(len(arr)):
            if integer_count == len(arr) - i - 1:
                return i
            if arr[i] == integer:
                integer_count += 1
        return -1


if __name__ == "__main__":
    arr = [5, 5, 2, 3, 5, 1, 6]
    integer = 5
    result = Solution().splitArray(arr, integer)
    print(result)