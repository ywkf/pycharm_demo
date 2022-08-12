import operator
import random
import json

from excel01 import excel_tag
from po1 import page

print("Hello world!")


# name = "yi"
# print("Hello %s\n" % (name))


# result = input("输入：")
# print(type(result), result)
# a = int(input("a："))
# b = int(input("b："))
# print(f'a + b = {a + b}')
# if a == b:
#     print(a + b)
# score = int(input("分数："))
# if score >= 90:
#     print('you')
# elif score >= 80:
#     print('liang')
# elif score >= 70:
#     print('zhong')
# elif score >= 60:
#     print('cha')
# else:
#     print('bujige')

# pwd = '123456'
# m = 1000
# pwd1 = input('pwd: ')
# if pwd == pwd1:
#     m1 = int(input('m: '))
#     if m < m1:
#         print('buzu')
#     else:
#         m -= m1
#         print('success yue {}'.format(m))
# else:
#     print('error')

# username = 'admin'
# pwd = '123456'
# code = '8888'
# username1 = input('username: ')
# pwd1 = input('pwd: ')
# code1 = input('code: ')
# if code == code1:
#     print('right')
#     if username == username1 and pwd == pwd1:
#         print('success')
#     else:
#         print('false')
# else:
#     print('wrong')

# shitou == 1, jiandao == 2, bu == 3, exit == 0
# player = 0
# computer = 0
# print('shitou == 1, jiandao == 2, bu == 3, exit == 0')
# while True:
#     player = int(input('player: '))
#     computer = random.randint(1, 3)
#     if player == 0:
#         print('exit')
#         break
#     elif player == 1 or player == 2 or player == 3:
#         if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
#             print(f'win, computer: {computer}')
#         elif player == computer:
#             print(f'win win, computer: {computer}')
#         else:
#             print(f'lose, computer: {computer}')
#     else:
#         print('error')

# i = 1
# j = 0
# while i <= 100:
#     if i % 2 == 0:
#         j += i
#     i += 1
# print(j)
#
# my_str = 'hello'
# for i in my_str:
#     print(i)
#
# for i in range(5):
#     print(i)
#
# print('-' * 30)
#
# for i in range(5, 11):
#     if i == 7:
#         continue
#     print(i)

# str1 = 'I\'m I.'
# str1 = 'qwer as df'
# print(len(str1))
# print(str1[3])
# print(str1[:3])
# print(str1[::-1], '\n')
#
# print(str1.find('a'))
# print(str1.replace('a', 'b'))
# print(str1.split())

# list1 = ['qwer', 'as', 'as', 'df']
# print(' '.join(list1))
# print(' and '.join(list1))
#
# print(list1[0])
# print(list1[0:2])
#
# print(list1.index('as'))
#
# print('as' in list1)
#
# print(list1.count('as'))
#
# list2 = [1, 2, 3, 4, 5, 6]
# list2.append('6')
# print(list2)
#
# list2.insert(1, '2')
# print(list2)
#
# list1.extend(list2)
# print(list1)
#
# list1.append(list2)
# print(list1)
#
# print(['a' for i in range(5, 10, 2)])

# str0 = input('input:')
# for i in str0:
#     if i == 'q':
#         break
#     elif i == ' ':
#         continue
#     print(i)

# for i in range(1,100):
#     if (i % 7 == 0) or str(i).find('7') != -1:
#         print('pass')
#     else:
#         print(i)

# list1 = ['red', 'apples', 'orange', 'pink', 'bananas', 'blue', 'black', 'white']
# list2 = []
# for i in list1:
#     if (i[-1] == 's') or (i[-1] == 'e'):
#         list2.append(i)
# print(list2)

# str1 = input('input:')
# list1 = str1.split(',')
# num = random.randint(0, 4)
# print(list1[num])

# j = 0
# for i in range(1, 101):
#     j += i
# print(j)

# list1 = [1, 2, 3, 4, 5, 6]
# list1[2] = 2
# print(list1)

