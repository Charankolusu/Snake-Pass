def two_player():
    from message import crashed
    import turtle
    import time
    import random
    from pygame import mixer

    delay = 0.2

    # score
    score = 0
    score2 = 0

    # set up screen
    wn = turtle.Screen()
    wn.title("snake bite")
    wn.bgcolor("black")
    wn.setup(width=1370, height=690)
    wn.tracer(0)
    wn.bgpic("cover.gif")
    wn.addshape("apple.gif")
    wn.addshape(
        "upmouth.gif")  # Here we have given command to add shape  to thw window, and we use image in the form of gif
    wn.addshape(
        "rightmouth.gif")  # Here we have given command to add shape  to thw window, and we use image in the form of gif
    wn.addshape(
        "leftmouth.gif")  # Here we have given command to add shape  to thw window, and we use image in the form of gif
    wn.addshape(
        "downmouth.gif")  # Here we have given command to add shape  to thw window, and we use image in the form of gif
    wn.addshape("body.gif")

    wn.addshape(
        "upmouth1.gif")  # Here we have given command to add shape  to thw window, and we use image in the form of gif
    wn.addshape(
        "rightmouth1.gif")  # Here we have given command to add shape  to thw window, and we use image in the form of gif
    wn.addshape(
        "leftmouth1.gif")  # Here we have given command to add shape  to thw window, and we use image in the form of gif
    wn.addshape(
        "downmouth1.gif")  # Here we have given command to add shape  to thw window, and we use image in the form of gif
    wn.addshape("body2.gif")

    # Background music
    mixer.init()
    mixer.music.load("Snake.wav")
    mixer.music.play(-1)

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("upmouth.gif")
    head.penup()
    head.goto(-100, 0)
    head.direction = "stop"
    head.shapesize(1.3)

    # Snake head2
    head2 = turtle.Turtle()
    head2.speed(0)
    head2.shape("upmouth1.gif")
    head2.penup()
    head2.goto(100, 0)
    head2.direction = "stop"
    head2.shapesize(1.3)

    # snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("apple.gif")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    segments = []
    segments2 = []

    # pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("circle")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(610, 200)
    pen.write("""
    Blue snake: 0 
    """, align="right", font=("courier", 24, "normal"))
    pen.goto(250, 150)
    pen.write("""
    Green snake: 0 
    """, align="left", font=("courier", 24, "normal"))

    pen1 = turtle.Turtle()
    pen1.hideturtle()
    pen1.pencolor("black")
    pen1.goto(-300, 250)
    pen1.clear()
    for i in range(2):
        pen1.forward(100)
        pen1.left(90)
        pen1.forward(30)
        pen1.left(90)
    pen1.penup()
    pen1.write("🏠Home", font=("courier", 20, "normal"), align="left")

    def buttonClick(x, y):
        global colorvar
        if x > -300 and x < -200 and y > 250 and y < 290:
            wn.bye()
            crashed()

    wn.onscreenclick(buttonClick, 1)
    wn.listen()

    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"
            head.shape("downmouth.gif")

    def go_down():
        if head.direction != "up":
            head.direction = "down"
            head.shape("downmouth.gif")

    def go_left():
        if head.direction != "right":
            head.direction = "left"
            head.shape("leftmouth.gif")

    def go_right():
        if head.direction != "left":
            head.direction = "right"
            head.shape("rightmoth.gif")

    def move():
        if head.direction == "up":
            head.sety(head.ycor() + 20)
            head.shape("upmouth.gif")
        if head.direction == "down":
            head.sety(head.ycor() - 20)
            head.shape("downmouth.gif")
        if head.direction == "right":
            head.setx(head.xcor() + 20)
            head.shape("rightmouth.gif")
        if head.direction == "left":
            head.setx(head.xcor() - 20)
            head.shape("leftmouth.gif")

    # Functions
    def go_up2():
        if head2.direction != "down":
            head2.direction = "up"
            head2.shape("downmouth1.gif")

    def go_down2():
        if head2.direction != "up":
            head2.direction = "down"
            head2.shape("downmouth1.gif")

    def go_left2():
        if head2.direction != "right":
            head2.direction = "left"
            head2.shape("leftmouth1.gif")

    def go_right2():
        if head2.direction != "left":
            head2.direction = "right"
            head2.shape("rightmoth1.gif")

    def move2():
        if head2.direction == "up":
            head2.sety(head2.ycor() + 20)
            head2.shape("upmouth1.gif")
        if head2.direction == "down":
            head2.sety(head2.ycor() - 20)
            head2.shape("downmouth1.gif")
        if head2.direction == "right":
            head2.setx(head2.xcor() + 20)
            head2.shape("rightmouth1.gif")
        if head2.direction == "left":
            head2.setx(head2.xcor() - 20)
            head2.shape("leftmouth1.gif")

    # keyboard

    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    wn.listen()
    wn.onkeypress(go_up2, "Up")
    wn.onkeypress(go_down2, "Down")
    wn.onkeypress(go_left2, "Left")
    wn.onkeypress(go_right2, "Right")

    # Main game Loop
    while True:
        wn.update()
        # border collisions
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 280 or head.ycor() < -280:
            time.sleep(0.1)
            head.goto(-100, 0)
            head.direction = "stop"
            # hiding segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clearing segments
            segments.clear()

            score = 0

            # reset the speed
            delay = 0.2

            pen.clear()
            pen.write(f"""
                            Blue Snake: {score}     
                            Green Snake: {score2}
                    """.format(score, score2), align="center", font=("courier", 24, "normal"))
        # border collisions2
        if head2.xcor() > 290 or head2.xcor() < -290 or head2.ycor() > 280 or head2.ycor() < -280:
            time.sleep(0.1)
            head2.goto(100, 0)
            head2.direction = "stop"
            # hiding segments
            for segment2 in segments2:
                segment2.goto(1000, 1000)

            # clearing segments
            segments2.clear()

            score2 = 0

            # reset the speed
            delay = 0.2

            pen.clear()
            pen.write(f"""
                            Blue Snake: {score}     
                            Green Snake: {score2}
                    """.format(score, score2), align="center", font=("courier", 24, "normal"))

        if head.distance(food) < 20:
            x = random.randrange(-250, 250, 20)
            y = random.randrange(-250, 220, 20)
            food.goto(x, y)
            bite = mixer.Sound("bite.wav")
            bite.play()

            # SEGMENTS
            new_segemnt = turtle.Turtle()
            new_segemnt.shape("body.gif")
            new_segemnt.penup()
            segments.append(new_segemnt)

            # reducing speed
            delay -= 0.003

            # score
            score += 1

            pen.clear()
            pen.write(f"""
                            Blue Snake: {score}     
                            Green Snake: {score2}
                    """.format(score, score2), align="center", font=("courier", 24, "normal"))

        if head2.distance(food) < 20:
            x = random.randrange(-260, 260, 20)
            y = random.randrange(-240, 230, 20)
            food.goto(x, y)
            bite = mixer.Sound("bite.wav")
            bite.play()

            # SEGMENTS
            new_segemnt1 = turtle.Turtle()
            new_segemnt1.speed(0)
            new_segemnt1.shape("body2.gif")
            new_segemnt1.penup()
            segments2.append(new_segemnt1)

            # reducing speed
            delay -= 0.003

            # score
            score2 += 1

            pen.clear()
            pen.write(f"""
                            Blue Snake: {score}     
                            Green Snake: {score2}
                    """.format(score, score2), align="center", font=("courier", 24, "normal"))

        # moving segemnt along head
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        # moving segemnt along head
        for index in range(len(segments2) - 1, 0, -1):
            x = segments2[index - 1].xcor()
            y = segments2[index - 1].ycor()
            segments2[index].goto(x, y)

        # segment 0
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        # segment 0
        if len(segments2) > 0:
            x = head2.xcor()
            y = head2.ycor()
            segments2[0].goto(x, y)

        move()
        move2()

        # body collisions
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(0.1)
                head.goto(-100, 0)
                head.direction = "stop"

                # hiding segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # clearing segments
                segments.clear()

                # update of score
                score = 0

                # reset the speed
                delay = 0.2

                pen.clear()
                pen.write(f"""
                                Blue Snake: {score}     
                                Green Snake: {score2}
                    """.format(score, score2), align="center", font=("courier", 24, "normal"))

        # body collisions
        for segment2 in segments2:
            if segment2.distance(head2) < 20:
                time.sleep(0.1)
                head2.goto(100, 0)
                head2.direction = "stop"

                # hiding segments
                for segment2 in segments2:
                    segment2.goto(1000, 1000)

                # clearing segments
                segments2.clear()

                # update of score
                score2 = 0

                # reset the speed
                delay = 0.2

                pen.clear()
                pen.write(f"""
                                Blue Snake: {score}     
                                Green Snake: {score2}
                    """.format(score, score2), align="center", font=("courier", 24, "normal"))
        time.sleep(delay)
    wn.mainloop()
