'''from tkinter import *

wishnum = 5

def click():
  if int(entry.get()) > wishnum:
    label.config(text = 'уменьшить')
  elif int(entry.get()) < wishnum:
    label.config(text = 'увеличить')
  else:
    label.config(text = 'победа')

window = Tk()
window.title('MyProj')
window.geometry('600x400')

label = Label(
  window, 
  text = 'Это работает!', 
  background='cyan', 
  font = ('Consolas', 15), 
  underline = 2,
  height = 2,
  width = 15
  )
label.pack()

entry = Entry()
entry.pack()

button = Button(
  window, 
  text = 'Click', 
  background='yellow', 
  font = ('Consolas', 15),
  height = 2,
  width = 10,
  activebackground = 'green',
  command = click
  )
button.pack()

window.mainloop()'''

s = '1 2 3 4 5'

s = s.split()

for i in range(len(s)):
  s.append(int(s.pop(0)))

print(s)

# 1
# Игра - угадай число. 
# В программе задано число, пользователь должен его угадать
# Если введенное число > чем загаданное, то просим уменьшить введеное число
# Если введенное число < чем загаданное, то просим увеличить введеное число

# 2
# Напишите программу, которая считывает N значений от пользователя в поле Entry,
# после ввода значений необходимо посчитать сред. арифметическое по нажатию на кнопку 
# и вывести в поле Label
# 1 2 3 4 5
'1 2 3 4 5'

# 3
# Пользователь вводит строку из нескольких слов
# Необходимо отобразить 2е слово введенное пользователем на кнопке

# 3*
# Необходимо поочередно выводить каждое слово, написанное пользователем на кнопке, когда слова закончились, 
# то меняем цвет кнопки на красный и вводим Слова закончились
# Если пользователь изменил введеную строку, то начинаем сначала

# 4
# Необходимо написать программу для генерации пароля из целых чисел и 
# символов алфавита (английский, буквы заглавные и/или прописные)
# Пользовать при этом вводит размер пароля (n - мерный пароль)
# Поля для ввода размера пароля, поле для вывода пароля и кнопка для генерации

# 5
# Необходимо написать программу для генерирования множества случайных фигур на хосте
# Фигуры должны иметь разную заливку - filln (choise(list))
# Фигуры рисуются по нажатию на кнопку
# Фигура за холст не должна выходить
# lst = ['w', 'b', 'g']
# choice(lst)
# randint(1, 5)

# 6
# Необходимо написать программу для рисования произвольного рисунка по N точек (вершин)
# Количество точек вводит пользователь, но не более 20
# Рисунок за холст не должен выходить
# В программе должно присутствовать поле для ввода N точек и кнопка
# При вводе новых значений, холст должен очищаться.

'''x = randint()
y = randint()

tmpx = x
tmpy = y

lastx = 0
lasty = 0

for i in range(5):
  xnext = randint()
  ynext = randint()
  create_line(tmpx, tmpy, xnext, ynext)
  tmpx = xnext
  tmpy = ynext
  lastx = xnext
  lasty = ynext
create_line(x, y, lastx, lasty)'''

# 7
# Напишите программу, в которой определенный символ в тексте будет заменять 
# с одного на другой. Текст пользователь пишет в виджете Text, так же у пользователя
# должна быть возможность выбрать с какого на какой символ он хочет поменять.
# Символы должны заменять по нажатию на кнопку.

# 8 
# Пользователь записывает текст в текстовом поле. 
# Нажав на кнопку, текст в поле выстраивается в обратном порядке.

#'ab c d' -> 'd c ba'

# 8 *
# Только слова должны встать в обратном порядке.

# 9
# Программа должна рисовать столбчатую диаграмму в зависимости от слов в абзаце.
# Т.е. есть виджет Text, в котором пользователь пишет текст с абзацами,
# высота прямоугольника в диаграмме зависит от количества слов,
# подсчет итоговой диаграммы происходит по нажатию на кнопку.

'''from tkinter import *
from tkinter import messagebox
import random

tap = 0

def click():
  global tap
  tap += 1
  if tap > 20:
    messagebox.showinfo('End leve', 'You win!')
    button.config(state = 'disabled')
  else:
    button.place(x = random.randint(0, 500), y = random.randint(0, 300))

root = Tk()
root.geometry('600x400')
root.resizable(False, False)

button = Button(
  text = 'Click',
  width = 10,
  height = 2,
  command = click
)
button.pack()
 
root.mainloop()'''

