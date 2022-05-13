def countSquares(self, matrix: List[List[int]]) -> int:

    rows = len(matrix) #애초에 이렇게 변수에 담아두는 게 훨씬 빠름
    cols = len(matrix[0])

    result = 0
    for i in range(rows):
        for j in range(cols):
            # 최대한 뭐에 안담고 배열 포인터에 접근하는게 빠름. 조건문은 줄일수록 좋음
            if matrix[i][j] and i and j:
                matrix[i][j] += min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])
            result += matrix[i][j]
    return result


"""
output = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]==1:
                if row==0 or col==0:
                    output +=1
                else:
                    #memoization
                    temp = min(matrix[row-1][col-1], matrix[row-1][col], matrix[row][col-1])+matrix[row][col]
                    matrix[row][col]=temp
                    output+=temp

    return output


 """       
