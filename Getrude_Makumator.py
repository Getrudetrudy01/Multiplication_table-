def multiplication(number):
    for j in range(0,13):
        print(str(number) + " × " + str(j) + " = ", number*j)
        
user_num = input("Enter a number to view it's multiplication table: ")        
multiplication(int(user_num))