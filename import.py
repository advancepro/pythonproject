a = input('What is your name: ')
b = int(input('How old are you: '))
c = input('Where are you from: ')
d = int(input('What did you get on midterm exam:'))

try:
    f = open("file.txt", "w+")
    try:
        f.write('What is you name: ' + a)
        f.write('\nHow old are you: ' + str(b))
        f.write('\nWhere are you from: ' + c)
        f.write('\nWhat did you get on midterm exam: ' + str(d))
    finally:
        f.close()
except Exception as e:
  print(e)
