import numpy as np
from manimlib import Scene, Tex
from classes.characters import lilGuy
from classes.mathObjects import SmoothieVector
from ref.constants import y_p, sig_x


class testSmoothie(Scene):
    def construct(self):
        test= SmoothieVector(2, 1, y_p)
        self.add(*test.add_all())
        test.vec = np.dot(sig_x,test.vec)
        self.play(*test.tracker_set_vals())

        test_guy = lilGuy(Tex("\\zeta"))

        self.add(test_guy.lilguy)
