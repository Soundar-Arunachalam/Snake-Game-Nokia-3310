from turtle import Turtle
DIMENSIONS= [(0, 0), (-20, 0), (-40, 0),(-60,0),(-80,0),(-100,0),(120,0),(-140,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180


class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]




    def create_snake(self):
        for position in DIMENSIONS:
            self.add_segments(position)
    def add_segments(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
    #add new segment to the snake
        self.add_segments(self.segments[-1].position())




    def move(self):

        for x in range(len(self.segments)-1,0,-1):
            new_x=self.segments[x-1].xcor();
            new_y=self.segments[x-1].ycor();
            self.segments[x].goto(new_x,new_y)
        self.segments[0].forward(20)
    def getAngle(self):
        return self.segments[0].heading()


    def right(self):
        if self.getAngle()!=LEFT:
            self.segments[0].setheading(RIGHT)




    def left(self):
        if self.getAngle()!=RIGHT:
            self.segments[0].setheading(LEFT)



    def up(self):
        if self.getAngle()!=DOWN:
            self.segments[0].setheading(UP)



    def down(self):
        if self.getAngle()!=UP:
            self.segments[0].setheading(DOWN)











