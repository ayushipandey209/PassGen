import time
import random
import string
import re

print()
print()
print("\t \t \t Hello , Welcome to PassGenPro !!!​ ")
print()
print("\t \t \t 𝒞𝑜𝒹𝑒 𝓎𝑜𝓊𝓇 𝓈𝒽𝒾𝑒𝓁𝒹, 𝑔𝓊𝒶𝓇𝒹 𝓎𝑜𝓊𝓇 𝒹𝒶𝓉𝒶. 𝒮𝒾𝓂𝓅𝓁𝑒 𝓅𝒶𝓈𝓈𝓌𝑜𝓇𝒹𝓈, 𝒷𝒾𝑔 𝓈𝑒𝒸𝓊𝓇𝒾𝓉𝓎")
print()
def loading_animation(duration):
    print("\t \t \t Loading: ", end="")
    for _ in range(duration):
        print(".", end="", flush=True)
        time.sleep(1)
        
loading_animation(7)

def generate_password(min_length , numbers = True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits 
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters +=digits
    if special_characters:
        characters+= special
    
    pwd = ""   #storing of password
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length: #one true
        new_char = random.choice(characters)
        pwd+=new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special=True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special    
        
    return pwd    


def check_password_strength(password):
    no_length = len(password) < 8
    
    no_uppercase = not any(char.isupper() for char in password)
    
    no_digit = not any(char.isdigit() for char in password)
    
    no_lowercase = not any(char.islower() for char in password)
    
    no_special = not re.search(r"[!@#$%^&*(),.?\":{}|<>]" ,password)
    
    no_common = any(no_common in password.lower() for no_common in ['password', '123456', 'qwerty'])
    
    strength_rating = 5 - sum([no_length , no_uppercase , no_lowercase , no_digit , no_special , no_common ])
    
    return strength_rating

#generates ont time password
def generate_otp(length):
    digits = "0123456789"
    otp = "".join(random.choice(digits) for _ in range(length))
    return otp



print()
#taking value from user
while True:
  try:
      print()  
      user_choice = int(input("\t  1] Generate Password   2] Generate OTP   3] Saved Password   4] Password Strength   5] Tips for password   6] FeedBack   7] Exit: "))
      if user_choice==1:
       print()   
       min_length = int(input("Enter the minimum length : "))
       has_number = input("Do you want to have a numbers (y/n)? ").lower() == "y"
       has_special = input("Do you want to have special characters (y/n)? ").lower() =="y"
       pwd = generate_password(min_length,has_number,has_special) 
       print("The generated password is : ", pwd)
       print()
       print("Do you want to save password ??")
       save_option=int(input("1] yes  2] no : "))
       if save_option==1:
           print()  
           title = input("Title of the password ? : ")
           f=open('SavedPassword.txt' ,'a')
           f.write(title + "[ " + pwd + " ]" + "  ")
           print("Password saved successfully !!")
      elif user_choice==2:
           print()  
           otp_len=int(input("Length of OTP : "))
           otp = generate_otp(otp_len)  # Generate a 6-digit OTP
           print("Generated OTP: ", otp)
      elif user_choice==3:
           print()  
           f = open('SavedPassword.txt' ,'r')
           text = f.read()
           print(text)
           f.close()
      elif user_choice==4:
           print()  
           password = input("Enter your password : ")
           strength_rating = check_password_strength(password)
           print(f"Password Strength : {strength_rating}/5")
     
      elif user_choice==5:
          print()  
          f = open('TipsOfPassword.txt' ,'r')
          text = f.read()
          print(text)
          f.close() 
          
      elif user_choice==6:
          print()  
          name= input(" Your good name please ??  ")
          user_input = input(" Please provide your feedback: ")
          f=open('FeedBack.txt' ,'a')
          f.write( name + " ->  [ " + user_input + " ] \n")
          print(f" Thankyou {name} for your feedback .")
          
      elif user_choice==7:
          break 
         
      else:
          print()  
          print("Invalid choice !!")     
  except Exception as e:
       print()
       print("Enter valid input!! ")  
 
      
         

  
    
   
  
   
   
   
