#conditionals
x = 2
y = 5

print (x,y)

if x < y:
    print('x < y','yes')

if y < x:
    print('y < x','yes')

if x:
    print('x','yes')

if y:
    print('y','yes')


weather = 'not nice'

if weather == 'nice':
    print('---Weather is nice true---')
    print('Mow the lawn')
    print('Weed the Garden') 
    print('Take the dog for a walk')
print('outside if')

#pass --> ditempatkan didalam kondisi jika belum diketahui akan diisi dengan statement apa
if True:
    pass
print('outside if')

a = ['baz','qux']
while len(a):
    print(a.pop(0))

    b = ['baz','qux']
    while len(b):
        print('>',b.pop(0))