# list1.pop()
# print(list1)
# print(list1.pop(0))
# list1.remove(6)
# list1.remove(2)
# list1.clear()
# print(list1)

# list1.reverse()
# print(list1)
#
# list2 = list1.copy()
# print(list2)
#
# list2.sort()
# print(list2)
# list2.sort(reverse=True)
# print(list2)

# dict1 = {'name': '张三', 'age': 18, 'like': ['1', '2', '3']}
# dict1['sex'] = '男'
# print(dict1)

# dict1.pop('name')
# print(dict1)
# del dict1['name']
# print(dict1)

# print(dict1.get('age', 20))

# for ks in dict1:
#     print(ks)

# for ks1 in dict1.keys():
#     print(ks1)

# for i1, i2 in dict1.items():
#     print(i1, ':', i2)

# def hello():
#     """print two 'hello'"""
#     print('hello')
#     print('hello')
#
# hello()

# list1 = ["hello", "python", "itcast", "hello"]

# list1.append('hm')
# print(list1)

# list1.pop(0)
# print(list1)

# list1.remove('hello')
# print(list1)

# list1[0] = 'cz'
# print(list1)
#
# print(list1.index('cz'))
# print(list1[2])
# print(list1.count('hello'))
# print(len(list1))

# def my_sum():
#     j = 0
#     for i in range(1, 101):
#         if i%2 == 0 :
#             j += i
#     print(j)
#
# my_sum()


# list1 = []
# dict1 = {}
#
# def pt(dict1):
#     print(dict1['name'], dict1['age'])
# def ip():
#     for i in range(3):
#         name = input('name:')
#         age = input('age:')
#         dict1 = {'name': name, 'age': age}
#         list1.append(dict1)
#
#     for j in range(3):
#         pt(list1[j])
#
# ip()

# def func():
#     list1 = [{'id': 1, 'money': 10}, {'id': 2, 'money': 20}, {'id': 3, 'money': 30}, {'id': 4, 'money': 40}]
#     for i in list1:
#         if i['id'] % 2 == 1:
#             i['money'] += 20
#         else:
#             i['money'] += 10
#     print(list1)
#
# func()

# dict1 = {'登录': [{'desc': '正确的用户名密码', 'username': 'admin', 'password': '123456', 'expect': '登录成功'},
#                 {'desc': '错误的用户名', 'username': 'root', 'password': '123456', 'expect': '登录失败'},
#                 {'desc': '错误的密码', 'username': 'admin', 'password': '123123', 'expect': '登录失败'},
#                 {'desc': '错误的用户名和密码', 'username': 'aaaa', 'password': '123123', 'expect': '登录失败'}],
#          '注册': [{'desc': '注册1', 'username': 'abcd', 'password': '123456'},
#                 {'desc': '注册1', 'username': 'xyz', 'password': '123456'}]}
#
# def pe():
#     inp = input('input: ')
#     if inp == '登录':
#         list0 = []
#         for i in dict1['登录']:
#             tuple1 = (i['username'], i['password'], i['expect'])
#             list0.append(tuple1)
#         print(list0)
#     else:
#         list2 = []
#         for j in dict1['注册']:
#             tuple2 = (j['username'], j['password'])
#             list2.append(tuple2)
#         print(list2)
#
# pe()

# list1 = [1, 2, 2, 1, 3]
# list2 = []
# for i in list1:
#     if i in list2:
#         continue
#     else:
#         list2.append(i)
# print(list2)
#
# print(list(set(list1)))


# def ssum(a, b):
#     return a + b
#
#
# print(ssum(1, 2))

# def show(name, age = 0):
#     print(name, age)
#
#
# show('11')

# a, b = {'name': "11", 'age': 0}
# print(a, b)

# def ssum(n):
#     i = 1
#     j = 0
#     while i <= n:
#         j += i
#         i += 1
#     print(j)
#
# ssum(100)

