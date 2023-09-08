position = "right", "center", "left"
direction = "l", "r"

for i in range(1, 20, 2):
    position = "right"
    if position == "right":
        print("right")
        direction = "l"
        if direction == "l":
            print("center")
    position = "center"
    if position == "center":
        print("left")
        direction = "r"
        if direction == "r":
            print("center")
