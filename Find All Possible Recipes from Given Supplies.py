https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj_list, indegree_for_food_in_recipes = defaultdict(list), dict()
        queue = deque([s for s in supplies])
        res = []
        
        for food, ingredients_for_food in zip(recipes, ingredients):
            if food not in indegree_for_food_in_recipes:
                indegree_for_food_in_recipes[food] = 0
            
            # For each food in recipes, we want to know how many ingredients it needs to create it
            # key in adj_list is the ingredient 
            # value in adj_list[key] is the food this key can make
            for ingredient in ingredients_for_food:
                adj_list[ingredient].append(food)
                indegree_for_food_in_recipes[food] += 1
        
        while queue:
            food = queue.popleft()
            # If the current food is one of the dishes in recipes, append it to res
            if food in indegree_for_food_in_recipes:
                res.append(food)
            
            for neighbour in adj_list[food]:
                indegree_for_food_in_recipes[neighbour] -= 1
                if indegree_for_food_in_recipes[neighbour] == 0:
                    queue.append(neighbour)
        
        return res
