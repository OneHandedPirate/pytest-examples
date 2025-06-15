def add(*nums: int) -> int:
    if not nums:
        raise ValueError("You should pass at least one number")
    if not all(isinstance(n, int) for n in nums):
        raise TypeError("Each argument must be an integer")
    return sum(nums)
