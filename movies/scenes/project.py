from movies.scenes.dysphoria import *
from ref.hold_constants import *
import copy

class Intro(Scene):
    def construct(self):
        psi_pure = Tex("\\psi").scale(2)
        electron = ImageMobject("imgs/electron.png").scale(1/3).shift(RIGHT*3).shift(UP*2)
        spring = ImageMobject("imgs/spring.png").scale(1 / 3).shift(RIGHT * 3).shift(DOWN * 2)
        self.add(psi_pure)
        self.play(FadeIn(electron),FadeIn(spring))

        psi_vector_form = Matrix(
            [["5"],["2"],["9.6"],["0"],["3+2i"],["..."]]
        )
        self.play(FadeOut(psi_pure),FadeIn(psi_vector_form))

        psi_ket = Tex("\\ket{", "\\psi}").scale(2)
        self.play(FadeOut(psi_vector_form), FadeIn(psi_ket))
        self.play(FadeOut(electron),FadeOut(spring))
        psi_ket_t0 = Tex("\\ket{", "\\psi", "(t_0)}").scale(2)
        self.play(TransformMatchingTex(psi_ket,psi_ket_t0,
                                       key_map={
                                           psi_ket[0]:psi_ket_t0[0],
                                           psi_ket[1]: psi_ket_t0[1]
                                       }))
        question = Tex("\\ket{\\psi(t)}", "\stackrel{?}{\longleftarrow}", "\\ket{", "\\psi", "(t_0)}").scale(2)
        self.play(psi_ket_t0.animate.move_to(question[3]))
        self.play(TransformMatchingTex(psi_ket_t0, question,
                                       key_map={
                                           psi_ket_t0[0]: question[2],
                                           psi_ket_t0[1]: question[3]
                                       }))
        hamiltonian = Tex("\\hat{H}").scale(10).set_opacity(0.2).set_color(RED).shift(UP)
        self.play(FadeIn(hamiltonian),run_time=2)
        self.play(FadeOut(question),FadeOut(hamiltonian))

class Evolution(Scene):
    def construct(self):
        # # with our Hamiltonian of course!
        C = Tex("\\hat{H}")
        C.set_color(RED)
        C.scale(9)
        self.play(Write(C))
        self.play(ScaleInPlace(C, (1 / 9)))

        # # But what does the Hamiltonian even do?
        D = Tex("\\hat{H}", "|", "\\psi", "\\rangle")
        # Here we can see that we can act on our submobjects as if they are just elements in a list
        D[0].shift(LEFT)
        D[1].shift(RIGHT)
        D[2].shift(RIGHT)
        D[3].shift(RIGHT)

        E = Tex("\\hat{H}",
                "|",
                "\\psi",
                "\\rangle")
        self.play(TransformMatchingTex(C, D))
        self.play(TransformMatchingTex(D, E))
        F = Tex("i\\hbar",
                "|",
                "\\dot{\\psi}",
                "\\rangle")

        # Couldn't find a good accelerating func in the rate_func library
        def accelerate(t, acc=3):
            return t ** acc

        # # In place transformation to emphasize H acting on psi as an action, rather than an equality
        self.play(E[0].animate.shift(LEFT / 2),
                  # The rate_fun and run_time are incredibly useful control kobs for making animations look prettier
                  rate_func=exponential_decay,
                  run_time=1.4)
        self.play(E[0].animate.shift(RIGHT / 2),
                  rate_func=accelerate,
                  run_time=0.5)
        self.play(TransformMatchingTex(E, F,
                                       # These key maps will come up a lot in this code. The TransformMatchingTex is
                                       # okay at translating matching characters between LaTeX expressions, but you'll
                                       # need a key map to tell the function which submobjects map to which submobjects
                                       key_map={
                                           E[0]: F[0],
                                           E[1]: F[1],
                                           E[2]: F[2],
                                           E[3]: F[3],
                                       }),
                  run_time=0.2)
        self.play(WiggleOutThenIn(F, scale_value=1.0, n_wiggles=2),
                  rate_func=exponential_decay, run_time=3)
        G = Tex("i\\hbar",
                "|",
                "\\dot{\\psi}",
                "\\rangle",
                "=",
                "\\hat{H}",
                "|",
                "\\psi",
                "\\rangle")

        # # Summarizing action to tie into familiar vernacular
        self.play(TransformMatchingTex(F, G,
                                       key_map={
                                           F[0]: G[0],
                                           F[1]: G[1],
                                           F[2]: G[2],
                                           F[3]: G[3],
                                       }
                                       ))
        H = Tex("|",
                "\\dot{\\psi}",
                "\\rangle",
                "=",
                "\\frac{1}{i\\hbar}",
                "\\hat{H}",
                "|",
                "\\psi",
                "\\rangle")

        # Explicit rearranging of Schrödinger eqn
        self.play(TransformMatchingTex(G, H,
                                       key_map={
                                           G[1]: H[0],
                                           G[2]: H[1],
                                           G[3]: H[2],
                                           G[4]: H[3],
                                           G[0]: H[4],
                                           G[5]: H[5],
                                           G[6]: H[6],
                                           G[7]: H[7],
                                           G[8]: H[8],
                                       }
                                       )
                  )

        I = Tex("|",
                "\\dot{\\psi}",
                "\\rangle",
                "=",
                "-\\frac{i}{",
                "\\hbar}",
                "\\hat{H}",
                "|",
                "\\psi",
                "\\rangle")
        self.play(TransformMatchingTex(H, I,
                                       key_map={
                                           H[0]: I[0],
                                           H[1]: I[1],
                                           H[2]: I[2],
                                           H[3]: I[3],
                                           H[4]: I[4],
                                           H[4]: I[5],
                                           H[5]: I[6],
                                           H[6]: I[7],
                                           H[7]: I[8],
                                           H[8]: I[9],
                                       }
                                       )
                  )

        # # inserting time dependence into our expression
        J = Tex("|",
                "\\dot{\\psi}",
                "(t)",
                "\\rangle",
                "=",
                "-\\frac{i}{",
                "\\hbar}",
                "\\hat{H}",
                "|",
                "\\psi ",
                "(t)",
                "\\rangle")
        # of course we can change the color of specific substrings! Very useful for color coding
        J[2].set_color(RED)
        J[10].set_color(RED)
        self.play(TransformMatchingTex(I, J,
                                       key_map={
                                           I[0]: J[0],
                                           I[1]: J[1],
                                           I[2]: J[3],
                                           I[3]: J[4],
                                           I[4]: J[5],
                                           I[5]: J[6],
                                           I[6]: J[7],
                                           I[7]: J[8],
                                           I[8]: J[9],
                                           I[9]: J[11]
                                       }
                                       )
                  )
        # We can animate the color change live for dramatic effect
        self.play(J[2].animate.set_color(WHITE), J[10].animate.set_color(WHITE))

        # The four lines after this comment are my current best attempt at "restructuring" a TeX object for
        # more convenient use. Jn will be illustrated identically to J, so its addition will be invisible to the viewer.
        # The FadeOut animation for some reason is the only "delete" function that actually does anything without
        # being overtly obnoxious about it.
        Jn = Tex("|\\dot{\\psi}(t)\\rangle",
                 "=",
                 "-\\frac{i}{\\hbar}\\hat{H}",
                 "|\\psi(t)\\rangle")
        self.add(Jn)
        self.play(FadeOut(J))

        # After many a trial and error, I have realized that in order to illustrate the TeX object, the program
        # will ruthlessly concatenate each string. ie, don't forget spaces where they're needed or you'll punch a
        # hole in your wall.
        Ansatz = Tex("\\dot{f}(t)",
                     "=",
                     "C",
                     "f(t)",
                     "\\longrightarrow ",
                     "f(t)",
                     "=",
                     " e^{",
                     "C",
                     "t",
                     "} ",
                     " f(t_0) ")
        Ansatz.shift(UP * 2)
        Ansatz.set_color(BLUE)

        # Insert the 1st order dif eq ansatz to skip a few steps and reinforce pattern recognition
        self.play(Write(Ansatz), run_time=1)

        Ansatz[0].set_color(ORANGE)
        Jn[0].set_color(ORANGE)
        self.play(Indicate(Ansatz[0], color=ORANGE), Indicate(Jn[0], color=ORANGE))
        # I'm keep this code below commented out just to make an example of it. I tell it to simultaneously
        # change color and do the little indication, and it chooses to completely forego the color change.
        # How pathetic.
        # self.play(Ansatz[0].animate.set_color(ORANGE),Jn[0].animate.set_color(ORANGE),
        #           Indicate(Ansatz[0]),Indicate(Jn[0]))
        Ansatz[2].set_color(PINK)
        Jn[2].set_color(PINK)
        self.play(Indicate(Ansatz[2], color=PINK), Indicate(Jn[2], color=PINK))
        Ansatz[3].set_color(GREEN)
        Jn[3].set_color(GREEN)
        self.play(Indicate(Ansatz[3], color=GREEN), Indicate(Jn[3], color=GREEN))

        # Expressing how our ansatz solution translates to our case
        K = Tex("|\\dot{\\psi}(t)\\rangle ",
                "=",
                "-\\frac{i}{\\hbar}\\hat{H} ",
                "|\\psi(t)\\rangle ",
                "\\longrightarrow ",
                "|\\psi(t)\\rangle ",
                "= ",
                "e^{",
                "-\\frac{i}{\\hbar}\\hat{H}",
                "t",
                "} ",
                "|\\psi(t_0)\\rangle ")
        K[0].set_color(ORANGE)
        K[2].set_color(PINK)
        K[3].set_color(GREEN)

        self.play(TransformMatchingTex(Jn, K,
                                       key_map={
                                           Jn[0]: K[0],
                                           Jn[1]: K[1],
                                           Jn[2]: K[2],
                                           Jn[3]: K[3],
                                       }
                                       ))
        self.play(K.animate.set_color(WHITE), Ansatz.animate.set_color(BLUE))

        Ansatz[5].set_color(GREEN)
        K[5].set_color(GREEN)
        self.play(Indicate(Ansatz[5], color=GREEN), Indicate(K[5], color=GREEN))
        Ansatz[8].set_color(PINK)
        K[8].set_color(PINK)
        self.play(Indicate(Ansatz[8], color=PINK), Indicate(K[8], color=PINK))
        Ansatz[9].set_color(YELLOW)
        K[9].set_color(YELLOW)
        self.play(Indicate(Ansatz[9], color=YELLOW), Indicate(K[9], color=YELLOW))
        Ansatz[10].set_color(RED)
        K[10].set_color(RED)
        self.play(Indicate(Ansatz[10], color=RED), Indicate(K[10], color=RED))

        Kn = Tex("|\\dot{\\psi}(t)\\rangle = -\\frac{i}{\\hbar}\\hat{H} |\\psi(t)\\rangle \\longrightarrow  ",
                 "|\\psi(t)\\rangle = e^{-\\frac{i}{\\hbar}\\hat{H} t} |\\psi(t_0)\\rangle ")

        self.play(FadeOut(Ansatz))

        self.play(K.animate.set_color(WHITE))
        self.add(Kn)
        self.play(FadeOut(K), run_time=0.1)
        self.play(FadeOut(Kn[0]))
        self.play(Kn[1].center)
        # self.play(ApplyWave(Kn[1]))

        L = Tex("|\\psi(t)\\rangle =",
                "e^{-\\frac{i}{\\hbar}\\hat{H} t}",
                "|\\psi(t_0)\\rangle ")
        L0c = L[0].get_center()
        L2c = L[2].get_center()
        self.add(L)
        self.play(FadeOut(Kn[1]))

        # Multiple iterations of a quick ApplyWave function to give a little "Shimmer"
        # # Our exponential friend has a secret identity!
        self.play(ApplyWave(L[1], direction=np.array((1.0, 1.0, 0.0)), time_width=0.2, amplitude=0.01), run_time=0.1)
        self.play(ApplyWave(L[1], direction=np.array((1.0, 1.0, 0.0)), time_width=0.2, amplitude=0.06), run_time=0.2)
        self.play(ApplyWave(L[1], direction=np.array((1.0, 1.0, 0.0)), time_width=0.2, amplitude=0.1), run_time=0.3)

        # Rotating e^{...} halfway along the UP axis to give a flat stanley state for a sort of seamless transition into
        # a different Tex expression
        self.play(
            Rotate(
                L[1],
                angle=PI / 2,
                axis=UP
            )
        )
        M = Tex("|\\psi(t)\\rangle =",
                "U(t,t_0)",
                "|\\psi(t_0)\\rangle ")
        # explicitly moving around new Tex expression to match positions of old Tex expressions
        M[0].move_to(L0c)
        M[2].move_to(L2c)

        # prepping our new U(t,t_0) into the same flat stanley state
        M[1].rotate(PI / 2, UP)

        self.add(M)
        self.play(FadeOut(L),
                  Rotate(M[1], angle=-PI / 2, axis=UP))
        self.play(FadeOut(M[0]), FadeOut(M[2]), M[1].center)
        # # Look at our new operator!
        self.play(Flash(M[1], flash_radius=1))
        self.play(FadeInFromPoint(M[2], RIGHT_SIDE))

        # Storing some helps posns for later
        m1center = M[1].get_center()
        m2width = M[2].get_width()
        m2right = M[2].get_right()
        m2left = M[2].get_left()
        m2width = M[2].get_width()

        # This will be our path for an upcoming animation
        moveline = Line(m1center, m1center + LEFT)
        # Keeping this function since its a useful reference way to specify which axis should be stretching
        # M[2].set_width(m2width, stretch=True)

        # storing the old state of this string for an easy revert animation
        M[2].save_state()

        # # U(t,t_0) pulling on psi(t_0)
        # These next few animations is my FAVORITE part of this code.
        self.play(MoveAlongPath(M[1], moveline), ApplyPointwiseFunction(
            # This "lambda point: ..." is a way of feeding in a function to another function
            # the first "point" establishes what we're calling the input variable in our lambda function
            lambda point: ((point - m2right) / m2width) * RIGHT + point, M[2]
        ), run_time=2)

        O = Tex("|\\psi ",
                "(t",
                "_0",
                ")",
                "\\rangle ")
        O.move_to(M[2])

        self.play(FadeOut(M[1]), Restore(M[2]), run_time=0.2)
        self.add(O)
        self.play(FadeOut(M[2]), FadeOut(O[2], run_time=0.2), WiggleOutThenIn(O, scale_value=1.0, n_wiggles=3),
                  rate_func=exponential_decay)
        # explicitly setting O[2] to transparent, since the TransformMatchingTex function will otherwise make our
        # faded out component reappear.
        O[2].set_opacity(0)
        On = Tex("|\\psi ",
                 "(t",
                 ")",
                 "\\rangle ")
        # # Our t_0 constant is now our chosen end point t!
        self.play(TransformMatchingTex(O, On,
                                       key_map={
                                           O[0]: On[0],
                                           O[1]: On[1],
                                           O[3]: On[2],
                                           O[4]: On[3]
                                       }
                                       )
                  )
        self.play(FadeOut(On))
        P = Tex("U(t,t_0)",
                "\\langle \\psi (t_0)|")

        # # So now starting with our psi at t_0, we can quickly use U(t,t_0) to act on psi and "pull" it from
        # # t_0 to t!
        # self.play(FadeIn(P[1]))
        # self.play(FadeInFromPoint(P[0], LEFT_SIDE))
        #
        # p0center = P[0].get_center()
        # p1right = P[1].get_right()
        # p1width = P[1].get_width()
        # moveline = Line(p0center, p0center + (LEFT / 2))
        # P.save_state()

