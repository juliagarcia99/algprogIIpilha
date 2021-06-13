class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#######################

class pilha:
    def __init__(self):
        self.top = None
        self._size = 0


    def push(self, elem):
        #serve p inserir elemento
        node = Node(elem)
        node.next = self.top
        self.top = node
        self.size = self.size + 1

    def pop(self):
        #remove o elemento no topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self.size = self.size - 1
            return node
        raise IndexError("pilha vazia")

    def mostrarpilha(self):
        print(pilha)
