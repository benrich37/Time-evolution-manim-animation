from manimlib import *
# from manimlib.animation.indication import ElipFlash
import numpy as np


# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

sig_x = np.array([[0, 1],[1,0]])
sig_y = np.array([[0, -1j],[1j, 0]])
sig_z = np.array([[1, 0],[0, -1]])
z_vals, z_U = np.linalg.eig(sig_z)
z_U_dag = np.linalg.inv(z_U)
x_vals, x_U = np.linalg.eig(sig_x)
x_U_dag = np.linalg.inv(x_U)
y_vals, y_U = np.linalg.eig(sig_y)
y_U_dag = np.linalg.inv(y_U)
sig_z_pert = np.array([[0.9, 0.1],[-0.1, -0.9]])
z_pert_vals, z_pert_U = np.linalg.eig(sig_z_pert)
z_pert_U_dag = np.linalg.inv(z_pert_U)

z_p = np.array([1,0],dtype=complex)
z_m = np.array([0,1],dtype=complex)
x_p = np.array([1,1],dtype=complex) * (1/np.sqrt(2))
x_m = np.array([1,-1],dtype=complex) * (1/np.sqrt(2))
y_p = np.array([1,1j],dtype=complex) * (1/np.sqrt(2))
y_m = np.array([1,-1j],dtype=complex) * (1/np.sqrt(2))


def prop_sig_x(dt):
    prop_diag = np.diag(np.exp(-1j * dt * x_vals))
    return np.dot(x_U, np.dot(prop_diag, x_U_dag))

def prop_sig_y(dt):
    prop_diag = np.diag(np.exp(-1j * dt * y_vals))
    return np.dot(y_U, np.dot(prop_diag, y_U_dag))

def prop_sig_z(dt):
    prop_diag = np.diag(np.exp(-1j * dt * z_vals))
    return np.dot(z_U, np.dot(prop_diag, z_U_dag))

def prop_gen(dt, basis):
    # Make our propogator
    if basis == "x":
        propogator = prop_sig_x(dt)
    elif basis == "y":
        propogator = prop_sig_y(dt)
    elif basis == "z":
        propogator = prop_sig_z(dt)
    return propogator

def prop_sig_z_pert(dt):
    prop_diag = np.diag(np.exp(-1j * dt * z_pert_vals))
    return np.dot(z_pert_U, np.dot(prop_diag, z_pert_U_dag))

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



class simple(Scene):
    def construct(self):
        # Set up our scene, axes, and constants
        n = 2
        ax_range = 2
        self.add(ThreeDAxes(
            x_range=[-ax_range, ax_range, 1],
            y_range=[-ax_range, ax_range, 1],
            z_range=[-ax_range, ax_range, 1],
            x_length=ax_range,
            y_length=ax_range,
            z_length=ax_range,
        ))


        # The vector for our math
        vec = np.empty((2,), dtype=complex)
        vec[0] = 1 + 1j
        vec[1] = 1 - 1j

        testvec = Vector().set_color(RED).set_points_by_ends(ORIGIN,ORIGIN + (np.imag(vec[0]) * UP))
        self.add(testvec)

        # number = DecimalNumber(self.time)
        number = ValueTracker(0)
        number2 = ValueTracker(0)
        numbers=[number,number2]
        # always(
        #     number.set_value,
        #     self.time
        # )
        # number.add_updater(
        #     lambda n: n.set_value(self.time)
        # )
        # testvec.add_updater(
        #     lambda v: v.set_points_by_ends(ORIGIN, UP * np.cos(number.get_value()))
        # )
        # testtest = always_redraw(
        #     Text,
        #     str(self.time)
        # )
        text1 = always_redraw(
            Text,
            "num1"
        )
        text2 = always_redraw(
            Text,
            "num2"
        )

        # testtest = Text(
        #     str(number.get_value())
        # )

        text1.add_updater(
            lambda t: t.set_x(numbers[0].get_value(),ORIGIN)
        )
        text2.add_updater(
            lambda t: t.set_x(numbers[1].get_value(), ORIGIN)
        )
        self.add(text1)
        self.add(text2)
        testarray = np.array([[1, 2], [3, 4]])
        testarray2 = np.array([[0, 0], [0, 0]])
        #self.play(number.animate.set_value(testarray[0][0]))
        # anim_list = [numbers[0].animate.set_value(testarray[0][0]),
        #              numbers[1].animate.set_value(testarray[1][1])]
        def auto_play():
            args = []
            for i in np.arange(2):
                args.append(numbers[i].animate.set_value(testarray[i][i]))
            self.play(*args)
        # def return_anims():
        #     for i in np.arange(len(numbers)):
        #         return numbers[i].animate.set_value(testarray[i][i])
        auto_play()
        # testarray = testarray*0
        # auto_play()
        # for i in np.arange(2):
        #     for j in np.arange(2):
        #         self.play(number.animate.set_value(testarray[i][j]))

        testvec= Vector().set_color(WHITE)
        testvec.add_updater(
            lambda v: v.set_points_by_ends(ORIGIN, ORIGIN + (abs(vec[0]) * OUT))
        )

