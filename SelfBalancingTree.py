from Node import Node
import copy
class AVLTree:
    def __init__(self) -> None:
        self.HeadNode = None
    
    def RecursiveInsert(self,NodeToInsert:Node,Subtree=None):
        if self.HeadNode == None:
                self.HeadNode = NodeToInsert
                self.HeadNode.Height = 1 + max(self.GetHeight(self.HeadNode.LeftNode),self.GetHeight(self.HeadNode.RightNode))
                self.HeadNode.BalanceFactor = self.GetBalance(Subtree)
                # self.printTree(self.HeadNode)
                # print("\n")
        else:
            if Subtree == None:
                Subtree = self.HeadNode
            if NodeToInsert.Key > Subtree.Key and Subtree.RightNode != None:
                self.RecursiveInsert(NodeToInsert,Subtree.RightNode)
            elif NodeToInsert.Key <= Subtree.Key and Subtree.LeftNode != None:
                self.RecursiveInsert(NodeToInsert,Subtree.LeftNode)
            if NodeToInsert.Key > Subtree.Key and Subtree.RightNode == None:
                Subtree.RightNode = NodeToInsert
            elif NodeToInsert.Key <= Subtree.Key and Subtree.LeftNode == None:
                Subtree.LeftNode = NodeToInsert
            
            Subtree.Height = 1 + max(self.GetHeight(Subtree.LeftNode),self.GetHeight(Subtree.RightNode))

            Subtree.BalanceFactor = self.GetBalance(Subtree)

            #If Subtree.BalanceFactor -ve, right skewed
            #If Subtree.BalanceFactor +ve, left skewed

            #Imbalance in the left child's right subtree
            if Subtree.BalanceFactor > 1 and self.GetHeight(self.GetLeftChild(Subtree.LeftNode)) <= self.GetHeight(self.GetRightChild(Subtree.LeftNode)):
                LeftNode = Subtree.LeftNode
                self.LeftRotate(LeftNode)
                self.RightRotate(Subtree)
            #Imbalance in the left child's left subtree
            elif Subtree.BalanceFactor > 1 and self.GetHeight(self.GetLeftChild(Subtree.LeftNode)) > self.GetHeight(self.GetRightChild(Subtree.LeftNode)):
                self.RightRotate(Subtree)
            #Imbalance in the right child's left subtree
            elif Subtree.BalanceFactor < -1 and self.GetHeight(self.GetLeftChild(Subtree.RightNode)) > self.GetHeight(self.GetRightChild(Subtree.RightNode)):
                RightNode = Subtree.RightNode
                self.RightRotate(RightNode)
                self.LeftRotate(Subtree)
            #Imbalance in the right child's right subtree
            elif Subtree.BalanceFactor < -1 and self.GetHeight(self.GetLeftChild(Subtree.RightNode)) < self.GetHeight(self.GetRightChild(Subtree.RightNode)):
                self.LeftRotate(Subtree)
            #self.printTree(self.HeadNode)
            #print("\n")

    def LeftRotate(self,Subtree: Node):
        print(f"L at {Subtree.Key} \n")
        Copy = copy.deepcopy(Subtree)
        RightNode = Copy.RightNode
        Copy.RightNode = RightNode.LeftNode
        RightNode.LeftNode = Copy
        Subtree.LeftNode = RightNode.LeftNode
        Subtree.RightNode = RightNode.RightNode
        Subtree.Key = RightNode.Key
        Subtree.Height = RightNode.Height
        Subtree.Data = RightNode.Data

        Subtree.LeftNode.Height = 1 + max(self.GetHeight(Subtree.LeftNode.LeftNode),self.GetHeight(Subtree.LeftNode.RightNode))
        Subtree.Height = 1 + max(self.GetHeight(Subtree.LeftNode),self.GetHeight(Subtree.RightNode))


    def RightRotate(self,Subtree: Node):
        print(f"R at {Subtree.Key} \n")
        Copy = copy.deepcopy(Subtree)
        LeftNode = Copy.LeftNode
        Copy.LeftNode = LeftNode.RightNode
        LeftNode.RightNode = Copy
        Subtree.LeftNode = LeftNode.LeftNode
        Subtree.RightNode = LeftNode.RightNode
        Subtree.Key = LeftNode.Key
        Subtree.Height = LeftNode.Height
        Subtree.Data = LeftNode.Data

        Subtree.RightNode.Height = 1 + max(self.GetHeight(Subtree.RightNode.LeftNode),self.GetHeight(Subtree.RightNode.RightNode))
        Subtree.Height = 1 + max(self.GetHeight(Subtree.LeftNode),self.GetHeight(Subtree.RightNode))

    #To handle null values
    def GetLeftChild(self,Node:Node):
        if Node == None:
            return None
        else:
            return Node.LeftNode
    
    def GetRightChild(self,Node:Node):
        if Node == None:
            return None
        else:
            return Node.RightNode
    
    def GetHeight(self,Node:Node):
        if Node == None:
            return 0
        return Node.Height

    def GetBalance(self,Node:Node):
        if Node == None:
            return 0
        return self.GetHeight(Node.LeftNode) - self.GetHeight(Node.RightNode)
    
    def Search(self,ValueToBeFound) -> Node|None:
        if self.HeadNode == None:
            return None
        else:
            CurrentNode = self.HeadNode
            EndReached = False
            ReturnNode = None
            while EndReached == False:
                if ValueToBeFound > CurrentNode.Key and CurrentNode.RightNode != None:
                    CurrentNode = CurrentNode.RightNode
                elif ValueToBeFound < CurrentNode.Key and CurrentNode.LeftNode != None:
                    CurrentNode = CurrentNode.LeftNode
                elif ((ValueToBeFound > CurrentNode.Key and CurrentNode.RightNode == None) or 
                      (ValueToBeFound < CurrentNode.Key and CurrentNode.LeftNode == None)):
                    EndReached = True
                elif CurrentNode.Key == ValueToBeFound:
                    ReturnNode = CurrentNode
                    EndReached = True
            return ReturnNode

    def printTree(self,node:Node=None, level=0):
        if level == 0:
            node = self.HeadNode
        if node != None:
            self.printTree(node.LeftNode, level + 1)
            print(' ' * 4 * level + '-> '+ f"({node.Key}, {node.Data})")
            self.printTree(node.RightNode, level + 1)

    def InOrderTraversal(self,node: Node):
        if node.LeftNode != None:
        #    print("L")
            self.InOrderTraversal(node.LeftNode)
        #print("E")
        print(node.Key)
        if node.RightNode != None:
        #    print("R")
            self.InOrderTraversal(node.RightNode)

    def PreOrderTraversal(self,node: Node):
        print(node.Key)
        if node.LeftNode != None:
        #    print("L")
            self.InOrderTraversal(node.LeftNode)
        if node.RightNode != None:
        #    print("R")
            self.InOrderTraversal(node.RightNode)