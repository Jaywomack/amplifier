userNum1 = input("Please enter first number you would like to add: ")
userNum2 = input("Please enter the second number you would like to add: ")
        
def computeOnTwo(add1, add2):
    if(add1 != add2):
        print(f"The sum of your two values {int(add1) + int(add2)}")
    if(add1 == add2):
        print(f"The sum of your two values {int(add1)*3}")

computeOnTwo(userNum1, userNum2)