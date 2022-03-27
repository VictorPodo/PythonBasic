#Задание 1: Вывести на экран сумму четных чисел от 1 до 100 включительно, используя функцию range()

x=0
for a in range(100):
    if a%2==0:
        x+=a
print(x)

#Задание 2: Дана строка s = 'bfgshbkis'
# Преобразовать её в строку 'ibs', используя оператор извлечения среза только один раз.

s = 'bfgshbkis'
s = s[-2:-7:-2]
print(s)

#Задание 3: Есть список numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
# Вывести все нечетные числа больше 50, используя функцию filter().

def more50_even(number):
    if number % 2 == 1 and number > 50:
        return True
    else:
        return False


numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
print(list(filter(more50_even, numbers)))

#Задание 4: Есть словарь dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
# Составить из него новый словарь, содержащий только те элементы, у которых значение больше или равно 3.

dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
new_dict={}
for i in dict:
    if dict[i] >= 3:
        new_dict[dict[i]] = i
print(new_dict)

#Задание 5:Есть список numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
# Используя модуль random, вывести случайный элемент этого списка.

import random

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
print(random.choice(numbers))

#Задание 6: Есть класс Animal c одним методом voice().
# class Animal:
# def voice(self):
# pass
# 1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
# 2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().

class Animal:
    def voice(self):
        pass


class Dog(Animal):
    def voice(self):
        return "Gav - gav!"


class Cat(Animal):
    def voice(self):
        return "may!"


class Wolf(Animal):
    def voice(self):
        return "Auuuff!"


just_dog = Dog()
just_cat = Cat()
just_wolf = Wolf()

print(just_wolf.voice())
print(just_dog.voice())
print(just_cat.voice())

#Задание 7: Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали статический метод родительского класса Animal,
# который вывел бы нам количество всех созданных экземпляров. Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.

class Animal:
    numInstance = 0

    def __init__(self):
        Animal.numInstance += 1

    def voice(self):
        pass


class Dog(Animal):
    def voice(self):
        return "Gav - gav!"


class Cat(Animal):
    def voice(self):
        return "May!"


class Wolf(Animal):
    def voice(self):
        return "Auuuff!"


def print_amount_instance():
    print('We created ', Animal.numInstance, ' instances')


just_dog = Dog()
just_cat = Cat()
just_wolf = Wolf()
just_another_animal = Animal()

print(just_dog.voice())
print(just_cat.voice())
print(just_wolf.voice())
print_amount_instance()

#Задание 8: Необходимо считать любой текстовый файл на вашем ПК (можно создать новый) и создать на его основе новый файл,
# где содержимое будет записано в обратном порядке. В конце программы вывести на экран оба файла - старый в неизменном виде и новый в обратном порядке.

import os


if os.path.exists('test_1.txt'):
    os.remove('test_1.txt')


if os.path.exists('test.txt'):
    pass
else:
    with open('test.txt','x') as a:
        a.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                  'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
                  'Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                  'laboris nisi ut aliquip ex ea commodo consequat.')


with open('test.txt', 'r') as a:
    a = a.read()
    print(a)

with open('test_1.txt','x') as x:
    x.write(a[::-1])

with open('test_1.txt','r') as x:
    x_str = x.read()
    print(x_str)

#Задание 9: Необходимо создать два параллельных потока, каждый из которых выводил бы на экран числа от 10 до 1 в
# обратном порядке с интервалом в одну секунду. В выводе должно быть понятно какая нить выполняется,
# и когда каждая из них начинает и заканчивает своё выполнение.

import threading
import time


def count(i):
    k = 10
    while k > 0:
        print(f"{i} Очередь сейчас пишет: {k}")
        k -= 1
        time.sleep(1)


for i in range(1, 3):
    th = threading.Thread(target=count, args=(i,))
    th.start()

#Задание 10: 1. Открыть страницу http://google.com/ncr
# 2. Выполнить поиск слова “selenide
# 3. Проверить, что первый результат – ссылка на сайт selenide.org.
# 4. Перейти в раздел поиска изображений
# 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
# 6. Вернуться в раздел поиска Все
# 7. Проверить, что первый результат такой же, как и на шаге 3.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

test = webdriver.Chrome(executable_path='C:\selenium browser driver\chromedriver.exe')
test.implicitly_wait(5)
test.get("http://google.com/ncr")
test.find_element(By.CSS_SELECTOR, 'input.gLFyf').send_keys('selenide')
test.find_element(By.CSS_SELECTOR, 'input.gLFyf').send_keys(Keys.ENTER)
assert "selenide.org" in test.find_element(By.TAG_NAME, "cite").text
test.find_element(By.LINK_TEXT, 'Images').click()
print(test.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]').text)

assert "selenide.org" in test.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]').text

test.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]').click()
assert "selenide.org" in test.find_element(By.TAG_NAME, "cite").text
test.quit()