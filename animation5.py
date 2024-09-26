from manim import *
# this works the way i want it to


class MoveRight(Animation):
    def __init__(self, mobject, move_distance=2, **kwargs):
        self.move_distance = move_distance
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, linear):
        self.mobject.shift(RIGHT*self.move_distance*linear)


class Test(Scene):
    def construct(self):
        circle = Circle()
        circle.shift(2*UP)
        self.add(circle)

        self.play(MoveRight(circle, move_distance=0.2))
