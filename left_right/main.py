def solution(nums):
    n = len(nums)
    result = [0] * n

    for i in range(n):
        # nums[i]から左へ広げる
        left = i
        while left > 0 and nums[left - 1] < nums[i]:
            left -= 1
        
        L = i - left + 1
        # nums[i]から右へ広げる
        right = i
        while right < n - 1 and nums[right + 1] < nums[i]:
            right += 1
        
        R = right - i + 1
        # 結果をカウントする
        result[i] = L + R - 1
    
    return result

if __name__ == "__main__":
    nums = [3, 4, 1, 6, 2]
    print(solution(nums))
    