class complex3(Scene):
    def construct(self):
        n = 2
        ax_range = 2
        origins = [None] * n
        for i in np.arange(n):
            origins[i] = (i - (n / 2)) * UP * 3 * ax_range

        axes = [None] * n
        for i in np.arange(n):
            axes[i] = ThreeDAxes(
                x_range=[-ax_range, ax_range, 1],
                y_range=[-ax_range, ax_range, 1],
                z_range=[-ax_range, ax_range, 1],
                x_length=ax_range,
                y_length=ax_range,
                z_length=ax_range,
            ).move_to(origins[i])
        for i in np.arange(n):
            self.add(axes[i])

        vec = np.empty((2,), dtype=complex)
        vec[0] = 1 + 1j
        vec[1] = 1 - 1j
        vec_tracker = [
            ComplexValueTracker(vec[0]),
            ComplexValueTracker(vec[1])
        ]

class complex(Scene):
    def construct(self):
        # Set up our scene, axes, and constants
        n = 2
        ax_range = 2
        tracker1 = ValueTracker()
        # tracker2 = ValueTracker().add_updater(
        #     lambda t: t.set_value(self.time)
        # )
        tracker2 = DecimalNumber()
        f_always(
            tracker2.set_value,
            self.get_time
        )

        origins = [None] * n
        for i in np.arange(n):
            origins[i] = (i - (n/2)) * UP * 3 * ax_range

        axes = [None] * n
        for i in np.arange(n):
            axes[i] = ThreeDAxes(
                    x_range=[-ax_range, ax_range, 1],
                    y_range=[-ax_range, ax_range, 1],
                    z_range=[-ax_range, ax_range, 1],
                    x_length=ax_range,
                    y_length=ax_range,
                    z_length=ax_range,
                ).move_to(origins[i])
        for i in np.arange(n):
            self.add(axes[i])

        # The vector for our math
        vec = np.empty((2,), dtype=complex)
        vec[0] = 1 + 1j
        vec[1] = 1 - 1j

        # List of lists for [Re,Im,Mod] of each vector component
        vec_comps = [None] * n
        # 0 for Real, 1 for Im, 2 for mod
        for i in np.arange(n):
            vec_comps[i] = [
                always_redraw(
                    lambda: Vector().set_color(BLUE).set_points_by_ends(origins[i],
                                                                origins[i] + (np.cos(tracker2.get_value()) * RIGHT))
                ),
                Vector().set_color(RED).set_points_by_ends(origins[i],
                                                            origins[i] + (np.imag(vec[i]) * UP)),
                Vector().set_color(WHITE).set_points_by_ends(origins[i],
                                                            origins[i] + (abs(vec[i]) * OUT))
            ]
        for i in np.arange(n):
            for j in np.arange(len(vec_comps[i])):
                self.add(vec_comps[i][j])

        # tracker2.add_updater(
        #     lambda t: t.set_value(self.time)
        # )
        # vec_comps[0][0].add_updater(
        #     lambda v: v.set_points_by_ends(
        #         origins[0], origins[0] + (RIGHT * np.cos(tracker2.get_value()))
        #     )
        # )

