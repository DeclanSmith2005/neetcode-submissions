class Solution:
    def countPrimes(self, n: int) -> int:
        from math import sqrt
        
        if n <= 2:
            return 0
        
        prime = [1] * n

        for i in range(2, int(sqrt(n)+1)):
            for m in range(i**2 , n, i):
                prime[m] = 0
                
        return sum(prime) - 2