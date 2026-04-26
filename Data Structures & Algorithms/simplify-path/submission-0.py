class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        component=path.split("/")
        for c in component:
            if c==".." :
                if len(stack)!=0:
                    stack.pop()
            elif c=="." or c=="" or c=="/":
                continue
            else:
                stack.append(c)
        return "/"+"/".join(stack)