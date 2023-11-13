import sys, os

sys.path.append("../../../GESTALT/code/compass/")

from manim import *
from compass import Point as cPoint, Compass


class CardinalityInvariant(MovingCameraScene):

    def construct(self):
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(2.0).move_to((5,5,0)))
        self.Compass = Compass()

        title = Text("CARDINALITY INVARIANCE", color=WHITE, font="Courier New", stroke_width=3).move_to((5,11,0))
        self.add(title)

        pt_CENTROID = Text(text="+",color=WHITE,font="Courier New").move_to((5,5,0))
        CENTROID = cPoint(name="centroid",x_coord=pt_CENTROID.get_center()[0], y_coord=pt_CENTROID.get_center()[1])

        pt_NN = Text(text="north",color=WHITE,font="Courier New").move_to((pt_CENTROID.get_x(), pt_CENTROID.get_y()+5,0))
        NN = cPoint(name="north",x_coord=pt_NN.get_center()[0], y_coord=pt_NN.get_center()[1])
        pt_WW = Text(text="north",color=WHITE,font="Courier New").move_to((pt_CENTROID.get_x()-5, pt_CENTROID.get_y(),0))
        WW = cPoint(name="west",x_coord=pt_WW.get_center()[0], y_coord=pt_WW.get_center()[1])
        pt_NW = Text(text="northwest",color=WHITE,font="Courier New").move_to((pt_CENTROID.get_x()-5, pt_CENTROID.get_y()+5,0))
        NW = cPoint(name="northwest",x_coord=pt_NW.get_center()[0], y_coord=pt_NW.get_center()[1])


        #Prepare Canvas
        grid =NumberPlane(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"color": BLUE}).move_to(pt_CENTROID)
        border = Square(color=WHITE,side_length=10,fill_color=None).move_to(pt_CENTROID)
        self.play(Create(grid),Create(border))

        #Insert Points
        pt_A = Text(text="A",font="Courier New",color=WHITE).move_to((3,3,0))
        A = cPoint(name=pt_A.animate.get_text(),x_coord=pt_A.get_center()[0], y_coord=pt_A.get_center()[1])
        pt_B = Text(text="B",font="Courier New",color=WHITE).move_to((6,9,0))
        B = cPoint(name=pt_B.animate.get_text(),x_coord=pt_B.get_center()[0], y_coord=pt_B.get_center()[1])
        pt_C = Text(text="C",font="Courier New",color=WHITE).move_to((7,8,0))
        C = cPoint(name=pt_C.animate.get_text(),x_coord=pt_C.get_center()[0], y_coord=pt_C.get_center()[1])
        self.play(Write(pt_A),Write(pt_B), Write(pt_C))

        points = [A,B,C]

        #Create Reference Lines
        line_NORTH = Line(pt_CENTROID.get_center(),(pt_CENTROID.get_x()+0,pt_CENTROID.get_y()+5,0))  
        line_WEST = Line(pt_CENTROID.get_center(),(pt_CENTROID.get_x()-5,pt_CENTROID.get_y()+0,0))
        line_NORWEST = Line(pt_CENTROID.get_center(),(pt_CENTROID.get_x()-5,pt_CENTROID.get_y()+5,0))
        self.play(Create(line_NORTH), Create(line_WEST), Create(line_NORWEST))

        #GET Angles

        print(NN.dumpTuple(), WW.dumpTuple(), NW.dumpTuple(), CENTROID.dumpTuple())

        all_north_angles = self.Compass.getAllAngles(reference=NN,centroid=CENTROID,points=points)
        all_north_angles.sort()
        subtractive_north_angles = [all_north_angles[0], all_north_angles[1]-all_north_angles[0], all_north_angles[2]-all_north_angles[1] ]
            
        all_west_angles = self.Compass.getAllAngles(reference=WW,centroid=CENTROID,points=points)
        all_west_angles.sort()
        subtractive_west_angles = [all_west_angles[0], all_west_angles[1]-all_west_angles[0], all_west_angles[2]-all_west_angles[1] ]
        
        all_northwest_angles= self.Compass.getAllAngles(reference=NW,centroid=CENTROID,points=points)
        all_northwest_angles.sort()
        subtractive_northwest_angles = [all_northwest_angles[0], all_northwest_angles[1]-all_northwest_angles[0], all_northwest_angles[2]-all_northwest_angles[1] ]


        # Animate Get Angles

        angle_line = Line(pt_CENTROID,((5,10,0)), color=YELLOW)
        self.play(Create(angle_line))
        all_angles_objs = []
        all_angles = []

        angle_lbl = Text(text="Angle:", font="Courier New", color=WHITE).scale(2).move_to((12.5,10,0))
        n_angle_lbl = Text(text="From N :", font="Courier New", color=WHITE).move_to((12,6,0))
        w_angle_lbl = Text(text="From W :", font="Courier New", color=WHITE).move_to((12,5,0))
        nw_angle_lbl = Text(text="From NW:", font="Courier New", color=WHITE).move_to((12,4,0))

        self.play(Write(angle_lbl), Write(n_angle_lbl), Write(w_angle_lbl), Write(nw_angle_lbl))

        
        pos = 1
        for i in range(len(subtractive_north_angles)):
            temp= Text(text=str(round(all_north_angles[i])),font="Courier New", color=WHITE).scale(2).move_to((16,10,0))
            self.play(Rotate(angle_line,angle=(-1*subtractive_north_angles[i])*DEGREES, about_point=pt_CENTROID.get_center()),
                      Write(temp),
                      line_NORTH.animate.set_color(YELLOW))
            if all_north_angles[i]>100:
                self.play(temp.animate.scale(0.5).move_to((13+(1*pos)+0.25,6,0)))
                pos+=1.5
            else:
                self.play(temp.animate.scale(0.5).move_to((13+(1*pos),6,0)))
                pos+=1
            all_angles_objs.append(temp)
            all_angles.append(all_north_angles[i])
            

        self.play(Transform(angle_line, Line(pt_CENTROID,((0,5,0)), color=YELLOW)))
        pos = 1
        for i in range(len(subtractive_west_angles)):
            temp= Text(text=str(round(all_west_angles[i])),font="Courier New", color=WHITE).scale(2).move_to((16,10,0))
            self.play(Rotate(angle_line,angle=(-1*subtractive_west_angles[i])*DEGREES, about_point=pt_CENTROID.get_center()),
                      Write(temp),
                      line_NORTH.animate.set_color(WHITE),
                      line_WEST.animate.set_color(YELLOW))
            if all_west_angles[i]>100:
                self.play(temp.animate.scale(0.5).move_to((13+(1*pos)+0.25,5,0)))
                pos+=1.5
            else:
                self.play(temp.animate.scale(0.5).move_to((13+(1*pos),5,0)))
                pos+=1
            all_angles_objs.append(temp)
            all_angles.append(all_west_angles[i])

        self.play(Transform(angle_line, Line(pt_CENTROID,((1.5,8.5,0)), color=YELLOW)))
        pos = 1
        for i in range(len(subtractive_northwest_angles)):
            temp= Text(text=str(round(all_northwest_angles[i])),font="Courier New", color=WHITE).scale(2).move_to((16,10,0))
            self.play(Rotate(angle_line,angle=(-1*subtractive_northwest_angles[i])*DEGREES, about_point=pt_CENTROID.get_center()),
                      Write(temp),
                      line_WEST.animate.set_color(WHITE),
                      line_NORWEST.animate.set_color(YELLOW))
            if all_northwest_angles[i]>100:
                self.play(temp.animate.scale(0.5).move_to((13+(1*pos)+0.25,4,0)))
                pos+=1.5
            else:
                self.play(temp.animate.scale(0.5).move_to((13+(1*pos),4,0)))
                pos+=1
            all_angles_objs.append(temp)
            all_angles.append(all_northwest_angles[i])

        self.play(line_NORWEST.animate.set_color(WHITE))

        all_angles.append(360) #Back to original positions
        all_angles_objs.append(Text(text=str(360),font="Courier New", color=WHITE).move_to((14,3.5,0)))

        self.play(angle_lbl.animate.set_color(BLACK), Transform(angle_line, Line(pt_CENTROID,((5,10,0)), color=WHITE)))

        lbl_all_angles_objs = Text(text="Order:", color=WHITE, font="Courier New",stroke_width=3.0).move_to((12,10,0))

        targets = [((12.5,9,0)),
                   ((12.5,8.5,0)),
                   ((12.5,8,0)),
                   ((12.5,7.5,0)),
                   ((12.5,7,0)),
                   ((12.5,6.5,0)),
                   ((12.5,6,0)),
                   ((12.5,5.5,0)),
                   ((12.5,5,0)),
                   ((12.5,4.5,0))
                   ]  
        
        sorted_all_angles_objs = [all_angles_objs[0],
                             all_angles_objs[1],
                             all_angles_objs[6],
                             all_angles_objs[7],
                             all_angles_objs[3],
                             all_angles_objs[4],
                             all_angles_objs[2],
                             all_angles_objs[8],
                             all_angles_objs[5],
                             all_angles_objs[9]]

             

        self.play(n_angle_lbl.animate.set_color(BLACK),
                  w_angle_lbl.animate.set_color(BLACK),
                  nw_angle_lbl.animate.set_color(BLACK),
                  Write(lbl_all_angles_objs))
        
        for obj, tgt in zip(sorted_all_angles_objs, targets):
            self.play(obj.animate.move_to(tgt),run_time=0.3)


        sorted_subtractive_angles = []

        all_angles.sort()

        for i in range(len(all_angles)):
            if i == 0:
                sorted_subtractive_angles.append(all_angles[i])
            else:
                sorted_subtractive_angles.append(all_angles[i]-all_angles[i-1])

        all_sets = [Text(" {A:(2.5,3.5),B:(5.0,9.0),C:(6.0,8.0)}",color=WHITE,font="Courier New"),
                    Text(" {A:(4.5,2.0),B:(3.5,9.0),C:(5.0,8.5)}",color=WHITE,font="Courier New"),
                    Text(" {A:(6.0,2.0),B:(2.8,8.0),C:(3.5,8.5)}",color=WHITE,font="Courier New"),
                    Text(" {A:(6.5,3.0),B:(1.0,7.0),C:(2.5,7.5)}",color=WHITE,font="Courier New"),
                    Text("{A:(7.5,3.5),B:(1.0,5.0),C:(1.5,6.0)}",color=WHITE,font="Courier New"),
                    Text("{A:(8.0,4.5),B:(1.0,3.5),C:(1.5,5.0)}",color=WHITE,font="Courier New"),
                    Text("{A:(5.0,8.0),B:(7.0,1.5),C:(6.0,1.5)}",color=WHITE,font="Courier New"),
                    Text("{A:(3.0,7.0),B:(9.0,4.0),C:(8.0,3.0)}",color=WHITE,font="Courier New"),
                    Text("{A:(2.0,5.0),B:(8.5,7.0),C:(8.5,6.0)}",color=WHITE,font="Courier New"),
                    Text("{A:(3.0,3.0),B:(6.0,9.0),C:(7.0,8.0)}",color=WHITE,font="Courier New")]


        self.play(self.camera.frame.animate.move_to((12,5,0)), title.animate.move_to((12,11,0)))


        query = 0
        q_box = SurroundingRectangle(sorted_all_angles_objs[0])
        for angle,s in zip(sorted_subtractive_angles,all_sets):
            
            self.play(Rotate(pt_A,angle=angle*DEGREES,about_point=pt_CENTROID.get_center()),
                      Rotate(pt_B,angle=angle*DEGREES,about_point=pt_CENTROID.get_center()),
                      Rotate(pt_C,angle=angle*DEGREES,about_point=pt_CENTROID.get_center()),
                      Transform(q_box, SurroundingRectangle(sorted_all_angles_objs[query])))
            self.play(
                      Rotate(pt_A,angle=-1*angle*DEGREES, about_point=pt_A.get_center()),
                      Rotate(pt_B,angle=-1*angle*DEGREES, about_point=pt_B.get_center()),
                      Rotate(pt_C,angle=-1*angle*DEGREES, about_point=pt_C.get_center()),
                      run_time=0.1)
            
            temp = s.scale(0.75).next_to(sorted_all_angles_objs[query],RIGHT,buff=0.5)
            self.play(Write(temp),run_time=0.3)
            query +=1
            
        
        #Unique (14-BA, 34-BB, 59-CB, 124, 225)

        self.play(sorted_all_angles_objs[3].animate.set_color(BLACK).shift(RIGHT*50),
                  all_sets[3].animate.set_color(BLACK).shift(RIGHT*50),
                  sorted_all_angles_objs[4].animate.set_color(BLACK).shift(RIGHT*50),
                  all_sets[4].animate.set_color(BLACK).shift(RIGHT*50),
                  sorted_all_angles_objs[8].animate.set_color(BLACK).shift(RIGHT*50),
                  all_sets[8].animate.set_color(BLACK).shift(RIGHT*50),
                  sorted_all_angles_objs[9].animate.set_color(BLACK).shift(RIGHT*50),
                  all_sets[9].animate.set_color(BLACK).shift(RIGHT*50),
                  sorted_all_angles_objs[5].animate.shift(UP*1),
                  all_sets[5].animate.shift(UP*1),
                  sorted_all_angles_objs[6].animate.shift(UP*1),
                  all_sets[6].animate.shift(UP*1),
                  sorted_all_angles_objs[7].animate.shift(UP*1),
                  all_sets[7].animate.shift(UP*1),
                  q_box.animate.set_color(BLACK)
                  )

        #Return 

        return_text = Text("Return:(Query Q, 6 Rotations)",font="Courier New").move_to((18, 5, 0))
        return_box = SurroundingRectangle(return_text,corner_radius=0.25)

        self.play(Write(return_text), Create(return_box))



            
         





    



        






















    # def construct(self):
    #     ONE_ROTATION = 360
    #     self.camera.frame.save_state()
        
    #     self.play(self.camera.frame.animate.scale(1.5).move_to((5,5,0)))

    #     rotation_center = ((5,5,0))

    #     rotation_tracker = ValueTracker(180)
    #     line_NORTH = Line(((5,5,0)),(5,10,0))
        
    #     line_WEST = Line(((5,5,0)),(0,5,0))
    #     line_NORWEST = Line(((5,5,0)),(0,10,0))

    #     line_A = Line(((5,5,0)), ((0,0,0)))
    #     line_B = Line(((5,5,0)), ((8,10,0)))
    #     line_C = Line(((5,5,0)), ((10,7,0)))
    #     line_ref_A = line_A.copy()
    #     line_ref_B = line_B.copy()
    #     line_ref_C = line_C.copy()
    #     line_A.rotate(
    #         (rotation_tracker.get_value() * DEGREES)%ONE_ROTATION, about_point=rotation_center
    #     )
    #     line_B.rotate(
    #         (rotation_tracker.get_value() * DEGREES)%ONE_ROTATION, about_point=rotation_center
    #     )
    #     line_C.rotate(
    #         (rotation_tracker.get_value() * DEGREES)%ONE_ROTATION, about_point=rotation_center
    #     )

    #     a = Angle(line_A,line_NORTH, radius=5, other_angle=False)
    #     b = Angle( line_B,line_NORTH, radius=4, other_angle=False)
    #     c = Angle( line_C,line_NORTH, radius=2, other_angle=False)

    #     text_A = Text("A", color=WHITE).move_to(
    #         Angle(
    #              line_A,line_NORTH, radius=5 + 3*SMALL_BUFF, other_angle=False
    #         ).point_from_proportion(0.5)
    #     )

    #     text_B = Text("B", color=WHITE).move_to(
    #         Angle(
    #              line_B,line_NORTH, radius=4 + 3*SMALL_BUFF, other_angle=False
    #         ).point_from_proportion(0.5)
    #     )

    #     text_C = Text("C", color=WHITE).move_to(
    #         Angle(
    #              line_C,line_NORTH, radius=2 + 3*SMALL_BUFF, other_angle=False
    #         ).point_from_proportion(0.5)
    #     )

    #     self.add(line_NORTH, line_WEST, line_NORWEST, line_A, a, text_A, line_B, b, text_B, line_C, c, text_C)
    #     self.wait()

    #     line_A.add_updater(
    #         lambda x: x.become(line_ref_A.copy()).rotate(
    #             (rotation_tracker.get_value() * DEGREES)%ONE_ROTATION, about_point=rotation_center
    #         )
    #     )
        
    #     line_B.add_updater(
    #         lambda x: x.become(line_ref_B.copy()).rotate(
    #             (rotation_tracker.get_value() * DEGREES)%ONE_ROTATION, about_point=rotation_center
    #         )
    #     )

    #     line_C.add_updater(
    #         lambda x: x.become(line_ref_C.copy()).rotate(
    #             (rotation_tracker.get_value() * DEGREES)%ONE_ROTATION, about_point=rotation_center
    #         )
    #     )

    #     a.add_updater(
    #         lambda x: x.become(Angle( line_A,line_NORTH, radius=5, other_angle=False))
    #     )
    #     b.add_updater(
    #         lambda x: x.become(Angle( line_B,line_NORTH, radius=4, other_angle=False))
    #     )
    #     c.add_updater(
    #         lambda x: x.become(Angle( line_C,line_NORTH, radius=2, other_angle=False))
    #     )

    #     text_A.add_updater(
    #         lambda x: x.move_to(
    #             Angle(
    #                  line_A,line_NORTH, radius=5 + 3*SMALL_BUFF, other_angle=False
    #             ).point_from_proportion(0.5)
    #         )
    #     )

    #     text_B.add_updater(
    #         lambda x: x.move_to(
    #             Angle(
    #                  line_B,line_NORTH, radius= 4 + 3*SMALL_BUFF, other_angle=False
    #             ).point_from_proportion(0.5)
    #         )
    #     )

    #     text_C.add_updater(
    #         lambda x: x.move_to(
    #             Angle(
    #                  line_C,line_NORTH, radius=2 + 3*SMALL_BUFF, other_angle=False
    #             ).point_from_proportion(0.5)
    #         )
    #     )

    #     self.play(rotation_tracker.animate.set_value(0))
    #     self.wait(1)
    #     self.play(rotation_tracker.animate.set_value(40))
    #     self.wait(1)
    #     #self.play(tex.animate.set_color(RED), run_time=0.5)
    #     self.play(rotation_tracker.animate.set_value(90))