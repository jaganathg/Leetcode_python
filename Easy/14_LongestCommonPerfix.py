from typing import List 
def LongestCommonPerfix(strs: List[str]) -> str:
    if not strs:
        return ""
    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i >= len(string) or string[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]

def longestCommonPrefix(strs: List[str]) -> str:
        pre = ""
        strs.sort()
        l = min(len(strs[0]), len(strs[-1]))

        for i in range(l):
            if strs[0][i] == strs[-1][i]:
                pre += strs[0][i]
            else:
                break
            
        return pre
        

if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))
    strs = ["car", "caraser", "cars"]
    print(longestCommonPrefix(strs))