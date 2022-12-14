import numpy
from manimlib import Scene, ValueTracker, DEGREES, LEFT, RIGHT

from classes.math_from_pm import SpikyVector
from methods.propogation import create_evolver


class moreDimension(Scene):
    def construct(self):
        frame_theta = ValueTracker(-30)
        frame_phi = ValueTracker(60)
        frame_gamma = ValueTracker(0)
        self.camera.frame.add_updater(
            lambda f: f.set_euler_angles(theta=frame_theta.get_value(),
                                         phi=frame_phi.get_value(),
                                         # gamma=frame_gamma.get_value(),
                                         units=DEGREES)
        )
        bigV = np.array([
            1,
            0,
            0,
            0
        ])
        bigH = np.array([
            [1, 0, 0, 0],
            [0, 1, 3, 0],
            [0, 3, 1, 0],
            [0, 0, 0, 1]
        ])
        perturber = np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0.1, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        newBigH = bigH + perturber
        dt = 1
        evolver = create_evolver(bigH, dt)
        evolver_p = create_evolver(newBigH, dt)


        spiky = SpikyVector(False, 4, 1, bigV)
        self.add(*spiky.axes)
        self.add(*spiky.brackets)
        self.add(*spiky.give_vec())
        spiky2 = SpikyVector(False, 4, 1, bigV)
        self.add(*spiky2.axes)
        self.add(*spiky2.brackets)
        self.add(*spiky2.give_vec())

        self.play(*spiky.animate_shift_mobjects(LEFT*spiky.ax_range*2),
                  *spiky2.animate_shift_mobjects(RIGHT*spiky2.ax_range*2))

        steps = 50
        for i in np.arange(steps):
            spiky.vec = np.dot(evolver, spiky.vec)
            spiky2.vec = np.dot(evolver, spiky2.vec)
            self.play(*spiky.tracker_set_vals(),
                      *spiky2.tracker_set_vals(),
                      run_time=dt/10)
        steps = 50
        for i in np.arange(steps):
            spiky.vec = np.dot(evolver_p, spiky.vec)
            spiky2.vec = np.dot(evolver, spiky2.vec)
            self.play(*spiky.tracker_set_vals(),
                      *spiky2.tracker_set_vals(),
                      run_time=dt / 10)
        steps = 50
        for i in np.arange(steps):
            spiky.vec = np.dot(evolver, spiky.vec)
            spiky2.vec = np.dot(evolver, spiky2.vec)
            self.play(*spiky.tracker_set_vals(),
                      *spiky2.tracker_set_vals(),
                      run_time=dt / 10)

        self.camera.frame.clear_updaters()
