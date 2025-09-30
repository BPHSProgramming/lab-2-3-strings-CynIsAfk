import os
os.system("cls")

print("Task #1")
full_name = input("Enter Full Name:")
space_Location = full_name.find(" ",0)
first_name = full_name[:space_Location]
last_name = full_name[(space_Location+1):]
print(first_name.title(),last_name.title())
print(first_name[0].lower(),first_name[1:].upper()," ",last_name[0].lower(),last_name[1:].upper(),sep="")
print("Task #2")
star_wars = "Once you start down the dark path, forever will it dominate your destiny."
semi_encryption = star_wars.upper()
encrypt_a = semi_encryption.replace("A","1")
encrypt_b = encrypt_a.replace("E","2")
encrypt_c = encrypt_b.replace("I","3")
encrypt_d = encrypt_c.replace("O","4")
encryption = encrypt_d.replace("U","5")
print(encryption)
print("Task #3")
original_length = len(star_wars)
phrase_split = ((original_length-1)//3)
print(phrase_split)
phrase_part1 = star_wars[0:phrase_split]
phrase_part2 = star_wars[phrase_split:2*phrase_split]
phrase_part3 = star_wars[2*phrase_split:3*phrase_split]
print(phrase_part2,phrase_part3,phrase_part1,sep="\n")