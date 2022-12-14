import scipy.stats
from ref.hold_constants import *

scipy.stats.linregress()


class DvProof(Scene):
    def construct(self):

        self.ax_range = 10
        axes = ThreeDAxes(
                x_range=[-self.ax_range, self.ax_range, 1],
                y_range=[-self.ax_range, self.ax_range, 1],
                z_range=[0, self.ax_range, 1],
                x_length=self.ax_range,
                y_length=self.ax_range,
                z_length=self.ax_range,
            )
        self.add(axes)

        origin = ORIGIN
        r1 = Point(RIGHT)
        r2 = Point(RIGHT*2)
        line = Line(r1.get_center(), r2.get_center())
        self.add(line)

        self.play(line.animate.rotate_about_origin(10 * DEGREES, OUT))

        r1.move_to(line.get_start_and_end()[0])
        r2.move_to(line.get_start_and_end()[1])

        line.add_updater(
            lambda l: l.set_points_by_ends(r1.get_center(), r2.get_center())
        )

        self.play(r1.animate.shift(UP))

class Cartesian_tests(Scene):
    def update_list(self,list):
        args = []
        for i in np.arange(len(list)):
            args.append(list[i].animate.update())
        return args

    def construct(self):
        frame_theta = ValueTracker(np.pi/6)
        frame_phi = ValueTracker(np.pi/3)
        self.camera.frame.set_euler_angles(theta=frame_theta.get_value(),
                                           phi=frame_phi.get_value(),
                                           units=RADIANS)
        self.camera.frame.add_updater(
            lambda f: f.set_euler_angles(theta=frame_theta.get_value(),
                                           phi=frame_phi.get_value(),
                                           units=RADIANS)
        )
        def zoom(d):
            return self.camera.frame.animate.shift(
                ORIGIN - [
                    d*np.sin(frame_phi.get_value()) * np.sin(PI - frame_theta.get_value()),
                    d*np.sin(frame_phi.get_value()) * np.cos(PI - frame_theta.get_value()),
                    d*np.cos(frame_phi.get_value()),
                ]
            )

        self.ax_range = 10
        axes = ThreeDAxes(
                x_range=[-self.ax_range, self.ax_range, 1],
                y_range=[-self.ax_range, self.ax_range, 1],
                z_range=[0, self.ax_range, 1],
                x_length=self.ax_range,
                y_length=self.ax_range,
                z_length=self.ax_range,
            )
        #self.add(axes)

        base_range = 2
        p_s = 2

        ################################################################################################################
        radius_i = 1
        θ_i = np.pi / 6
        φ_i = np.pi / 6
        radius_f = 1.5
        θ_f = np.pi / 3
        φ_f = np.pi / 3

        p_center = Point(LEFT*2)
        x_center = ValueTracker(-2)
        x_wid = ValueTracker(0.1)
        y_center = ValueTracker(0)
        y_wid = ValueTracker(0.1)
        target_wid = ValueTracker(0.5)
        radius_back = ValueTracker().set_value(radius_i)
        radius_front = ValueTracker().set_value(radius_i)
        θ_left = ValueTracker().set_value(θ_i)
        θ_right = ValueTracker().set_value(θ_i)
        φ_top = ValueTracker().set_value(φ_i)
        φ_bottom = ValueTracker().set_value(φ_i)
        ################################################################################################################
        def flat(u,v):
            return [u,v,0.015]
        def test_sin(u,v):
            return [u,v,np.sin(u)*np.cos(v)]
        def wave_packet(u,v):
            u_tight = x_wid.get_value()
            v_tight = y_wid.get_value()
            u_c = x_center.get_value()
            v_c = y_center.get_value()
            return [u, v,
                    p_s*np.exp(-((u-u_c) ** 2) / u_tight) * np.exp(-((v-v_c) ** 2) / v_tight)]
        def curve_out(u,v):
            return [u,v,np.sin(v)]
        def y_packet(t):
            return [x_center.get_value(),t,p_s*np.exp(-((t-y_center.get_value())**2)/y_wid.get_value())]
        def x_packet(t):
            return [t,y_center.get_value(),p_s*np.exp(-((t-x_center.get_value())**2)/x_wid.get_value())]
        def constant_r_back(u,v):
            r = radius_back.get_value()
            θ = u
            φ = v
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        def constant_r_front(u,v):
            r = radius_front.get_value()
            θ = u
            φ = v
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        def constant_θ_left(u,v):
            r = u
            θ = θ_left.get_value()
            φ = v
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        def constant_θ_right(u,v):
            r = u
            θ = θ_right.get_value()
            φ = v
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        def constant_φ_top(u,v):
            r = v
            θ = u
            φ = φ_top.get_value()
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        def constant_φ_bottom(u,v):
            r = v
            θ = u
            φ = φ_bottom.get_value()
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        ################################################################################################################
        base_surface = ParametricSurface(flat,u_range=[-base_range,base_range],v_range=[-base_range,base_range])
        box_surfaces = [
            # back
            ParametricSurface(
                constant_r_back,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
            ),
            # front
            ParametricSurface(
                constant_r_front,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
            ),
            # left
            ParametricSurface(
                constant_θ_left,
                u_range=[radius_back.get_value(), radius_front.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
            ),
            # right
            ParametricSurface(
                constant_θ_right,
                u_range=[radius_back.get_value(), radius_front.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
            ),
            # top
            ParametricSurface(
                constant_φ_top,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[radius_back.get_value(), radius_front.get_value()]
            ),
            # bottom
            ParametricSurface(
                constant_φ_bottom,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[radius_back.get_value(), radius_front.get_value()]
            )
        ]
        def set_box_surfaces(box_surfaces_dummy):
            box_surfaces_dummy[0] = ParametricSurface(
                    constant_r_back,
                    u_range=[θ_left.get_value(), θ_right.get_value()],
                    v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
                # front
            box_surfaces_dummy[1] =ParametricSurface(
                    constant_r_front,
                    u_range=[θ_left.get_value(), θ_right.get_value()],
                    v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
                # left
            box_surfaces_dummy[2] =ParametricSurface(
                    constant_θ_left,
                    u_range=[radius_back.get_value(), radius_front.get_value()],
                    v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
                # right
            box_surfaces_dummy[3] = ParametricSurface(
                    constant_θ_right,
                    u_range=[radius_back.get_value(), radius_front.get_value()],
                    v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
                # top
            box_surfaces_dummy[4] = ParametricSurface(
                    constant_φ_top,
                    u_range=[θ_left.get_value(), θ_right.get_value()],
                    v_range=[radius_back.get_value(), radius_front.get_value()]
                )
                # bottom
            box_surfaces_dummy[5] =ParametricSurface(
                    constant_φ_bottom,
                    u_range=[θ_left.get_value(), θ_right.get_value()],
                    v_range=[radius_back.get_value(), radius_front.get_value()]
                )
        box_surfaces_redraw = [
            # back
            always_redraw(
                lambda:
                ParametricSurface(
                constant_r_back,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
            ),
            # front
            always_redraw(
                lambda:
                ParametricSurface(
                constant_r_front,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
            ),
            # left
            always_redraw(
                lambda:
                ParametricSurface(
                constant_θ_left,
                u_range=[radius_back.get_value(), radius_front.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
            ),
            # right
            always_redraw(
                lambda:
                ParametricSurface(
                constant_θ_right,
                u_range=[radius_back.get_value(), radius_front.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
            ),
            # top
            always_redraw(
                lambda:
                ParametricSurface(
                constant_φ_top,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[radius_back.get_value(), radius_front.get_value()]
                )
            ),
            # bottom
            always_redraw(
                lambda:
                ParametricSurface(
                constant_φ_bottom,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[radius_back.get_value(), radius_front.get_value()]
                )
            )
        ]
        updater_surface = always_redraw(
            lambda: ParametricSurface(
            test_sin,
            u_range=[-x_wid.get_value(), x_wid.get_value()],
            v_range=[-y_wid.get_value(), y_wid.get_value()]
            )
        )
        # indicator_line = always_redraw(
        #     lambda: Line(
        #         ORIGIN,
        #         [radius_front.get_value() * np.sin(φ_top.get_value()) * np.cos(θ_right.get_value()),
        #          radius_front.get_value() * np.sin(φ_top.get_value()) * np.sin(θ_right.get_value()),
        #          radius_front.get_value() * np.cos(φ_top.get_value())]
        #     )
        # )
        indicator_line = Line(
                ORIGIN,
                [radius_front.get_value() * np.sin(φ_top.get_value()) * np.cos(θ_right.get_value()),
                 radius_front.get_value() * np.sin(φ_top.get_value()) * np.sin(θ_right.get_value()),
                 radius_front.get_value() * np.cos(φ_top.get_value())]
            )
        # test_theta = np.pi/
        line_x = Line(ORIGIN,[1,0,0]).set_color(RED)
        line_y = Line(ORIGIN, [0, 1, 0]).set_color(YELLOW)
        line_z = Line(ORIGIN, [0, 0, 1]).set_color(GREEN)

        ###############################################################################################################

        self.add(axes,line_x,line_y,line_z)
        # self.add(*box_surfaces_redraw,
        #          indicator_line)
        # self.play(
        #     radius_front.animate.set_value(radius_f),
        # )
        # self.play(
        #     θ_right.animate.set_value(θ_f),
        # )
        # self.play(
        #     φ_top.animate.set_value(φ_f),
        # )

        # radius_front.set_value(radius_f)
        # θ_right.set_value(θ_f)
        # φ_top.set_value(φ_f)
        # set_box_surfaces(box_surfaces)
        self.add(*box_surfaces,
                 indicator_line)
        # self.play(frame_phi.animate.set_value(45))
        # self.play(frame_theta.animate.set_value(-60))
        self.camera.frame.move_to(ORIGIN)
        self.play(
            frame_theta.animate.set_value(0),
            frame_phi.animate.set_value(0)
        )
        self.play(frame_phi.animate.set_value(PI/2),
                  frame_theta.animate.set_value(0),
                  # run_time=3
                  )
        self.play(zoom(3))
        self.play(zoom(-3))
        self.play(
            indicator_line.animate.set_points_by_ends(
                ORIGIN,
                [
                    np.sin(frame_phi.get_value()) * np.sin(PI-frame_theta.get_value()),
                    np.sin(frame_phi.get_value()) * np.cos(PI-frame_theta.get_value()),
                    np.cos(frame_phi.get_value()),
                ]
            )
        )
        self.play(frame_phi.animate.set_value(PI / 3),
                  frame_theta.animate.set_value(0),
                  # run_time=3
                  )
        self.play(zoom(3))
        self.play(zoom(-3))
        self.play(
            indicator_line.animate.set_points_by_ends(
                ORIGIN,
                [
                    np.sin(frame_phi.get_value()) * np.sin(PI - frame_theta.get_value()),
                    np.sin(frame_phi.get_value()) * np.cos(PI - frame_theta.get_value()),
                    np.cos(frame_phi.get_value()),
                ]
            )
        )
        self.play(frame_phi.animate.set_value(PI / 3),
                  frame_theta.animate.set_value(PI/6),
                  # run_time=3
                  )
        self.play(zoom(3))
        self.play(zoom(-3))
        self.play(
            indicator_line.animate.set_points_by_ends(
                ORIGIN,
                [
                    np.sin(frame_phi.get_value()) * np.sin(PI - frame_theta.get_value()),
                    np.sin(frame_phi.get_value()) * np.cos(PI - frame_theta.get_value()),
                    np.cos(frame_phi.get_value()),
                ]
            )
        )
        self.play(zoom(3))
        self.play(self.camera.frame.animate.move_to(ORIGIN))
        self.play(zoom(3))
        # self.play(zoom(3))
        # self.play(frame_phi.animate.set_value(90),
        #           run_time=3)
        # self.play(frame_phi.animate.set_value(125),
        #           run_time=3)
        # self.play(frame_phi.animate.set_value(180),
        #           run_time=3)
        # self.play(frame_phi.animate.set_value(270),
        #           run_time=3)
        # self.play(frame_phi.animate.set_value(360),
        #           run_time=3)
        # self.play(
        #     frame_theta.animate.set_value(90),
        #     run_time=3
        # )
        # self.wait()
        # self.play(
        #     frame_phi.animate.set_value(90),
        #     run_time=3
        # )
        # self.play(θ_wid.animate.set_value(np.pi/4),
        #           φ_wid.animate.set_value(np.pi/4),
        #           polar_surface.animate.update()
        #           )
        # self.add(updater_surface)
        # self.play(test_sin_surface.animate.rotate(90*DEGREES,LEFT))
        # self.play(x_wid.animate.set_value(10),
        #           y_wid.animate.set_value(10),
        #           test_sin_surface.animate.update())
        # self.play(test_sin_surface.animate.rotate(-90 * DEGREES, LEFT))
        # self.add(test_surface)
        # self.add(linear_packet_x,linear_packet_y)

        # self.play(x_center.animate.set_value(0),
        #           x_wid.animate.set_value(target_wid.get_value()),
        #           y_wid.animate.set_value(target_wid.get_value())
        #           )
        self.camera.frame.clear_updaters()

class Cartesian(Scene):
    def update_list(self,list):
        args = []
        for i in np.arange(len(list)):
            args.append(list[i].animate.update())
        return args

    def construct(self):
        frame_theta = ValueTracker(6*np.pi/4)
        frame_phi = ValueTracker(np.pi/3)
        self.camera.frame.set_euler_angles(theta=frame_theta.get_value(),
                                           phi=frame_phi.get_value(),
                                           units=RADIANS)
        self.camera.frame.add_updater(
            lambda f: f.set_euler_angles(theta=frame_theta.get_value(),
                                           phi=frame_phi.get_value(),
                                           units=RADIANS)
        )
        def zoom(d):
            return self.camera.frame.animate.shift(
                ORIGIN - [
                    d*np.sin(frame_phi.get_value()) * np.sin(PI - frame_theta.get_value()),
                    d*np.sin(frame_phi.get_value()) * np.cos(PI - frame_theta.get_value()),
                    d*np.cos(frame_phi.get_value()),
                ]
            )

        self.ax_range = 10
        axes = ThreeDAxes(
                x_range=[-self.ax_range, self.ax_range, 1],
                y_range=[-self.ax_range, self.ax_range, 1],
                z_range=[0, self.ax_range, 1],
                x_length=self.ax_range,
                y_length=self.ax_range,
                z_length=self.ax_range,
            )

        ################################################################################################################
        radius_i = 1
        θ_i = np.pi / 6
        φ_i = np.pi / 3
        radius_f = 1.5
        θ_f = np.pi / 3
        φ_f = np.pi / 6

        p_center = Point(LEFT*2)
        x_center = ValueTracker(-2)
        x_wid = ValueTracker(0.1)
        y_center = ValueTracker(0)
        y_wid = ValueTracker(0.1)
        target_wid = ValueTracker(0.5)
        radius_back = ValueTracker().set_value(radius_i)
        radius_front = ValueTracker().set_value(radius_i)
        θ_left = ValueTracker().set_value(θ_i)
        θ_right = ValueTracker().set_value(θ_i)
        φ_top = ValueTracker().set_value(φ_i)
        φ_bottom = ValueTracker().set_value(φ_i)
        ################################################################################################################
        def flat(u,v):
            return [u,v,0.015]
        def test_sin(u,v):
            return [u,v,np.sin(u)*np.cos(v)]
        def wave_packet(u,v):
            u_tight = x_wid.get_value()
            v_tight = y_wid.get_value()
            u_c = x_center.get_value()
            v_c = y_center.get_value()
            return [u, v,
                    p_s*np.exp(-((u-u_c) ** 2) / u_tight) * np.exp(-((v-v_c) ** 2) / v_tight)]
        def curve_out(u,v):
            return [u,v,np.sin(v)]
        def y_packet(t):
            return [x_center.get_value(),t,p_s*np.exp(-((t-y_center.get_value())**2)/y_wid.get_value())]
        def x_packet(t):
            return [t,y_center.get_value(),p_s*np.exp(-((t-x_center.get_value())**2)/x_wid.get_value())]
        def constant_r_back(u,v):
            r = radius_back.get_value()
            θ = u
            φ = v
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        def constant_r_front(u,v):
            r = radius_front.get_value()
            θ = u
            φ = v
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        def constant_θ_left(u,v):
            r = u
            θ = θ_left.get_value()
            φ = v
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        def constant_θ_right(u,v):
            r = u
            θ = θ_right.get_value()
            φ = v
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        def constant_φ_top(u,v):
            r = v
            θ = u
            φ = φ_top.get_value()
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        def constant_φ_bottom(u,v):
            r = v
            θ = u
            φ = φ_bottom.get_value()
            return [r*np.sin(φ)*np.cos(θ),
                    r*np.sin(φ)*np.sin(θ),
                    r*np.cos(φ)]
        ################################################################################################################
        base_surface = ParametricSurface(flat,
                                         u_range=[-10,10],
                                         v_range=[-10,10])
        base = SurfaceMesh(base_surface).set_color(GREY_C)
        box_surfaces = [
            # back
            ParametricSurface(
                constant_r_back,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
            ).set_color(PURPLE),
            # front
            ParametricSurface(
                constant_r_front,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
            ),
            # left
            ParametricSurface(
                constant_θ_left,
                u_range=[radius_back.get_value(), radius_front.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
            ),
            # right
            ParametricSurface(
                constant_θ_right,
                u_range=[radius_back.get_value(), radius_front.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
            ),
            # top
            ParametricSurface(
                constant_φ_top,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[radius_back.get_value(), radius_front.get_value()]
            ),
            # bottom
            ParametricSurface(
                constant_φ_bottom,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[radius_back.get_value(), radius_front.get_value()]
            )
        ]
        def set_box_surfaces(box_surfaces_dummy):
            box_surfaces_dummy[0] = ParametricSurface(
                    constant_r_back,
                    u_range=[θ_left.get_value(), θ_right.get_value()],
                    v_range=[φ_bottom.get_value(), φ_top.get_value()]
                ).set_color(PURPLE_D)
                # front
            box_surfaces_dummy[1] =ParametricSurface(
                    constant_r_front,
                    u_range=[θ_left.get_value(), θ_right.get_value()],
                    v_range=[φ_bottom.get_value(), φ_top.get_value()]
                ).set_color(PURPLE)
                # left
            box_surfaces_dummy[2] =ParametricSurface(
                    constant_θ_left,
                    u_range=[radius_back.get_value(), radius_front.get_value()],
                    v_range=[φ_bottom.get_value(), φ_top.get_value()]
                ).set_color(GREEN_B)
                # right
            box_surfaces_dummy[3] = ParametricSurface(
                    constant_θ_right,
                    u_range=[radius_back.get_value(), radius_front.get_value()],
                    v_range=[φ_bottom.get_value(), φ_top.get_value()]
                ).set_color(GREEN_B)
                # top
            box_surfaces_dummy[4] = ParametricSurface(
                    constant_φ_top,
                    u_range=[θ_left.get_value(), θ_right.get_value()],
                    v_range=[radius_back.get_value(), radius_front.get_value()]
                ).set_color(GREEN_B)
                # bottom
            box_surfaces_dummy[5] =ParametricSurface(
                    constant_φ_bottom,
                    u_range=[θ_left.get_value(), θ_right.get_value()],
                    v_range=[radius_back.get_value(), radius_front.get_value()]
                ).set_color(GREEN_B)
        box_surfaces_redraw = [
            # back
            always_redraw(
                lambda:
                ParametricSurface(
                constant_r_back,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
            ),
            # front
            always_redraw(
                lambda:
                ParametricSurface(
                constant_r_front,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
            ),
            # left
            always_redraw(
                lambda:
                ParametricSurface(
                constant_θ_left,
                u_range=[radius_back.get_value(), radius_front.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
            ),
            # right
            always_redraw(
                lambda:
                ParametricSurface(
                constant_θ_right,
                u_range=[radius_back.get_value(), radius_front.get_value()],
                v_range=[φ_bottom.get_value(), φ_top.get_value()]
                )
            ),
            # top
            always_redraw(
                lambda:
                ParametricSurface(
                constant_φ_top,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[radius_back.get_value(), radius_front.get_value()]
                )
            ),
            # bottom
            always_redraw(
                lambda:
                ParametricSurface(
                constant_φ_bottom,
                u_range=[θ_left.get_value(), θ_right.get_value()],
                v_range=[radius_back.get_value(), radius_front.get_value()]
                )
            )
        ]
        indicator_line = always_redraw(
            lambda: Line(
                ORIGIN,
                [radius_i * np.sin(φ_top.get_value()) * np.cos(θ_right.get_value()),
                 radius_i * np.sin(φ_top.get_value()) * np.sin(θ_right.get_value()),
                 radius_i * np.cos(φ_top.get_value())]
            )
        )
        wand = always_redraw(
            lambda: Line(
                [radius_i * np.sin(φ_top.get_value()) * np.cos(θ_right.get_value()),
                 radius_i * np.sin(φ_top.get_value()) * np.sin(θ_right.get_value()),
                 radius_i * np.cos(φ_top.get_value())],
                [radius_front.get_value() * np.sin(φ_top.get_value()) * np.cos(θ_right.get_value()),
                 radius_front.get_value() * np.sin(φ_top.get_value()) * np.sin(θ_right.get_value()),
                 radius_front.get_value() * np.cos(φ_top.get_value())]
            ).set_color(GREY_B)
        )

        ###############################################################################################################

        self.add(axes,base)
        self.add(
                 indicator_line,
                 wand)
        self.play(
            self.camera.frame.animate.move_to(wand)
        )
        self.play(
            radius_front.animate.set_value(radius_f),
        )
        self.add(*box_surfaces_redraw,)
        self.add(wand,indicator_line)
        self.play(
            θ_right.animate.set_value(θ_f),
        )
        self.play(
            φ_top.animate.set_value(φ_f),
        )
        # θ_right.set_value(θ_f)
        # φ_top.set_value(φ_f)
        # radius_front.set_value(radius_f)
        # set_box_surfaces(box_surfaces)
        # self.add(*box_surfaces)


        # θ_right.set_value(θ_f)
        # φ_top.set_value(φ_f)
        # set_box_surfaces(box_surfaces)
        # self.add(*box_surfaces,
        #          indicator_line)
        # self.play(θ_wid.animate.set_value(np.pi/4),
        #           φ_wid.animate.set_value(np.pi/4),
        #           polar_surface.animate.update()
        #           )

        self.camera.frame.clear_updaters()


class Wavepacket(Scene):
    def construct(self):
        frame_theta = ValueTracker(30)
        frame_phi = ValueTracker(60)
        self.camera.frame.set_euler_angles(theta=frame_theta.get_value(),
                                           phi=frame_phi.get_value(),
                                           units=DEGREES)
        self.ax_range = 10
        axes = ThreeDAxes(
                x_range=[-self.ax_range, self.ax_range, 1],
                y_range=[-self.ax_range, self.ax_range, 1],
                z_range=[0, self.ax_range, 1],
                x_length=self.ax_range,
                y_length=self.ax_range,
                z_length=self.ax_range,
            )
        self.add(axes)

        base_range = 20
        p_s = 2

        ################################################################################################################
        p_center = Point(LEFT*2)
        x_center = ValueTracker().add_updater(
            lambda xc: xc.set_value(p_center.get_x())
        )
        x_wid = ValueTracker(0.1)
        y_center = ValueTracker().add_updater(
            lambda yc: yc.set_value(p_center.get_y())
        )
        y_wid = ValueTracker(0.1)
        target_wid = ValueTracker(0.5)
        int_wid_x = ValueTracker(2 * np.pi)
        int_wid_y = ValueTracker(2 * np.pi)
        n_select = ValueTracker(5)
        nmax = 6
        n_sliders = []
        for i in np.arange(nmax):
            n_sliders.append(ValueTracker(0))
        n_sliders[0].set_value(1)

        def wp_decomp_x(n,u):
            x = u
            lx = int_wid_x.get_value()
            αx = x_wid.get_value()
            pi = np.pi
            xexp = np.exp((((n * pi) / (2 * lx)) ** 2) * αx)
            xfn = np.exp(1j * np.pi * (
                    (n * x / lx)
            ))
            return (xexp*xfn) / (2 * lx)
        def wp_decomp_y(m,v):
            y = v
            ly = int_wid_y.get_value()
            αy = y_wid.get_value()
            pi = np.pi
            yexp = np.exp((((m * pi) / (2 * ly)) ** 2) * αy)
            yfn = np.exp(1j * np.pi * (
                    (m * y / ly)
            ))
            return (yexp*yfn) / (2 * ly)
        def wp_y_pure_x_select_norm():
            αy = y_wid.get_value()
            pi = np.pi
            y_comp = (1 / (np.sqrt(pi * αy)))
            x_comp = wp_decomp_x(n_select.get_value(), 0)
            return y_comp*x_comp
        wp_y_pure_x_select_static_norm = wp_y_pure_x_select_norm()
        def wp_y_pure_x_select(u,v):
            αy = y_wid.get_value()
            pi = np.pi
            y_comp = abs((np.exp(-(v**2)/αy))/(np.sqrt(pi*αy)))
            x_comp = wp_decomp_x(n_select.get_value(),u)
            return [u,v,x_comp*y_comp/wp_y_pure_x_select_norm()]
        def wp_y_pure_x_0_nmax_norm():
            αy = y_wid.get_value()
            pi = np.pi
            y_comp = 1 / (np.sqrt(pi * αy))
            x_comp = 0
            for i in np.arange(nmax):
                x_comp += wp_decomp_x(i, 0) * n_sliders[i].get_value()
            return x_comp * y_comp / wp_y_pure_x_select_norm()
        def wp_y_pure_x_0_nmax(u,v):
            αy = y_wid.get_value()
            pi = np.pi
            y_comp = abs((np.exp(-(v**2)/αy))/(np.sqrt(pi*αy)))
            x_comp = 0
            for i in np.arange(nmax):
                x_comp += wp_decomp_x(i,u)*n_sliders[i].get_value()
            return [u,v,x_comp*y_comp/wp_y_pure_x_select_norm()]
        def wp_decomp_const(n,m):
            lx = int_wid_x.get_value()
            ly = int_wid_y.get_value()
            αx = x_wid.get_value()
            αy = y_wid.get_value()
            pi = np.pi
            xexp = np.exp((((n * pi) / (2 * lx)) ** 2) * αx)
            yexp = np.exp((((m * pi) / (2 * ly)) ** 2) * αy)
            return (xexp*yexp)/(4*lx*ly)
        def wp_decomp_fn_nm(n,m,u,v):
            x = u
            y = v
            lx = int_wid_x.get_value()
            ly = int_wid_y.get_value()
            fn = np.exp(1j*np.pi*(
                (n * x / lx) + (m * y / ly)
            ))
            return wp_decomp_const(n,m) * fn
        def flat(u,v):
            return [u,v,0.015]
        def wave_packet(u,v):
            u_tight = x_wid.get_value()
            v_tight = y_wid.get_value()
            u_c = x_center.get_value()
            v_c = y_center.get_value()
            return [u, v,
                    p_s*np.exp(-((u-u_c) ** 2) / u_tight) * np.exp(-((v-v_c) ** 2) / v_tight)]
        def curve_out(u,v):
            return [u,v,np.sin(v)]
        def y_packet(t):
            return [x_center.get_value(),t,p_s*np.exp(-((t-y_center.get_value())**2)/y_wid.get_value())]
        def x_packet(t):
            return [t,y_center.get_value(),p_s*np.exp(-((t-x_center.get_value())**2)/x_wid.get_value())]
        x_elts = ValueTracker(10)
        y_elts = ValueTracker(10)
        def decomp_norm():
            nmax = int(x_elts.get_value())
            mmax = int(y_elts.get_value())
            output = 0
            for i in np.arange(nmax):
                for j in np.arange(mmax):
                    output += wp_decomp_fn_nm(i, j, 0, 0)
            return abs(output)
        decomp_norm_static = decomp_norm()
        def decomp_wp(u,v):
            nmax = int(x_elts.get_value())
            mmax = int(y_elts.get_value())
            output = 0
            for i in np.arange(nmax):
                for j in np.arange(mmax):
                    output += wp_decomp_fn_nm(i,j,u,v)
            return [u,v,abs(output)/decomp_norm_static]
        s_elts = ValueTracker(5)
        L = ValueTracker(1)
        def series_gen(u):
            srs = 0
            for ii in np.arange(s_elts.get_value()):
                i = ii*2 + 1
                srs += (1/i)*(np.sin(i*np.pi*u/L.get_value()))
            return [0,u,
                    (4/np.pi)*srs]
        ################################################################################################################
        base_surface = ParametricSurface(flat,u_range=[-base_range,base_range],v_range=[-base_range,base_range])
        # test_surface = always_redraw(
        #     lambda: ParametricSurface(wave_packet,
        #                               u_range=[x_center - 2 * np.sqrt(x_wid),
        #                                        x_center + 2 * np.sqrt(x_wid)],
        #                               v_range=[y_center - 2 * np.sqrt(y_wid),
        #                                        y_center + 2 * np.sqrt(y_wid)]
        #                                  )
        # )
        # test_surface.set_opacity(0.7)
        #hoop = ParametricSurface(curve_out,u_range=[-0.1,0.1])
        linear_packet_y = always_redraw(
            lambda: ParametricCurve(y_packet,t_range=[y_center.get_value() - 5 * np.sqrt(y_wid.get_value()),
                                                            y_center.get_value() + 5 * np.sqrt(y_wid.get_value())])
        )
        linear_packet_x = always_redraw(
            lambda: ParametricCurve(x_packet, t_range=[x_center.get_value() - 5 * np.sqrt(x_wid.get_value()),
                                                            x_center.get_value() + 5 * np.sqrt(x_wid.get_value())])
        )
        # fourier_series = ParametricCurve(
        #     series_gen,
        #     t_range=[-L.get_value(),L.get_value()]
        # )
        wp_series = ParametricSurface(
            wp_y_pure_x_select,
            u_range=[-3,3],
            v_range=[-3,3]
            # u_range=[-int_wid_x.get_value(),int_wid_x.get_value()],
            # v_Range=[-int_wid_y.get_value(),int_wid_y.get_value()]
        )
        wp_transform = always_redraw(
            lambda: ParametricSurface(
                wp_y_pure_x_0_nmax,
                u_range=[-3,3],
                v_range=[-3,3]
                )
        )
        ################################################################################################################
        # self.add(base_surface)
        # self.add(test_surface)
        # self.add(linear_packet_x,linear_packet_y)
        # self.add(fourier_series)
        self.add(wp_transform)
        self.play(n_sliders[1].animate.set_value(1),
                  )
        self.play(n_sliders[2].animate.set_value(1),
                  )
        self.play(n_sliders[3].animate.set_value(1),
                  )
        self.play(n_sliders[4].animate.set_value(1),
                  )
        self.play(n_sliders[5].animate.set_value(1),
                  )

        # self.play(p_center.animate.shift(RIGHT*2),
        #           x_center.animate.update(),
        #           y_center.animate.update(),
        #           x_wid.animate.set_value(target_wid.get_value()),
        #           y_wid.animate.set_value(target_wid.get_value())
        #           )
        # line = ArcBetweenPoints(LEFT*3,RIGHT*3)
        # circle = Circle(radius=3)
        # self.play(
        #     MoveAlongPath(p_center,circle),
        # )


