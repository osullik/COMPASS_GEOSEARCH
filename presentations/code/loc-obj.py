from manim import *

class LocationObjectSearch(MovingCameraScene):
    def construct(self):
        #self.camera.background_color = WHITE
        self.camera.frame.save_state()

        self.play(self.camera.frame.animate.scale(1.5))

        title = Text("LOCATION-OBJECT SEARCH", color=WHITE, font="Courier New", stroke_width=3).move_to((0,5,0))
        self.add(title)

        ##########
        #Here we have a location, Location "X"
        ##########

        loc_x = Text("X", color=WHITE, font="Courier New", stroke_width=3).move_to((-0.5,0,0))

        self.play(Write(loc_x))
        self.wait(2)

        ##########
        #Assocated with Location X are objects, A-D. There can be multiple objects of same class.
        ##########

        # Define the text labels, colors, and coordinates
        labels = ["A", "B", "B", "B", "C", "C", "D", "D"]
        colors = [RED, BLUE, BLUE, BLUE, GREEN, GREEN, YELLOW, YELLOW]
        coordinates = [ (4, -3, 0), #A -SE
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
        self.wait(1)

        ##########
        # We index them by assuming that they are all relative to the location, 
        # and that queries will reflect that assumption. We assume alignment
        # with a global coordinate system
        ##########

        # Create Dashed Lines from X & group them into single object
        right_line = DashedVMobject(Line((0,0,0), (4.5,0,0)), num_dashes=20)
        left_line = DashedVMobject(Line((-1,0,0), (-5,0,0)), num_dashes=20)
        up_line = DashedVMobject(Line((-0.5,0.5,0), (-0.5,4.5,0)), num_dashes=20)
        down_line = DashedVMobject(Line((-0.5,-0.5,0), (-0.5,-4.5,0)), num_dashes=20)
        gridGroup = Group(loc_x, right_line, left_line, up_line, down_line)

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
        NW = [text_objects[1]]
        NE = [text_objects[2], text_objects[5], text_objects[7]]
        SW = [text_objects[4], text_objects[6]]
        SE = [text_objects[0],text_objects[3]]

        O_tgt = [(0,0,0)]
        NW_tgt = [(5,3,0)]
        NE_tgt = [(5,2.5,0),(5.5,2.5,0),(6,2.5,0)]
        SW_tgt = [(5,2,0),(5.5,2,0)]
        SE_tgt = [(5,1.5,0),(5.5,1.5,0)]  

        #Animate creation of the lists

        loc_name = Text("LOC X", color=WHITE, font='Courier New', stroke_width=3).move_to((4.75,3.5,0))
        self.add(loc_name)
        self.add(*[quad for quad in quad_objects])      

        #Animate the move to the lists
        for nw_txt, nw_tgt in zip (NW,NW_tgt):
            self.play(nw_txt.animate.move_to(nw_tgt))
        for ne_txt, ne_tgt in zip (NE,NE_tgt):
            self.play(ne_txt.animate.move_to(ne_tgt))
        for sw_txt, sw_tgt in zip (SW,SW_tgt):
            self.play(sw_txt.animate.move_to(sw_tgt))
        for se_txt, se_tgt in zip (SE,SE_tgt):
            self.play(se_txt.animate.move_to(se_tgt))

        self.wait(1)

        #Combine the lists into a box and add a border
        list_group = Group(  loc_name,
                            quad_objects[0],
                            quad_objects[1],
                            quad_objects[2],
                            quad_objects[3], 
                            NW[0], 
                            NE[0],NE[1], NE[2], 
                            SW[0], SW[1], 
                            SE[0], SE[1])

        box_border = SurroundingRectangle(list_group, corner_radius=0.25, color=WHITE)

        box_group = Group(list_group,box_border)

        ##########
        # There could be many of these locations with their associated objects in the database.
        ##########

        #Zoom out while drawing that border and moving the box
        self.play(box_border.animate, 
                  box_group.animate.move_to((8,6,0)), 
                  title.animate.scale(2).move_to((8,10,0)),
                  self.camera.frame.animate.scale(2.0).move_to((8,0,0)))


        ##########
        # We encode queries in the same manner
        ##########


        #Place a Q at the centre of the new query

        query_q = Text("Q", color=WHITE, font="Courier New", stroke_width=3).move_to((16,0,0))
        q_right_line = DashedVMobject(Line((16.5,0,0), (21,0,0),color=WHITE), num_dashes=20)
        q_left_line = DashedVMobject(Line((15.5,0,0), (11,0,0),color=WHITE), num_dashes=20)
        q_up_line = DashedVMobject(Line((16,0.5,0), (16,4.5,0),color=WHITE), num_dashes=20)
        q_down_line = DashedVMobject(Line((16,-0.5,0), (16,-4.5,0),color=WHITE), num_dashes=20)

        self.play(query_q.animate)
        self.play(Create(q_up_line), Create(q_down_line), Create(q_left_line), Create(q_right_line))
        
        q_gridGroup = Group(query_q, q_right_line, q_left_line, q_up_line, q_down_line)


        #Add query terms

        q_E = Text("E", color=PURPLE, font="Courier New").move_to((13,2.5,0))
        q_D1 = Text("D", color=YELLOW, font="Courier New").move_to((18,2.5,0))
        q_C = Text("C", color=GREEN, font="Courier New").move_to((13,-2.5,0))
        q_D2 = Text("D", color=YELLOW, font="Courier New").move_to((14,-2.5,0))
        q_B = Text("B", color=BLUE, font="Courier New").move_to((18,-2.5,0))

        query_objects = [q_E, q_D1, q_C, q_D2, q_B]

        self.play(*[Write(query) for query in query_objects])


        #Move to Query Box:

        query_name = Text("QUERY Q", color=WHITE, font='Courier New', stroke_width=3).move_to((8,-5,0))
        self.add(query_name)

        q_quad_labels = ["NW:", "NE:", "SW:", "SE:"]
        q_quad_coords = [(7,-5.5,0), (7,-6,0), (7,-6.5,0), (7,-7,0)]
        q_quad_objects = []

        for lbl, crd in zip(q_quad_labels,q_quad_coords):
            text = Text(lbl,color=WHITE, font='Courier New').move_to(crd)
            q_quad_objects.append(text)

        self.add(*[q_quad for q_quad in q_quad_objects])      

        q_list_group = Group(query_name, 
                             q_quad_objects[0],
                             q_quad_objects[1],
                             q_quad_objects[2],
                             q_quad_objects[3])

        q_box_border = SurroundingRectangle(q_list_group, corner_radius=0.25, color=WHITE)
        
        self.play(q_box_border.animate)
                  
        

        q_tgts = [(8,-5.5,0),(8,-6,0),(8,-6.5,0),(8.5,-6.5,0),(7.95,-7,0)]  

        for txt, tgt in zip (query_objects,q_tgts):
            self.play(txt.animate.move_to(tgt))

        q_box_group = Group(q_list_group,q_box_border, q_E, q_D1, q_C, q_D2, q_B)
        

        #Remove the grids and zoom in
        self.remove(gridGroup, q_gridGroup)
        self.play(self.camera.frame.animate.scale(0.4).move_to((8,0,0)),
                  title.animate.scale(0.4).move_to((8,4,0)),
                  gridGroup.animate.scale(0).move_to((-50,0,0)),
                  q_gridGroup.animate.scale(0).move_to((50,0,0)),
                  box_group.animate.move_to(((4,2,0))),
                  q_box_group.animate.move_to(((4,-2,0))))#, right_line.animate.move_to((-10,0,0)), q_left_line.animate.move_to((20,0,0)))
        
        ##########
        # Search is a simple string comparison between the data structures. 
        # We return the number of matches and use that to rank the returned
        # list of candidate locations.
        ##########        

        #Search:

        q_rect = SurroundingRectangle(q_E, color=RED)
        a_rect= SurroundingRectangle(text_objects[1])

        counting_text = Text("Match Count:", color=WHITE, font="Courier New").move_to((9,0,0))
        counter=0
        count = Integer(counter, color=WHITE).move_to((12,0,0))

        self.play(q_rect.animate, a_rect.animate, Write(counting_text), count.animate)
        #Search NW
        self.play(q_rect.animate.move_to(q_D1), a_rect.animate.move_to(text_objects[2]))
        #Search NE
        self.play(a_rect.animate.move_to(text_objects[5]))
        counter+=1
        self.play(a_rect.animate.move_to(text_objects[7]), Transform(count, Integer(counter,color=WHITE).move_to((12,0,0))))
        #Search SW
        counter+=1
        self.play(q_rect.animate.move_to(q_C), a_rect.animate.move_to(text_objects[4]),Transform(count, Integer(counter,color=WHITE).move_to((12,0,0))))
        self.play(a_rect.animate.move_to(text_objects[6]))
        self.play(q_rect.animate.move_to(q_D2),a_rect.animate.move_to(text_objects[4]))
        counter+=1
        self.play(a_rect.animate.move_to(text_objects[6]),Transform(count, Integer(counter,color=WHITE).move_to((12,0,0))))
        #Search SE
        self.play(q_rect.animate.move_to(q_B),a_rect.animate.move_to(text_objects[0]) )
        counter+=1
        self.play(a_rect.animate.move_to(text_objects[3]),Transform(count, Integer(counter,color=WHITE).move_to((12,0,0))))

        return_txt = Text("Return:(Location_X,{count})".format(count=counter),font="Courier New").move_to((10, -2, 0))

        return_box = SurroundingRectangle(return_txt, corner_radius=0.25)

        self.play(Write(return_txt))
        self.play(Create(return_box))

