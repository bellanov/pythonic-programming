#set
# Create a set
my_set = {1, 2, "three", 4.0}
# Accessing elements in a set (Note: sets are unordered, so we cannot access by index)
# Checking membership
is_member = 2 in my_set  # Returns True
# Adding elements to a set
my_set.add(5)
# Removing elements from a set
my_set.remove("three")  # Raises KeyError if element not found
my_set.discard(10)      # Does not raise an error if element not found
# Set operations
another_set = {4.0, 5, 6, 7}
# Union
union_set = my_set.union(another_set)