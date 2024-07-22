# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        while self.s1:
            item = self.s1.pop()
            self.s2.append(item)
        
        res = self.s2.pop()

        while self.s2:
            item = self.s2.pop()
            self.s1.append(item)
        
        return res
        
    def peek(self) -> int:
        while self.s1:
            item = self.s1.pop()
            self.s2.append(item)
        
        res = self.s2[-1]

        while self.s2:
            item = self.s2.pop()
            self.s1.append(item)
        
        return res

    def empty(self) -> bool:
        if not self.s1:
            return True
        return False
    
    