# def ssum(*args, **kwargs):
#     j = 0
#     for i in args:
#         j += i
#     for v in kwargs.values():
#         j += v
#     print(j)
#
# list1 = [1, 2, 3, 4]
# dict1 = {'a': 1, 'b': 2}
#
# ssum(*list1, **dict1)

# f1 = lambda a, b: a * b
# print(f1(2, 3))

# f2 = lambda a: a.get('age')
# print(f2({'name': 11, 'age': 0}))

# class Cat:
#     def eat(self):
#         print('eat')
#
#     def drink(self):
#         print('drink')
#
#
# cat1 = Cat()
# cat1.eat()
# cat1.drink()


# list1 = [{'id': 1, 'money': 10}, {'id': 2, 'money': 20}, {'id': 3, 'money': 30}, {'id': 4, 'money': 40}]
# list1.sort(key=lambda x: x['id'], reverse=True)
# print(list1)


# class Computer:
#
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
#     def __str__(self):
#         return f'brand: {self.brand}, price: {self.price}'
#
#     def play_movie(self, movie):
#         print(f'{self.brand} play movie {movie}')
#
#
# mi = Computer('mi', 1)
# mac = Computer('mac', 2)
# print(mi)
# mi.play_movie('hlw')
# mac.play_movie('bxjg')


# class Person:
#
#     def __init__(self, n, w):
#         self.name = n
#         self.weight = w
#         print(f"{self.name}'s weight = {self.weight} kg")
#
#     def run(self):
#         self.weight -= 0.5
#         return f"After run, {self.name}'s weight - 0.5 = {self.weight} kg"
#
#     def eat(self):
#         self.weight += 1
#         return f"After eat, {self.name}'s weight + 1 = {self.weight} kg"
#
#     def __str__(self):
#         return f"{self.name}'s weight = {self.weight} kg"
#
# xm = Person('xm', 75)
# print(xm.run())
# print(xm.eat())


# class House:
#
#     def __init__(self, h, a):
#         self.type = h
#         self.area = a
#         self.rarea = a
#         self.houseItem = []
#
#     def __str__(self):
#         return f'户型：{self.type}, 总面积：{self.area} m², 剩余面积：{self.rarea} m², 家具名称列表：{self.houseItem}'
#
#     def add_item(self, *args):
#         for i in args:
#             if self.rarea < i.area:
#                 print('area not enough')
#                 break
#             self.houseItem.append(i.name)
#             self.rarea -= i.area
#
#
# class HouseItem:
#
#     def __init__(self, n, a):
#         self.name = n
#         self.area = a
#
#     def __str__(self):
#         return f'家具名称：{self.name}, 占地面积：{self.area} m²'
#
#
# house = House('type', 120)
# bed = HouseItem('bed', 4)
# chest = HouseItem('chest', 2)
# table = HouseItem('table', 1.5)
#
# print(house)
# print(bed)
# print(chest)
# print(table)
# house.add_item(bed, chest, table)
# print(house)


# class Game:
#
#     top_score = 0
#     name = ''
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def show_help():
#         print('help')
#
#     @classmethod
#     def show_top_score(cls):
#         print(f'top_score: {cls.top_score}, name: {cls.name}')
#
#     def start_game(self):
#         score = random.randint(10, 100)
#         if score > Game.top_score:
#             Game.top_score = score
#             Game.name = self.name
#         print(f"{self.name}'s score: {score}")
#
#
# xw = Game('xw')
# zs = Game('zs')
# xw.start_game()
# zs.start_game()
# Game.show_top_score()
# xw.start_game()
# zs.start_game()
# Game.show_top_score()
# Game.show_help()


# f = open('a.txt', 'a', encoding='utf-8')
# # f.write('hhxx')
# # print(f.read())
# # f.write('\nttxs')
# f.close()


