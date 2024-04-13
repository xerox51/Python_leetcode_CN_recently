from sortedcontainers import SortedSet

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fs = {}
        self.cs = defaultdict(SortedSet)
        for f, c, r in zip(foods, cuisines, ratings):
            self.fs[f] = [r, c]
            self.cs[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        r, c = self.fs[food]
        s = self.cs[c]
        s.remove((-r, food))  
        s.add((-newRating, food))  
        self.fs[food][0] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cs[cuisine][0][1]