import numpy as np
from funcs.methods.misc import rgb_to_hex

red = np.array([[1],[0],[0]],dtype=complex)*(1/np.sqrt(2))
green = np.array([[0],[1],[0]],dtype=complex)*(1/np.sqrt(2))
blue = np.array([[0],[0],[1]],dtype=complex)*(1/np.sqrt(2))

im_blue = np.array([[0,0,0],[0,0,0],[0,0,1j]],dtype=complex)

sample_H = np.array([[3,0,0],[0,2,0],[0,0,6]],dtype=complex)

hat_mustache_H = np.array([
    [0,1,0],
    [1,0,1],
    [0,1,0]],dtype=complex)

mustache_H = np.array([
    [0,1,1j],
    [1,0,1],
    [-1j,1,0]],dtype=complex)

hat_vals, hat_U = np.linalg.eig(hat_mustache_H)
hat_U_dag = np.linalg.inv(hat_U)
hat_eig_0 = hat_U[0]
hat_eig_1 = hat_U[1]
hat_eig_2 = hat_U[2]
red_color = np.array([1,0,0])
green_color = np.array([0,1,0])
blue_color = np.array([0,0,1])

hat_0_red_overlap = np.dot(red_color,hat_U[0])
hat_1_red_overlap = np.dot(red_color,hat_U[1])
hat_2_red_overlap = np.dot(red_color,hat_U[2])
hat_0_green_overlap = np.dot(green_color,hat_U[0])
hat_1_green_overlap = np.dot(green_color,hat_U[1])
hat_2_green_overlap = np.dot(green_color,hat_U[2])
hat_0_blue_overlap = np.dot(blue_color,hat_U[0])
hat_1_blue_overlap = np.dot(blue_color,hat_U[1])
hat_2_blue_overlap = np.dot(blue_color,hat_U[2])

hat_0_color_array = np.abs(hat_U[0])
hat_1_color_array = np.abs(hat_U[1])
hat_2_color_array = np.abs(hat_U[2])

hex_blue = rgb_to_hex(3, 3, 252)
hex_red = rgb_to_hex(252, 3, 3)
hex_green = rgb_to_hex(3, 252, 3)

hat_0_hex_color = rgb_to_hex(int(256 * hat_0_color_array[0]), int(256 * hat_0_color_array[1]), int(256 * hat_0_color_array[2]))
hat_1_hex_color = rgb_to_hex(int(256 * hat_1_color_array[0]), int(256 * hat_1_color_array[1]), int(256 * hat_1_color_array[2]))
hat_2_hex_color = rgb_to_hex(int(256 * hat_2_color_array[0]), int(256 * hat_2_color_array[1]), int(256 * hat_2_color_array[2]))

sig_x = np.array([[0, 1],[1,0]])
sig_y = np.array([[0, -1j],[1j, 0]])
sig_z = np.array([[1, 0],[0, -1]])
z_vals, z_U = np.linalg.eig(sig_z)
x_vals, x_U = np.linalg.eig(sig_x)
y_vals, y_U = np.linalg.eig(sig_y)
z_U_dag = np.linalg.inv(z_U)
x_U_dag = np.linalg.inv(x_U)
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