'''from tkinter import *
from functools import partial

primer = ''  # '3 + (2 * 2) ** 2'

def click(nameB):
  global primer
  if nameB == '=':
    primer = str(eval(primer))
    label.config(text = primer)
  elif nameB == 'C':
    primer = ''
    label.config(text = primer)
  elif nameB == 'DEL':
    primer = primer[:-1]
    label.config(text = primer)
  elif nameB == 'X^2':
    primer += '**2'
    label.config(text = primer)
  else:
    primer += nameB
    label.config(text = primer)

root = Tk()
root.config(bg = "black")
root.geometry("485x550")
root.title("Калькулятор")
root.resizable(False, False)

label = Label(text='0', font=("Consolas", 21, "bold"), bg="black", foreground="white")
label.place(x = 10, y = 50)

buttonNames = [
"C", "DEL", "*", "=",
"1", "2", "3", "/",
"4", "5", "6", "+", 
"7", "8", "9", "-",
"(", "0", ")", "X^2"
]

# '3 + (2 * 2) ** 2'

x = 10
y = 140

for i in buttonNames:
  Button(
    text = i,
    bg="white",
    font=("Consolas", 15),
    command = partial(click, i)
    ).place(
      x = x, 
      y = y,
      width = 115,
      height = 79)
  x += 117
  if x > 400:
      x = 10
      y += 81

root.mainloop()'''

'''from tkinter import *

def click():
  s = text.get('1.0', 'end')
  ns = ''
  for i in s:
    if i != entry1.get():
      ns += i
    else:
      ns += entry2.get()
  text.delete('1.0', 'end')
  text.insert('1.0', ns)


window = Tk()

text = Text(
  font = ('Arial', 20),
  wrap = WORD
)
text.pack()

entry1 = Entry()
entry1.pack()

entry2 = Entry()
entry2.pack()

button = Button(
  text = 'Click',
  command = click
)
button.pack()

window.mainloop()'''

'''drom = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def roman_to_int(num):
    return drom[num]

def int_to_roman(num):
    rim = ''
    for key, value in drom.items():
        if num == value:
            rim = key
            break
    return rim
'''

'''def plus(a, b):
  print(a + b)

plus(4,3)
print(__name__)
if __name__ == '__main__':
  print('Выполнено myproj')'''

'''from myproj import *'''







# 1) Необходимо написать класс для реализации pow(x, n)

# 1.1) Необходимо реализовать статические методы для вычисления суммы и разности двух чисел

# 2) Необходимо написать класс для преобразования целого числа в римскую цифру и обратно

'''class RomanClass:
  __drom = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
  }

  @classmethod
  def roman_to_int(cls, num):
      return cls.__drom[num]

  @classmethod
  def int_to_roman(cls, num):
      rim = ''
      for key, value in cls.__drom.items():
          if num == value:
              rim = key
              break
      return rim

print(RomanClass.int_to_roman(5))'''






# 3) Необходимо создать классы со свойствами: Rectangle (a, b), Triangle(a, b, c) и Circle(radius)

# 3.1)
# Затем необходимо реализовать: 
# метод нахождения площади у Rectangle,
# метод нахождения периметра круга у Circle, 
# метод у Triangle, который проверит - существует ли данный треугольник

'''import math

class Rec:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def test(self):
      return (self.a + self.b) * 2

recOne = Rec(2, 2)
print(recOne.test())
        
class Trian:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_exist(self):
      if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
        print('Exist')
      else:
        print('Not')
        
class Cir:
    def __init__(self, rad):
        self.rad = rad

    def perimetr(self):
      return 2 * math.pi * self.rad'''

####

'''class TableClass:
  _mat = 'no mat'

  def nameCls(self):
    print('TableClass')
  
  def __init__(self, color, height):
    self.height = height
    self.color = color

class RollTableClass(TableClass):
  def __init__(self, color, height, roll):
    super().__init__(color, height)
    self.roll = roll
    
test = RollTableClass('white', 5, 100)
test.nameCls()'''

