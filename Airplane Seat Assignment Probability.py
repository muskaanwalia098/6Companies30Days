class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        """
        This is because the choice is only between the 
        1st seat and last seat mainly. If the 1st person 
        chooses the 1st seat, then everyone else will sit 
        accordingly, but if the 1st person chooses the last 
        seat or seat in between then, the others will have a 
        choice between others' seat and the last seat, and 
        so the cycle continues.
        Formula = (1/(n+1)) + ((n-1)/2*(n+1)) = 1/2
        """
        return 1 if n == 1 else 0.5
