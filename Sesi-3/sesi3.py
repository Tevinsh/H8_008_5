#Function, module, Package

# def function_name(parameters): 
#         "docstring"
#         statement(s)

#contoh function menghitung lingkaran
#misal : 
#Volume Tabung : phi * r * t
#Luas Lingkaran : phi * r * r

#contoh 1
print('-------------Function1------------')
def my_function(p,l):
    '''function to calculate are of a square'''
    print(p*l)

my_function(2,3) #memanggil fungsi my_function
# memanggil fungsi diluar block function

def printme( str_input ):
    '''This prints a passerd into this function'''
    print(str_input)

printme("Hello") #memanggil fungsi printme

#tanda asterik menujukkan tuple dan dapat diakses menggunakan for
def printinfo( name, *pets):
    '''print name and pets'''
    print("result : ",name)
    for x in pets:
        print('pets :',x)

printinfo('test','test')

#tanda double asterik  akan ditampung di dictionary dictionary //keywordarguments // **kwargs
def print_bought_items(name,**bought_items):
    print('Name :',name)
    for i in bought_items:
        print(i,bought_items[i])

print_bought_items('Ani',first_item='onion',second_item='chili')

#annonymous function
#menggunakan lambda
sum = lambda arg1, arg2: arg1 + arg2
print('value of total :', sum(10,20))

multiply = lambda arg1, arg2: arg1 * arg2
print('Multiply value : ',multiply(10,20))

#return value function
def sum(a,b):
    return a + b
print('hasil :',sum(2,7))

total = sum(7,5)
print('total',total)



for i in range(5): 
    printme(i)

print("----------Calculate Rect-----------")
def calculate_rect(length,width):
    '''This Function is used to calculate area of rectangle'''
    print('Area : ',length*width)

calculate_rect(7,10) #Jika hanya membuat satu parameter maka akan error
#bisa menggunakan optional parameter jika ingin seperti itu

#Keyword Argument
def printme( str_input ):
    '''This prints a passerd into this function'''
    print(str_input)

printme(str_input="Hello") 

def printinfo( name, age):
    '''This prints a passed info into this function'''
    print("Name :", name)
    print("Age : ", age)

printinfo( age=4, name="a")

#menambahkan nilai default ke function parameter
def printinfo( name, age=18):
    '''This prints a passed info into this function'''
    print("Name :", name)
    print("Age : ", age)
printinfo('test') #age by default 18
printinfo('test',20) #bisa di replace dengan value baru

# def printinfo(age=18, name): #error, default value harus dibelakang atau name harus disikan default valuenya
#     '''This prints a passed info into this function'''
#     print("Name :", name)
#     print("Age : ", age)
# printinfo('test') #age by default 18
# printinfo('test',20) #bisa di replace dengan value baru


#variable
#global variable
#local variable ->function->nested function

#contoh
total = 0
def sum(a,b):
    total = a+b #total disini adalah local variable
    return total
total = sum(2,9) #assign global variable dengan function yang mereturn value
print('total',total)

#penggunaan docstring

def sum_number(a,b):
    '''
    This function is ised to sum of 2 variables.
    :param a : float or int
    :param b : float or int
    :return: num3: Sum of number | int or float
    '''
    return a+b

print(sum_number.__doc__) #mengakses docstring dalam function

print(dir(sum_number))
print(sum_number.__dict__)

# Python module
import sys
print('syspath : ',sys.path)
import module1 #dari module1 yang sudah dibuat di folser Sesi-3
print(f'hasil = {module1.sum(2,3)}')
# module yang bisa di import adalah yang ada didalam direktori yang sama
# atau yang ada didalam python path. bisa dicek di sys.path 
# atau menggunakan sys.path.append(r'C:/direktori/path/nya)
sys.path.append(r'C:\Users\Pangeran Tevin Shidq\Desktop\OCBC Fullstack Development 2')
import person
print('from person module :',person.person('test','test'))

#cara import module





















