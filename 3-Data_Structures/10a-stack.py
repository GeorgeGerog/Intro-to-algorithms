# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:14:03 2018

@author: George Gerog
"""
#implementation of stack
class Stack :
    def __init__(self):
        self.stack = list()
        self.maxSize = 5
        self.top = 0
        
    def IsEmpty(self):
        #check if stack is empty
        if self.top == 0:
            return True
        else:
            return False

    def Push(self, x):
        #push an element to the stack
        if self.top>=self.maxSize:
            return ("Stack is full")
        self.top = self.top +1
        self.stack.append(x)
        return True
    
    def Pop(self):
        #remove an element from the stack
        if self.IsEmpty():
            return ('Stack Empty! Error underflow')
        else:
            data =self.stack.pop()
            self.top = self.top -1
            return data
    def Top(self):
        #return the top(size) of the stack
        return self.top
        
def main():
    s = Stack()
    for i in range(6):
        print(s.Push(i**2))
    print(s.Top())
    for i in range(6):
        print(s.Pop())
main()
        
    