class complex2(Scene):
    def construct(self):
        # Set up our scene, axes, and constants
        n = 2
        ax_range = 2

        origins = [None] * n
        for i in np.arange(n):
            origins[i] = (i - (n / 2)) * UP * 3 * ax_range

        axes = [None] * n
        for i in np.arange(n):
            axes[i] = ThreeDAxes(
                x_range=[-ax_range, ax_range, 1],
                y_range=[-ax_range, ax_range, 1],
                z_range=[-ax_range, ax_range, 1],
                x_length=ax_range,
                y_length=ax_range,
                z_length=ax_range,
            ).move_to(origins[i])
        for i in np.arange(n):
            self.add(axes[i])

        # The vector for our math
        vec_i = np.empty((2,), dtype=complex)
        vec_i[0] = 1 + 1j
        vec_i[1] = 1 - 1j
        vec = vec_i
        # vec = np.dot(vec_i, np.cos(self.time)*np.array([[1, 0], [0, 1]], dtype=complex))
        # vec = np.dot(vec_i,np.array([[np.cos(self.time),1],[1,1]],dtype=complex))
        tracker = ComplexValueTracker(
            np.cos(self.time)
        )
        tracker.add_updater(
            lambda t: t.set_value(t.get_value())
        )
        # tracker = ComplexValueTracker(
        #     np.real(np.dot(vec_i, np.cos(self.time)*np.array([[1, 0], [0, 1]], dtype=complex))[0])
        # )

        # List of lists for [Re,Im,Mod] of each vector component
        vec_comps = [None] * n
        # 0 for Real, 1 for Im, 2 for mod
        for i in np.arange(n):
            vec_comps[i] = [
                Vector().set_color(BLUE).set_points_by_ends(origins[i],
                                                            origins[i] + (np.real(vec[i]) * RIGHT)),
                Vector().set_color(RED).set_points_by_ends(origins[i],
                                                           origins[i] + (np.imag(vec[i]) * UP)),
                Vector().set_color(WHITE).set_points_by_ends(origins[i],
                                                             origins[i] + (abs(vec[i]) * OUT))
            ]

        always(
            vec_comps[0][0].set_points_by_ends,
            origins[0],
            origins[0] + (tracker.get_value() * RIGHT)
        )
        # vec_comps[0][0].add_updater(
        #     lambda v: v.set_points_by_ends(origins[0],
        #                                    origins[0] + (tracker.get_value() * RIGHT))
        # )
        vec_comps[0][1].add_updater(
            lambda v: v.set_points_by_ends(origins[0],
                                           origins[0] + (np.imag(vec[0]) * UP))
        )
        vec_comps[0][2].add_updater(
            lambda v: v.set_points_by_ends(origins[0],
                                           origins[0] + (abs(vec[0]) * OUT))
        )
        vec_comps[1][0].add_updater(
            lambda v: v.set_points_by_ends(origins[1],
                                           origins[1] + (np.real(vec[1]) * RIGHT))
        )
        vec_comps[1][1].add_updater(
            lambda v: v.set_points_by_ends(origins[1],
                                           origins[1] + (np.imag(vec[1]) * UP))
        )
        vec_comps[1][2].add_updater(
            lambda v: v.set_points_by_ends(origins[1],
                                           origins[1] + (abs(vec[1]) * OUT))
        )
        for i in np.arange(n):
            for j in np.arange(len(vec_comps[i])):
                self.add(vec_comps[i][j])

