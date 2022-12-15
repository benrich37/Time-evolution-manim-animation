import numpy as np

from ref.hold_constants import x_vals, x_U, x_U_dag, y_vals, y_U, y_U_dag, \
    z_vals, z_U, z_U_dag, z_pert_vals, z_pert_U, z_pert_U_dag


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


def create_evolver(matrix,dt):
    norms = np.linalg.norm(matrix, axis=1)
    normed = matrix/norms
    eigenvalues, m_U = np.linalg.eig(normed)
    m_U_dag = np.linalg.inv(m_U)
    diag = np.diag(np.exp(-1j * dt * eigenvalues))
    return np.dot(m_U, np.dot(diag, m_U_dag))


def improper_evolver(matrix,dt):
    # Evolves without returning to the regular basis
    norms = np.linalg.norm(matrix, axis=1)
    normed = matrix/norms
    eigenvalues, m_U = np.linalg.eig(normed)
    m_U_dag = np.linalg.inv(m_U)
    diag = np.diag(np.exp(-1j * dt * eigenvalues))
    return diag
