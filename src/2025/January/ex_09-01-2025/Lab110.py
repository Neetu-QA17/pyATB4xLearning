# DEQUE - double ended queue
# queue basically follows FIFO

from collections import deque

# create a dequeue

# d = dequeue()  or even like below
d = deque([1,2,3])
print(d)
# append - value will be added at the end of the list - adding an item - will add only single elsement
d.append(4)
print(d)
# add element to the left end
d.appendleft(0)
print(d)
# extend the dequeue - add a list - add multiple element
d.extend([5,6])
print(d)
# to remove element from right
d.pop()
print(d)
# to remove element from left
d.popleft()
print(d)
# we can reverse the queue also
d.reverse()
print(d)