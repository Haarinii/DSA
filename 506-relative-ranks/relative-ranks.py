class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score=sorted(score, reverse=True)
        dic={}
        for i, val in enumerate(sorted_score):
            if i==0:
                dic[val]='Gold Medal'
            elif i==1:
                dic[val]='Silver Medal'
            elif i==2:
                dic[val]='Bronze Medal'
            else:
                dic[val]=str(i+1)
        answer=[]
        for s in score:
            answer.append(dic[s])
        return answer
        