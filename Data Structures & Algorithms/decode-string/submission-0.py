class Solution:
    def decodeString(self, s: str) -> str:
        cur_str=""
        cur_num=0
        stack=[]
        for i in s:
            if i.isdigit():
                cur_num= cur_num*10+int(i)
            elif i=="[":
                stack.append((cur_num , cur_str))
                cur_num=0
                cur_str=""
            elif i=="]":
                pre_num , pre_str=stack.pop()
                cur_str=pre_str+(cur_str*pre_num)
            else:
                cur_str+=i
        return cur_str