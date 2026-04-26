class MinStack:

    def __init__(self):
        self.stack=[]
        self.sstack=[]
        

    def push(self, val: int) -> None:
        self.sstack.append(val)

        if not self.stack:
            self.stack.append(val)
        else:
            curmin=min(val , self.stack[-1])
            self.stack.append(curmin)

    def pop(self) -> None:
        self.sstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.sstack[-1]

    def getMin(self) -> int:
        return self.stack[-1]
        
