# hwo to reverse the string in python 

# using for loop reverse the string 

print("1. using for loop ")
print("2. using while loop ")
print("3. using slice oprator ")
print("4. using reverse function ")
print("5. using recursion ")
option  = int(input("enter your choice "))


if option == 1:
    def reverse_string(str):
        str_1 = " "
        for i in str:
            str_1 =  i + str_1
        return str_1

    str = input("enter the string :")
    print("original str is : ",str)
    print("after reverse str : ",reverse_string(str))

elif option == 2:
    str_2 = input("enter string ")
    print("original string ",str_2)
    reverse_str2 = " "
    count_2 = len(str_2)
    while count_2 > 0 :
        reverse_str2  += str_2[count_2 - 1 ]
        count_2 = count_2 -1 
    print(" reverse string : ",reverse_str2)


elif option == 3:
    str_3 = input("enter the string ")
    def reverse_str3(str_3):
        reverse_str3 = str_3[ : : -1]
        return reverse_str3
    print("original string ",str_3)
    print("reverser string",reverse_str3(str_3))

elif option == 4:
    str_4 = input("enter the string ")
    reverse_str4 = "".join(reversed(str_4))
    print("reverse string ",reverse_str4)

elif option == 5:
    print("5 work in progress")
    def reverse_str5(str_5):
        if len(str_5) == 0:
            return str_5
        else:
            return reverse_str5(str_5[1:]) - str_5[0]
    str_5 = "kailash"    
    print("reverse string ",reverse_str5(str_5))


else:
    print("wrong input pls select from menu")
