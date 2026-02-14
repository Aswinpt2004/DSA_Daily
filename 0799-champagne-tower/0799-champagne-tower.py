class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * (i + 1) for i in range(query_row + 1)]
        
        tower[0][0] = poured
        
        for r in range(query_row):
            for c in range(len(tower[r])):
                overflow = (tower[r][c] - 1.0) / 2.0
                
                if overflow > 0:
                    tower[r+1][c] += overflow
                    tower[r+1][c+1] += overflow
        
        return min(1.0, tower[query_row][query_glass])