class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.finalBobArrows = None
        self.finalScore = 0
        
        def backtrack(k, remainArrows, score, bobArrows):
            # Bob loses
            if k == 12:
                if score > self.finalScore:
                    self.finalScore = score
                    self.finalBobArrows = bobArrows[::]
                return
            backtrack(k+1, remainArrows, score, bobArrows)
            
            # Bob wins
            arrowsNeeded = aliceArrows[k] + 1
            if remainArrows >= arrowsNeeded:
                old = bobArrows[k]
                bobArrows[k] = arrowsNeeded #set now
                backtrack(k+1, remainArrows- arrowsNeeded, score+k, bobArrows)
                bobArrows[k] = old  #backtrack
        
        backtrack(0, numArrows, 0, [0]*12)
        # In case of having remain arrows then it means in all sections Bob always win 
        # then we can distribute the remain to any section, here we simple choose first section.
        self.finalBobArrows[0] += numArrows - sum(self.finalBobArrows)
        return self.finalBobArrows
