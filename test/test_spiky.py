from manimlib import *
import numpy as np
import unittest
from classes.mathObjects import SpikyVector
from ref.constants import y_p


class TestSpiky(unittest.TestCase):
    def test_shapes(self):
        testSpiky = SpikyVector(False, 2, 2, y_p)
        self.assertEqual(np.shape(testSpiky.vec), (2,))
        self.assertEqual(np.shape(testSpiky.origins), (2,3))
        # self.assertEqual(np.shape(testSpiky.axes), (2,))
        self.assertIsInstance(testSpiky.axes[0],ThreeDAxes)
        self.assertIsInstance(testSpiky.vec_draw[0][0], Vector)
        self.assertIsInstance(testSpiky.vec_draw[0][1], Vector)
        self.assertIsInstance(testSpiky.vec_draw[0][2], Vector)
        self.assertIsInstance(testSpiky.vec_draw[1][0], Vector)
        self.assertIsInstance(testSpiky.vec_draw[1][1], Vector)
        self.assertIsInstance(testSpiky.vec_draw[1][2], Vector)
        self.assertIsInstance(testSpiky.vec_track[0][0], ValueTracker)
        self.assertIsInstance(testSpiky.vec_track[0][1], ValueTracker)
        self.assertIsInstance(testSpiky.vec_track[0][2], ValueTracker)
        self.assertIsInstance(testSpiky.vec_track[1][0], ValueTracker)
        self.assertIsInstance(testSpiky.vec_track[1][1], ValueTracker)
        self.assertIsInstance(testSpiky.vec_track[1][2], ValueTracker)
        testSpiky.set_tracker(0,0)
        self.assertEqual(testSpiky.vec_track[0][0].get_value(), np.real(
            y_p[0]))
        testSpiky.set_tracker(0,1)
        self.assertEqual(testSpiky.vec_track[0][0].get_value(), np.real(
            y_p[0]))
        self.assertEqual(testSpiky.vec_track[0][1].get_value(), np.imag(
            y_p[0]))
        # testSpiky.set_tracker(1, 0)
        # self.assertEqual(testSpiky.vec_track[0][0].get_value(), np.real(y_p[0]))
        testSpiky.set_tracker(1, 1)
        self.assertEqual(testSpiky.vec_track[0][0].get_value(), np.real(
            y_p[0]))
        self.assertEqual(testSpiky.vec_track[0][1].get_value(), np.imag(
            y_p[0]))
        self.assertEqual(testSpiky.n,2)

        testOut = testSpiky.give_vec()
        self.assertEqual(np.shape(testOut), (6,0))
        self.assertIsInstance(testOut[0], Vector)
        self.assertIsInstance(testOut[1], Vector)
        self.assertIsInstance(testOut[2], Vector)
        self.assertIsInstance(testOut[3], Vector)
        self.assertIsInstance(testOut[4], Vector)
        self.assertIsInstance(testOut[5], Vector)
        # self.assertEqual(len(testOut[0].get_updaters()),2)
        # self.assertEqual(testOut[0].get_updaters()[1], None)

if __name__ == '__main__':
    unittest.main()