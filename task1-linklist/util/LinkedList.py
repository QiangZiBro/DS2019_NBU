from util.Student import Student


class Node(object):
    pass


class ChainTable(object):
    pass


ls = ChainTable()

if __name__ == '__main__':
    stu0 = Student(name='0')
    node = Node(data=stu0)
    ls.append(node)
    for i in range(3):
        stu = Student(name=str(i + 1))
        node = Node(data=stu)
        ls.append(node)
