value=float(input("Enter a value:-"))

if value>1.0 and value<2.0:
    print("Microearthquakes not felt or rarely felt")
elif value>2.0 and value<4.0:
    print("Very rarely causes damage")
elif value>4.0 and value<5.0:
    print("Damage done to weak buildings")
elif value>5.0 and value<6.0:
    print("Cause damage to the poorly constructed building")
elif value>6.0 and value<7.0:
    print("Causes damage to well-built structures")
elif value>7.0 and value<8.0:
    print("Causes damage to most buildings")
elif value>8.0 and value<9.0:
    print("Causes major destruction")
elif value>9.0:
    print("Causes unbelievable damage")
else:
    print("not valid input")
