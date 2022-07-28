print("Hello myself doing a project")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")
character_name = "Ivan "
character_age = "10"
isMale = True
print("hello I am doing a project")
print("I " + character_name + " I am " + character_age + " and you know that duh ")
# instead of changing the name etc. you can tell what charecter_name is equal to and copy and paste it.


character_name = "Mike"
print(
    "I am listening do a random " + character_name + " from youtube, and I dont like this " + character_name + ", and i am just saying the word " + character_name + " so much.")
phrase = "Girrafe\nAcademy"
print(phrase + " is not cool")
print(phrase.lower())
# or instead of lower case you can do upper case. Ex:print(phrase.upper())
print(phrase.isupper())
# to see if your string is actually lower case or not.You can also do "islower" to see if its up"

print(phrase.upper().isupper())
print(len(phrase))
print((phrase[0]))  # python starts counting starting at 0,1,2,,3,4 etc. that's why 0 = G in the word Giraffe Academy.
# the "numbers" in python are also called index.
print(phrase.index("c"))

print(phrase.replace("Girrafe", "Elephant"))
my_num = 5
print(str(my_num) + " not my favorite number")
print(pow(5, 4))
print(max(5, 4))
# or say min so it will say the smallest number out of whatever numbers you choose , you can round too. there is max too
from math import *

print(floor(3.7))  # just chops off the decimal.
print(ceil(3.7))  # just does the exact opposite (it just basically rounds the number)

# this will give you  a prompt (or question on the topic) and you can answer it
# Ex Enter your name: (You should put your answer over here!)
# this is just the same thing, but it's asking a different question ex age, name, address, etc.


age = input("How old were you when you ate your first hot dog?: ")

print("hello mIke " + "! You are " + age)

num1 = input("Enter a number:")
num2 = input("Enter another number:")
result = float(num1) + float(num2)
print(result)  # float = decimal=true int= decimal=false

# me making a simple  mad libs game.

color = input("Enter a color:")
plural_noun = input("Enter a Plural noun:")
celebrity = input("Enter a celebrity:")

# this is a " list function
lucky_numbers = ["1", "2", "2", "4", "4", "5", "5", "6"]
friends = ["kevin", "Captian underpants", "Spidy man that pooped his pants"]
friends.extend(lucky_numbers)
friends.append("Creed")  # This just adds the name to the list "friends"
friends.insert(1, "kelly")  # this just means insert in the index you wanted it to be in.
friends.pop()  # this just removes the last item from the list.
friends.sort()  # this just sort the lists the words in the alphabetical order.
friends2 = friends.copy()
print(friends.count("kevin"))
print(friends)

# this is a tuple   for people that do not want to change their data or their data will not be changed.
coordinates = (4, 5)
print(coordinates[0])


# this is a basic function.
def sayhi(name, age):
    print("Hello " + name + ",you are " + age)


sayhi("mike", "35")
sayhi("random user from the internet", "i dont know like 50?")


# by default the function will not print, you have to " call it" by "sayhi()" or whatever the name of the function is.

# this is a return statement
def cube(num):
    return num * num * num


result = cube(4)
print(result)

# if statements are  like when its raining im bring an umbrella else I bring sunglasses
is_male = True
is_tall = False
if is_male and is_tall:
    print("you are a male and you are tall ")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are a tall female.Well duh.")

else:
    print("you are not a male nor you are not tall")


# MORE IF STATEMENTS
def max_num(num1, num2, num3):
    if num1 == num2 and num1 == num3:
        return num1
    elif num2 == num1 and num2 == num3:
        return num2
    else:
        return num3

    # IMPORTANT there are lots of other operations like (>=, not equal: !=,  <=, and lots more which im lazy to list )


print(max_num(3, 4, 5))

# Making a "better" calculator
num1 = float(input("Enter you first number: "))
op = input("Enter your operator: ")
num2 = float(input("Enter  second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Um, I sorry, this calculator is  not like THAT better, Okay?  We just dont have this operator, Smart ass. ")

# basic dictionary
monthconversions = {
    "Jan": "January",
    "feb": "February",
    "Mar": "March",
    "apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthconversions["Dec"])

# while loop A while loop is when python is checking if the statement is true.
i = 1
while i <= 10:
    print(i)
    i += 1
print("done with the freaking loop")

# making a guessing game
secret_word = "Cattywampus"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("YOU LOSE, myself, you probably did it on purpose to see if the code is working fine. ")
else:
    print("You finally did it (myself), actually if this was another person he will probably didn't guess it.Dingus")

    # for loops
    friends = ["Jim", "Captain poopy pants", "idk i dont have that much friends"]
    for index in range(10):
        print(index)


    # exponent function this is a program that multiplies the number by itself so many times.
    # base_num is the number(1,2,3,4,5,6,7,8,9,) and pow_num is how many times it's going to multipy by its self
    def raise_to_the_freaking_power(base_num, pow_num):
        result: int = 1
        for index in range(pow_num):
            result = result * base_num
        return result


    print(raise_to_the_freaking_power(3, 2))

# this is basically a grid like 3 columns and 2 rows
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [0]

]
# this is going to print whatever index of the colum/row. 0 = row 1 and colum 0 is 1, so the answer is 1.
print(number_grid[0][0])

# if you want to get individual numbers:
for row in number_grid:
    for col in row:
        print(col)


# making a translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Please enter your word or whatever:")))

# This is just a program  when there is an error It's going to print out whatever input and avoid breaking-it
try:
    number = int(input("Enter a number:"))
    print(number)
except:
    print("you put a LETTER or a WORD you need to put a NUMBER dumbie")

# you could also put a specific err like (ZeroDivisionError)


# this program is used to read or modify a file like the one I did (emplyees.txt)
# there are different mods to open a file like "r" which means read, and "w" which means modify (or writing the file).
# there is also a mod called "a" which allows you to add new info but doesn't allow you to change the old info
# Another mod is "r+" this is just combine "r" and "w"
employee_file = open("employees.txt", "r")

print(employee_file.read())

employee_file.close()

# print(employee_file.readable())
# is just going to give us a boolean.For example if mode is r than he is going to say true and if its w then it's false
# readline is just going to read an individual line in the file
# readlineS is just going to put the lines (in the file) and going to put them in a list.
# and readiness[] to put a specific line in the list using index (0,1,2,3,4,5,6,7,8,9)