class HSeesWho1(Scene):
    def construct(self):

        scale = .7
        pup_radius = scale/2
        eye_width = scale*2
        eye_height = scale*4
        char_scale = scale*5

        # ######################
        # eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        # eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        # pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
        #     eye_white_left.get_right()+pup_radius*LEFT)
        # pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
        #     eye_white_right.get_right() + pup_radius * LEFT)
        # h_eye_left = VGroup(eye_white_left, pupil_left).shift(LEFT*eye_width)
        # h_eye_right = VGroup(eye_white_right, pupil_right).shift(RIGHT*eye_width)
        # eyes = VGroup(h_eye_left,h_eye_right).scale(1/5).shift(RIGHT*.1)
        # H = Tex("\\hat{U}").set_color(GREY_B).scale(char_scale)
        # H_guy = VGroup(H,eyes)
        # ######################

        H_guyy = lilGuy(text = Tex("\\hat{U}"))
        H_guy = H_guyy.lilguy

        ######################
        eye_white_left_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left_white_ket = Circle(radius=pup_radius,color=BLACK,fill_opacity=1).move_to(
            eye_white_left_white_ket.get_left() + pup_radius * RIGHT)
        pupil_right_white_ket = Circle(radius=pup_radius,color=BLACK,fill_opacity=1).move_to(
            eye_white_right_white_ket.get_left() + pup_radius * RIGHT)
        h_eye_left_white_ket = VGroup(eye_white_left_white_ket,pupil_left_white_ket).shift(LEFT * eye_width)
        h_eye_right_white_ket = VGroup(eye_white_right_white_ket,pupil_right_white_ket).shift(RIGHT * eye_width)
        eyes = VGroup(h_eye_left_white_ket, h_eye_right_white_ket).scale(1 / 5).shift(LEFT * .1)
        Psi_white = Tex("\\ket{\\psi}").set_color(GREY_B).scale(char_scale)
        Psi_white_guy = VGroup(Psi_white, eyes)
        ######################


        H_guy.shift(LEFT*8)
        Psi_white_guy.shift(RIGHT*4)
        self.play(FadeIn(Psi_white_guy),FadeIn(H_guy))
        # self.add(Psi_white_guy,H_guy)
        self.play(H_guy.animate.shift(RIGHT*6),run_time=3)
        self.play(H_guy[1][0][1].animate.shift(LEFT*H_guy[1][0][1].get_width()),
                  H_guy[1][1][1].animate.shift(LEFT*H_guy[1][1][1].get_width()),
                  run_time=0.6)
        self.play(H_guy[1][0][1].animate.shift((UP + RIGHT/2) * H_guy[1][0][1].get_width()),
                  H_guy[1][1][1].animate.shift((UP + RIGHT/2) * H_guy[1][1][1].get_width()),
                  run_time=1.1)
        self.play(H_guy[1][0][1].animate.shift(DOWN * 2 * H_guy[1][0][1].get_width()),
                  H_guy[1][1][1].animate.shift(DOWN * 2 * H_guy[1][1][1].get_width()),
                  run_time=1.4)
        self.play(Psi_white_guy[1][0][1].animate.shift((DOWN + RIGHT / 2) * Psi_white_guy[1][0][1].get_width()),
                  Psi_white_guy[1][1][1].animate.shift((DOWN + RIGHT / 2) * Psi_white_guy[1][1][1].get_width()),
                  run_time=0.4)
        self.play(H_guy.animate.shift(UP*2.3),Psi_white_guy.animate.shift(UP*2.3))
        self.play(H_guy.animate.set_opacity(0.3),Psi_white_guy.animate.set_opacity(0.3))

        ######################
        hmem1_eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        hmem1_eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        hmem1_pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            hmem1_eye_white_left.get_right() + pup_radius * LEFT)
        hmem1_pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            hmem1_eye_white_right.get_right() + pup_radius * LEFT)
        hmem1_h_eye_left = VGroup(hmem1_eye_white_left, hmem1_pupil_left).shift(LEFT * eye_width)
        hmem1_h_eye_right = VGroup(hmem1_eye_white_right, hmem1_pupil_right).shift(RIGHT * eye_width)
        eyes = VGroup(hmem1_h_eye_left, hmem1_h_eye_right).scale(1 / 5).shift(RIGHT * .1)
        hmem1 = Tex("\\hat{H}").set_color(GREY_B).scale(char_scale)
        hmem1_guy = VGroup(hmem1, eyes)
        ######################

        ######################
        eye_white_left_red_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right_red_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left_red_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left_red_ket.get_left() + pup_radius * RIGHT)
        pupil_right_red_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right_red_ket.get_left() + pup_radius * RIGHT)
        h_eye_left_red_ket = VGroup(eye_white_left_red_ket, pupil_left_red_ket).shift(LEFT * eye_width)
        h_eye_right_red_ket = VGroup(eye_white_right_red_ket, pupil_right_red_ket).shift(RIGHT * eye_width)
        eyes = VGroup(h_eye_left_red_ket, h_eye_right_red_ket).scale(1 / 5).shift(LEFT * .1)
        Psi_red = Tex("\\ket{\\psi}").set_color(hex_red).scale(char_scale)
        Psi_red_guy = VGroup(Psi_red, eyes)
        ######################

        hmem1_guy.shift(LEFT * 8)
        Psi_red_guy.shift(RIGHT * 4)
        self.add(Psi_red_guy, hmem1_guy)
        self.play(hmem1_guy.animate.shift(RIGHT*6),run_time = 3, rate_func=exponential_decay)

        self.play(hmem1_guy.animate.move_to(Psi_red_guy.get_center_of_mass() + LEFT*scale*2),run_time = 0.4)
        red_child = Circle(radius=eye_width/4,color = hex_red, fill_opacity=1).move_to(
            hmem1_guy.get_bottom()+(UP*eye_width/4))
        self.play(FadeOut(hmem1_guy),FadeIn(red_child),run_time = 0.2)

        self.play(WiggleOutThenIn(Psi_red_guy, scale_value=1.0, n_wiggles=2),
                  rate_func=exponential_decay, run_time=1)
        self.play(Psi_red_guy[1][0][1].animate.shift(DOWN * Psi_red_guy[1][0][1].get_width()),
                  Psi_red_guy[1][1][1].animate.shift(DOWN * Psi_red_guy[1][0][1].get_width()))
        self.play(Psi_red_guy[1][0][1].animate.shift(UP*Psi_red_guy[1][0][1].get_width()),
                  Psi_red_guy[1][1][1].animate.shift(UP*Psi_red_guy[1][0][1].get_width()),
                  red_child.animate.shift(UP*Psi_red_guy.get_height()/4))
        self.play(Psi_red_guy[1][0][1].animate.shift(RIGHT * Psi_red_guy[1][0][1].get_width()/2),
                  Psi_red_guy[1][1][1].animate.shift(RIGHT * Psi_red_guy[1][0][1].get_width()/2),
                  run_time=2)

        ######################


        self.play(FadeOut(red_child),FadeOut(Psi_red_guy),
                  H_guy.animate.set_opacity(1),
                  Psi_white_guy.animate.set_opacity(1))
        self.play(H_guy[1][0][1].animate.shift((UP + RIGHT / 2) * H_guy[1][0][1].get_width()),
                  H_guy[1][1][1].animate.shift((UP + RIGHT / 2) * H_guy[1][1][1].get_width()),
                  Psi_white_guy[1][0][1].animate.shift((UP + LEFT / 2) * Psi_white_guy[1][0][1].get_width()),
                  Psi_white_guy[1][1][1].animate.shift((UP + LEFT / 2) * Psi_white_guy[1][1][1].get_width()),
                  run_time=1.1)
        self.play(H_guy[1][0][1].animate.shift((DOWN + LEFT / 2) * H_guy[1][0][1].get_width()),
                  H_guy[1][1][1].animate.shift((DOWN + LEFT / 2) * H_guy[1][1][1].get_width()),
                  Psi_white_guy[1][0][1].animate.shift((DOWN + RIGHT / 2) * Psi_white_guy[1][0][1].get_width()),
                  Psi_white_guy[1][1][1].animate.shift((DOWN + RIGHT / 2) * Psi_white_guy[1][1][1].get_width()),
                  run_time=1.1)
        self.play(H_guy.animate.set_opacity(0.5),
                  Psi_white_guy.animate.set_opacity(0.5))

        ######################
        hmem2_eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        hmem2_eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        hmem2_pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            hmem2_eye_white_left.get_right() + pup_radius * LEFT)
        hmem2_pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            hmem2_eye_white_right.get_right() + pup_radius * LEFT)
        hmem2_h_eye_left = VGroup(hmem2_eye_white_left, hmem2_pupil_left).shift(LEFT * eye_width)
        hmem2_h_eye_right = VGroup(hmem2_eye_white_right, hmem2_pupil_right).shift(RIGHT * eye_width)
        eyes = VGroup(hmem2_h_eye_left, hmem2_h_eye_right).scale(1 / 5).shift(RIGHT * .1)
        hmem2 = Tex("\\hat{H}").set_color(GREY_B).scale(char_scale)
        hmem2_guy = VGroup(hmem2, eyes)
        ######################

        ######################
        eye_white_left_blue_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right_blue_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left_blue_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left_blue_ket.get_left() + pup_radius * RIGHT)
        pupil_right_blue_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right_blue_ket.get_left() + pup_radius * RIGHT)
        h_eye_left_blue_ket = VGroup(eye_white_left_blue_ket, pupil_left_blue_ket).shift(LEFT * eye_width)
        h_eye_right_blue_ket = VGroup(eye_white_right_blue_ket, pupil_right_blue_ket).shift(RIGHT * eye_width)
        eyes = VGroup(h_eye_left_blue_ket, h_eye_right_blue_ket).scale(1 / 5).shift(LEFT * .1)
        Psi_blue = Tex("\\ket{\\psi}").set_color(hex_blue).scale(char_scale)
        Psi_blue_guy = VGroup(Psi_blue, eyes)
        ######################

        hmem2_guy.shift(LEFT * 8)
        Psi_blue_guy.shift(RIGHT * 4)
        self.add(Psi_blue_guy, hmem2_guy)
        self.play(hmem2_guy.animate.shift(RIGHT * 6), run_time=1, rate_func=exponential_decay)

        self.play(hmem2_guy.animate.move_to(Psi_blue_guy.get_center_of_mass() + LEFT * scale * 2), run_time=0.4)
        blue_child = Circle(radius=eye_width / 4, color=hex_blue, fill_opacity=1).move_to(
            hmem2_guy.get_bottom() + (UP * eye_width / 4))
        self.play(FadeOut(hmem2_guy), FadeIn(blue_child), run_time=0.2)

        self.play(WiggleOutThenIn(Psi_blue_guy, scale_value=1.0, n_wiggles=2),
                  rate_func=exponential_decay, run_time=0.5)
        self.play(Psi_blue_guy[1][0][1].animate.shift(DOWN * Psi_blue_guy[1][0][1].get_width()),
                  Psi_blue_guy[1][1][1].animate.shift(DOWN * Psi_blue_guy[1][0][1].get_width()),
                  run_time=0.5)
        self.play(Psi_blue_guy[1][0][1].animate.shift(UP * Psi_blue_guy[1][0][1].get_width()),
                  Psi_blue_guy[1][1][1].animate.shift(UP * Psi_blue_guy[1][0][1].get_width()),
                  blue_child.animate.shift(UP * Psi_blue_guy.get_height() / 4),
                  run_time=0.5)
        self.play(FadeOut(blue_child), FadeOut(Psi_blue_guy))

        ######################
        hmem3_eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        hmem3_eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        hmem3_pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            hmem3_eye_white_left.get_right() + pup_radius * LEFT)
        hmem3_pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            hmem3_eye_white_right.get_right() + pup_radius * LEFT)
        hmem3_h_eye_left = VGroup(hmem3_eye_white_left, hmem3_pupil_left).shift(LEFT * eye_width)
        hmem3_h_eye_right = VGroup(hmem3_eye_white_right, hmem3_pupil_right).shift(RIGHT * eye_width)
        eyes = VGroup(hmem3_h_eye_left, hmem3_h_eye_right).scale(1 / 5).shift(RIGHT * .1)
        hmem3 = Tex("\\hat{H}").set_color(GREY_B).scale(char_scale)
        hmem3_guy = VGroup(hmem3, eyes)
        ######################

        ######################
        eye_white_left_yellow_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right_yellow_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left_yellow_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left_yellow_ket.get_left() + pup_radius * RIGHT)
        pupil_right_yellow_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right_yellow_ket.get_left() + pup_radius * RIGHT)
        h_eye_left_yellow_ket = VGroup(eye_white_left_yellow_ket, pupil_left_yellow_ket).shift(LEFT * eye_width)
        h_eye_right_yellow_ket = VGroup(eye_white_right_yellow_ket, pupil_right_yellow_ket).shift(RIGHT * eye_width)
        eyes = VGroup(h_eye_left_yellow_ket, h_eye_right_yellow_ket).scale(1 / 5).shift(LEFT * .1)
        Psi_yellow = Tex("\\ket{\\psi}").set_color(hex_green).scale(char_scale)
        Psi_yellow_guy = VGroup(Psi_yellow, eyes)
        ######################

        hmem3_guy.shift(LEFT * 8)
        Psi_yellow_guy.shift(RIGHT * 4)
        self.add(Psi_yellow_guy, hmem3_guy)
        self.play(hmem3_guy.animate.shift(RIGHT * 6), run_time=0.5, rate_func=exponential_decay)

        self.play(hmem3_guy.animate.move_to(Psi_yellow_guy.get_center_of_mass() + LEFT * scale * 2), run_time=0.2)
        yellow_child = Circle(radius=eye_width / 4, color=hex_green, fill_opacity=1).move_to(
            hmem3_guy.get_bottom() + (UP * eye_width / 4))
        self.play(FadeOut(hmem3_guy), FadeIn(yellow_child), run_time=0.1)

        self.play(WiggleOutThenIn(Psi_yellow_guy, scale_value=1.0, n_wiggles=2),
                  rate_func=exponential_decay, run_time=0.25)
        self.play(Psi_yellow_guy[1][0][1].animate.shift(DOWN * Psi_yellow_guy[1][0][1].get_width()),
                  Psi_yellow_guy[1][1][1].animate.shift(DOWN * Psi_yellow_guy[1][0][1].get_width()),
                  run_time=0.25)
        self.play(Psi_yellow_guy[1][0][1].animate.shift(UP * Psi_yellow_guy[1][0][1].get_width()),
                  Psi_yellow_guy[1][1][1].animate.shift(UP * Psi_yellow_guy[1][0][1].get_width()),
                  yellow_child.animate.shift(UP * Psi_yellow_guy.get_height() / 4),
                  run_time=0.25)
        self.play(FadeOut(yellow_child), FadeOut(Psi_yellow_guy))

