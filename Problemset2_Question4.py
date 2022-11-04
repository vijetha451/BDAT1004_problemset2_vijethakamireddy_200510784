def collatz(x):
    """
        Following while loop runs until x is not equal to 1
        Once x==1 then the loop is terminated.
    """
    while x != 1:
        """
            At first we print whatever the current value of x is.
        """
        print(x)

        """
            Now there are two possibilities for x
            1) x is even
            2) x is odd
        """
        if x % 2 is 0:
            """
                x is even if remainder is 0 of division of x by 2.
                Using modulus operator we get to know if x is even or odd.

                -> So is x is even we divide it by 2 as x=x/2 
                In python we use double forward slashes to get integer after division
                See below
            """
            x = x // 2
        else:
            """
                If x is odd then we update x as x=3*x+1
            """
            x = 3 * x + 1
    """
        Once the while loop is terminated Note that 1 is not yet printed.
        As when x is 1, the loop gets terminated. So we need to print 1 explicitly in the end
        of the function collatz()
    """
    print(1)


"""
    Now the program prompts the user to enter to enter value of x
"""
x = int(input("Please enter the value of n ::"))

"""
    Below we call the function collatz() with x as parameter.
"""
collatz(x)

