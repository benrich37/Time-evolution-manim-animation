from manimlib import *
import numpy as np
from waiting import wait
import keyboard

class shortanim(Scene):
    def construct(self):
        E = Tex("\\hat{H}",
                "|",
                "\\psi",
                "\\rangle")
        self.add(E)
        F = Tex("i\\hbar",
                "|",
                "\\dot{\\psi}",
                "\\rangle")

        # Couldn't find a good accelerating func in the rate_func library
        def accelerate(t, acc=3):
            return t ** acc

        # mouse_posn = self.mouse_point

        # # In place transformation to emphasize H acting on psi as an action, rather than an equality
        self.play(E[0].animate.shift(LEFT / 2),
                  # The rate_fun and run_time are incredibly useful control kobs for making animations look prettier
                  rate_func=exponential_decay,
                  run_time=1.4)
        baby = False

        # def check_on_baby(input):
        #     if keyboard.is_pressed('n'):
        #         return True
        #     return False
        # # def check_on_baby(input):
        # #     if self.on_key_press():
        # #         return True
        # #     return False
        #
        # self.wait_until(lambda: check_on_baby(input), max_time = 10)

        #wait(lambda: check_on_baby(input), timeout_seconds = 20, waiting_for = "baby not ready")
        # always(E[0].move_to,self.mouse_point)
        # trackthis = np.mag
        # self.wait_until(self.mouse_point == E[1].get_center())
        self.wait(1)
        self.add_key_press_listener(self.on_key_press)
        self.on_key_press('n', self.play(E[0].animate.shift(RIGHT / 2),
                  rate_func=accelerate,
                  run_time=0.5))
        # self.play(TransformMatchingTex(E, F,
        #                                # These key map=s will come up a lot in this code. The TransformMatchingTex is
        #                                # okay at translating matching characters between LaTeX expressions, but you'll
        #                                # need a key map to tell the function which submobjects map to which submobjects
        #                                key_map={
        #                                    E[0]: F[0],
        #                                    E[1]: F[1],
        #                                    E[2]: F[2],
        #                                    E[3]: F[3],
        #                                }),
        #           run_time=0.2)
        # self.play(WiggleOutThenIn(F, scale_value=1.0, n_wiggles=2),
        #           rate_func=exponential_decay,run_time=3)


