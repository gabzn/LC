https://leetcode.com/problems/design-a-food-rating-system/

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine_and_rating = {}
        self.cuisine_to_food_and_rating = defaultdict(list)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine_and_rating[food] = (cuisine, rating)
            heappush(self.cuisine_to_food_and_rating[cuisine], (-rating, food)) 
            
    def changeRating(self, food: str, new_rating: int) -> None:
        # Update the rating
        cuisine, _ = self.food_to_cuisine_and_rating[food]
        self.food_to_cuisine_and_rating[food] = (cuisine, new_rating)
        heappush(self.cuisine_to_food_and_rating[cuisine], (-new_rating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_food_and_rating[cuisine]
        
        while heap:
            rating, food = heap[0]
            if -self.food_to_cuisine_and_rating[food][1] == rating:
                return food
              
            heappop(heap)
