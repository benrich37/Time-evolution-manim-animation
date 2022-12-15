import numpy as np
from manimlib import Scene, ValueTracker, DEGREES, Dot, WHITE, IN, \
    ComplexValueTracker, DecimalNumber, RIGHT, Tex, LEFT, FadeOut, FadeIn


class vectormath(Scene):
    def construct(self):
        frame_theta = ValueTracker(0)
        frame_phi = ValueTracker(0)
        frame_gamma = ValueTracker(0)


        self.add(axes[i])
        self.add(bracketL,bracketR)


        self.camera.frame.add_updater(
            lambda f: f.set_euler_angles(theta=frame_theta.get_value(),
                                         phi=frame_phi.get_value(),
                                         # gamma=frame_gamma.get_value(),
                                         units=DEGREES)
        )
        self.play(frame_theta.animate.set_value(-30),frame_phi.animate.set_value(60))

        for i in np.arange(vecdim[0]):
            for j in np.arange(vecdim[1]):
                self.add(vec_draw[i][j])
        mag_draw = [
            Dot().set_color(WHITE).move_to(origins[0]).scale(8).shift(IN/10).add_updater(
                lambda c: c.set_opacity(vec_track[0][2].get_value())
            ),
            Dot().set_color(WHITE).move_to(origins[1]).scale(8).shift(IN/10).add_updater(
                lambda c: c.set_opacity(vec_track[1][2].get_value())
            )
        ]
        if cirhuh:
            for i in np.arange(vecdim[0]):
                self.add(mag_draw[i])


        def auto_play():
            args = []
            for i in np.arange(vecdim[0]):
                args.append(vec_track[i][0].animate.set_value(np.real(vec[i])))
                args.append(vec_track[i][1].animate.set_value(np.imag(vec[i])))
                args.append(vec_track[i][2].animate.set_value(abs(vec[i])))
            args.append(vec_complex_track[0].animate.set_value(vec[0]))
            args.append(vec_complex_track[1].animate.set_value(vec[1]))
            self.play(*args)




        shift_scale = 4
        vec_complex_track = [ComplexValueTracker(0),ComplexValueTracker(0)]
        id1 = DecimalNumber(0).move_to(origins[0]).shift(shift_scale*RIGHT*ax_range).add_updater(
            lambda d: d.set_value(vec_complex_track[0].get_value()))
        id2 = DecimalNumber(0).move_to(origins[1]).shift(shift_scale*RIGHT*ax_range).add_updater(
            lambda d: d.set_value(vec_complex_track[1].get_value()))
        self.add(id1,id2)

        def play_dt(dt):
            args = []
            for i in np.arange(vecdim[0]):
                args.append(vec_track[i][0].animate.set_value(np.real(vec[i])))
                args.append(vec_track[i][1].animate.set_value(np.imag(vec[i])))
                args.append(vec_track[i][2].animate.set_value(abs(vec[i])))
            args.append(vec_complex_track[0].animate.set_value(vec[0]))
            args.append(vec_complex_track[1].animate.set_value(vec[1]))
            self.play(*args,run_time=dt)

        hamil_sigz = Tex("\\hat{H} = \\begin{bmatrix} 1 & 0 \\\ 0 & -1 \\end{bmatrix}")
        hamil_sigz_pert = Tex("\\hat{H} = \\begin{bmatrix} 0.9 & 0.1 \\\ 0.1 & -0.9 \\end{bmatrix}")
        # hamil_sigy = Tex("\\hat{H} = \\begin{bmatrix} 0 & -i \\\ i & 0 \\end{bmatrix}")
        # hamil_sigx = Tex("\\hat{H} = \\begin{bmatrix} 0 & 1 \\\ 1 & 0 \\end{bmatrix}")
        # h_sigz = Matrix([["1", "0"], ["0", "-1"]])
        # h_sigx = Matrix([["0", "1"], ["1", "0"]])
        # hamil_sigz = VGroup(Tex("\\hat{H} = ").align_to(h_sigz.get_left(),LEFT).shift(h_sigz.get_width()*LEFT/2),h_sigz)
        # hamil_sigz = Tex("\\hat{H} = \\begin{bmatrix} 1 ", " & ", " 0 ", " \\\\ ", " 0 ", " & ", " -1 ", " \\end{bmatrix}")
        # hamil_sigz = Tex("\\hat{H} = \\begin{bmatrix} 1 ", " & ", " 0 ", " \\\\ ", " 0 ", " & ", " -1 "," \\end{bmatrix}")
        hamil_sigy = Tex("\\hat{H} = \\begin{bmatrix} 0 & -i \\\ i & 0 \\end{bmatrix}")
        hamil_sigx = Tex("\\hat{H} = \\begin{bmatrix} 0 & 1 \\\ 1 & 0 \\end{bmatrix}")


        id1 = DecimalNumber(0).add_updater(lambda n: n.set_value(vec_complex_track[0].get_value()))
        id2 = DecimalNumber(0).add_updater(lambda n: n.set_value(vec_complex_track[1].get_value()))

        self.add(hamil_sigz.shift(shift_scale*LEFT))
        dt_1 = 0.1
        steps = 20
        for i in np.arange(steps):
            vec = np.dot(prop_gen(dt_1, "z"), vec)
            play_dt(dt_1/2)

        hamil_sigz_pert.move_to(hamil_sigz)
        self.play(FadeOut(hamil_sigz),FadeIn(hamil_sigz_pert))

        dt_1 = 0.5
        steps = 20
        for i in np.arange(steps):
            vec = np.dot(prop_sig_z_pert(dt_1), vec)
            play_dt(dt_1 / 10)




        # self.play(frame_gamma.animate.set_value(180),run_time=3)
        # # self.play(frame_gamma.animate.set_value(0), run_time=1)
        # self.play(frame_theta.animate.set_value(180), run_time=3)
        # self.play(frame_theta.animate.set_value(30), run_time=1)
        # self.play(frame_phi.animate.set_value(180), run_time=3)
        # self.play(frame_phi.animate.set_value(0), run_time=1)
        # self.play(frame_theta.animate.set_value(-30))
        # self.play(frame_theta.animate.set_value(-50))

        # self.remove(hamil_sigz)
        # self.add(hamil_sigy)
        #
        # steps = 200
        # for i in np.arange(steps):
        #     vec = np.dot(prop_gen(dt_1, "y"), vec)
        #     play_dt(dt_1/2)

        self.camera.frame.clear_updaters()
        # Keep this ^ so that you can play around after scene is over
