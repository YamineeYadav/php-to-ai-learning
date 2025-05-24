def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return fact(n-1)*n

print(fact(6))



# def calculate_sum(input1,input2):
#     sum = input1+input2
#     print(sum)
#     return sum


# calculate_sum(2,3)

# calculate_sum(3,3)

# calculate_sum(7,3)

# def calculate_cities(list):
#     print(len(list))

# cities_detail = ["delhi","gurgaon","noida","mumbai"]
# cities_detail1 = ["delhi","gurgaon","noida"]
# calculate_cities(cities_detail1)

# n=5
# fact =1

# def calculate_factorial(n):
#     """Calculate and return the factorial of a given number n."""
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i  # Shorthand for fact = fact * i
#         print(result)
#     return fact

# # Call the function and print the result
# result = calculate_factorial(6)


# Calculate INR for USD
# def converter(usd_val):
#     """Convert USD to INR using a fixed conversion rate of 1 USD = 83 INR."""
#     inr_val = usd_val * 83  # Conversion logic
#     return inr_val  # Return the converted value

# # Call the function and print the result
# result = converter(73)
# print(result)

# calculate even and odd of given number
def calculate_even_odd(val):
    """Convert USD to INR using a fixed conversion rate of 1 USD = 83 INR."""
    if val % 2 == 0 :
        print("Even")
    else:
        print("odd")
    

# Call the function and print the result
result = calculate_even_odd(72)
# print(result)




