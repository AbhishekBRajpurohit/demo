# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# write in a file
# st = "hey harry"
# f = open("myfile.txt","w")
# f.write(st)
# f.close()

# reading lines in the form of list.
# f = open("file.txt")
# lines = f.readlines()
# print(lines,type(lines))
# f.close()

# single line reading how to do
# f = open("file.txt")
# line1 = f.readline()
# print(line1)

# shine2 = f.readline()
# print(shine2)

# line4 = f.readline()
# print(line4)

# using while loop
# f = open("file.txt")
# line = f.readline()
# while(line!=""):
#     print(line,end =" ")
#     line = f.readline()
# f.close()    
 
# appending file
# st = "ur amazing"
# f = open("myfile.txt","a")
# f.write(st)
# f.close()

# if i dont want to write close statement ie f.close() every time what should i do
# with open("file.txt") as f:
#     print(f.read())

# to find file from the file read and search rthe given word
# f = open("file.txt")
# data = f.read()
# if("twinkle" in data):
#     print("twinkle is present in the given data")
# else:
#     print("twinkle is absent in the content")
# f.close()

# doing game which prints score
# import random
# def game():
#     print("your playing the game")
#     score = random.randint(1,62)
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"your score is:{score}")
#     if(score>hiscore):
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))
#     return score
# game()  
# tables inm file
def genTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} * {i} = {n*i}\n"
        with open(f"tables/table_{n}.txt", "w") as f:
            f.write(table)
for i in range(2,21):
    genTable(i)




                
        


