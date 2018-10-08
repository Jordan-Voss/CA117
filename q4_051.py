import sys


def main():
    nums = sorted(int(l.strip()) for l in sys.stdin)

    mean = sum(nums) / len(nums)
    mode = max(nums, key=lambda x: nums.count(x))
    median = nums[len(nums) // 2] if len(nums) % 2 else (
        nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2

    print("Mean: {:.1f}\nMode: {:.1f}\nMedian: {:.1f}".format(
        mean, mode, median))


if __name__ == '__main__':
    main()