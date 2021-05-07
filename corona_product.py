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
            LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in formulaTextTitle])
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

        # point to to of graph H
        arrow_to_graph_h = CurvedArrow(graph_h.get_center() + graph_h.width * RIGHT + 2 * UP, graph_h.get_center() + graph_h.width/2*RIGHT + graph_h.height/2*UP, radius=-8)
        arrow_to_graph_h_text = Tex("So We Copy the Graph H, 3 times", color=BLUE).scale(0.7).next_to(arrow_to_graph_h, RIGHT + UP)

        self.play(Transform(arrow_to_graph_g_text, arrow_to_graph_h_text),
                  Transform(arrow_to_graph_g, arrow_to_graph_h))
        self.wait(2)

        self.play(
            FadeOut(arrow_to_graph_g_text),
            Uncreate(arrow_to_graph_g)
        )

        self.wait()

        odotSymbol = MathTex(r" \odot ").scale(1.5).next_to(graph_g, RIGHT)

        self.add(odotSymbol)
        self.play(
            Create(odotSymbol),
            graph_h.animate.shift(RIGHT),
            graph_h_title.animate.shift(RIGHT)
        )

        equalSymbol = MathTex(r" = ").scale(1.5).next_to(graph_h, 2 * RIGHT)
        self.add(equalSymbol)
        self.play(
            Create(equalSymbol)
        )

        corona_product_graph_v = {1, 2, 3, 11, 12, 21, 22, 31, 32}

        corona_product_graph_e = [(1, 2), (2, 3), (1, 3), (11, 12), (21, 22), (31, 32)]
        corona_product_graph = Graph(
            corona_product_graph_v,
            corona_product_graph_e,
            layout={
                1: [1, 0, 0],
                2: [-1, 0, 0],
                3: [0, 1, 0],
                11: [2, 0, 0],
                12: [1, -1, 0],
                21: [-2, 0, 0],
                22: [-1, -1, 0],
                31: [1, 2, 0],
                32: [-1, 2, 0]
            }
        )
        corona_product_graph.move_to(2 * RIGHT)

        self.add(corona_product_graph)
        self.play(Create(corona_product_graph))
        self.wait()

        description = Text("then we connect\nall vertices of each copies\nto correspondig vertex in G").scale(0.5).next_to(corona_product_graph, UP)

        self.add(description)
        self.play(Write(description))

        self.play(corona_product_graph.animate.add_edges(
            *[
                (12, 1), (11, 1)
            ],
            edge_config={
                (12, 1): {"stroke_color": RED},
                (11, 1): {"stroke_color": RED}
            }
        ))

        self.wait()
        self.play(corona_product_graph.animate.add_edges(
            *[
                (21, 2), (22, 2)
            ],
            edge_config={
                (21, 2): {"stroke_color": RED},
                (22, 2): {"stroke_color": RED}
            }
        ))

        self.play(corona_product_graph.animate.add_edges(
            *[
                (31, 3), (32, 3)
            ],
            edge_config={
                (31, 3): {"stroke_color": RED},
                (32, 3): {"stroke_color": RED}
            }
        ))

        self.wait()
