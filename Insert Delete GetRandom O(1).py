https://leetcode.com/problems/insert-delete-getrandom-o1/

# Main thing to remember: 2 data structures: a list and a dict.
# The keys of the dict are the vals, the values are their corresponding indices in the list.
# To remove an element, we replace val with the last element in the list.
# After replacing it, we need to change the value for this val.

class RandomizedSet:

    def __init__(self):
        # Use 2 different data structures to keep track of the vals
        # Use a dict to implement contant look up and removal
        # Use a list to return a random val
        # We use counter as a value to a key to indicate the index of val in the list.
        self.num_dict = dict()
        self.num_list = []
        self.counter = 0

    def insert(self, val: int) -> bool:
        if val in self.num_dict:
            return False
        
        # To insert an element, we insert the element into both the dict and list.
        # Inserting to the dict: key is val, value is the index of this val in the list.
        self.num_dict[val] = self.counter
        self.num_list.append(val)
        self.counter += 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.num_dict:
            return False
        
        # Removing an element from a dict is O(1) .
        # Removing an element from a list is O(n) where n is the size of the list.
        # Instead of "removing" it from the list, what we can do is replace it with the last element in the list.
        # Then we pop the last element using pop which is O(1).
        
        # Get the index for val and a copy of the last element in the list.
        val_index = self.num_dict[val]
        last_element_in_list = self.num_list[-1]
        
        # Move the last element to where val was in the list.
        # Change its value to the new index in the dict.
        self.num_list[val_index] = last_element_in_list
        self.num_dict[last_element_in_list] = val_index
        
        # Clean-ups have to be done at the end. Otherwise, the size of the list will shrink, and an indexOutOfRange error can be thrown.
        del self.num_dict[val]
        self.num_list.pop()
        self.counter -= 1
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.num_list)
