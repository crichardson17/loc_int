#
# Wrapper to perform LOC integrations with standard Cloudy output
#

from reader import *
from integrator import *

#############################################

gridfile = '../data/lo_res_lrg.grd'
emisfile = '../data/cont_padova_5Myr_z_M0_6Z.abs_lin'
normline = 'INCI  4860A'

# Change to 'All' to print everything to file
lines_to_print = ['H  1  4861A','H  1  6563A','N  2  6584A','O  3  5007A']


alpha_start, alpha_end, alpha_step = -2.0, 2.0, 0.25
beta_start, beta_end, beta_step = -1.8, -0.6, 0.4

hden_lim = [2.0, 8.0]      # Limits given in the log
phi_lim = [18.0, 22.0]

#############################################

phi, hden, emisnames, emisdata, normdata, grid_size, num_of_lines = parser(gridfile,emisfile,normline)


ewdata = calc_ew(emisdata, normdata, normline, grid_size, num_of_lines)

"""
psi = calc_psi(phi[0], hden[0],
             alpha_start, alpha_end, alpha_step,
             beta_start, beta_end, beta_step)
"""

