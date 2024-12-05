class t:
    def __init__(self,v):
        self.v= v
        self.left = None
        self.right = None
class bt:
    def __init__(self,root):
        self.root =t(root)

    def insert(self,v):
        def insertr(n,v):
            if not n :#노드 비면 새거 생성
                return t(v)
            if v<n.v :#작으면
                n.left=insertr(n.left,v)
            elif v>n.v :#크면
                n.right=insertr(n.right,v)
            return n# 중복 재거
        self.root =insertr(self.root,v)

    def s(self,v):
        def sr(n,v):
            if not n :return False
            if n.v==v:return True
            elif v<n.v:
                return sr(n.left,v)
            else:
                return sr(n.right, v)
        return sr(self.root,v)

    def d(self,v):
        def dsr(n,v):
            if not n:return n
            if v<n.v:
                n.left=dsr(n.left,v)
            elif v>n.v:
                n.right=dsr(n.right,v) #찾을때까지 제귀
            else:
                if not n.left and not n.right:
                    return None
                elif not n.left:
                    return n.right
                elif not n.right:
                    return n.left
                temp= self.find_min(n.right)
                n.v=temp.v
                n.right=dsr(n.right,temp.v)
            return n
        self.root =dsr(self.root,v)
    def find_min(self,n):
        while n.left:
            n = n.left
        return n





tree=bt(10)
tree.insert(5)
tree.insert(10)
tree.insert(7)
print(tree.s(7))
print(tree.d(7))
print(tree.s(7))
print(tree.s(10))