class HSeesWho2(Scene):
    def construct(self):
        scale = .7
        pup_radius = scale / 2
        eye_width = scale * 2
        eye_height = scale * 4
        char_scale = scale * 5

        ######################
        eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left.get_right() + pup_radius * LEFT)
        pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right.get_right() + pup_radius * LEFT)
        h_eye_left = VGroup(eye_white_left, pupil_left).shift(LEFT * eye_width)
        h_eye_right = VGroup(eye_white_right, pupil_right).shift(RIGHT * eye_width)
        h_eyes = VGroup(h_eye_left, h_eye_right).scale(1 / 5).shift(RIGHT * .1)
        H = Tex("\\hat{U}").set_color(GREY_B).scale(char_scale)
        H_guy = VGroup(H, h_eyes)
        ######################

        ######################
        eye_white_left_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left_white_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left_white_ket.get_left() + pup_radius * RIGHT)
        pupil_right_white_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right_white_ket.get_left() + pup_radius * RIGHT)
        eye_left_white_ket = VGroup(eye_white_left_white_ket, pupil_left_white_ket).shift(LEFT * eye_width)
        eye_right_white_ket = VGroup(eye_white_right_white_ket, pupil_right_white_ket).shift(RIGHT * eye_width)
        psi_eyes = VGroup(eye_left_white_ket, eye_right_white_ket).scale(1 / 5).shift(LEFT * .1)
        Psi_white = Tex("\\ket{\\psi}").set_color(GREY_B).scale(char_scale)
        Psi_white_guy = VGroup(Psi_white, psi_eyes)
        ######################

        # Restablishing scene from HSeesWho1
        H_guy.shift(LEFT * 2)
        Psi_white_guy.shift(RIGHT * 4)
        H_guy[1][0][1].shift((DOWN + LEFT / 2) * H_guy[1][0][1].get_width())
        H_guy[1][1][1].shift((DOWN + LEFT / 2) * H_guy[1][1][1].get_width())
        Psi_white_guy[1][0][1].shift((DOWN + RIGHT / 2) * Psi_white_guy[1][0][1].get_width()),
        Psi_white_guy[1][1][1].shift((DOWN + RIGHT / 2) * Psi_white_guy[1][1][1].get_width())
        H_guy.shift(UP * 2.3)
        Psi_white_guy.shift(UP * 2.3)
        H_guy.set_opacity(0.3)
        Psi_white_guy.set_opacity(0.3)
        self.add(Psi_white_guy, H_guy)
        ######################
        ##### NEW SCENE #####
        ######################
        mem1eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left.get_right() + pup_radius * LEFT)
        mem1pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right.get_right() + pup_radius * LEFT)
        mem1h_eye_left = VGroup(mem1eye_white_left, mem1pupil_left).shift(LEFT * eye_width)
        mem1h_eye_right = VGroup(mem1eye_white_right, mem1pupil_right).shift(RIGHT * eye_width)
        mem1h_eyes = VGroup(mem1h_eye_left, mem1h_eye_right).scale(1 / 5).shift(RIGHT * .1)
        mem1H = Tex("\\hat{H}").set_color(GREY_B).scale(char_scale)
        mem1H_guy = VGroup(mem1H, mem1h_eyes)
        ######################

        ######################
        mem1eye_white_left_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_white_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_white_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_white_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_white_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_white_ket = VGroup(mem1eye_white_left_white_ket, mem1pupil_left_white_ket).shift(LEFT * eye_width)
        mem1eye_right_white_ket = VGroup(mem1eye_white_right_white_ket, mem1pupil_right_white_ket).shift(RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_white_ket, mem1eye_right_white_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_white = Tex("\\ket{\\psi}").set_color(GREY_B).scale(char_scale)
        mem1Psi_white_guy = VGroup(mem1Psi_white, mem1psi_eyes)
        ######################

        mem1H_guy.shift(LEFT * 2)
        mem1Psi_white_guy.shift(RIGHT * 4)
        self.play(FadeIn(mem1Psi_white_guy),
                  FadeIn(mem1H_guy))
        # self.add(mem1Psi_white_guy, mem1H_guy)


        ######################
        mem1eye_white_left_blue_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_blue_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_blue_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_blue_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_blue_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_blue_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_blue_ket = VGroup(mem1eye_white_left_blue_ket, mem1pupil_left_blue_ket).shift(LEFT * eye_width)
        mem1eye_right_blue_ket = VGroup(mem1eye_white_right_blue_ket, mem1pupil_right_blue_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_blue_ket, mem1eye_right_blue_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_blue = Tex("\\ket{\\psi}").set_color(hex_blue).scale(char_scale)
        mem1Psi_blue_guy = VGroup(mem1Psi_blue, mem1psi_eyes)
        ######################

        ######################
        mem1eye_white_left_red_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_red_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_red_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_red_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_red_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_red_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_red_ket = VGroup(mem1eye_white_left_red_ket, mem1pupil_left_red_ket).shift(LEFT * eye_width)
        mem1eye_right_red_ket = VGroup(mem1eye_white_right_red_ket, mem1pupil_right_red_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_red_ket, mem1eye_right_red_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_red = Tex("\\ket{\\psi}").set_color(hex_red).scale(char_scale)
        mem1Psi_red_guy = VGroup(mem1Psi_red, mem1psi_eyes)
        ######################

        ######################
        mem1eye_white_left_yellow_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_yellow_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_yellow_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_yellow_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_yellow_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_yellow_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_yellow_ket = VGroup(mem1eye_white_left_yellow_ket, mem1pupil_left_yellow_ket).shift(LEFT * eye_width)
        mem1eye_right_yellow_ket = VGroup(mem1eye_white_right_yellow_ket, mem1pupil_right_yellow_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_yellow_ket, mem1eye_right_yellow_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_yellow = Tex("\\ket{\\psi}").set_color(hex_green).scale(char_scale)
        mem1Psi_yellow_guy = VGroup(mem1Psi_yellow, mem1psi_eyes)
        ######################

        ######################
        mem1Psi_red_guy.scale(1 / 2).move_to(mem1Psi_white_guy.get_center())
        mem1Psi_yellow_guy.scale(1 / 4).move_to(mem1Psi_white_guy.get_center())
        mem1Psi_blue_guy.scale(1 / 4).move_to(mem1Psi_white_guy)
        # mem1Psi_red_guy.shift(mem1Psi_white_guy.get_height()*UP / 2)
        mem1Psi_yellow_guy.shift(mem1Psi_white_guy.get_height() * DOWN / 3)
        mem1Psi_blue_guy.shift(mem1Psi_white_guy.get_height() * DOWN / 2)

        self.play(FadeOut(mem1Psi_white_guy),
                  FadeIn(mem1Psi_red_guy),
                  FadeIn(mem1Psi_yellow_guy),
                  FadeIn(mem1Psi_blue_guy))

        self.play(mem1H_guy.animate.shift(scale * RIGHT * 6))



        mem1red_child = Circle(radius = mem1Psi_red_guy.get_width()/6,
                               color = hex_red,
                               fill_opacity = 1.0).move_to(mem1Psi_red_guy.get_bottom())
        mem1red_child.shift(
            (LEFT*mem1Psi_red_guy.get_width()/(1.4)) +
            (UP * mem1red_child.get_height()/2))
        mem1yellow_child = Circle(radius=mem1Psi_yellow_guy.get_width()/6,
                               color=hex_green,
                               fill_opacity=1.0).move_to(mem1Psi_yellow_guy.get_bottom())
        mem1yellow_child.shift(
            (LEFT * mem1Psi_yellow_guy.get_width() / (1.4)) +
            (UP * mem1yellow_child.get_height() / 2))
        mem1blue_child = Circle(radius=mem1Psi_blue_guy.get_width()/6,
                               color=hex_blue,
                               fill_opacity=1.0).move_to(mem1Psi_blue_guy.get_bottom())
        mem1blue_child.shift(
            (LEFT * mem1Psi_blue_guy.get_width() / (1.4)) +
            (UP * mem1blue_child.get_height() / 2))

        self.play(FadeOut(mem1H_guy),
                  FadeIn(mem1yellow_child),
                  FadeIn(mem1red_child),
                  FadeIn(mem1blue_child))
        self.add(mem1red_child,mem1yellow_child,mem1blue_child)

        mustache = ImageMobject("imgs/mustache.png").move_to(mem1Psi_white_guy[1]).scale(1/7)
        mustache.shift((DOWN*mem1Psi_white_guy[1].get_height()/2))
        bluehair = ImageMobject("imgs/bluestreakhair.png").move_to(mem1Psi_white_guy[1]).scale(1)
        bluehair.shift((DOWN * mem1Psi_white_guy[1].get_height() / 1.4)
                       #+(LEFT * mem1Psi_white_guy[1].get_width()/7)
                       )

        self.play(FadeIn(mem1Psi_white_guy),
                  FadeIn(mustache),
                  # FadeIn(bluehair),
                  FadeOut(mem1yellow_child),
                  FadeOut(mem1red_child),
                  FadeOut(mem1blue_child),
                  FadeOut(mem1Psi_red_guy),
                  FadeOut(mem1Psi_yellow_guy),
                  FadeOut(mem1Psi_blue_guy)
                  )

        mem1H_guy.shift(LEFT*4)
        mem1Psi_red_guy.scale(1/2).shift(UP*mem1Psi_white_guy.get_height()/4)
        mem1Psi_blue_guy.scale(1).shift(DOWN*mem1Psi_white_guy.get_height()/4)
        mem1Psi_yellow_guy.scale(2)
        self.play(FadeIn(mem1H_guy))
        self.play(FadeOut(mem1Psi_white_guy),
                  FadeOut(mustache),
                  FadeIn(mem1Psi_red_guy),
                  FadeIn(mem1Psi_yellow_guy),
                  FadeIn(mem1Psi_blue_guy))

        mem1red_child = Circle(radius=mem1Psi_red_guy.get_width() / 6,
                               color=hex_red,
                               fill_opacity=1.0).move_to(mem1Psi_red_guy.get_bottom())
        mem1red_child.shift(
            (LEFT * mem1Psi_red_guy.get_width() / (1.4)) +
            (UP * mem1red_child.get_height() / 2))
        mem1yellow_child = Circle(radius=mem1Psi_yellow_guy.get_width() / 6,
                                  color=hex_green,
                                  fill_opacity=1.0).move_to(mem1Psi_yellow_guy.get_bottom())
        mem1yellow_child.shift(
            (LEFT * mem1Psi_yellow_guy.get_width() / (1.4)) +
            (UP * mem1yellow_child.get_height() / 2))
        mem1blue_child = Circle(radius=mem1Psi_blue_guy.get_width() / 6,
                                color=hex_blue,
                                fill_opacity=1.0).move_to(mem1Psi_blue_guy.get_bottom())
        mem1blue_child.shift(
            (LEFT * mem1Psi_blue_guy.get_width() / (1.4)) +
            (UP * mem1blue_child.get_height() / 2))

        self.play(mem1H_guy.animate.shift(RIGHT * 4))

        self.play(FadeOut(mem1H_guy),
                  FadeIn(mem1yellow_child),
                  FadeIn(mem1red_child),
                  FadeIn(mem1blue_child))

        self.play(FadeIn(mem1Psi_white_guy),
                  # FadeIn(mustache),
                  FadeIn(bluehair),
                  FadeOut(mem1yellow_child),
                  FadeOut(mem1red_child),
                  FadeOut(mem1blue_child),
                  FadeOut(mem1Psi_red_guy),
                  FadeOut(mem1Psi_yellow_guy),
                  FadeOut(mem1Psi_blue_guy)
                  )

        self.play(FadeOut(mem1Psi_white_guy),
                  FadeOut(bluehair),
                  H_guy.animate.set_opacity(1),
                  Psi_white_guy.animate.set_opacity(1))

        self.play(
            H_guy.animate.shift(DOWN * 2.3),
            Psi_white_guy.animate.shift(DOWN * 2.3)
        )

        self.play(
            H_guy[1][0][1].animate.shift((UP + RIGHT / 2) * H_guy[1][0][1].get_width()),
            H_guy[1][1][1].animate.shift((UP + RIGHT / 2) * H_guy[1][1][1].get_width()),
            Psi_white_guy[1][0][1].animate.shift((UP + LEFT / 2) * Psi_white_guy[1][0][1].get_width()),
            Psi_white_guy[1][1][1].animate.shift((UP + LEFT / 2) * Psi_white_guy[1][1][1].get_width()),
            run_time = 0.3
        )

        self.play(
            H_guy.animate.move_to(Psi_white_guy.get_center() + LEFT*Psi_white_guy.get_width()),
            Psi_white_guy[1][0][1].animate.shift((RIGHT / 2) * Psi_white_guy[1][0][1].get_width()),
            Psi_white_guy[1][1][1].animate.shift((RIGHT / 2) * Psi_white_guy[1][1][1].get_width()),
            run_time = 1.1,
            rate_func = lambda t: t**3
        )

class SpikyShowoff(Scene):
    def construct(self):
        spiky_env = SpikyVector(False,3,1,blue)
        spiky_env.vec_draw[0][0].set_color(WHITE)
        spiky_env.vec_draw[0][1].set_color(WHITE)
        spiky_env.vec_draw[0][2].set_color(hex_red)
        spiky_env.vec_draw[1][0].set_color(WHITE)
        spiky_env.vec_draw[1][1].set_color(WHITE)
        spiky_env.vec_draw[1][2].set_color(hex_green)
        spiky_env.vec_draw[2][0].set_color(WHITE)
        spiky_env.vec_draw[2][1].set_color(WHITE)
        spiky_env.vec_draw[2][2].set_color(hex_blue)

        ######################
        scale = .7
        pup_radius = scale / 2
        eye_width = scale * 2
        eye_height = scale * 4
        char_scale = scale * 5
        eye_white_left_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left_white_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left_white_ket.get_left() + pup_radius * RIGHT)
        pupil_right_white_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right_white_ket.get_left() + pup_radius * RIGHT)
        eye_left_white_ket = VGroup(eye_white_left_white_ket, pupil_left_white_ket).shift(LEFT * eye_width)
        eye_right_white_ket = VGroup(eye_white_right_white_ket, pupil_right_white_ket).shift(RIGHT * eye_width)
        psi_eyes = VGroup(eye_left_white_ket, eye_right_white_ket).scale(1 / 5).shift(LEFT * .1)
        Psi_white = Tex("\\ket{\\psi}").set_color(GREY_B).scale(char_scale)
        Psi_white_guy = VGroup(Psi_white, psi_eyes)
        ######################

        Psi_white_guy.scale(3)
        self.play(FadeIn(Psi_white_guy))

        frame_theta = ValueTracker(0)
        frame_phi = ValueTracker(0)

        # frame_theta = ValueTracker(-30)
        # frame_phi = ValueTracker(60)
        # frame_gamma = ValueTracker(0)
        self.camera.frame.add_updater(
            lambda f: f.set_euler_angles(theta=frame_theta.get_value(),
                                         phi=frame_phi.get_value(),
                                         units=DEGREES)
        )
        self.play(
            frame_theta.animate.set_value(-30),
            frame_phi.animate.set_value(60)
        )

        def fade_in(list):
            args = []
            for i in np.arange(len(list)):
                args.append(FadeIn(list[i]))
            return args

        self.play(
            FadeOut(Psi_white_guy),
            *fade_in(spiky_env.axes),
            *fade_in(spiky_env.brackets),
            *fade_in(spiky_env.give_vec())
        )

        ######################
        mem1eye_white_left_blue_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_blue_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_blue_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_blue_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_blue_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_blue_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_blue_ket = VGroup(mem1eye_white_left_blue_ket, mem1pupil_left_blue_ket).shift(LEFT * eye_width)
        mem1eye_right_blue_ket = VGroup(mem1eye_white_right_blue_ket, mem1pupil_right_blue_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_blue_ket, mem1eye_right_blue_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_blue = Tex("\\ket{\\psi}").set_color(hex_blue).scale(char_scale)
        mem1Psi_blue_guy = VGroup(mem1Psi_blue, mem1psi_eyes)
        ######################

        ######################
        mem1eye_white_left_red_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_red_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_red_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_red_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_red_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_red_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_red_ket = VGroup(mem1eye_white_left_red_ket, mem1pupil_left_red_ket).shift(LEFT * eye_width)
        mem1eye_right_red_ket = VGroup(mem1eye_white_right_red_ket, mem1pupil_right_red_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_red_ket, mem1eye_right_red_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_red = Tex("\\ket{\\psi}").set_color(hex_red).scale(char_scale)
        mem1Psi_red_guy = VGroup(mem1Psi_red, mem1psi_eyes)
        ######################

        ######################
        mem1eye_white_left_yellow_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_yellow_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_yellow_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_yellow_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_yellow_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_yellow_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_yellow_ket = VGroup(mem1eye_white_left_yellow_ket, mem1pupil_left_yellow_ket).shift(
            LEFT * eye_width)
        mem1eye_right_yellow_ket = VGroup(mem1eye_white_right_yellow_ket, mem1pupil_right_yellow_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_yellow_ket, mem1eye_right_yellow_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_yellow = Tex("\\ket{\\psi}").set_color(hex_green).scale(char_scale)
        mem1Psi_yellow_guy = VGroup(mem1Psi_yellow, mem1psi_eyes)
        ######################

        mem1Psi_red_guy.move_to(spiky_env.origins[0]).shift(RIGHT*3)
        mem1Psi_yellow_guy.move_to(spiky_env.origins[1]).shift(RIGHT * 3)
        mem1Psi_blue_guy.move_to(spiky_env.origins[2]).shift(RIGHT * 3)

        self.play(FadeIn(mem1Psi_red_guy),
                  FadeIn(mem1Psi_yellow_guy),
                  FadeIn(mem1Psi_blue_guy))

        self.play(
            self.camera.frame.animate.move_to(spiky_env.origins[2]),
            frame_theta.animate.set_value(0),
            frame_phi.animate.set_value(0)
        )
        self.play(self.camera.frame.animate.shift(IN * 5))

        real = Text("Real").move_to(spiky_env.origins[2]).shift(RIGHT*1.1).scale(1/2).set_color(GREY_B).shift(OUT/10).rotate(-90*DEGREES)
        imaginary = Text("Imaginary").move_to(spiky_env.origins[2]).shift(UP*1.1).scale(1/2).set_color(GREY_B).shift(OUT/10)

        complex_guy = DecimalNumber().add_updater(
            lambda d: d.set_value(spiky_env.vec_track[2][0].get_value()+
                                  spiky_env.vec_track[2][1].get_value()*1j)
        ).move_to(spiky_env.origins[2]).shift(LEFT * 2.2).scale(1/2)
        z = Tex("\\cdot", " = ").move_to(complex_guy).shift(LEFT*1.3)
        z[0].set_color(hex_blue).scale(4).shift(LEFT*0.2)
        mod_guy = DecimalNumber().add_updater(
            lambda d: d.set_value(spiky_env.vec_track[2][2].get_value())
        ).move_to(complex_guy).shift(DOWN).scale(1 / 2)
        zmod = Tex("|", "\\cdot", "| = ").move_to(mod_guy).shift(LEFT)
        zmod[1].set_color(hex_blue).scale(3)


        self.add(real, imaginary,complex_guy,z)
        self.wait()

        spiky_env.vec = np.dot(im_blue,spiky_env.vec)
        self.play(*spiky_env.tracker_set_vals())
        self.wait()
        spiky_env.vec = np.dot(im_blue, spiky_env.vec)
        self.play(*spiky_env.tracker_set_vals())
        self.wait()
        spiky_env.vec = np.dot(im_blue, spiky_env.vec)
        self.play(*spiky_env.tracker_set_vals())
        self.wait()
        spiky_env.vec = np.dot(im_blue, spiky_env.vec)
        self.play(*spiky_env.tracker_set_vals())
        self.wait()

        self.play(
            self.camera.frame.animate.move_to(spiky_env.origins[2]),
            frame_theta.animate.set_value(-30),
            frame_phi.animate.set_value(60)
        )

        self.play(FadeIn(mod_guy),
                  FadeIn(zmod))

        spiky_env.vec = np.dot(im_blue, spiky_env.vec)
        self.play(*spiky_env.tracker_set_vals())
        spiky_env.vec = np.dot(im_blue, spiky_env.vec)
        self.play(*spiky_env.tracker_set_vals())
        spiky_env.vec = np.dot(im_blue, spiky_env.vec)
        self.play(*spiky_env.tracker_set_vals())
        spiky_env.vec = np.dot(im_blue, spiky_env.vec)
        self.play(*spiky_env.tracker_set_vals())

        spiky_env.vec = blue

        self.play(FadeOut(real),FadeOut(imaginary),FadeOut(complex_guy),FadeOut(mod_guy),FadeOut(z),FadeOut(zmod),
                  self.camera.frame.animate.move_to(spiky_env.origins[1]),
                  *spiky_env.tracker_set_vals(),
                  frame_theta.animate.set_value(0),
                  frame_phi.animate.set_value(0)
                  )

        ######################
        eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left.get_right() + pup_radius * LEFT)
        pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right.get_right() + pup_radius * LEFT)
        h_eye_left = VGroup(eye_white_left, pupil_left).shift(LEFT * eye_width)
        h_eye_right = VGroup(eye_white_right, pupil_right).shift(RIGHT * eye_width)
        h_eyes = VGroup(h_eye_left, h_eye_right).scale(1 / 5).shift(RIGHT * .1)
        H = Tex("\\hat{U}").set_color(GREY_B).scale(char_scale)
        H_guy = VGroup(H, h_eyes)
        ######################

        H_guy.move_to(spiky_env.origins[1]).shift(LEFT*6).scale(2)
        self.add(H_guy)
        self.play(H_guy.animate.shift(RIGHT*2))

        H_guy1 = copy.deepcopy(H_guy).move_to(H_guy).shift(LEFT*1).set_opacity(0.8).shift(IN*1)
        H_guy2 = copy.deepcopy(H_guy).move_to(H_guy).shift(LEFT*2).set_opacity(0.5).shift(IN*2)
        H_guy3 = copy.deepcopy(H_guy).move_to(H_guy).shift(LEFT*3).set_opacity(0.2).shift(IN*3)
        more_H = []
        more_H.append(H_guy1)
        more_H.append(H_guy2)
        more_H.append(H_guy3)

        self.play(FadeIn(more_H[0]),run_time=1)
        self.play(FadeIn(more_H[1]), run_time=0.7)
        self.play(FadeIn(more_H[2]), run_time=0.4)

        sample_evolver = create_evolver(sample_H,0.5)
        spiky_env.vec = np.dot(sample_evolver,spiky_env.vec)

        self.play(
            FadeOut(H_guy),
            *spiky_env.tracker_set_vals()
        )
        move_H_guys = []
        for i in np.arange(len(more_H)):
            move_H_guys.append(more_H[i].animate.shift(RIGHT+OUT))
        # H_guy1.set_opacity[1.0]
        # H_guy2.set_opacity[0.8]
        # H_guy3.set_opacity[0.5]
        self.play(*move_H_guys)

        spiky_env.vec = np.dot(sample_evolver, spiky_env.vec)
        self.play(
            FadeOut(H_guy1),
            *spiky_env.tracker_set_vals()
        )
        move_H_guys1 = []
        for i in np.arange(len(more_H)-1):
            move_H_guys1.append(more_H[i+1].animate.shift(RIGHT + OUT))
        self.play(*move_H_guys1)



        spiky_env.vec = np.dot(sample_evolver, spiky_env.vec)
        self.play(
            FadeOut(H_guy2),
            *spiky_env.tracker_set_vals()
        )
        move_H_guys2 = []
        for i in np.arange(len(more_H)-2):
            move_H_guys2.append(more_H[i+2].animate.shift(RIGHT + OUT))
        self.play(*move_H_guys2)






        spiky_env.vec = np.dot(sample_evolver, spiky_env.vec)
        self.play(
            FadeOut(H_guy3),
            *spiky_env.tracker_set_vals()
        )

        ######################
        eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left.get_right() + pup_radius * LEFT)
        pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right.get_right() + pup_radius * LEFT)
        h_eye_left = VGroup(eye_white_left, pupil_left).shift(LEFT * eye_width)
        h_eye_right = VGroup(eye_white_right, pupil_right).shift(RIGHT * eye_width)
        h_eyes = VGroup(h_eye_left, h_eye_right).scale(1 / 5).shift(RIGHT * .1)
        H = Tex("\\hat{H}").set_color(GREY_B).scale(char_scale)
        H_guyy = VGroup(H, h_eyes)
        ######################


        H_guyy.move_to(spiky_env.origins[1]).shift(LEFT * 5).scale(2)


        self.play(
            self.camera.frame.animate.shift(OUT*5),
            FadeIn(H_guyy)
        )



        dt_1 = 0.1
        steps = 50
        sample_evolver_1 = create_evolver(sample_H, dt_1)
        for i in np.arange(steps):
            spiky_env.vec = np.dot(sample_evolver_1, spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),run_time=dt_1)

        self.play(
            self.camera.frame.animate.move_to(spiky_env.origins[1]),
            frame_theta.animate.set_value(-30),
            frame_phi.animate.set_value(60)
        )




        self.camera.frame.clear_updaters()

