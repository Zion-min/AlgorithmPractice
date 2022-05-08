class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #최대 부분합을 구하는 문제. 각각의 최대 부분합은 이전 인덱스의 최대부분합과 현재 인덱스 값더한거 아니면 현재 인덱스 
        #A[i]=max(A[i-1]+A[i],A[i])
        
        maxsum = nums[0]
        currsum = nums[0]

        for i in range(1,len(nums)):
            currsum= max(currsum + nums[i], nums[i])
            maxsum = max(maxsum, currsum)
        
        return maxsum
        
#젤 마지막게 제일 최대 부분합일까? ㄴㄴ임. 그중에서도 최대가 있음.        
#아항. 미리 해주는게 좋구나! 왜냐면 마지막에 max(nums)해주면 O(n)이니깐 currsum도 마찬가지
#그리고 이전 값을 기억해둘 필요가 있으면 배열로 하는게 좋은데, 이건 바로 직전값만 기억하면 되서 int 하나로만 하는게 나은듯
