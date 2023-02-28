class MyCircularQueue:

        def __init__(self, k):
            self.h=None
            self.t=None
            self.k=k
            self.qu=[None]*k


        def enQueue(self, value):
            if self.isEmpty():
                self.qu[0]=value
                self.t,self.h=0,0
                return True

            new_t=(self.t+1)%self.k
            if new_t==self.h:
                return False
            else:
                self.qu[new_t]=value
                self.t=new_t
                return True


        def deQueue(self):
            if self.isEmpty():
                return False
            if self.h==self.t:
                self.h,self.t=None,None
                return True
            else:
                self.h=(self.h+1)%self.k
                return True


        def Front(self):
            if self.h is None:
                return -1
            else:
                return self.qu[self.h]


        def Rear(self):
            if self.t is None:
                return -1
            else:
                return self.qu[self.t]

        def isEmpty(self):
            if self.h is None and self.t is None:
                return True
            else:
                return False


        def isFull(self):
            if self.isEmpty():
                return False
            if (self.t+1)%self.k==self.h:
                return True
            else:
                return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()