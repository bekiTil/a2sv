# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        if self.iter.hasNext():
            self.temp=self.iter.next()
        else:
            self.temp=None
       
    def peek(self):
        return self.temp

    def next(self):
        temp = self.temp
        if self.iter.hasNext():
            self.temp=self.iter.next()
        else:
            self.temp=None
       
        return temp

    def hasNext(self):
        return self.temp != None

        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].