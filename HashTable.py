from Node import Node
from SelfBalancingTree import AVLTree
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

class HashTable:
    def __init__(self) -> None:
        self.Table = np.empty(10, dtype=Node)

    def Hash(self,Key):
        Hash = 0
        for Char in Key:
            Hash += ord(Char)
        return Hash
    
    def Insert(self,Node:Node):
        Index = self.Hash(Node.Key)%10
        if self.Table[Index] == None:
            Tree = AVLTree()
            self.Table[Index] = Tree
        self.Table[Index].RecursiveInsert(Node)

    def Delete(self,Key):
        Index = self.Hash(Key)%10
        self.Table[Index] = None

    def Find(self,Key):
        Index = self.Hash(Key)%10
        if self.Table[Index] == None:
            return None
        return self.Table[Index].Search(Key)