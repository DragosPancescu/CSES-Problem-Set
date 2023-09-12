# CSES - Introductory Problems - Increasing Array #

def main(n, nums):
    if n == 1: return 0
    
    count = 0
    for idx in range(1, n):
        diff = nums[idx - 1] - nums[idx]
        to_add = 0 if diff < 0 else diff
        
        count += to_add
        nums[idx] += to_add
        
    return count


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    output = main(n, nums)
    print(output)
    