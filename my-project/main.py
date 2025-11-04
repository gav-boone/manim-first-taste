from manim import *


class DeathlyHallows(Scene):
    def construct(self):
        tri_width = 4
        tri_height = (tri_width * 3**-2) / 2
        triangle = Triangle().set_color(WHITE)
        triangle.set_height(tri_height)
        triangle.set_width(tri_width)

        mid_bot = triangle.get_bottom()
        left = mid_bot + np.array([-tri_width / 2, 0, 0])
        right = mid_bot + np.array([tri_width / 2, 0, 0])
        top = triangle.get_top()

        mid_left = (left + top) / 2
        mid_right = (right + top) / 2

        circle = Circle().from_three_points(mid_bot, mid_left, mid_right, color=WHITE)

        d1 = Dot().set_color(WHITE)
        l1 = Line()
        l1.set_color(BLACK)
        l1.z_index = -1
        l1.put_start_and_end_on(triangle.get_top(), triangle.get_bottom())
        l2 = VMobject()

        self.wait(0.5)
        self.play(GrowFromCenter(triangle))
        self.play(FadeIn(circle, scale=0.5))
        self.add(d1, l1, l2)
        l2.add_updater(
            lambda x: x.become(
                Line(UP, d1.get_center())
                .set_color(WHITE)
                .put_start_and_end_on(triangle.get_top(), d1.get_center())
            )
        )
        self.play(MoveAlongPath(d1, l1), rate_func=linear)
        self.remove(d1)
        self.wait(0.5)
