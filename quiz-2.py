# Selecting Substrings : Writing a Python Procedure

# Let p and q each be strings containing two words separated by a space.

# Examples:
#    "bell hooks"
#    "grace hopper"
#    "alonzo church"

# Write a procedure called myfirst_yoursecond(p,q) that returns True if the
# first word in p equals the second word in q. Return False otherwise.


def myfirst_yoursecond(p, q):
    if p == '' or q == '':
        return False
    wordOne = p.split(' ')[0]
    wordTwo = q.split(' ')[1]
    return wordOne == wordTwo


print(myfirst_yoursecond("bell hooks", "curer bell"))
# >>> True