class SpikyShowoff2(Scene):
    def construct(self):
        spiky_env = SpikyVector(False,3,1,blue)
        spiky_env.vec_draw[0][0].set_color(WHITE)
        spiky_env.vec_draw[0][1].set_color(WHITE)
        spiky_env.vec_draw[0][2].set_color(hex_red)
        spiky_env.vec_draw[1][0].set_color(WHITE)
        spiky_env.vec_draw[1][1].set_color(WHITE)
        spiky_env.vec_draw[1][2].set_color(hex_green)
        spiky_env.vec_draw[2][0].set_color(WHITE)
        spiky_env.vec_draw[2][1].set_color(WHITE)
        spiky_env.vec_draw[2][2].set_color(hex_blue)

        ######################
        scale = .7
        pup_radius = scale / 2
        eye_width = scale * 2
        eye_height = scale * 4
        char_scale = scale * 5
        eye_white_left_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left_white_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left_white_ket.get_left() + pup_radius * RIGHT)
        pupil_right_white_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right_white_ket.get_left() + pup_radius * RIGHT)
        eye_left_white_ket = VGroup(eye_white_left_white_ket, pupil_left_white_ket).shift(LEFT * eye_width)
        eye_right_white_ket = VGroup(eye_white_right_white_ket, pupil_right_white_ket).shift(RIGHT * eye_width)
        psi_eyes = VGroup(eye_left_white_ket, eye_right_white_ket).scale(1 / 5).shift(LEFT * .1)
        Psi_white = Tex("\\ket{\\psi}").set_color(GREY_B).scale(char_scale)
        Psi_white_guy = VGroup(Psi_white, psi_eyes)
        ######################
        frame_theta = ValueTracker(-30)
        frame_phi = ValueTracker(60)

        self.camera.frame.add_updater(
            lambda f: f.set_euler_angles(theta=frame_theta.get_value(),
                                         phi=frame_phi.get_value(),
                                         units=DEGREES)
        )


        self.add(*spiky_env.axes,*spiky_env.brackets,*spiky_env.give_vec())

        ######################
        mem1eye_white_left_blue_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_blue_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_blue_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_blue_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_blue_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_blue_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_blue_ket = VGroup(mem1eye_white_left_blue_ket, mem1pupil_left_blue_ket).shift(LEFT * eye_width)
        mem1eye_right_blue_ket = VGroup(mem1eye_white_right_blue_ket, mem1pupil_right_blue_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_blue_ket, mem1eye_right_blue_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_blue = Tex("\\ket{\\psi}").set_color(hex_blue).scale(char_scale)
        mem1Psi_blue_guy = VGroup(mem1Psi_blue, mem1psi_eyes)
        ######################

        ######################
        mem1eye_white_left_red_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_red_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_red_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_red_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_red_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_red_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_red_ket = VGroup(mem1eye_white_left_red_ket, mem1pupil_left_red_ket).shift(LEFT * eye_width)
        mem1eye_right_red_ket = VGroup(mem1eye_white_right_red_ket, mem1pupil_right_red_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_red_ket, mem1eye_right_red_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_red = Tex("\\ket{\\psi}").set_color(hex_red).scale(char_scale)
        mem1Psi_red_guy = VGroup(mem1Psi_red, mem1psi_eyes)
        ######################

        ######################
        mem1eye_white_left_yellow_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_yellow_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_yellow_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_yellow_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_yellow_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_yellow_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_yellow_ket = VGroup(mem1eye_white_left_yellow_ket, mem1pupil_left_yellow_ket).shift(
            LEFT * eye_width)
        mem1eye_right_yellow_ket = VGroup(mem1eye_white_right_yellow_ket, mem1pupil_right_yellow_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_yellow_ket, mem1eye_right_yellow_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_yellow = Tex("\\ket{\\psi}").set_color(hex_green).scale(char_scale)
        mem1Psi_yellow_guy = VGroup(mem1Psi_yellow, mem1psi_eyes)
        ######################

        mem1Psi_red_guy.move_to(spiky_env.origins[0]).shift(RIGHT*3)
        mem1Psi_yellow_guy.move_to(spiky_env.origins[1]).shift(RIGHT * 3)
        mem1Psi_blue_guy.move_to(spiky_env.origins[2]).shift(RIGHT * 3)



        spiky_env.vec = blue

        ######################
        eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left.get_right() + pup_radius * LEFT)
        pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right.get_right() + pup_radius * LEFT)
        h_eye_left = VGroup(eye_white_left, pupil_left).shift(LEFT * eye_width)
        h_eye_right = VGroup(eye_white_right, pupil_right).shift(RIGHT * eye_width)
        h_eyes = VGroup(h_eye_left, h_eye_right).scale(1 / 5).shift(RIGHT * .1)
        H = Tex("\\hat{H}").set_color(GREY_B).scale(char_scale)
        H_guy = VGroup(H, h_eyes)
        ######################


        H_guy.move_to(spiky_env.origins[1]).shift(LEFT * 5).scale(2)

        sample_evolver = create_evolver(sample_H, 0.5)
        spiky_env.vec = np.dot(sample_evolver, spiky_env.vec)
        spiky_env.vec = np.dot(sample_evolver, spiky_env.vec)
        spiky_env.vec = np.dot(sample_evolver, spiky_env.vec)
        spiky_env.vec = np.dot(sample_evolver, spiky_env.vec)

        self.add(mem1Psi_red_guy, mem1Psi_yellow_guy, mem1Psi_blue_guy,H_guy)

        dt_1 = 0.1
        steps = 100
        sample_evolver_1 = create_evolver(sample_H, dt_1)
        for i in np.arange(steps):
            spiky_env.vec = np.dot(sample_evolver_1, spiky_env.vec)

        self.camera.frame.move_to(spiky_env.origins[1])
        frame_theta.set_value(-30)
        frame_phi.set_value(60)


        for i in np.arange(steps):
            spiky_env.vec = np.dot(sample_evolver_1, spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),run_time=dt_1)

        mustache = ImageMobject("imgs/mustache.png").move_to(H_guy[1]).scale(1/5).shift(DOWN*0.8)
        self.play(FadeIn(mustache))
        #self.add(mustache)

        mustache_evolver = create_evolver(mustache_H,dt_1*5)

        for i in np.arange(int(steps/1.5)):
            spiky_env.vec = np.dot(mustache_evolver, spiky_env.vec)
            spiky_env.vec = spiky_env.vec / np.linalg.norm(spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),run_time=dt_1)

        hat = ImageMobject("imgs/hat.png").move_to(H_guy[1]).scale(1/2).shift(UP*1.2)
        self.play(FadeIn(hat),FadeOut(mustache))

        hat_mustache_evolver = create_evolver(hat_mustache_H, dt_1 * 5)

        for i in np.arange(steps/2):
            spiky_env.vec = np.dot(hat_mustache_evolver, spiky_env.vec)
            spiky_env.vec = spiky_env.vec / np.linalg.norm(spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),run_time=dt_1)

        self.play(
            self.camera.frame.animate.move_to(spiky_env.origins[1]),
            frame_theta.animate.set_value(0),
            frame_phi.animate.set_value(0)
        )

        def fade_out_all(list):
            args = []
            for i in np.arange(len(list)):
                args.append(FadeOut(list[i]))
            return args

        self.play(
            *fade_out_all(spiky_env.brackets),
            *fade_out_all(spiky_env.axes),
            *fade_out_all(spiky_env.give_vec())
        )



        self.camera.frame.clear_updaters()

