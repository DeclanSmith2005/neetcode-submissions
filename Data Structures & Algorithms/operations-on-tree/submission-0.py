class LockingTree:
    def __init__(self,parent:List[int]):
        self.parent=parent[:]
        self.owner=[0]*len(parent)
        self.children=[[] for _ in parent]
        for i in range(1,len(parent)):
            self.children[parent[i]].append(i)
    def lock(self,num:int,user:int)->bool:
        if self.owner[num]:return False
        self.owner[num]=user
        return True
    def unlock(self,num:int,user:int)->bool:
        if self.owner[num]!=user:
            return False
        self.owner[num]=0
        return True
    def upgrade(self,num:int,user:int)->bool:
        v=num
        while v!=-1:
            if self.owner[v]:
                return False
            v=self.parent[v]
        stack=self.children[num][:]
        found=False
        while stack:
            v=stack.pop()
            found|=self.owner[v]!=0
            self.owner[v]=0
            stack.extend(self.children[v])
        if not found:return False
        self.owner[num]=user
        return True
