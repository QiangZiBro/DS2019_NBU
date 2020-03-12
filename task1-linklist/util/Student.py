from util.LinkedList import *


class Student(object):

    def __init__(self, sno=None, name=None, sex='Male', birthday=None, pic=None):
        self.sno = sno
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.pic = pic

    def __repr__(self):
        text = str(self.__dict__)
        return text




if __name__ == '__main__':
    stu = Student('1911082054', 'Rex', 'M', '19970207')
    node = Node(data=stu)
    ls = ChainTable()
    ls.append(node)