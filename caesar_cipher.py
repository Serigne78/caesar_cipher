import sys
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
def caesar():
      alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
      , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a'
      , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'
      , 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

      numbers_list = [str(nombre) for nombre in range(1, 101)]
      
      symboles = ['!', '@', '#', '$', '%', '&', '*']

      n= 0
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      texts = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      shift = shift % 26
            
      encrypt_list = []
      decrypt_list = [] 

      if direction == "encode":
            for i in range(0, len(texts)):
                  if texts[i] == " ":
                        encrypt_list.append(" ")
                        break

                  for numbers in numbers_list:
                        if texts[i] == numbers:
                              n=+2
                              
                  if n==2:
                        encrypt_list.append(texts[i]) 
                        break    
                  
                  for symbole in symboles:
                        if texts[i] == symbole:
                              n+=1 
                               
                  if n==1:
                        encrypt_list.append(texts[i])
                        break
                        
                  else:
                        position = alphabets.index(texts[i])
                        encrypt_list.append(alphabets[position+shift])
            print(f"Here is your encoded message {encrypt_list}")
      else:
            for i in range(0, len(texts)):
                  if texts[i] == " ":
                        decrypt_list.append(" ")

                  for numbers in numbers_list:
                        if texts[i] == numbers:
                              n=+2
                              
                  if n==2:
                        decrypt_list.append(texts[i]) 
                        break    
                  
                  for symbole in symboles:
                        if texts[i] == symbole:
                              n+=1 
                               
                  if n==1:
                        decrypt_list.append(texts[i])
                        break

                  
                  
                  else:
                        position = alphabets.index(texts[i])
                        decrypt_list.append(alphabets[position-shift])
            print(f"Here's the message after decytpting {decrypt_list}")

      descision = input("Type 'yes' if you want to go again or 'no' if want stop the application:\n")

      if descision == "yes":
            caesar()
      else:
            sys.exit()

caesar()


