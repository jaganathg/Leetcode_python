
def maxProfitAssignment( difficulty: list[int], profit: list[int], worker: list[int]) -> int:
    jobs = sorted(zip(difficulty, profit))
    
    res = idx = maxp = 0
    
    for work in sorted(worker):
        while idx < len(jobs) and work >= jobs[idx][0]:
            maxp = max(maxp, jobs[idx][1])
            idx += 1
        res += maxp
    return res


if __name__=="__main__":
    difficulty = [2,4,6,8,10]
    profit = [10,20,30,40,50]
    worker = [4,5,6,7]
    print(maxProfitAssignment(difficulty, profit, worker))  # Output: 100