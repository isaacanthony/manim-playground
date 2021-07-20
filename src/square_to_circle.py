"""Square to circle transformation."""
from manim import *


class SquareToCircle(Scene):
    """Square to circle transformation."""

    def construct(self):
        """Entrypoint."""
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