'''class TableClass:
  
  _color = 'Not'

  def get_color(self):
    return self.__color

  def set_color(self, color):
    self.__color = color

  def __init__(self, color, height):
    self.__color = color
    self.height = height
  
  def check_height(self):
    if self.height > 10:
      print('Больше 10')
    else:
      print('Не больше 10')

  @staticmethod
  def test(color):
    if color == '':
      print('Ничего нету')
    else:
      print('Есть')

  @classmethod
  def new_obj(cls, color, height):
    tmp = cls(color, height)
    return tmp

oneT = TableClass.new_obj('Red', 10)
print(oneT.get_color())''' 


'''class TableClass:

  __color = ''

  def get_color(self):
    return self.__color

  def set_color(self, color):
    self.__color = color

  def __init__(self, color, height):
    self.__color = color
    self.height = height

  def _set_color(self, color):
    self.color = color

  @staticmethod
  def chek_color(color):
    if color == 'Red':
      print('Red')
    else:
      print('Not Red')

  @classmethod
  def new_obj(cls, color, height):
    tmp = cls(color, height)
    return tmp

bluT = TableClass.new_obj('blu', 34)

redT = TableClass('red', 15)
print(redT.__color)
print(redT.height)'''



'''class TableClass:
  
  __legs = 1

  def get_legs(self):
    return self.__legs

  def set_legs(self, legs):
    self.__legs = legs

  def test(self, roll):
    self.roll = roll

  def __init__(self, legs, mat):
    self.__legs = legs
    self.mat = mat

  @staticmethod
  def testStatic(color):
    if color == 'red':
      print('Red')
    else:
      print('No Red')

  @classmethod
  def testClsMeth(cls, legs, mat):
    cls.legs = 5
    tmp = cls(legs, mat)
    return tmp
'''

'''=class PersonClass:
  def __init__(self, name = '', lname = ''):
    self.name = name
    self.lname = lname

  def __del__(self):
    print(f'Deted {self.name} {self.lname}!')'''



# PART 1
# Необходимо написать класс Lessons, в котором будут описаны школьные предметы
# MATH = 'math', PHY = 'phy'
# Затем необходимо создать класс Student, который будет наследоваться от Lessons



# PART 2
# В классе Ученик будут динамически создаваться поля:
# имя, фамилия 
# словарь оценок, где ключ - предмет (2 - 3 предмета), значение - список оценок,
# метод для вычисления средней оценки по какому-либо предмету.
# * Добавить метод заполения оценками предмет данными извне.
# Количество оценок = 15







'''import random

MATH = 'math'
PHYSICS = 'physics'
LESSONS_COUNT = 15

class StudentClass:

  __lessons_mark = {MATH : [], PHYSICS : []}

  def get_lessons_mark(self, les):
    return self.__lessons_mark.get(les, 'Les does`t exist!')
  
  def add_lessons_mark(self, les, lstmarks):
    self.__lessons_mark[les].append(lstmarks)

  def final_mark(self, les):
    if self.__lessons_mark.get(les):
      return (sum(self.__lessons_mark.get(les)) / len(self.__lessons_mark.get(les)))
    else:
      return f'{les} not exist!'

  def __init__(self, name, lname, math = [random.randint(0, 5) for i in range(LESSONS_COUNT)], 
                    physics = [random.randint(0, 5) for i in range(LESSONS_COUNT)]):
    self.name = name
    self.lname = lname
    self.__lessons_mark[MATH] = math
    self.__lessons_mark[PHYSICS] = physics

  def __del__(self):
    print(f'Student {self.name} {self.lname} deleted!')

Borya = StudentClass('Borya', 'Who')

print(f'{MATH} = {Borya.get_lessons_mark(MATH)}')
print(f'{PHYSICS} = {Borya.get_lessons_mark(PHYSICS)}')

print(f'{MATH} = {Borya.final_mark(MATH)}')
print(f'{PHYSICS} = {Borya.final_mark(PHYSICS)}')'''


# Необходимо написать класс Line, в котором будут свойства _a - длина линии и 
# метод get_a - возврат длины _a,
# он будет родителем класса Rectangle, 
# в котором добавятся свойство __b - одна из сторон прямоугольника и
# метод square - подсчет площади прямоугольника,
# метод perimeter - подсчет периметра прямоугольника.


'''class Line:
  def __init__(self, a = 0):
    self.__a = a
  
  def get_length(self):
    return self.__a

class Rectangle(Line):
  def __init__(self, a = 0, b = 0):
    super().__init__(a)
    self.__b = b

  def get_perimeter(self):
    return (super().get_length() + self.__b) * 2
  
recOne = Rectangle(2, 2)
print(recOne.get_perimeter())'''

