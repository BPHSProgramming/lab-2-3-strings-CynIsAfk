#Travis Coffey Period 8
import os
os.system("cls")

print("Task #1")
full_name = input("Enter Full Name: ")
space_Location = full_name.find(" ",0)
first_name = full_name[:space_Location]
last_name = full_name[(space_Location+1):]
print(first_name.title(),last_name.title())
print(first_name[0].lower(),first_name[1:].upper()," ",last_name[0].lower(),last_name[1:].upper(),sep="")

print("Task #2")
star_wars = "Once you start down the dark path, forever will it dominate your destiny."
encryption = star_wars.upper()
encryption = encryption.replace("A","1")
encryption = encryption.replace("E","2")
encryption = encryption.replace("I","3")
encryption = encryption.replace("O","4")
encryption = encryption.replace("U","5")
print(encryption)

print("Task #3")
original_length = len(star_wars)
phrase_split = ((original_length-1)//3)
print(phrase_split)
phrase_part1 = star_wars[0:phrase_split]
phrase_part2 = star_wars[phrase_split:2*phrase_split]
phrase_part3 = star_wars[2*phrase_split:3*phrase_split]
print(phrase_part2,phrase_part3,phrase_part1,sep="\n")

print("Task #4")
number = input("Enter 5 digit number: ")
number_1 = number[0]
number_2 = number[1]
number_3 = number[2]
number_4 = number[3]
number_5 = number[4]
number_total = int(number_1 + number_2 + number_3 + number_4 + number_5)
print(f"{number_1} + {number_2} + {number_3} + {number_4} + {number_5} = {number_total}")

print("Task #5")
funny_phrase = "Why, you stuck-up half-witted scruffy-looking nerf herder."
phrase_slice = funny_phrase.find(".")
print(funny_phrase[0:int(phrase_slice):2])
print(funny_phrase[-int(phrase_slice)::2])

print("Task #6")
from datetime import date


today = date.today()

today = today.strftime("%Y,%B,%d")


print(f"The date today is {today}")

date_length = int(len(today))
month_length = int(date_length-8)
year = today[0:4]
month = today[5:month_length+5]
day = today[-2:8+month_length]
print(f"It is the {day} of {month}, {year}")