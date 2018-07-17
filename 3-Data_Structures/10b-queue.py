# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:59:05 2018

@author: George Gerog
"""
#implementation of Queue
class Queue:
    def __init__(self):
        self.queue = list()
        self.maxSize = 5
        self.tail = 0
        self.head = 0
    
    def EnQueue(self, x):
        #add element
        if not self.IsFull():
            self.queue.insert(0, x)
            if self.tail == len(self.queue):
                self.tail = 1
            else:
                self.tail +=1
        else:
            return ('Queue is full overflow')
            
    def DeQueue(self):
        if not self.IsEmpty():
            data = self.queue.pop()
            if self.head == len(self.queue):
                self.head = 1
            else:
                self.head +=1
            return data
        else:
            return ('Queue is empty overflow')
    def IsEmpty(self):
        if  self.size() <= 0:
            return True
        else:
            return False
    def IsFull(self):
        if self.size() >= self.maxSize:
            return True
        else:
            return False
    def size(self):
        return len(self.queue)
    def printQueue(self):
        return self.queue
        
def main():
    myQ = Queue()
    for i in range(6):
        print(myQ.EnQueue(i**2))
    for i in range(6):
        print(myQ.printQueue())
        print(myQ.DeQueue())
main()
    
    
