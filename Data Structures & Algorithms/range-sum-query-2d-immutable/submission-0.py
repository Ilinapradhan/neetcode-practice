class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row , col = len(matrix) , len(matrix[0])
        self.reif = [[0] * (col+1) for _ in range(row+1)]
        for r in range(row):
            sumrow= 0
            for c in range(col):
                sumrow=sumrow+matrix[r][c]
                self.reif[r+1][c+1] = self.reif[r][c+1]+sumrow



    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (self.reif[r2+1][c2+1]- 
        self.reif[r1][c2+1]-
        self.reif[r2+1][c1]+
        self.reif[r1][c1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)