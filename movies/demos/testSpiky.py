import numpy as np
from manimlib import Scene, ValueTracker, DEGREES
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '../..'))
from funcs.classes.mathObjects import SpikyVector
from funcs.methods.propogation import prop_gen, prop_sig_z_pert
from funcs.ref.constants import z_p


class testSpiky(Scene):
    def construct(self):
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

        spiky = SpikyVector(False,2,1,z_p)



        self.add(*spiky.axes)
        self.add(*spiky.brackets)
        self.add(*spiky.give_vec())
        # spiky.vec = np.dot(spiky.vec,sig_x)
        # self.play(*spiky.tracker_set_vals())
        # self.play(*spiky.animate_shift_mobjects(UP))

        dt_1 = 0.1
        steps = 50
        for i in np.arange(steps):
            spiky.vec = np.dot(prop_gen(dt_1, "z"), spiky.vec)
            self.play(*spiky.tracker_set_vals(),frame_theta.animate.set_value(self.time*30),run_time=dt_1)
        self.play(self.camera.frame.animate.move_to(spiky.origins[1]))
        for i in np.arange(steps):
            spiky.vec = np.dot(prop_sig_z_pert(dt_1), spiky.vec)
            self.play(*spiky.tracker_set_vals(),frame_theta.animate.set_value(self.time*30),run_time=dt_1)
        for i in np.arange(steps):
            spiky.vec = np.dot(prop_gen(dt_1, "z"), spiky.vec)
            self.play(*spiky.tracker_set_vals(),frame_theta.animate.set_value(self.time*30),run_time=dt_1)

        self.camera.frame.clear_updaters()
