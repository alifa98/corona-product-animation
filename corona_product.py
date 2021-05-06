from manim import *


class CoronaProduct(Scene):
    def construct(self):
        question_title = Tex("What is Corona Product?")
        formulaTextTitle = MathTex(r"G \odot H")
        VGroup(question_title, formulaTextTitle).arrange(DOWN)
        self.play(
            Write(question_title),
            FadeInFrom(formulaTextTitle, UP),
        )
        self.wait()

        title = Tex("Corona Product")
        title.to_corner(UP + LEFT)
        self.play(
            Transform(question_title, title),
            LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in formulaTextTitle]),
        )
        self.wait()

        graph_g_vertices = [1, 2, 3]
        graph_g_edges = [(1, 2), (2, 3), (1, 3)]
        graph_g = Graph(graph_g_vertices, graph_g_edges)

        graph_g_title = Tex("This is G")
        graph_g_title.scale(1.5)

        graph_h_vertices = [1, 2]
        graph_h_edges = [(1, 2)]
        graph_h = Graph(graph_h_vertices, graph_h_edges)
        graph_h.next_to(graph_g, RIGHT)

        graph_h_title = Tex("This is H")
        graph_h_title.scale(1.5)

        VGroup(graph_g, graph_h).arrange(RIGHT)

        graph_g_title.next_to(graph_g, DOWN)
        graph_h_title.next_to(graph_h, DOWN)

        # Graph G
        self.add(graph_g)
        self.play(Create(graph_g))

        self.add(graph_g_title)
        self.play(FadeInFrom(graph_g_title, direction=UP))
        self.wait()

        # Graph H
        self.add(graph_h)
        self.play(Create(graph_h))

        self.add(graph_h_title)
        self.play(FadeInFrom(graph_h_title, direction=UP))
        self.wait()
