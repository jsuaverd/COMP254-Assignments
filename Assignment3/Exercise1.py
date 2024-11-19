def recursive_digit_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + recursive_digit_sum(n // 10)
    
# user input
num1 = 6
print("\nThe input is: " + str(num1))
print("\nThe sum of the digits is: " + str(recursive_digit_sum(num1)))

num2 = 23
print("\nThe input is: " + str(num2))
print("\nThe sum of the digits is: " + str(recursive_digit_sum(num2)))

num3 = 45
print("\nThe input is: " + str(num3))
print("\nThe sum of the digits is: " + str(recursive_digit_sum(num3)))