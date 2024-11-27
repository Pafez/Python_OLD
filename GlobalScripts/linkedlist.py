class LinkedList:

    def __init__(self, headvalue) -> None:
        self.value = headvalue
        self.next = None

    def length(self):
        length = 1
        if self.value == None:
            length = 0
        iterator = self
        while(iterator.next != None):
            iterator = iterator.next
            length += 1
        return length

    def append(self, value):
        iterator = self
        while(iterator.next != None):
            iterator = iterator.next
        iterator.next = LinkedList(value)

    def appinit(self, value):
        new_list = LinkedList(value)
        new_list.next = self
        self = new_list

    def getlist(self):
        list = "[" + str(self.value)
        iterator = self
        while(iterator.next != None):
            iterator = iterator.next
            list += ", " + str(iterator.value)
        list += "]"
        return list
    
    def getvalue(self, index):
        if index >= self.length():
            raise(IndexError("List Index Out Of Range"))
        iterator = self
        for i in range(index):
            iterator = iterator.next
        return iterator.value
    
    def pop(self, index=length()):
        if index >= self.length():
            raise(IndexError("List Index Out Of Range"))
        iterator = self
        for i in range(index):
            iterator = iterator.next
        return iterator.value

list = LinkedList(20)
list.append(34)
list.append(56)
list.appinit(11)

print(list.getlist())
print(list.getvalue())
