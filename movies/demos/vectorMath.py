import numpy as np
from manimlib import *
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '../..'))
from funcs.methods.propogation import prop_gen, prop_sig_z_pert

bracketL = Tex("\\Bigg[")
bracketR = Tex("\\Bigg]")

class vectormath(Scene):
    def construct(self):
        # Turn on for modulus circles
        cirhuh = False
        n = 2
        ax_range = 1
        origins = [None] * n
        for i in np.arange(n):
            origins[i] = (2*i - (n/2)) * UP * 1.5 * ax_range
        # self.camera.set_euler_angles(theta=None, phi=None, gamma=None, units=RADIANS)
        # self.camera.frame.set_euler_angles(theta=-30, phi=60, units=DEGREES)
        # self.camera.frame.shift(OUT*10)
        axes = [None] * n
        # for i in np.arange(n):
        #     axes[i] = ThreeDAxes(
        #         x_range=[-ax_range, ax_range, 1],
        #         y_range=[-ax_range, ax_range, 1],
        #         z_range=[-ax_range, ax_range, 1],
        #         x_length=ax_range,
        #         y_length=ax_range,
        #         z_length=ax_range,
        #     ).move_to(origins[i])
        for i in np.arange(n):
            axes[i] = ThreeDAxes(
                x_range=[-ax_range, ax_range, 1],
                y_range=[-ax_range, ax_range, 1],
                z_range=[0, ax_range, 1],
                x_length=ax_range,
                y_length=ax_range,
                z_length=ax_range,
            ).move_to(origins[i]).shift(OUT * ax_range / 2)
        for i in np.arange(n):
            self.add(axes[i])

        bracketL = Tex("\\Bigg[")
        bracketR = Tex("\\Bigg]")
        #bracket = Tex("\\Bigg[",  "\\;", "\\Bigg]")
        bracketL.scale((3 * n * ax_range) / bracketL.get_height()).shift(LEFT*ax_range)
        bracketR.scale((3 * n * ax_range) / bracketR.get_height()).shift(RIGHT*ax_range)
        self.add(bracketL,bracketR)

        frame_theta = ValueTracker(0)
        frame_phi = ValueTracker(0)
        frame_gamma = ValueTracker(0)
        self.camera.frame.add_updater(
            lambda f: f.set_euler_angles(theta=frame_theta.get_value(),
                                         phi=frame_phi.get_value(),
                                         # gamma=frame_gamma.get_value(),
                                         units=DEGREES)
        )
        self.play(frame_theta.animate.set_value(-30),frame_phi.animate.set_value(60))

        vec = np.empty((2,), dtype=complex)
        vec[0] = 1
        vec[1] = 0
        # vec_track = [[None]*3]*2
        # vecdim = np.shape(vec_track)
        # for i in np.arange(vecdim[0]):
        #     for j in np.arange(vecdim[1]):
        #         vec_track[i][j] = ValueTracker(0)
        # vec_track = [[ValueTracker(0)] * 3] * 2
        vec_track = [[ValueTracker(0),ValueTracker(0),ValueTracker(0)],
                     [ValueTracker(0),ValueTracker(0),ValueTracker(0)]]
        vecdim = np.shape(vec_track)
        # def vec_updater(vec,i,j):
        #     if j == 0:
        #         vec.set_points_by_ends(origins[i], origins[i] + vec_track[i][j].get_value() * RIGHT)
        #     if j == 1:
        #         vec.set_points_by_ends(origins[i], origins[i] + vec_track[i][j].get_value() * UP)
        #     if j == 2:
        #         vec.set_points_by_ends(origins[i], origins[i] + vec_track[i][j].get_value() * OUT)

        # vec_draw = [
        #     [Vector().set_color(BLUE),
        #     Vector().set_color(RED),
        #     Vector().set_color(WHITE)],
        #     [Vector().set_color(BLUE),
        #      Vector().set_color(RED),
        #      Vector().set_color(WHITE)]
        # ]

        # for i in np.arange(vecdim[0]):
        #     for j in np.arange(vecdim[1]):
        #         always(vec_updater,
        #                vec_draw[i][j],
        #                i,
        #                j
        #                )
        vec_draw = [
                [
                    Vector().set_color(BLUE).add_updater(
                        lambda v: v.set_points_by_ends(origins[0], origins[0] + vec_track[0][0].get_value() * RIGHT)),
                    Vector().set_color(RED).add_updater(
                        lambda v: v.set_points_by_ends(origins[0], origins[0] + vec_track[0][1].get_value() * UP)),
                    Vector().set_color(WHITE).add_updater(
                        lambda v: v.set_points_by_ends(origins[0], origins[0] + vec_track[0][2].get_value() * OUT))
                ],
                [
                    Vector().set_color(BLUE).add_updater(
                        lambda v: v.set_points_by_ends(origins[1], origins[1] + vec_track[1][0].get_value() * RIGHT)),
                    Vector().set_color(RED).add_updater(
                        lambda v: v.set_points_by_ends(origins[1], origins[1] + vec_track[1][1].get_value() * UP)),
                    Vector().set_color(WHITE).add_updater(
                        lambda v: v.set_points_by_ends(origins[1], origins[1] + vec_track[1][2].get_value() * OUT))
                ]
            ]
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

        # def prop_in_proj(dt,basis,vector=vec):
        #     # Make our propogator
        #     if basis == "x":
        #         propogator = prop_sig_x(dt)
        #     elif basis == "y":
        #         propogator = prop_sig_y(dt)
        #     elif basis == "z":
        #         propogator = prop_sig_z(dt)
        #     # Apply it to our vector
        #     global vec
        #     vec = np.dot(propogator,vector)
        #     # Play the updated vector
        #     args = []
        #     for i in np.arange(vecdim[0]):
        #         args.append(vec_track[i][0].animate.set_value(np.real(vec[i])))
        #         args.append(vec_track[i][1].animate.set_value(np.imag(vec[i])))
        #         args.append(vec_track[i][2].animate.set_value(abs(vec[i])))
        #     self.play(*args,runtime=dt)

        # auto_play()
        #
        # vec = np.dot(vec,sig_z)
        #
        # auto_play()
        #
        # vec = np.dot(prop_sig_y(1),vec)
        #
        # auto_play()



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

        # partA, id1, spacer, id2, partB = vectorTex = VGroup(
        #     Tex("\\ket{\\psi} = \\begin{bmatrix}"),
        #     str(DecimalNumber(0).add_updater(lambda d: d.set_value(vec[0])).get_value()),
        #     Tex(" \\ "),
        #     str(DecimalNumber(0).add_updater(lambda d: d.set_value(vec[1])).get_value()),
        #     Tex("\\end{bmatrix}")
        # )
        # vectorMatrix = Matrix([
        #     DecimalNumber(0).add_updater(lambda d: d.set_value(vec[0])).get_value(),
        #     DecimalNumber(0).add_updater(lambda d: d.set_value(vec[1])).get_value()
        # ])



        # f_always(id1.set_value, vec[0])
        # f_always(id2.set_value, vec[1])
        # vectorMatrix = Matrix([[str(id1.get_value())], [str(id2.get_value())]])
        # vectorMatrix = DecimalMatrix([
        #     [DecimalNumber(0).add_updater(lambda n: n.set_value(vec_complex_track[0].get_value()))],
        #     [DecimalNumber(0).add_updater(lambda n: n.set_value(vec_complex_track[1].get_value()))]
        # ])
        id1 = DecimalNumber(0).add_updater(lambda n: n.set_value(vec_complex_track[0].get_value()))
        id2 = DecimalNumber(0).add_updater(lambda n: n.set_value(vec_complex_track[1].get_value()))

        # show_psi = Tex("\\ket{\\psi} = \\Bigg[").move_to(origins[0])
        # show_psi.shift(RIGHT*(ax_range+show_psi.get_width()))
        # self.add(show_psi)

        # vec = z_p
        # vec = np.dot(z_U,vec)
        # auto_play()
        # vec = np.dot(z_U_dag, vec)
        # auto_play()
        # vec = np.dot(x_U, vec)
        # auto_play()
        # vec = np.dot(x_U_dag, vec)
        # auto_play()
        # vec = np.dot(y_U, vec)
        # auto_play()
        # vec = np.dot(y_U_dag, vec)
        # auto_play()

        self.add(hamil_sigz.shift(shift_scale*LEFT))
        dt_1 = 0.1
        steps = 200
        for i in np.arange(steps):
            vec = np.dot(prop_gen(dt_1, "z"), vec)
            play_dt(dt_1/2)

        hamil_sigz_pert.move_to(hamil_sigz)
        self.play(FadeOut(hamil_sigz),FadeIn(hamil_sigz_pert))

        dt_1 = 0.5
        steps = 200
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


