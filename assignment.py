def user_input(alphabets, Index):
    if Index > 25 or Index<0:
        print("The letter cannot be recognized !\n")
    else: 
        print(alphabets[Index]+"\n")


    

alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
while True:
    Index=eval(input("Enter an index number:"))
    user_input(alphabets,Index)
    
