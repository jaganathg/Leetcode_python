class Solution:
    def fib(self, num: int) -> int:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            prev = 0
            curr = 1
            for i in range(2, num+1):
                prev, curr = curr, prev + curr
            return curr
        
if __name__=="__main__":
    s = Solution()
    print(s.fib(100))