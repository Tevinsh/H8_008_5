#Sesi 1
print("--------------------integer--------------------------------")
print(123123123123123123123123123123123123123123123123 + 1)
print(type(123123123123123123123123123123123123123123123123 + 1))
print("------------------Floating point Numbers---------------")
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)

print("------------------------Strings------------------------")
print('hello world')
print("Hacktiv8")

print(type("hacktiv8"))
print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')
 
print('This string contains a single quote (\') character.')
print("This string contains a double quote (\") character.")

a = 4
b = 2
print(a ** b)
print(a // b)   #integer division atau floor division *coba bandingkan pembagian biasa dengan integer division ini
print(a/b)      #by default mengembalikan value float
print (type(a/b))

print("------assign multiple variable with the same value")
a = b = c = 300 #assign multiple variable with the same value
print(a,b,c) #300 300 300
print(a+b+c) #900
print(str(a)+' '+str(b)+' '+str(c)) #print sebagai string   

print("------------variable dapat diganti tipe data nya-------------")
var = 23.5
print('var :',var)
print(type(var))

var = "Now I'm a string"
print('var :',var)
print(type(var))

#comparison
print('--------comparison--------')
print(100 > 200)
print(100 == 200)
print(100 < 200)
print('A' == 'a')
print('A' == 'A')  

print('---------------penulisan variabel-------------')
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)
has_5laptops = False
print(has_5laptops)
# 9_kepala_naga = True #penamaan variable yang salah


#string manipulation
print('--------------string manipulation---------------')
s='foo'
t='bar'

print(s,t)
print(s+t)
print(s*4)
print(t*4)

print(s.capitalize())
print(s in 'That food for us')
print(s in 'That good for us')
print('-------------')
print('s :',s)
print('s.lower() :',s.lower())
print('s.swapcase() :',s.swapcase()) #mengganti dari huruf besar ke kecil sebaliknya yang huruf kecil menjadi huruf besar
print('s.title() :',s.title())
print('s.upper() : ',s.upper())

print('------------list-------------')


testA = ['foo','bar','baz']
testB = ['foo','baz','bar']
print(type(testA))
print(testA)
print(testB)
#membandingkan 2 list
print(testA == testB) #comparison list

testA = testA + ['grault', 'garply'] #menambahkan list
print('testA :',testA)

#list indexing
# -5  -4  -3  -2  -1 -->bisa memanggil dengan index disini
# [1 , 2 , 3 , 4 , 5 ]
#  0   1   2   3   4 --> atau yang disini
#contoh
p= [1,2,3,4,5]
print(p[-1])
print(p[4])
print(p[1:2]) #print slice array
p[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5] #set potongan array menjadi value baru
print('p :',p)
#print(min(a))
print(a) #menambahkan array baru ke a

print('---------------tuple-------------')

#python tuples >> tidak mutable, berbeda dengan list
(s1,s2,s3,s4) = ('foo','baz','bar','qux')
print(s1,s2,s3,s4)
t4 = ('foo', 'bar', 'baz', 'qux')
print('t4 :',t4)
# (s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
(s1, s2, s3, s4) = t4
print('t4 :',t4)

t4 = ('foo', 'bar', 'baz', 'qux')
t4 = ('aa','bb', 'cc') #bisa diganti dengan value baru bukan mengganti value yang ada didalamnya
print('t4 :',t4) 
print(t4[0]) #print tuple

person1_age = 42
person2_age = 16
person3_age = 71
print(person1_age, person2_age, person3_age)

someone_is_of_working_age = (
    (person1_age >= 18 and person1_age <= 65)       # True
    or (person2_age >= 18 and person2_age <= 65)    # False
    or (person3_age >= 18 and person3_age <= 65)    # False
)

print(someone_is_of_working_age) #true or false or false = true