class EvolutionDraft(Scene):
    def construct(self):

        # I will be using capital letters in alphabetical order for the LaTeX strings. (yes I know this is bad practice,
        # pycharm was yelling at me the entire time)
        # Following object-oriented design (and so I can anthropomorphize my lil guys as much as possible), we can refer
        # to each of these Tex strings as "mobjects" (manim objects). Mostly all of the animation functions will work on
        # other types of mobjects.

        # # How do we take psi from t_0 to t?
        A = Tex("\\psi(t_0)")
        # It has been revealed! Our Tex mobject actually contains a list of submobjects!
        # The manim program stores these sub-strings for manipulation, but will concatenate them right before feeding
        # them to LaTeX to illustrate.
        B = Tex("\\ket{\\psi(t)}", "\stackrel{?}{\longleftarrow}", "\\psi(t_0)")
        # Transitionless adding a mobject
        self.add(A)
        # A cool function that will recognize matching sub-strings and create a "reorganizing" type of transition
        self.play(TransformMatchingTex(A,B))
        self.play(FadeOut(B, RIGHT))


        # # with our Hamiltonian of course!
        C = Tex("\\hat{H}")
        C.set_color(RED)
        C.scale(9)
        self.play(Write(C))
        self.play(ScaleInPlace(C,(1/9)))

        # # But what does the Hamiltonian even do?
        D = Tex("\\hat{H}", "|","\\psi","\\rangle")
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
        self.play(J[2].animate.set_color(WHITE),J[10].animate.set_color(WHITE))

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
        Ansatz.shift(UP*2)
        Ansatz.set_color(BLUE)

        # Insert the 1st order dif eq ansatz to skip a few steps and reinforce pattern recognition
        self.play(Write(Ansatz),run_time=1)

        Ansatz[0].set_color(ORANGE)
        Jn[0].set_color(ORANGE)
        self.play(Indicate(Ansatz[0],color=ORANGE), Indicate(Jn[0],color=ORANGE))
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
        self.play(ApplyWave(Kn[1]))

        L = Tex("|\\psi(t)\\rangle =",
                "e^{-\\frac{i}{\\hbar}\\hat{H} t}",
                "|\\psi(t_0)\\rangle ")
        L0c = L[0].get_center()
        L2c = L[2].get_center()
        self.add(L)
        self.play(FadeOut(Kn[1]))

        # Multiple iterations of a quick ApplyWave function to give a little "Shimmer"
        # # Our exponential friend has a secret identity!
        self.play(ApplyWave(L[1],direction=np.array((1.0,1.0,0.0)), time_width=0.2, amplitude=0.01), run_time=0.1)
        self.play(ApplyWave(L[1], direction=np.array((1.0, 1.0, 0.0)), time_width=0.2, amplitude=0.06), run_time=0.2)
        self.play(ApplyWave(L[1], direction=np.array((1.0, 1.0, 0.0)), time_width=0.2, amplitude=0.1), run_time=0.3)

        # Rotating e^{...} halfway along the UP axis to give a flat stanley state for a sort of seamless transition into
        # a different Tex expression
        self.play(
                Rotate(
                    L[1],
                    angle=PI/2,
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
        M[1].rotate(PI/2,UP)

        self.add(M)
        self.play(FadeOut(L),
                  Rotate(M[1], angle=-PI/2, axis=UP))
        self.play(FadeOut(M[0]),FadeOut(M[2]),M[1].center)
        # # Look at our new operator!
        self.play(Flash(M[1],flash_radius=1))
        self.play(FadeInFromPoint(M[2],RIGHT_SIDE))

        # Storing some helps posns for later
        m1center = M[1].get_center()
        m2width = M[2].get_width()
        m2right = M[2].get_right()
        m2left = M[2].get_left()
        m2width=M[2].get_width()

        # This will be our path for an upcoming animation
        moveline = Line(m1center, m1center + LEFT)
        # Keeping this function since its a useful reference way to specify which axis should be stretching
        # M[2].set_width(m2width, stretch=True)

        # storing the old state of this string for an easy revert animation
        M[2].save_state()

        # # U(t,t_0) pulling on psi(t_0)
        # These next few animations is my FAVORITE part of this code.
        self.play(MoveAlongPath(M[1],moveline),ApplyPointwiseFunction(
            # This "lambda point: ..." is a way of feeding in a function to another function
            # the first "point" establishes what we're calling the input variable in our lambda function
            lambda point: ((point - m2right)/m2width) * RIGHT + point, M[2]
        ), run_time=2)

        O = Tex("|\\psi ",
                "(t",
                "_0",
                ")",
                "\\rangle ")
        O.move_to(M[2])

        self.play(FadeOut(M[1]),Restore(M[2]),run_time=0.2)
        self.add(O)
        self.play(FadeOut(M[2]),FadeOut(O[2],run_time=0.2),WiggleOutThenIn(O,scale_value=1.0,n_wiggles=3),
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
        self.play(FadeIn(P[1]))
        self.play(FadeInFromPoint(P[0],LEFT_SIDE))

        p0center = P[0].get_center()
        p1right = P[1].get_right()
        p1width = P[1].get_width()
        moveline = Line(p0center, p0center + (LEFT/2))
        P.save_state()

        # Yes this is an identical function as last time, but implementing custom animation functions is a lot
        # tricker than custom arithmetic functions
        # # What are you doing!!! U(t,t_0) can't act from that end of a ket!!!
        self.play(MoveAlongPath(P[0], moveline), ApplyPointwiseFunction(
            lambda point: ((point - p1right)/p1width) * (RIGHT/2) + point, P[1]
        ), run_time=1, rate_func=exponential_decay)
        self.play(Restore(P),run_time=0.3)
        # Using the "WiggleOutThenIn" function with scale_value set to 1 to get an easy shudder animation
        self.play(WiggleOutThenIn(P[1],scale_value=1.0,n_wiggles=2), rate_func=exponential_decay)

        moveline = Line(p0center, p0center + (LEFT))
        P.save_state()

        # # Stop!! You're hurting it!!
        self.play(MoveAlongPath(P[0], moveline), ApplyPointwiseFunction(
            lambda point: ((point - p1right) / p1width) * (RIGHT) + point, P[1]
        ), run_time=1, rate_func=exponential_decay)
        self.play(FadeOut(P))

        # # The grand result
        SynEr = Tex("SyntaxError :)")
        self.play(Write(SynEr),run_time=3)






