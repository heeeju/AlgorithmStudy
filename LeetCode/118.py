class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        for n in range(0,numRows-1):
            newAnswer = [1]
            for i in range(1,len(answer[n])):
                newAnswer.append(answer[n][i-1]+answer[n][i])
            newAnswer.append(1)
            answer.append(newAnswer)

        return answer


        
