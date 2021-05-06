from manim import *


class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        circle.move_to(LEFT * 2)
        self.add(circle)
        self.play(FadeIn(circle))

        # place the square to the left of the circle
        square.next_to(circle, LEFT)
        square.set_fill(YELLOW, opacity=0.7)

        self.add(square)
        self.play(Rotate(square, PI/4))
        square.shift(UP)

        # align the left border of the triangle to the left border of the circle
        triangle.next_to(circle, RIGHT)

        self.add(triangle)
        self.play(FadeOut(triangle))

        self.wait(1)