class newHatNewSee(Scene):
    def construct(self):
        frame_theta = ValueTracker(0)
        frame_phi = ValueTracker(0)
        self.camera.frame.add_updater(
            lambda f: f.set_euler_angles(theta=frame_theta.get_value(),
                                         phi=frame_phi.get_value(),
                                         units=DEGREES)
        )
        ######################
        scale = .7
        pup_radius = scale / 2
        eye_width = scale * 2
        eye_height = scale * 4
        char_scale = scale * 5
        eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left.get_right() + pup_radius * LEFT)
        pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right.get_right() + pup_radius * LEFT)
        h_eye_left = VGroup(eye_white_left, pupil_left).shift(LEFT * eye_width)
        h_eye_right = VGroup(eye_white_right, pupil_right).shift(RIGHT * eye_width)
        h_eyes = VGroup(h_eye_left, h_eye_right).scale(1 / 5).shift(RIGHT * .1)
        H = Tex("\\hat{H}").set_color(GREY_B).scale(char_scale)
        H_guy = VGroup(H, h_eyes).scale(2)
        ######################

        ######################
        mem1eye_white_left_blue_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_blue_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_blue_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_blue_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_blue_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_blue_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_blue_ket = VGroup(mem1eye_white_left_blue_ket, mem1pupil_left_blue_ket).shift(LEFT * eye_width)
        mem1eye_right_blue_ket = VGroup(mem1eye_white_right_blue_ket, mem1pupil_right_blue_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_blue_ket, mem1eye_right_blue_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_blue = Tex("\\ket{\\psi}").set_color(hex_blue).scale(char_scale)
        mem1Psi_blue_guy = VGroup(mem1Psi_blue, mem1psi_eyes)
        ######################

        ######################
        mem1eye_white_left_red_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_red_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_red_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_red_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_red_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_red_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_red_ket = VGroup(mem1eye_white_left_red_ket, mem1pupil_left_red_ket).shift(LEFT * eye_width)
        mem1eye_right_red_ket = VGroup(mem1eye_white_right_red_ket, mem1pupil_right_red_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_red_ket, mem1eye_right_red_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_red = Tex("\\ket{\\psi}").set_color(hex_red).scale(char_scale)
        mem1Psi_red_guy = VGroup(mem1Psi_red, mem1psi_eyes)
        ######################

        ######################
        mem1eye_white_left_yellow_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1eye_white_right_yellow_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        mem1pupil_left_yellow_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_left_yellow_ket.get_left() + pup_radius * RIGHT)
        mem1pupil_right_yellow_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            mem1eye_white_right_yellow_ket.get_left() + pup_radius * RIGHT)
        mem1eye_left_yellow_ket = VGroup(mem1eye_white_left_yellow_ket, mem1pupil_left_yellow_ket).shift(
            LEFT * eye_width)
        mem1eye_right_yellow_ket = VGroup(mem1eye_white_right_yellow_ket, mem1pupil_right_yellow_ket).shift(
            RIGHT * eye_width)
        mem1psi_eyes = VGroup(mem1eye_left_yellow_ket, mem1eye_right_yellow_ket).scale(1 / 5).shift(LEFT * .1)
        mem1Psi_yellow = Tex("\\ket{\\psi}").set_color(hex_green).scale(char_scale)
        mem1Psi_yellow_guy = VGroup(mem1Psi_yellow, mem1psi_eyes)
        ######################

        spiky_env = SpikyVector(False, 3, 1, green)
        H_guy.move_to(spiky_env.origins[1]).shift(LEFT * 5)
        hat = ImageMobject("imgs/hat.png").move_to(H_guy[1]).scale(1 / 2).shift(UP * 1.2)
        mem1Psi_red_guy.move_to(spiky_env.origins[0]).shift(RIGHT * 3)
        mem1Psi_yellow_guy.move_to(spiky_env.origins[1]).shift(RIGHT * 3)
        mem1Psi_blue_guy.move_to(spiky_env.origins[2]).shift(RIGHT * 3)
        self.camera.frame.move_to(spiky_env.origins[1])

        self.add(
            H_guy,hat,mem1Psi_red_guy,mem1Psi_yellow_guy,mem1Psi_blue_guy
        )

        self.play(
            H_guy[1][0][1].animate.shift(UP * H_guy[1][0][1].get_height()),
            H_guy[1][1][1].animate.shift(UP * H_guy[1][1][1].get_height())
        )

        self.play(
            H_guy[1][0][1].animate.shift(2 * DOWN * H_guy[1][0][1].get_height()),
            H_guy[1][1][1].animate.shift(2 * DOWN * H_guy[1][1][1].get_height())
        )

        self.play(
            H_guy[1][0][1].animate.shift(UP * H_guy[1][0][1].get_height()),
            H_guy[1][1][1].animate.shift(UP * H_guy[1][1][1].get_height())
        )

        what = Text("?").move_to(hat).shift(UP*1.1).scale(3)
        self.play(FadeIn(what))

        hat_0_red_overlap_guy = copy.deepcopy(mem1Psi_red_guy).scale(abs(hat_0_red_overlap)).move_to(mem1Psi_red_guy).shift(LEFT*1.5)
        hat_1_red_overlap_guy = copy.deepcopy(mem1Psi_red_guy).scale(abs(hat_1_red_overlap)).move_to(mem1Psi_red_guy)
        hat_2_red_overlap_guy = copy.deepcopy(mem1Psi_red_guy).scale(abs(hat_2_red_overlap)).move_to(mem1Psi_red_guy).shift(RIGHT*1.5)
        hat_0_green_overlap_guy = copy.deepcopy(mem1Psi_yellow_guy).scale(abs(hat_0_green_overlap)).move_to(mem1Psi_yellow_guy).shift(LEFT*1.5)
        hat_1_green_overlap_guy = copy.deepcopy(mem1Psi_yellow_guy).scale(abs(hat_1_green_overlap)).move_to(mem1Psi_yellow_guy)
        hat_2_green_overlap_guy = copy.deepcopy(mem1Psi_yellow_guy).scale(abs(hat_2_green_overlap)).move_to(mem1Psi_yellow_guy).shift(RIGHT*1.5)
        hat_0_blue_overlap_guy = copy.deepcopy(mem1Psi_blue_guy).scale(abs(hat_0_blue_overlap)).move_to(mem1Psi_blue_guy).shift(LEFT*1.5)
        hat_1_blue_overlap_guy = copy.deepcopy(mem1Psi_blue_guy).scale(abs(hat_1_blue_overlap)).move_to(mem1Psi_blue_guy)
        hat_2_blue_overlap_guy = copy.deepcopy(mem1Psi_blue_guy).scale(abs(hat_2_blue_overlap)).move_to(mem1Psi_blue_guy).shift(RIGHT*1.5)

        hat_0_red_overlap_guy[0].set_color(hat_0_hex_color)
        hat_1_red_overlap_guy[0].set_color(hat_1_hex_color)
        hat_2_red_overlap_guy[0].set_color(hat_2_hex_color)
        hat_0_green_overlap_guy[0].set_color(hat_0_hex_color)
        hat_1_green_overlap_guy[0].set_color(hat_1_hex_color)
        hat_2_green_overlap_guy[0].set_color(hat_2_hex_color)
        hat_0_blue_overlap_guy[0].set_color(hat_0_hex_color)
        hat_1_blue_overlap_guy[0].set_color(hat_1_hex_color)
        hat_2_blue_overlap_guy[0].set_color(hat_2_hex_color)

        self.play(FadeOut(mem1Psi_red_guy),
                  FadeIn(hat_0_red_overlap_guy),
                  FadeIn(hat_1_red_overlap_guy),
                  FadeIn(hat_2_red_overlap_guy))
        self.play(FadeOut(mem1Psi_yellow_guy),
                  FadeIn(hat_0_green_overlap_guy),
                  FadeIn(hat_1_green_overlap_guy),
                  FadeIn(hat_2_green_overlap_guy))
        self.play(FadeOut(mem1Psi_blue_guy),
                  FadeIn(hat_0_blue_overlap_guy),
                  FadeIn(hat_1_blue_overlap_guy),
                  FadeIn(hat_2_blue_overlap_guy))

        oh = Text("!").move_to(what).scale(3)
        self.play(FadeOut(what),
                  FadeIn(oh))

        hat_0_guy = copy.deepcopy(mem1Psi_red_guy)
        hat_1_guy = copy.deepcopy(mem1Psi_yellow_guy)
        hat_2_guy = copy.deepcopy(mem1Psi_blue_guy)

        hat_0_guy[0].set_color(hat_0_hex_color)
        hat_1_guy[0].set_color(hat_1_hex_color)
        hat_2_guy[0].set_color(hat_2_hex_color)

        self.play(FadeOut(hat_0_red_overlap_guy),
                  FadeOut(hat_1_red_overlap_guy),
                  FadeOut(hat_2_red_overlap_guy),
                  FadeOut(hat_0_green_overlap_guy),
                  FadeOut(hat_1_green_overlap_guy),
                  FadeOut(hat_2_green_overlap_guy),
                  FadeOut(hat_0_blue_overlap_guy),
                  FadeOut(hat_1_blue_overlap_guy),
                  FadeOut(hat_2_blue_overlap_guy),
                  FadeIn(hat_0_guy),
                  FadeIn(hat_1_guy),
                  FadeIn(hat_2_guy)
                  )

        # spiny_env_vec_i = copy.copy(spiky_env.vec)

        # hat_0_vec_proj = np.dot(np.conjugate(hat_U[0]), spiny_env_vec_i)
        # hat_1_vec_proj = np.dot(np.conjugate(hat_U[1]), spiny_env_vec_i)
        # hat_2_vec_proj = np.dot(np.conjugate(hat_U[2]), spiny_env_vec_i)
        # hat_vec_i = np.array([[-1.0],
        #                       [0],
        #                       [1.0]
        #                       ],dtype=complex)

        # hat_vec_i = np.array([[hat_0_vec_proj][0],
        #                       [hat_1_vec_proj][0],
        #                       [hat_2_vec_proj][0]
        #                       ])


        # Giving it blue because that has the corresponding index to first eigenvector in hat_mustache_H
        hat_spiky_env = SpikyVector(False,3,1,blue)
        spiky_env.vec = hat_U[0]

        hat_spiky_env.vec_draw[0][0].set_color(WHITE)
        hat_spiky_env.vec_draw[0][1].set_color(WHITE)
        hat_spiky_env.vec_draw[0][2].set_color(hat_0_hex_color)
        hat_spiky_env.vec_draw[1][0].set_color(WHITE)
        hat_spiky_env.vec_draw[1][1].set_color(WHITE)
        hat_spiky_env.vec_draw[1][2].set_color(hat_1_hex_color)
        hat_spiky_env.vec_draw[2][0].set_color(WHITE)
        hat_spiky_env.vec_draw[2][1].set_color(WHITE)
        hat_spiky_env.vec_draw[2][2].set_color(hat_2_hex_color)

        spiky_env.vec_draw[0][0].set_color(WHITE)
        spiky_env.vec_draw[0][1].set_color(WHITE)
        spiky_env.vec_draw[0][2].set_color(hex_red)
        spiky_env.vec_draw[1][0].set_color(WHITE)
        spiky_env.vec_draw[1][1].set_color(WHITE)
        spiky_env.vec_draw[1][2].set_color(hex_green)
        spiky_env.vec_draw[2][0].set_color(WHITE)
        spiky_env.vec_draw[2][1].set_color(WHITE)
        spiky_env.vec_draw[2][2].set_color(hex_blue)

        def fade_out_all(list):
            args = []
            for i in np.arange(len(list)):
                args.append(FadeOut(list[i]))
            return args

        def fade_in_all(list):
            args = []
            for i in np.arange(len(list)):
                args.append(FadeIn(list[i]))
            return args

        self.play(
            *fade_in_all(hat_spiky_env.axes),
            *fade_in_all(hat_spiky_env.brackets),
            *fade_in_all(hat_spiky_env.give_vec()),
            self.camera.frame.animate.move_to(hat_spiky_env.origins[1]),
            frame_theta.animate.set_value(-30),
            frame_phi.animate.set_value(60),
            FadeOut(oh)
        )

        dt_1 = 0.1
        steps = 100
        hat_evolver = create_evolver(hat_mustache_H, dt_1)
        hat_evolver_improper = improper_evolver(hat_mustache_H,dt_1)
        for i in np.arange(steps):
            hat_spiky_env.vec = np.dot(hat_evolver_improper, hat_spiky_env.vec)
            spiky_env.vec = np.dot(hat_evolver, spiky_env.vec)
            self.play(*hat_spiky_env.tracker_set_vals(),run_time=dt_1)

        out_scale = 5

        self.play(*spiky_env.animate_shift_mobjects(OUT*out_scale),
                  mem1Psi_red_guy.animate.shift(OUT*out_scale),
                  mem1Psi_yellow_guy.animate.shift(OUT * out_scale),
                  mem1Psi_blue_guy.animate.shift(OUT * out_scale),
                  self.camera.frame.animate.shift((OUT*out_scale/1.3)+DOWN*3+LEFT)
                  )

        for i in np.arange(steps):
            hat_spiky_env.vec = np.dot(hat_evolver_improper, hat_spiky_env.vec)
            spiky_env.vec = np.dot(hat_evolver, spiky_env.vec)
            self.play(*hat_spiky_env.tracker_set_vals(),
                      *spiky_env.tracker_set_vals(),
                      run_time=dt_1)

        self.camera.frame.clear_updaters()

