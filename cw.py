#write a program to detect double spaces in a string.
#replace the double spaces from problem 3 with singlr spaces.
#write a program to format the following letter using escape sequence characters.
# letter = "Dear students, this python coyrse is going well. Thanks"

#write a program to detect double spaces in a string.
ext = input ("enter a string ")
if " " in text:
    print("double space detected")
else:
    print("No double space found")

#replace the double spaces from problem 3 with singlr spaces.
text=input("enter a string")
fixed_text=text.replace(" "," ")
print("fixed string:",fixed_text)

#write a program to format the following letter using escape sequence characters.
# letter = "Dear students, this python coyrse is going well. Thanks"
letter = "Dear Students,\nThis python course is going well.\nThank you"
print