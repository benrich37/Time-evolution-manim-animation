from manimlib import *
import numpy as np
import unittest
from movies.scenes.dysphoria import SpikyVector

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

class TestSpiky(unittest.TestCase):
    def test_shapes(self):
        testSpiky = SpikyVector(False,2,2,y_p)
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
        self.assertEqual(testSpiky.vec_track[0][0].get_value(), np.real(y_p[0]))
        testSpiky.set_tracker(0,1)
        self.assertEqual(testSpiky.vec_track[0][0].get_value(), np.real(y_p[0]))
        self.assertEqual(testSpiky.vec_track[0][1].get_value(), np.imag(y_p[0]))
        # testSpiky.set_tracker(1, 0)
        # self.assertEqual(testSpiky.vec_track[0][0].get_value(), np.real(y_p[0]))
        testSpiky.set_tracker(1, 1)
        self.assertEqual(testSpiky.vec_track[0][0].get_value(), np.real(y_p[0]))
        self.assertEqual(testSpiky.vec_track[0][1].get_value(), np.imag(y_p[0]))
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