# Decimal to binary conversion
# using recursion
def getbinary(number):
    # Base case
    if number == 0:
        return 0

    # Recursion call and storing the result
    smallans = getbinary(number // 2)

    return number % 2 + 10 * smallans


# Driver Code
decimal_number = 19
print(getbinary(decimal_number))

