# class HelloMixIn:
#     def greeting(self):
#         print('안녕하세요')
    
# class Person():
#     def __init__(self, name):
#         self.name = name

# class Student(HelloMixIn, Person):
#     def study(self):
#         print('공부하기')

# class Teacher(HelloMixIn, Person):
#     def teach(self):
#         print('가르치기')

# a = Student('lilo')
# a.greeting()

class A:
    my = '내 '

class B(A):
    def print_i(self):
        print('나다')

class C(A):
    pass

class M:
    # def print_total(self):
    #     print(self.total)
    
    def print_name(self, name, **kwargs):
        result = self.my + "%s %s" %(name, (kwargs.get('iam')))
        print(result)
    
class D(B, M):
    pass

class E(C, M):
    pass

d = D()
d.print_name('이름은', iam='lilo')