# class vectormath(Scene):
#     def construct(self):
#         frame_theta = ValueTracker(0)
#         frame_phi = ValueTracker(0)
#         frame_gamma = ValueTracker(0)
#
#
#         self.add(axes[i])
#         self.add(bracketL,bracketR)
#
#
#         self.camera.frame.add_updater(
#             lambda f: f.set_euler_angles(theta=frame_theta.get_value(),
#                                          phi=frame_phi.get_value(),
#                                          # gamma=frame_gamma.get_value(),
#                                          units=DEGREES)
#         )
#         self.play(frame_theta.animate.set_value(-30),frame_phi.animate.set_value(60))
#
#         for i in np.arange(vecdim[0]):
#             for j in np.arange(vecdim[1]):
#                 self.add(vec_draw[i][j])
#         mag_draw = [
#             Dot().set_color(WHITE).move_to(origins[0]).scale(8).shift(IN/10).add_updater(
#                 lambda c: c.set_opacity(vec_track[0][2].get_value())
#             ),
#             Dot().set_color(WHITE).move_to(origins[1]).scale(8).shift(IN/10).add_updater(
#                 lambda c: c.set_opacity(vec_track[1][2].get_value())
#             )
#         ]
#         if cirhuh:
#             for i in np.arange(vecdim[0]):
#                 self.add(mag_draw[i])
#
#
#         def auto_play():
#             args = []
#             for i in np.arange(vecdim[0]):
#                 args.append(vec_track[i][0].animate.set_value(np.real(vec[i])))
#                 args.append(vec_track[i][1].animate.set_value(np.imag(vec[i])))
#                 args.append(vec_track[i][2].animate.set_value(abs(vec[i])))
#             args.append(vec_complex_track[0].animate.set_value(vec[0]))
#             args.append(vec_complex_track[1].animate.set_value(vec[1]))
#             self.play(*args)
#
#
#
#
#         shift_scale = 4
#         vec_complex_track = [ComplexValueTracker(0),ComplexValueTracker(0)]
#         id1 = DecimalNumber(0).move_to(origins[0]).shift(shift_scale*RIGHT*ax_range).add_updater(
#             lambda d: d.set_value(vec_complex_track[0].get_value()))
#         id2 = DecimalNumber(0).move_to(origins[1]).shift(shift_scale*RIGHT*ax_range).add_updater(
#             lambda d: d.set_value(vec_complex_track[1].get_value()))
#         self.add(id1,id2)
#
#         def play_dt(dt):
#             args = []
#             for i in np.arange(vecdim[0]):
#                 args.append(vec_track[i][0].animate.set_value(np.real(vec[i])))
#                 args.append(vec_track[i][1].animate.set_value(np.imag(vec[i])))
#                 args.append(vec_track[i][2].animate.set_value(abs(vec[i])))
#             args.append(vec_complex_track[0].animate.set_value(vec[0]))
#             args.append(vec_complex_track[1].animate.set_value(vec[1]))
#             self.play(*args,run_time=dt)
#
#         hamil_sigz = Tex("\\hat{H} = \\begin{bmatrix} 1 & 0 \\\ 0 & -1 \\end{bmatrix}")
#         hamil_sigz_pert = Tex("\\hat{H} = \\begin{bmatrix} 0.9 & 0.1 \\\ 0.1 & -0.9 \\end{bmatrix}")
#         # hamil_sigy = Tex("\\hat{H} = \\begin{bmatrix} 0 & -i \\\ i & 0 \\end{bmatrix}")
#         # hamil_sigx = Tex("\\hat{H} = \\begin{bmatrix} 0 & 1 \\\ 1 & 0 \\end{bmatrix}")
#         # h_sigz = Matrix([["1", "0"], ["0", "-1"]])
#         # h_sigx = Matrix([["0", "1"], ["1", "0"]])
#         # hamil_sigz = VGroup(Tex("\\hat{H} = ").align_to(h_sigz.get_left(),LEFT).shift(h_sigz.get_width()*LEFT/2),h_sigz)
#         # hamil_sigz = Tex("\\hat{H} = \\begin{bmatrix} 1 ", " & ", " 0 ", " \\\\ ", " 0 ", " & ", " -1 ", " \\end{bmatrix}")
#         # hamil_sigz = Tex("\\hat{H} = \\begin{bmatrix} 1 ", " & ", " 0 ", " \\\\ ", " 0 ", " & ", " -1 "," \\end{bmatrix}")
#         hamil_sigy = Tex("\\hat{H} = \\begin{bmatrix} 0 & -i \\\ i & 0 \\end{bmatrix}")
#         hamil_sigx = Tex("\\hat{H} = \\begin{bmatrix} 0 & 1 \\\ 1 & 0 \\end{bmatrix}")
#
#
#         id1 = DecimalNumber(0).add_updater(lambda n: n.set_value(vec_complex_track[0].get_value()))
#         id2 = DecimalNumber(0).add_updater(lambda n: n.set_value(vec_complex_track[1].get_value()))
#
#         self.add(hamil_sigz.shift(shift_scale*LEFT))
#         dt_1 = 0.1
#         steps = 20
#         for i in np.arange(steps):
#             vec = np.dot(prop_gen(dt_1, "z"), vec)
#             play_dt(dt_1/2)
#
#         hamil_sigz_pert.move_to(hamil_sigz)
#         self.play(FadeOut(hamil_sigz),FadeIn(hamil_sigz_pert))
#
#         dt_1 = 0.5
#         steps = 20
#         for i in np.arange(steps):
#             vec = np.dot(prop_sig_z_pert(dt_1), vec)
#             play_dt(dt_1 / 10)
#
#
#
#
#         # self.play(frame_gamma.animate.set_value(180),run_time=3)
#         # # self.play(frame_gamma.animate.set_value(0), run_time=1)
#         # self.play(frame_theta.animate.set_value(180), run_time=3)
#         # self.play(frame_theta.animate.set_value(30), run_time=1)
#         # self.play(frame_phi.animate.set_value(180), run_time=3)
#         # self.play(frame_phi.animate.set_value(0), run_time=1)
#         # self.play(frame_theta.animate.set_value(-30))
#         # self.play(frame_theta.animate.set_value(-50))
#
#         # self.remove(hamil_sigz)
#         # self.add(hamil_sigy)
#         #
#         # steps = 200
#         # for i in np.arange(steps):
#         #     vec = np.dot(prop_gen(dt_1, "y"), vec)
#         #     play_dt(dt_1/2)
#
#         self.camera.frame.clear_updaters()
#         # Keep this ^ so that you can play around after scene is over
