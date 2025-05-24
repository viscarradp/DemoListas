from node import Node

class linked_list:
    def __init__(self):
        self.first = self.last = Node(None)

    def is_empty(self):
        return self.first.data is None

    def add(self, data):
        aux = Node(data)
        if self.is_empty():
            self.first = self.last = aux
        else:
            self.last.next = aux
            self.last = aux

    def show(self):
        if self.is_empty():
            print("Your list is empty")
            return
        else:
            aux = self.first
            while aux is not None:
                print(aux.data)
                aux = aux.next
    def find_at(self, index):
        current_index = 0
        current_node = self.first
        while current_index != index:
            current_node = current_node.next
            current_index += 1
        return current_node

    def add_to_start(self, data):
        aux = Node(data)
        if self.is_empty():
            self.first = self.last = aux
        else:
            self.show()
            aux.next = self.first
            self.first = aux
    def insert_at(self, index, data):
        aux = Node(data)
        if self.is_empty():
            self.first = self.last = aux
            return
        if index <= 0:
            self.add(data)
            return
        else:
            current_index = 0
            current_node = self.first
            node_before_index = index -1
            while current_index != node_before_index:
                current_node = current_node.next
                current_index += 1
            node_before_index = current_node
            current_node = current_node.next
            aux.next = current_node
            node_before_index.next = aux
    def length(self):
        if self.is_empty(): return 0
        else:
            iterator = 0
            current_node = self.first
            while current_node is not None:
                current_node = current_node.next
                iterator += 1
            return iterator
    def delete_first(self):
        if self.is_empty():
            return
        else:
            aux = self.first
            self.first = self.first.next
            aux.next = None

    def delete_last(self):
        if self.is_empty():
            return
        elif self.length() == 1:
            self.delete_first()
            return
        else:
            aux = self.last
            self.last = self.find_at(self.length() - 1)
            aux.next = None

    def delete_at(self, index):
        if self.is_empty(): return
        elif index < 0 or index >= self.length(): return
        elif index == 0: self.delete_first()
        elif index == self.length()-1: self.delete_last()
        else:
            aux = self.find_at(index)
            next_node = aux.next
            previous_node = self.find_at(index - 1)
            previous_node.next = next_node
            aux.next = None




