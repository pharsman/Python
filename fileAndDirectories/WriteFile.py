text1 = "Yoooooooooo\nThis is some text\nHave a good one!\n"
text2= "Have a nice day! See ya"

with open('./fileAndDirectories/test.txt','w') as file:
    file.write(text1)
    
with open('./fileAndDirectories/test.txt','a') as file:
    file.write(text2)