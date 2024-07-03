import pybrightness
b=int(input("Enter your brightness percentage: "))
# pybrightness.increase()  # Increase to 100%
# pybrightness.decrease()  # Decrease to 0%
pybrightness.custom(percent=b)  # Set to a custom level
