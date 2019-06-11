import turtle

def main():
    filename = ('turtle_commands.txt')

    # Create a turtle graphic window
    t = turtle.Turtle()
    # Screen is used at the end of the program
    screen = t.getscreen()

    # Read the file from tha above path
    file = open(filename, 'r')
    # Read the files line by line
    for line in file:
        text = line.strip()

        # For instance, if text contained "goto, 10, 20, 1, black" then
        # commandList will be equal to ["goto", "10", "20", "1", "black"] after
        # splitting text.
        commandlist = text.split(',')
        command = commandlist[0]

        if command == 'goto':
            x = float(commandlist[1])
            y = float(commandlist[2])
            width = float(commandlist[3])
            color = commandlist[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)
        elif command == 'circle':
            radius = float(commandlist[1])
            width = float(commandlist[2])
            color = commandlist[3].strip()
            t.width(width)
            t.color(color)
            t.circle(radius)
        elif command == 'beginfill':
            color = commandlist[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == 'endfill':
            t.end_fill()
        elif command == 'penup':
            t.penup()
        elif command == 'pendown':
            t.pendown()
        else:
            ('Unknown command found in file: ', command)

    file.close()
    # hide the turtle that we used to draw the picture
    t.ht()
    # This causes the program to hold the turtle graphics window open
    # until the mouse is clicked.
    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ == '__main__':
    main()