#链表
#创建节点（Node）
#value：该节点的值 next:指向下一个节点
class Node():
    def __init__(self,value):
        self._value = value
        self._next = None
#创建链表（LinkList）
class LinkedList():
    def __init__(self):
        self._head = None
#检查链表是否为空
def isEmpty(self):
    return self._head == None
#返回链表节点的数量
def length(self):
    if self.isEmpty():
        return 0
    else:
        cur = self._head
        count = 1
        while cur._next != None:
            count += 1
            cur = cur._next
        return count
#遍历所有节点
def travel(self):
    if self.isEmpty():
        print("The linkedlist is empty!")
    else:
        cur = self._head
        values = []
        while cur != None:
            values.append(cur._value)
            cur = cur._next
        print(values)
#头部添加节点
def add(self,value):
    node = Node(value)
    node._next = self._head
    self._head = node
#尾部添加节点
def append(self,value):
    node = Node(value)
    if self.isEmpty():
        self._head = node
    else:
        cur = self._head
        while cur._next != None:
            cur = cur._next
        cur._next = node
#插入节点
def insert(self,pos,value):
    if pos <= 0:
        self.add(value)
    elif pos > (self.length()-1):
        self.appned(value)
    else:
        node = Node(value)
        cur = self._head
        index = 0
        while index < (pos-1):
            index += 1
            cur = cur._next
        node._next = cur._next
        cur._next = node
#删除某个索引对应的节点
def delete(self,index):
    if index < 0 or index > (self.length()-1):
        print("The input index is out of range!")
    elif index == 0:
        self._head = self._head._next
    else:
        count = 1
        pre, cur = self._head, self._head._next
        while count < index:
            count += 1
            pre,cur = cur, cur._next
        pre._next = cur._next
#根据值查找索引
def search(self,value):
    count = 0
    cur = self._head
    index = []
    while cur != None:
        if cur._value == value:
            index.append(count)
        count += 1
        cur = cur._next
    if not index:
        return False
    else:
        return index