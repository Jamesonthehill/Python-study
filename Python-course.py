Integer = 11
Alpha = 'Mario'
ss = '11'


# print(Alpha + str(Integer))
# print(10 + int(ss))

# age = 18
# isHappy = False

# if age > 29:
#     print('you are old!')
# elif age >= 18:
#     print('you are getting old!')
# else:
#     print('you are still young!')
    
# if isHappy:
#     print('Happy Thankgiving')
# else: 
#     print('Proud of yourself')

i = 124
# even if we assign the i value, if we use again, it would be overwritten.
for i in range(3):
        print('Hello', i+3)


print (range(3))

name_list = ['jacob', 'Lee', 'hanse']

for name in name_list:
    print(name)

while True:
      user_input = input('entersometing >>')
      if user_input == '0':
            print('we are done here')
            break
      

def say_hello(name):
      print('Hey there', name)

say_hello('mario')

def get_internet():
      pass

number = input('Please provide a number >>')

try:
    print(10 + int(number))
except:
    print('that is not a valid number!')