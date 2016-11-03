# Bonus Practice: Find Max

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Given a list l and a function f, return the element of l that maximizes f.

# Assume:
#    l is not empty
#    f returns a number

# Example:

l = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood', 'Bible']
f = len


# Try it on your own!

def find_max(l, f, prev_max_item=None, prev_max_result=None):
    if len(l) == 0:
        return prev_max_item
    else:
        max_item = prev_max_item
        max_result = prev_max_result
        if max_item is None:
            max_item = l[0]
            max_result = f(l[0])
        else:
            item = l[0]
            result = f(item)
            if result > max_result:
                max_item = item
                max_result = result
        return find_max(l[1:], f, max_item, max_result)


print find_max(l, f)
