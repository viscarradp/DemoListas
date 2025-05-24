from node import Node
from linked_list import linked_list

def welcome():
    print("-----------------------")
    print("-Welcome To DemoListas-")
    print("-----------------------")

welcome()

lista = linked_list()
lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.add(5)
lista.add(6)
lista.add(7)


lista.delete_at()
lista.show()