class judgment(Scene):
    def construct(self):
        ######################
        scale = .7
        pup_radius = scale / 2
        eye_width = scale * 2
        eye_height = scale * 4
        char_scale = scale * 5
        eye_white_left_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right_white_ket = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left_white_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left_white_ket.get_left() + pup_radius * RIGHT)
        pupil_right_white_ket = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right_white_ket.get_left() + pup_radius * RIGHT)
        eye_left_white_ket = VGroup(eye_white_left_white_ket, pupil_left_white_ket).shift(LEFT * eye_width)
        eye_right_white_ket = VGroup(eye_white_right_white_ket, pupil_right_white_ket).shift(RIGHT * eye_width)
        psi_eyes = VGroup(eye_left_white_ket, eye_right_white_ket).scale(1 / 5).shift(LEFT * .1)
        Psi_white = Tex("\\ket{\\psi}").set_color(GREY_B).scale(char_scale)
        Psi_white_guy = VGroup(Psi_white, psi_eyes)
        ######################

        ######################
        scale = .7
        pup_radius = scale / 2
        eye_width = scale * 2
        eye_height = scale * 4
        char_scale = scale * 5
        eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
        pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_left.get_right() + pup_radius * LEFT)
        pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
            eye_white_right.get_right() + pup_radius * LEFT)
        h_eye_left = VGroup(eye_white_left, pupil_left).shift(LEFT * eye_width)
        h_eye_right = VGroup(eye_white_right, pupil_right).shift(RIGHT * eye_width)
        h_eyes = VGroup(h_eye_left, h_eye_right).scale(1 / 5).shift(RIGHT * .1)
        H = Tex("\\hat{H}").set_color(GREY_B).scale(char_scale)
        H_guy = VGroup(H, h_eyes)
        H_guy.flip()
        ######################

        spiky_env = SpikyVector(False, 3, 1, blue)

        Psi_white_guy.add_updater(
            lambda p: p[0].set_color(rgb_to_hex(round(256*spiky_env.vec_track[0][2].get_value()),
                                                round(256*spiky_env.vec_track[1][2].get_value()),
                                                round(256*spiky_env.vec_track[2][2].get_value())))
        )
        H_guy.shift(RIGHT*H_guy.get_width()*4)
        H_guy_hat = copy.deepcopy(H_guy)
        H_guy_hat.shift(UP * 1.5 * H_guy.get_height()).set_opacity(0.2)
        hat = ImageMobject("imgs/hat.png").move_to(H_guy_hat[1]).scale(1 / 4).shift(UP * 0.6).set_opacity(0.2)
        H_guy_mustache = copy.deepcopy(H_guy)
        H_guy_mustache.shift(DOWN * 1.5 * H_guy.get_height()).set_opacity(0.2)
        mustache = ImageMobject("imgs/mustache.png").move_to(H_guy_mustache[1]).scale(1 / 10).shift(DOWN * 0.4).set_opacity(0.2)
        self.add(Psi_white_guy,H_guy,H_guy_hat,H_guy_mustache,hat,mustache)

        # self.add(*spiky_env.give_vec())



        steps = 50
        dt = 0.1
        evolver = create_evolver(hat_mustache_H, dt)
        for i in np.arange(steps):
            spiky_env.vec = np.dot(evolver,spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy.animate.shift(LEFT*dt),
                      run_time=dt/2)

        for i in np.arange(steps/10):
            spiky_env.vec = np.dot(evolver,spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy.animate.shift(LEFT * 0),
                      Psi_white_guy[1][0][1].animate.shift(RIGHT*dt/3),
                      Psi_white_guy[1][1][1].animate.shift(RIGHT*dt/3),
                      run_time=dt)
        for i in np.arange(steps/5):
            spiky_env.vec = np.dot(evolver,spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy.animate.shift(LEFT * 0),
                      run_time=dt)
        self.play(
            H_guy.animate.set_opacity(0.2),
            H_guy_mustache.animate.set_opacity(1),
            mustache.animate.set_opacity(1),
            Psi_white_guy.animate.shift(LEFT * 0),
        )
        for i in np.arange(steps/10):
            spiky_env.vec = np.dot(evolver,spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy.animate.shift(RIGHT * 2 * dt),
                      run_time=dt)
        for i in np.arange(steps/10):
            spiky_env.vec = np.dot(evolver,spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy[1][0][1].animate.shift(UP*dt/3),
                      Psi_white_guy[1][1][1].animate.shift(UP*dt/3),
                      Psi_white_guy.animate.shift(LEFT * 0),
                      run_time=dt)
        for i in np.arange(4):
            spiky_env.vec = np.dot(evolver, spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy.animate.shift(LEFT * 0),
                      run_time=dt)
        for i in np.arange(steps/10):
            spiky_env.vec = np.dot(evolver,spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy[1][0][1].animate.shift(DOWN*2*dt/3.1),
                      Psi_white_guy[1][1][1].animate.shift(DOWN*2*dt/3.1),
                      Psi_white_guy.animate.shift(LEFT * 0),
                      run_time=dt)
        for i in np.arange(4):
            spiky_env.vec = np.dot(evolver, spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy.animate.shift(LEFT * 0),
                      run_time=dt)
        for i in np.arange(steps/5):
            spiky_env.vec = np.dot(evolver,spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy.animate.shift((RIGHT+DOWN) * 2 * dt),
                      run_time=dt)
        for i in np.arange(steps/10):
            spiky_env.vec = np.dot(evolver,spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy[1][0][1].animate.shift(UP*dt/3.1),
                      Psi_white_guy[1][1][1].animate.shift(UP*dt/3.1),
                      Psi_white_guy.animate.shift(LEFT * 0),
                      run_time=dt)
        for i in np.arange(steps):
            spiky_env.vec = np.dot(evolver,spiky_env.vec)
            self.play(*spiky_env.tracker_set_vals(),
                      Psi_white_guy.animate.shift((RIGHT) * dt/2),
                      run_time=dt/2)
        spiky_env.vec = np.dot(evolver, spiky_env.vec)
        self.play(
            *spiky_env.tracker_set_vals(),
            mustache.animate.set_opacity(0.2),
            H_guy_mustache.animate.set_opacity(0.2),
            hat.animate.set_opacity(1),
            Psi_white_guy.animate.shift(LEFT * 0),
            H_guy_hat.animate.set_opacity(1)
        )
        Psi_white_guy.clear_updaters()
        self.play(FadeOut(Psi_white_guy),
                  run_time = 0.3)
        Psi_white_guy[0].set_color(hat_1_hex_color)
        self.play(FadeIn(Psi_white_guy),
                  Psi_white_guy.animate.shift(LEFT * 0),
                  run_time = 0.6)
        for i in np.arange(steps/10):
            spiky_env.vec = np.dot(evolver,spiky_env.vec)
            self.play(Psi_white_guy[1][0][1].animate.shift((LEFT/3+UP/4)*dt),
                      Psi_white_guy[1][1][1].animate.shift((LEFT/3+UP/4)*dt),
                      run_time=dt)
        self.wait(0.3)
        self.play(Psi_white_guy.animate.shift((LEFT + UP) * 8),
                  run_time=10)


















