import string
import random

#storing characters in lists
s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)

#ask validation from user
while True:

    try:
        characters=int(input("how many character do you want in your password?\n"))
        
        if characters < 8:
            
            print("the password should be atleast 8")
            
            user=input("please , try again")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a number.")

#shuffle all lists

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

password=[s1[0],s2[0],s3[0],s4[0]]
remaining_length = characters-4
all_char = s1+s2+s3+s4
password += random.choices(all_char, k=remaining_length)


random.shuffle(password)

#join result
final_password="".join(password)
print("strong password:",final_password)







