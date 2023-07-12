class Node:
    def __init__(self,Key,Data=None,LeftNode=None,RightNode=None) -> None:
        self.Key = Key
        self.Data = Data
        self.BalanceFactor = 0
        self.Height = 1
        self.LeftNode = LeftNode
        self.RightNode = RightNode
    
    def __str__(self) -> str:
        return f"({self.Key}, {self.Data})"
    
    __repr__ = __str__