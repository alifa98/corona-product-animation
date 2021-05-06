from manim import *


class CoronaProduct(Scene):
    def construct(self):

        frame_width = config["frame_width"]
        frame_height = config["frame_height"]

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

        graph_g_title = Tex("G")
        graph_g_title.scale(1.5)

        graph_h_vertices = [1, 2]
        graph_h_edges = [(1, 2)]
        graph_h = Graph(graph_h_vertices, graph_h_edges)
        graph_h.next_to(graph_g, RIGHT)

        graph_h_title = Tex("H")
        graph_h_title.scale(1.5)

        graphs_group = VGroup(VGroup(graph_g, graph_g_title).arrange(DOWN), VGroup(graph_h, graph_h_title).arrange(DOWN)).arrange(RIGHT)

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

        self.play(graphs_group.animate.scale(.5))
        self.play(graphs_group.animate.shift(((frame_width / 2) - (graphs_group.width / 2)) * LEFT))
        self.wait()

        # point to to of graph G
        arrow_to_graph_g = CurvedArrow(graph_g.get_center() + graph_g.width * RIGHT + 2 * UP, graph_g.get_center() + graph_g.width/2*RIGHT + graph_g.height/2*UP, radius=-8)
        self.add(arrow_to_graph_g)
        self.play(Create(arrow_to_graph_g))

        arrow_to_graph_g_text = Tex("Has 3 Vertices").scale(0.7).next_to(arrow_to_graph_g, RIGHT + UP)
        self.add(arrow_to_graph_g_text)
        self.play(Write(arrow_to_graph_g_text))
        self.wait()

        arrow_to_graph_g_text_transformed = Tex("So We Copy the Graph H, 3 times", color=BLUE).scale(0.7).next_to(arrow_to_graph_g, RIGHT + UP)
        self.play(Transform(arrow_to_graph_g_text, arrow_to_graph_g_text_transformed))
        self.wait()
