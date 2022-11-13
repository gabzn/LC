https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
  
import random
class RandomizedCollection:

    def __init__(self):
        self.values = []
        self.value_indices_dict = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        if val not in self.value_indices_dict:
            self.value_indices_dict[val].add(len(self.values))
            self.values.append(val)
            return True
        
        self.value_indices_dict[val].add(len(self.values))
        self.values.append(val)
        return False        
    
    def remove(self, val: int) -> bool:
        if val not in self.value_indices_dict:
            return False
        
        # Check if val is the last element in values
        if val == self.values[-1]:
            self.value_indices_dict[val].remove(len(self.values)-1)
            self.values.pop()
            
            # Check if the set still has indices. If it has no more indices, we delete it from the dict.
            if not self.value_indices_dict[val]:
                del self.value_indices_dict[val]
            return True
        
        # Get an index of val from the set
        val_index = next(iter(self.value_indices_dict[val]))
        
        # Swap val with the last element in the list
        self.values[val_index] = self.values[-1]
        
        """
        Since the previous last index has been swapped to val_index
        we need to update its index in the set.
        """
        self.value_indices_dict[self.values[-1]].remove(len(self.values)-1)
        self.value_indices_dict[self.values[-1]].add(val_index)
        
        """
        val is not longer in val_index now. Remove this index from the val's set.
        Check if the set still has indices. If it has no more indices, we delete it from the dict.
        """
        self.value_indices_dict[val].remove(val_index)
        if not self.value_indices_dict[val]:
            del self.value_indices_dict[val]
        
        self.values.pop()
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.values)
