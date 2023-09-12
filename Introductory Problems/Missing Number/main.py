# CSES - Introductory Problems - Missing Number #

def main(n, nums):
    if n == 2: return int(nums[0] == 1) + 1
    
    nums.sort()

    for idx in range(1, n - 2):
        if nums[idx + 1] - nums[idx] > 1:
            return nums[idx] + 1
        
    if nums[0] == 1: return n
    return 1

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    output = main(n, nums)
    print(output)
    