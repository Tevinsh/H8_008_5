print('hello World')

x,y,z = 3,5,'a'
print(x,y,z)

x = "awesome"
def greetings():
    #x="fantastic"
    print("Python is "+x)

greetings()

print("python is "+x)

#Tugas Sesi 2
numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 
  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 
  942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 
  615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 
  626, 949
  ]

numbers.sort()
for x in numbers:
    if x>918:
        print('Done')
        break
    else:
        print(x)
#print(numbers)