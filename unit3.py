def determine_direction(message):
    if message == "TAKE THE ROAD LESS TRAVELLED":
        print("Turn Left")
    elif message == "COMFORT IS DIVINE":
        print("Turn Right")
    else:
        print("I don't know")

print determine_direction("TAKE THE ROAD LESS TRAVELLED")