class complex1(Scene):
    def construct(self):
        # Set up our scene, axes, and constants
        n = 2
        ax_range = 2

        origins = [None] * n
        for i in np.arange(n):
            origins[i] = (i - (n/2)) * UP * 3 * ax_range

        axes = [None] * n
        for i in np.arange(n):
            axes[i] = ThreeDAxes(
                    x_range=[-ax_range, ax_range, 1],
                    y_range=[-ax_range, ax_range, 1],
                    z_range=[-ax_range, ax_range, 1],
                    x_length=ax_range,
                    y_length=ax_range,
                    z_length=ax_range,
                ).move_to(origins[i])
        for i in np.arange(n):
            self.add(axes[i])

        # The vector for our math
        vec = np.empty((2,), dtype=complex)
        vec[0] = 1 + 1j
        vec[1] = 1 - 1j

        # List of lists for [Re,Im,Mod] of each vector component
        vec_comps = [None] * n
        # 0 for Real, 1 for Im, 2 for mod
        for i in np.arange(n):
            vec_comps[i] = [
                Vector().set_color(BLUE).set_points_by_ends(origins[i],
                                                            origins[i] + (np.real(vec[i]) * RIGHT)),
                Vector().set_color(RED).set_points_by_ends(origins[i],
                                                            origins[i] + (np.imag(vec[i]) * UP)),
                Vector().set_color(WHITE).set_points_by_ends(origins[i],
                                                            origins[i] + (abs(vec[i]) * OUT))
            ]
        # for i in np.arange(n):
        #     origin = origins[i]
        #     vec_comps[i][0].add_updater(
        #         lambda v: v.set_points_by_ends(origin,
        #                                        origin + (np.real(vec[i]) * RIGHT))
        #     )
        #     vec_comps[i][1].add_updater(
        #         lambda v: v.set_points_by_ends(origin,
        #                                        origin + (np.imag(vec[i]) * UP))
        #     )
        #     vec_comps[i][2].add_updater(
        #         lambda v: v.set_points_by_ends(origin,
        #                                        origin + (abs(vec[i]) * OUT))
        #     )

        vec_comps[0][0].add_updater(
            lambda v: v.set_points_by_ends(origins[0],
                                           origins[0] + (np.real(vec[0]) * RIGHT))
        )
        vec_comps[0][1].add_updater(
            lambda v: v.set_points_by_ends(origins[0],
                                           origins[0] + (np.imag(vec[0]) * UP))
        )
        vec_comps[0][2].add_updater(
            lambda v: v.set_points_by_ends(origins[0],
                                           origins[0] + (abs(vec[0]) * OUT))
        )
        vec_comps[1][0].add_updater(
            lambda v: v.set_points_by_ends(origins[1],
                                           origins[1] + (np.real(vec[1]) * RIGHT))
        )
        vec_comps[1][1].add_updater(
            lambda v: v.set_points_by_ends(origins[1],
                                           origins[1] + (np.imag(vec[1]) * UP))
        )
        vec_comps[1][2].add_updater(
            lambda v: v.set_points_by_ends(origins[1],
                                           origins[1] + (abs(vec[1]) * OUT))
        )





        # for i in np.arange(n):
        #     vec_comps[i][0].add_updater(
        #         lambda v: v.set_points_by_ends(origins[i],
        #                                        origins[i] + (np.real(vec[i]) * RIGHT))
        #     )
        #     vec_comps[i][1].add_updater(
        #         lambda v: v.set_points_by_ends(origins[i],
        #                                        origins[i] + (np.imag(vec[i]) * UP))
        #     )
        #     vec_comps[i][2].add_updater(
        #         lambda v: v.set_points_by_ends(origins[i],
        #                                        origins[i] + (abs(vec[i]) * OUT))
        #     )
        # for i in np.arange(n):
        #     vec_comps[i] = [
        #         Vector().set_color(BLUE).add_updater(
        #             lambda v: v.set_points_by_ends(origins[i], origins[i] + (np.real(vec[i]) * RIGHT))
        #         ),
        #         Vector().set_color(RED).add_updater(
        #             lambda v: v.set_points_by_ends(origins[i], origins[i] + (np.imag(vec[i]) * UP))
        #         ),
        #         Vector().set_color(WHITE).add_updater(
        #             lambda v: v.set_points_by_ends(origins[i], origins[i] + (abs(vec[i]) * OUT))
        #         )
        #     ]
        # Add the vectors in vec_comps
        for i in np.arange(n):
            for j in np.arange(len(vec_comps[i])):
                self.add(vec_comps[i][j])

        # self.add(Text(str(origins[0])).move_to(origins[0]))
        # self.add(Text(str(vec_comps)).move_to(origins[0]))
        # self.add(vec_comps[0][0])
        # vec_comps[0][0].add_updater(
        #     lambda v: v.shift(RIGHT*self.time/10)
        # )
        # self.add(Vector().set_color(BLUE).add_updater(
        #             lambda v: v.set_points_by_ends(origins[0], origins[0] + (np.real(vec[0]) * RIGHT))
        #         ))