'''class TableClass:
  
  __legs = 0

  def __init__(self, legs, color = ''):
    self.__color = color
    self.legs = legs

  def get_color(self):
    return self.__color

  def set_color(self, color):
    self.__color = color

  @staticmethod
  def testStaticMet(color):
    if color == 'red':
      print('Red')
    else:
      print('No red')

  @classmethod
  def change_legs(cls):
    cls.legs = 5

  @classmethod
  def testClsMet(cls, legs, color):
    tmp = cls(legs, color)
    return tmp

TableClass.testStaticMet()

redT = TableClass(5, 'red')
print(redT.__color)'''


'''class Color:
    
    #red = 0
    #green = 0
    #blue = 0
    
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def toHex(self):  
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)
    
    def stats(self):
      return self.red + self.green + self.blue

class ColorAlpha(Color):
    alpha = 1

    def __init__(self, r, g, b, a):
        super().__init__(r, g, b)
        self.alpha = a
    
    def stats(self):
        return super().stats() + self.alpha

test = ColorAlpha('r', 'g', 'b', 'a')
print(test.stats())'''


'''class tableClass:
  __color = 'Not Color'

  def __init__(self, color, mat):
    self.color = color
    self.__mat = mat

  def get_mat(self):
    return self.__mat

  def set_mat(self, mat):
    self.__mat = mat

  @staticmethod
  def testStMet(color):
    if color == 'red':
      print('Red')
    else:
      print('No Red')

  @classmethod
  def testClsMet(cls):
    tmp = cls('metal')
    return tmp
    

redT = tableClass('red', 'wood')
#print(redT.__mat)
print(redT.color)'''



'''class WinDoorCls:
  def __init__(self, a, b):
    self.square = a * b

class RoomCls:
  def __init__(self, x, y, z):
    self.square = 2 * z * (x + y)
    self.wd = []

  def add_wd(self, a, b):
    self.wd.append(WinDoorCls(a, b))
  
  def free_space(self):
    freesquare = self.square
    for i in self.wd:
      freesquare -= i.square
    return freesquare

roomOne = RoomCls(5, 5, 5)
print(roomOne.square)

roomOne.add_wd(2, 2)

print(roomOne.free_space())'''

# PART 1
# Необходимо написать класс Lessons, в котором будут описаны школьные предметы
# MATH = 'math', PHY = 'phy'
# Затем необходимо создать класс Student, который будет наследоваться от Lessons

# PART 2
# В классе Student будут динамически создаваться поля:
# имя, фамилия
# словарь оценок, где ключ - предмет (2 - 3 предмета), значение - список оценок,
# метод для вычисления средней оценки по какому-либо предмету.
# * Добавить метод заполения оценками предмет данными извне.
# Количество оценок = 15

# PART 2
# Создать класс - контейнер ShoolroomCls, в котором будет создавать список учеников
# Необходимо дополнить данный класс своими методами, например реализовать посещяемость учеников

'''import random

MATH = 'math'
PHYSICS = 'phy'
LETERATURE = 'lit'

USER_ID = 0
LESSONS_COUNT = 25

class StudentCls:
  def __init__(self, name, surname):
    global USER_ID
    self.__id = USER_ID
    self.name = name
    self.surname = surname
    self.__lessons = {MATH : [], PHYSICS : [], LETERATURE : []}
    USER_ID += 1
  
  def get_id(self):
    return self.__id

  def fill_marks(self):
    for key in self.__lessons.keys():
      self.__lessons[key] = [random.randint(0, 5) for i in range(LESSONS_COUNT)]

  def get_all_les_marks(self):
    for key, value in self.__lessons.items():
      print(f'{key} - {value}')

  def get_les_marks(self, les):
    return self.__lessons.get(les, 'Такого урока нету!')

  def add_mark(self, les, mark):
    self.__lessons.get(les, 'Такого урока нету!').append(mark)

  def average_les_mark(self, les):
    s = sum(self.__lessons.get(les, 'Такого урока нету!'))
    l = len(self.__lessons.get(les, 'Такого урока нету!'))
    return s / l

  def get_average_all_les_marks(self):
    for key, value in self.__lessons.items():
      print(f'{key} - {sum(value) / len(value)}')

Borya = StudentCls('Borya', 'Ivanov')
Borya.fill_marks()
Borya.get_average_all_les_marks()'''
