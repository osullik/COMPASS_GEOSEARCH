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

        #C to 1,3
        tup_4 = (NS_objects[3], WE_objects[1])
        tgt_4 = (((s_x+1,s_y-3,0)))

        #D to 2,4
        tup_5 = (NS_objects[4], WE_objects[2])
        tgt_5 = (((s_x+2,s_y-4,0)))

        #B to 4,5
        tup_6 = (NS_objects[5], WE_objects[4])
        tgt_6 = (((s_x+4,s_y-5,0)))

        #C to 3,6
        tup_7 = (NS_objects[6], WE_objects[3])
        tgt_7 = (((s_x+3,s_y-6,0)))

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