# def ran():
#     list1 = []
#     list2 = []
#     for i in range(10):
#         j = random.randint(1, 20)
#
#         with open('data.txt', 'a', encoding='utf-8') as f1:
#             if i < 9:
#                 f1.write(f'{j},')
#             else:
#                 f1.write(f'{j}')
#
#     with open('data.txt', 'r', encoding='utf-8') as f2:
#         list1 = f2.read().split(',')
#
#     for i in list1:
#         list2.append(int(i))
#     list2.sort(reverse=True)
#     print(list2)
#
#     with open('data1.txt', 'a', encoding='utf-8') as f3:
#         for i3 in range(0, 5):
#             if i3 == 4:
#                 f3.write(f'{list2[i3]}')
#             else:
#                 f3.write(f'{list2[i3]},')
#
#
# def re():
#     with open('data.txt', 'w') as f:
#         f.write('')
#     with open('data1.txt', 'w') as f1:
#         f1.write('')
#
#
# ran()
# # re()
#
#
# def ran2():
#     list1 = []
#     for i in range(10):
#         j = random.randint(1, 20)
#         list1.append(j)
#
#     with open('data.txt', 'w') as f:
#         json.dump(list1, f)
#
#     with open('data.txt', 'r') as f:
#         list2 = json.load(f)
#
#         list2.sort(reverse=True)
#         print(list2)
#         print(list2[:5])
#
#     with open('data1.txt', 'w') as f:
#         json.dump(list2[:5], f)
#
#
# ran2()


# def ex():
#     num = input('input: ')
#     try:
#         int(num)
#     except ValueError:
#         print('error')
#     else:
#         try:
#             int(1/(int(num)%2 - 1))
#         except ZeroDivisionError:
#             print('ji')
#         else:
#             print('ou')
#     finally:
#         print('end')
#
#
# ex()



# num = '1'
# print(num.isdigit())


# import tools
#
# tools.func()
# dog = tools.Dog('dd', 1)
# dog.play()

# name = './2022.7.25--2022.7.31 .xlsx'
# num = 1
#
# prog = Programme()
# list1 = prog.excel_tag(name, num)

list1 = excel_tag()

list_tag = []

for j in list1:
    list_tag.append(j.get('tag'))

for i in list1:
    # print(i.get('tag')[6:])
    # print(i.get('time'))
    # print(i.get('copy_name'))
    print('本条节目：', i)
    print('上条节目：', list1[list1.index(i) - 1])
    print(list_tag[-1])
    print()

loc = page.mskj_binding_date_select_day
print((loc[0], loc[1].format(1)))
# print(*loc)

tag = page.pmake_project_name_list
for i in range(1, 11):
    print((tag[0], tag[1].format(i)))


def get_newest_prog():
    # pro_new = ''
    # list0 = ['123', '080636河南法治报道晚间版（次日重播1次）', '080638法治现场集锦版（次日重播1次）']
    list0 = ['123', '111', '333']
    for i in list0:
        if operator.contains(list_tag, i):
            pro_new = i
            return pro_new


pro = get_newest_prog()

if not pro:
    print(111)
else:
    print(222)

# str = '<unittest.suite.TestSuite tests=[<po1.scripts.test_copy_prog_to_check.TestCopyProgToCheck testMethod=test_copy_to_check>, <po1.scripts.test_copy_prog_to_check.TestCopyProgToCheck testMethod=test_copy_to_check_0_072501_1_>, <po1.scripts.test_copy_prog_to_check.TestCopyProgToCheck testMethod=test_copy_to_check_1_072502_2_>]>'
# print(str.split('testMethod=')[1].split('>')[0])

# list_tag = []
# for j in list1:
#     tag_name = j.get('tag')[6:]
#     if operator.contains(tag_name, '好剧'):
#         tag_name = tag_name[:7]
#     elif operator.contains(tag_name, '剧场'):
#         tag_name = tag_name[:8]
#     tag_name = '000000' + tag_name
#     list_tag.append(tag_name)
#     print(tag_name)

# list_tag = []
# for j in list1:
#     list_tag.append(j.get('tag'))
#
# print(list_tag)
# tag1 = '070201好剧连连看-1剿匪英雄'
# print(not operator.contains(list_tag, tag1))