class test(Scene):
    def construct(self):
        axes3d = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=5,
            y_length=5,
            z_length=5,
        )
        self.add(axes3d)
        UpArrow = Arrow(ORIGIN, UP)
        UpArrow.set_color(RED)
        RightLine = Line3D(ORIGIN,RIGHT)
        RightLine.set_color(BLUE)
        OutVecter = Vector(OUT)
        OutVecter.add_updater
        OutVecter.set_color(GREEN)
        self.add(UpArrow)
        self.add(RightLine)
        self.add(OutVecter)
        always(
            OutVecter.rotate,
            DEGREES, axis=UP, about_point=ORIGIN
        )
        testext = Tex("\hat{H}").set_color(RED).scale(3)
        storeheight = testext.get_height()
        testext.rotate(PI/2,RIGHT).set_coord(storeheight/2,2)
        # testext = Text("Hi").set_color(RED)
        self.add(testext)
        freq = 10.0
        testext.add_updater(
            lambda t: t.shift((RIGHT/20)*np.cos(self.time*freq))
        )
        # testext.add_updater(
        #     lambda t: t.move_to(OutVecter)
        # )

        # ham = Tex("H").scale(2)
        # ham.set_color(BLUE)
        #
        # hamgraph = axes3d.get_x_axis_label(ham).scale(2)
        # hamgraph.set_color(RED)
        # # self.add(hamgraph)
        # # hamgraph.add_updater(
        # #     lambda h: h.move_to(OutVecter)
        # # )
        # # self.add(ham)
        # # ham.add_updater(
        # #     lambda h: h.move_to(OutVecter)
        # # )
        # self.play(ShowCreation(ham))
        # self.play(ShowCreation(hamgraph))
        # self.add(hamgraph)
        # hamgraph.add_updater(
        #     lambda h: h.rotate(DEGREES,OUT)
        # )
        # self.add(ham)
        # ham.add_updater(
        #     lambda h: h.rotate(DEGREES, OUT)
        # )
        # axesRe = ThreeDAxes(
        #     x_range=[-2, 2, 1],
        #     y_range=[-2, 2, 1],
        #     z_range=[-2, 2, 1],
        #     x_length=2,
        #     y_length=2,
        #     z_length=2,
        # )
        # axesIm = ThreeDAxes(
        #     x_range=[-2, 2, 1],
        #     y_range=[-2, 2, 1],
        #     z_range=[-2, 2, 1],
        #     x_length=2,
        #     y_length=2,
        #     z_length=2,
        # )
        #
        # im_origin = np.array((5., 0., 0.))
        # im_origin_pt = Point(im_origin)
        # axesIm.move_to(im_origin_pt)
        # axesIm.set_color(RED)
        #
        # self.add(axesIm)
        # # axesIm.add_updater(
        # #     lambda a: a.shift(RIGHT/50)
        # # )
        # self.add(axesRe)
        # z_p = Vector(OUT)
        # UpArrow = Arrow(ORIGIN, UP)
        # UpArrowIm = Arrow(im_origin, im_origin + UP)
        # UpArrowIm.set_color(WHITE)
        # self.add(UpArrowIm)
        # UpArrow.set_color(RED)
        # RightLine = Line3D(ORIGIN, RIGHT)
        # RightLine.set_color(BLUE)
        # OutVecter = Vector(OUT)
        # OutVecterIm = Vector(OUT)
        # OutVecterIm.move_to(im_origin_pt).shift(+OUT / 2)
        # self.add(OutVecterIm)
        # OutVecter.set_color(GREEN)
        # self.add(UpArrow)
        # self.add(RightLine)
        # self.add(OutVecter)
        # # always(
        # #     OutVecter.rotate,
        # #     DEGREES, axis=UP, about_point=ORIGIN
        # # )

class movie(Scene):
    def construct(self):

        axesRe = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=2,
            y_length=2,
            z_length=2,
        )
        axesIm = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=2,
            y_length=2,
            z_length=2,
        )

        im_origin = np.array((5.,0.,0.))
        im_origin_pt = Point(im_origin)
        axesIm.move_to(im_origin_pt)
        axesRe.set_color(BLUE)
        axesIm.set_color(RED)

        self.add(axesIm)
        self.add(axesRe)


        z_im = Vector(UP).move_to(im_origin_pt).shift(UP/2)
        z_re = Vector(UP)
        x_im = Vector(RIGHT).move_to(im_origin_pt).shift(RIGHT/2)
        x_re = Vector(RIGHT)
        self.add(z_im)
        z_im.add_updater(
            lambda z: z.set_points_by_ends(im_origin,-(UP)*np.sin(self.time)+im_origin)
        )
        self.add(z_re)
        z_re.add_updater(
            lambda z: z.set_points_by_ends(ORIGIN, (UP) * np.cos(self.time))
        )
        self.add(x_im)
        x_im.add_updater(
            lambda z: z.set_points_by_ends(im_origin, (RIGHT) * np.sin(self.time) + im_origin)
        )
        self.add(x_re)
        x_re.add_updater(
            lambda z: z.set_points_by_ends(ORIGIN, (RIGHT) * np.cos(self.time))
        )

        sum_re=Vector(UP+RIGHT).set_color(GREEN)
        self.add(sum_re)
        sum_re.add_updater(
            lambda z: z.set_points_by_ends(ORIGIN, (UP+RIGHT) * np.cos(self.time) + OUT*np.cos(self.time*10))
        )

        # always(
        #     OutVecter.rotate,
        #     DEGREES, axis=UP, about_point=ORIGIN
        # )
        # OutVecter = Vector(OUT)
        # OutVecterIm = Vector(OUT)
        # OutVecterIm.move_to(im_origin_pt).shift(+OUT / 2)
        # OutVecter.set_color(GREEN)

