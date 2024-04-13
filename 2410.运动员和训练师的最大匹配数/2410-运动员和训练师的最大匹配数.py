class Solution:
    def matchPlayersAndTrainers(
        self, 
        players: List[int], 
        trainers: List[int]
    ) -> int:
        
        n, m = len(players), len(trainers)        
        players.sort()
        trainers.sort()        
        res, lo = 0, 0
        for i in range(n):
            idx = bisect.bisect_left(
                trainers, players[i], lo=lo
            )
            if idx == m:
                break                
            res += 1
            lo = idx + 1            
        return res
        
          
    
            

           
           