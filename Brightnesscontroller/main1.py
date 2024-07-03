import screen_brightness_control as sbc
b=int(input("Enter your brightness level: "))
current_brightness = sbc.get_brightness()
print(current_brightness)  # Output: Current brightness level (e.g., 50)

sbc.set_brightness(b)
print(sbc.get_brightness())  # Output: Updated brightness level (e.g., 75)
