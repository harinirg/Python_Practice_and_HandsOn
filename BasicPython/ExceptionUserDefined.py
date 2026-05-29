#define user_Defined exceptions
class Error(Exception):
    """Base class for other exception"""
    pass
class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass
number=10
while True:
    try:
        num = int(input("Enter a number: "))

        if num < number:
            raise ValueTooSmallError

        elif num > number:
            raise ValueTooLargeError

        break

    except ValueTooSmallError:
        print("This value is too small,try again!")

    except ValueTooLargeError:
        print("This value is too large,try again!")
print("Congratulations! You guessed correctly.")