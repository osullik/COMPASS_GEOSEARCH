from manim import *

class ArrangeTextObjects(Scene):
    def construct(self):
        # Define the text labels, colors, and coordinates
        labels = ["X", "A", "B", "B", "B", "C", "C", "D", "D"]
        colors = [WHITE, RED, BLUE, BLUE, BLUE, GREEN, GREEN, YELLOW, YELLOW]
        coordinates = [ (-0.5, 0, 0),#X 
                        (4, -3, 0), #A -SE
                        (-3, 3, 0), #B -NW  
                        (3, 2, 0),  #B -NE
                        (2, -2, 0), #B -SE
                        (-2, -2, 0),#C -SW
                        (1, 1, 0),  #C -NE
                        (-1, -1, 0),#D -SW
                        (2, 3, 0)]  #D -NE

        # Create a list to store Text objects
        text_objects = []

        for label, color, coord in zip(labels, colors, coordinates):
            text = Text(label, color=color, font='Courier New').move_to(coord)
            text_objects.append(text)

        # Add the Text objects to the scene
        self.play(*[Write(text) for text in text_objects])

        self.wait(2)

        # Create Dashed Lines from X
        right_line = DashedVMobject(Line((0,0,0), (10,0,0)), num_dashes=20)
        left_line = DashedVMobject(Line((-1,0,0), (-10,0,0)), num_dashes=20)
        up_line = DashedVMobject(Line((-0.5,0.5,0), (-0.5,10,0)), num_dashes=20)
        down_line = DashedVMobject(Line((-0.5,-0.5,0), (-0.5,-10,0)), num_dashes=20)

        #vertical_line.shift(coordinates[0][0])
        #horizontal_line.shift(coordinates[0][1])

        self.play(Create(up_line), Create(down_line), Create(left_line), Create(right_line))




        #Move the letters to lists: 

        quad_labels = ["NW:", "NE:", "SW:", "SE:"]
        quad_coords = [(4,3,0), (4,2.5,0), (4,2,0), (4,1.5,0)]
        quad_objects = []

        for lbl, crd in zip(quad_labels,quad_coords):
            text = Text(lbl,color=WHITE, font='Courier New').move_to(crd)
            quad_objects.append(text)

        origin = []
        NW = []
        NE = []
        SW = []
        SE = []
        origin = [text_objects[0]]
        NW = [text_objects[2]]
        NE = [text_objects[3], text_objects[6], text_objects[8]]
        SW = [text_objects[5], text_objects[7]]
        SE = [text_objects[1],text_objects[4]]

        O_tgt = [(0,0,0)]
        NW_tgt = [(5,3,0)]
        NE_tgt = [(5,2.5,0),(5.5,2.5,0),(6,2.5,0)]
        SW_tgt = [(5,2,0),(5.5,2,0)]
        SE_tgt = [(5,1.5,0),(5.5,1.5,0)]

        self.add(*[quad for quad in quad_objects])        

        #for o_txt, o_tgt in zip (origin,O_tgt):
        #    self.play(o_txt.animate.move_to(o_tgt))
        for nw_txt, nw_tgt in zip (NW,NW_tgt):
            self.play(nw_txt.animate.move_to(nw_tgt))
        for ne_txt, ne_tgt in zip (NE,NE_tgt):
            self.play(ne_txt.animate.move_to(ne_tgt))
        for sw_txt, sw_tgt in zip (SW,SW_tgt):
            self.play(sw_txt.animate.move_to(sw_tgt))
        for se_txt, se_tgt in zip (SE,SE_tgt):
            self.play(se_txt.animate.move_to(se_tgt))

        # self.play(*[text.animate.move_to(O_tgt) for text in origin],
        #           *[text.animate.move_to(NW_tgt) for text in NW],
        #           *[text.animate.move_to(NE_tgt) for text in NE],
        #           *[text.animate.move_to(SW_tgt) for text in SW],
        #           *[text.animate.move_to(SE_tgt) for text in SE]
        #           )

        self.wait(2)
