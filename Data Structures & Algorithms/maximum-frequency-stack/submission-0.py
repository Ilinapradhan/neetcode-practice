class FreqStack:

    def __init__(self):
        self.freq={}
        self.stack={}
        self.max_f=0

    def push(self, val: int) -> None:
        f=self.freq.get(val,0)+1
        self.freq[val]=f
        
        if f>self.max_f:
            self.max_f=f
            self.stack[f]=[]
        self.stack[f].append(val)
        

    def pop(self) -> int:
        res=self.stack[self.max_f].pop()
        self.freq[res]-=1
        if not self.stack[self.max_f]:
            self.max_f-=1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()