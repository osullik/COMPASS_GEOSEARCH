from manim import *

class ObjectObjectSearch(MovingCameraScene):
    def construct(self):
        #self.camera.background_color = WHITE
        self.camera.frame.save_state()

        self.play(self.camera.frame.animate.scale(1.5))

        title = Text("OBJECT-OBJECT SEARCH", color=WHITE, font="Courier New", stroke_width=3).move_to((0,5,0))
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
                        (-2, -2.5   , 0),#C -SW
                        (1, 1, 0),  #C -NE
                        (-1, -1, 0),#D -SW
                        (2.5, 3.5, 0)]  #D -NE
        

        # Create a list to store Text objects
        text_objects = []

        for label, color, coord in zip(labels, colors, coordinates):
            text = Text(label, font='Courier New').move_to(coord)
            text.set_color(color)
            text_objects.append(text)

        # Add the Text objects to the scene
        self.play(*[Write(text) for text in text_objects])
        self.wait(1)

        north_lbl = Text("N to S:", font="Courier New", color=WHITE).move_to((7,4,0))
        west_lbl = Text("W to E:", font="Courier New", color=WHITE).move_to((7,3,0))

        self.play(self.camera.frame.animate.move_to((5,0,0)),
                  title.animate.move_to((5,5,0)),
                  north_lbl.animate,
                  west_lbl.animate)
        

        #Line

        # Create a yellow line at the top of the canvas
        NS_line = Line((-5,4.5,0), ((5,4.5,0)), color=YELLOW)
        self.play(Create(NS_line))

        north_to_south= sorted(text_objects, key=lambda m: m.get_center()[1], reverse=True)

        position = 1
        NS_objects = []
        for obj in north_to_south:
            y = obj.get_center()[1]
            temp = Text(text=obj.text, 
                            font=obj.font,
                            color=obj.get_color()).move_to(obj.get_center())
            NS_objects.append(temp)

            target = north_lbl.get_right()
            target[0] = target[0]+0.5*position

            self.play(NS_line.animate.move_to((0,y,5)),run_time=0.1)
            self.play(temp.animate.move_to(target))
            
            position += 1

        self.remove(NS_line)


                # Create a yellow line at the top of the canvas
        WE_line = Line((-4,-4.5,0), ((-4,4.5,0)), color=YELLOW)
        self.play(Create(WE_line))

        west_to_east= sorted(text_objects, key=lambda m: m.get_center()[0])

        position = 1
        WE_objects = []
        for obj in west_to_east:
            x = obj.get_center()[0]
            temp = Text(text=obj.text, 
                            font=obj.font,
                            color=obj.get_color()).move_to(obj.get_center())
            WE_objects.append(temp)

            target = west_lbl.get_right()
            target[0] = target[0]+0.5*position

            self.play(WE_line.animate.move_to((x,0,5)),run_time=0.1)
            self.play(temp.animate.move_to(target))
            
            position += 1
            
        self.remove(WE_line)


        
        label_group = Group(north_lbl, west_lbl, NS_objects[0], 
                                                NS_objects[1], 
                                                NS_objects[2],
                                                NS_objects[3], 
                                                NS_objects[4], 
                                                NS_objects[5], 
                                                NS_objects[6],
                                                NS_objects[7],
                                                WE_objects[0],
                                                WE_objects[1],
                                                WE_objects[2],
                                                WE_objects[3],
                                                WE_objects[4],
                                                WE_objects[5],
                                                WE_objects[6],
                                                WE_objects[7],  )

        numbers = [0,1,2,3,4,5,6,7]
        num_objects = []
        for num in numbers: 
            pos = (numbers.index(num))+1
            tgt = west_lbl.get_right()
            tgt[0] = tgt[0]+(0.5*pos)
            tgt[1] = tgt[1]+1
            text = Text(text=str(num), color=RED, font="Courier New").move_to(tgt)
            num_objects.append(text)

        self.play(label_group.animate.shift(DOWN*1),*[Write(num) for num in num_objects])

        lft = west_lbl.get_left()[0]
        rgt = lft+len(WE_objects)
        top = west_lbl.get_left()[1]-1
        bot = top-len(NS_objects)

        print(lft, rgt, top, bot)

        grid = NumberPlane(
            x_range=[0, 8, 1],
            y_range=[0, 8, 1],
            axis_config={"color": BLUE},
        ).shift(RIGHT*10,DOWN*4)

        border = Square(color=WHITE,side_length=8)
        border.set_fill(None)
        border.shift(RIGHT*10,DOWN*4)

        xNums = ([nx.copy() for nx in num_objects])
        yNums = ([ny.copy() for ny in num_objects])

        start_x = grid.get_left()[0]
        start_y = grid.get_top()[1]
        x = start_x +0.5

        position = 1
        for x_num in xNums:
            y = start_y+0.5
            x_num.move_to((x,y,0))
            x = x+1
            
            position+=1
        
        position=1
        y = start_y-0.5
        for y_num in yNums:
            x = start_x-0.5
            y_num.move_to((x,y,0))
            y = y-(1*position)
            

        self.play(Create(grid),
                  self.camera.frame.animate.scale(1.4),
                  title.animate.scale(1.4).move_to((5,7,0)),
                  Create(border))
        self.play(*[Write(num) for num in xNums], *[Write(num) for num in yNums])
        self.wait(1)


        # Build the Concept map

        s_x = grid.get_left()[0]+0.5
        s_y = grid.get_top()[1]-0.5  

        tup_list = []
        tgt_list = []

        #D to 5,0
        tup_1 = (NS_objects[0], WE_objects[5]) 
        tgt_1 = (((s_x+5,s_y,0)))

        #B to 0,1
        tup_2 = (NS_objects[1], WE_objects[0])
        tgt_2 = (((s_x,s_y-1,0)))

        #B to 6,2
        tup_3 = (NS_objects[2], WE_objects[6])
        tgt_3 = (((s_x+6,s_y-2,0)))

        #C to 3,3
        tup_4 = (NS_objects[3], WE_objects[3])
        tgt_4 = (((s_x+3,s_y-3,0)))

        #D to 2,4
        tup_5 = (NS_objects[4], WE_objects[2])
        tgt_5 = (((s_x+2,s_y-4,0)))

        #B to 4,5
        tup_6 = (NS_objects[5], WE_objects[4])
        tgt_6 = (((s_x+4,s_y-5,0)))

        #C to 1,6
        tup_7 = (NS_objects[6], WE_objects[1])
        tgt_7 = (((s_x+1,s_y-6,0)))

        #A to 7,7
        tup_8 = (NS_objects[7], WE_objects[7])
        tgt_8 = (((s_x+7,s_y-7,0)))

        tup_list =[tup_1, tup_2, tup_3, tup_4, tup_5, tup_6, tup_7, tup_8]
        tgt_list =[tgt_1, tgt_2, tgt_3, tgt_4, tgt_5, tgt_6, tgt_7, tgt_8]

        for tup,tgt in zip(tup_list, tgt_list):
            self.play(tup[0].animate.move_to(tgt), tup[1].animate.move_to(tgt),
                      north_lbl.animate)

        

        #Zoom In

        self.play(*[txt.animate.set_color(BLACK) for txt in text_objects],
                  north_lbl.animate.set_color(BLACK),
                  west_lbl.animate.set_color(BLACK),
                  loc_x.animate.set_color(BLACK),
                  self.camera.frame.animate.scale(0.7).move_to((s_x+8,s_y-3,0)),
                  title.animate.scale(0.7).move_to((s_x+8, s_y+2,0)))


        #Build Query

        query_label = Text(text="Query:", font="Courier New", stroke_width=3).move_to((s_x+9.6,s_y,0))
        q_C = Text(text="C",color=GREEN, font="Courier New").move_to((s_x+12,s_y-2,0))
        q_D = Text(text="D",color=YELLOW, font="Courier New").move_to((s_x+11,s_y-3,0))
        q_B = Text(text="B",color=BLUE, font="Courier New").move_to((s_x+12.5,s_y-3.5,0))
        q_A = Text(text="A",color=RED, font="Courier New").move_to((s_x+13.5,s_y-4.5,0))

        so = Text(text="Search Order:", color=WHITE, font="Courier New").move_to((s_x+11,s_y-6,0))

        q_list = [q_C,q_D,q_B,q_A]

        self.play(*[Create(q) for q in q_list], Write(query_label))


        q_line_ns = Line((s_x+10,s_y-1,0), ((s_x+15,s_y-1,0)), color=YELLOW)
        q_line_we = Line((s_x+10,s_y-1,0), ((s_x+10,s_y-5,0)), color=YELLOW)

        self.play(Write(so))
        self.play(Create(q_line_ns))
        self.play(q_line_ns.animate.move_to((q_line_ns.get_center()[0],q_C.get_center()[1]-0.25,0)),run_time=0.2)
        self.play(q_C.animate.move_to((so.get_right()[0]+0.5,so.get_right()[1],0)))
    

        self.play(Create(q_line_we), q_line_ns.animate.set_color(BLACK))
        self.play(q_line_we.animate.move_to((q_D.get_center()[0]+0.25,q_line_we.get_center()[1],0)),run_time=0.2)
        self.play(q_D.animate.move_to((so.get_right()[0]+1,so.get_right()[1],0)))
        
        self.play(q_line_we.animate.set_color(BLACK),
                  q_line_ns.animate.set_color(YELLOW))
        
        self.play(q_line_ns.animate.move_to((q_line_ns.get_center()[0],q_B.get_center()[1]-0.25,0)),run_time=0.2)
        self.play(q_B.animate.move_to((so.get_right()[0]+1.5,so.get_right()[1],0)))
        
        self.play(q_line_ns.animate.set_color(BLACK),
                  q_line_we.animate.set_color(YELLOW))

        self.play(q_line_we.animate.move_to((q_A.get_center()[0]+0.25,q_line_we.get_center()[1],0)),run_time=0.2)
        self.play(q_A.animate.move_to((so.get_right()[0]+2,so.get_right()[1],0)), q_line_we.animate.set_color(BLACK))

        q_group = Group(so,q_C,q_D,q_B,q_A)

        self.play(q_group.animate.shift(UP*5))

        #Search

        q_rect = SurroundingRectangle(q_C, color=RED)
        ns_rect = Rectangle(height=0,width=8,color=GRAY).move_to((grid.get_top()[0], grid.get_top()[1], 0))
        found_C = SurroundingRectangle(NS_objects[3],color=YELLOW)
        found_D = SurroundingRectangle(NS_objects[4],color=YELLOW)
        found_B = SurroundingRectangle(NS_objects[5],color=YELLOW)
        found_A = SurroundingRectangle(NS_objects[7],color=YELLOW)

        self.play(Create(q_rect),Create(ns_rect))        
        self.play(Transform(ns_rect, Rectangle(height=1,width=8,fill_color=GRAY,fill_opacity=0.5).move_to((grid.get_top()[0], grid.get_top()[1]-0.5, 0))))
        self.play(Transform(ns_rect, Rectangle(height=2,width=8,fill_color=GRAY,fill_opacity=0.5).shift(DOWN*1,RIGHT*10)))
        self.play(Transform(ns_rect, Rectangle(height=3,width=8,fill_color=GRAY,fill_opacity=0.5).shift(DOWN*1.5,RIGHT*10)))
        self.play(Transform(ns_rect, Rectangle(height=4,width=8,fill_color=GRAY,fill_opacity=0.5).shift(DOWN*2,RIGHT*10)),
                  Create(found_C))
        
        we_rect = Rectangle(height=4,width=0,color=GRAY,fill_color=GRAY,fill_opacity=0.4).move_to((grid.get_left()[0], grid.get_left()[1]-2, 0))
        
        self.play(Create(we_rect))
        self.play(q_rect.animate.move_to(q_D), Transform(we_rect, Rectangle(height=4, width=1, fill_color=DARK_GRAY, fill_opacity=0.5).shift(DOWN*6,RIGHT*6.5)))
        self.play(Transform(we_rect, Rectangle(height=4, width=2, fill_color=DARK_GRAY, fill_opacity=0.5).shift(DOWN*6,RIGHT*7)))
        self.play(Transform(we_rect, Rectangle(height=4, width=3, fill_color=DARK_GRAY, fill_opacity=0.5).shift(DOWN*6,RIGHT*7.5)),Create(found_D))


        ns_rect_2 = Rectangle(height=1,width=5,fill_color=DARKER_GRAY,fill_opacity=0.5).move_to((grid.get_top()[0]+1.5, grid.get_top()[1]-4.5, 0))
        self.play(Create(ns_rect_2), q_rect.animate.move_to(q_B))
        self.play(Transform(ns_rect_2, Rectangle(height=2,width=5,fill_color=DARKER_GRAY,fill_opacity=0.5).shift(DOWN*5,RIGHT*11.5)),Create(found_B))

        ss_x = s_x+3
        ss_y = s_y-6

        search_rect= Rectangle(height=1,width=1,color=RED).move_to((ss_x,ss_y,0))

        self.play(Create(search_rect), q_rect.animate.move_to(q_A))

        to_check = [((ss_x+1,ss_y,0)),((ss_x+2,ss_y,0)),((ss_x+3,ss_y,0)),((ss_x+4,ss_y,0)),
                    ((ss_x,ss_y-1,0)),((ss_x+1,ss_y-1,0)), ((ss_x+2,ss_y-1,0)), ((ss_x+3,ss_y-1,0)), ((ss_x+4,ss_y-1,0))]
        
        for coord in to_check:
            self.play(search_rect.animate.move_to(coord), run_time=0.1)

        self.play(Create(found_A))

        return_txt = Text("Return:(Location_X,TRUE)",font="Courier New").move_to((ss_x+10, ss_y+2, 0))

        return_box = SurroundingRectangle(return_txt, corner_radius=0.25)

        self.play(Write(return_txt))
        self.play(Create(return_box))


