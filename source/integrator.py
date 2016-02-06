#
# Calculate eq widths and spatial distribution function; integrate over LOC plane
#

from numpy import *

###########################################

def calc_ew(emisdata,normdata,normline,grid_size,num_of_lines):

    ewdata = zeros((len(emisdata[:,0]),len(emisdata[0,:])))

    if normline == 'INCI  4860A':
        norm_wl = 4860.0
    elif normline == 'INCI  1215A':
        norm_wl = 1215.0
    else:
        print "*** Normalization wavelength not recognized! ***"

    for i in range(0,grid_size):
        for j in range(0,num_of_lines):

            ewdata[i,j] = norm_wl*emisdata[i,j]/normdata[i]

    return ewdata

###########################################

def get_stepsizes(phi,hden):

    # Get phi and hden step sizes.
    # Not necessary if normalizing.

    for i in range(0, len(phi)):
        if phi[i+1] != phi[i]:
            phi_step = log10(phi[i+1])-log10(phi[i])
            break
        elif i == len(phi):
            "Phi step size not found!"
    
    for i in range(0, len(hden)):
        if hden[i+1] != hden[i]:
            hden_step = log10(hden[i+1])-log10(hden[i])
            break
        elif i == len(hden):
            "Hden step size not found!"

    return phi_step, hden_step

###########################################


def calc_psi(phi, hden, alpha, beta):
    
    # Evaluate the cloud distribution function at each grid point.
    # Psi is a returned array containing the cloud distribution
    # at each model grid point.

    psi = zeros((len(alpha),len(beta)))

    for i in range(0,len(alpha)):
        for j in range(0,len(beta)):
   
            psi[i,j] = (phi**alpha[i])*(hden**beta[j])
            
    return psi

###########################################

"""
def integrate(phi, hden, eq_widths, grid_size, num_of_lines,
              alpha_start, alpha_end, alpha_step,beta_start, beta_end, beta_step):

    # Integrate
    
    alpha = array(arange(alpha_start, alpha_end+alpha_step, alpha_step),float)
    beta = array(arange(beta_start, beta_end+beta_step, beta_step),float)
    
    for i in range(0, grid_size):
        for j in range(0, num_of_lines):

            if (log10(phi[i]) >= phi_lim[0] and log10(phi[i]) <= phi_lim[1] 
                and log10(hden[i]) >= hden_lim[0] and log10(hden[i]) <= hden_lim[1]):
        
                # This is WRONG! Don't sum over lines, sum over grid!!!
                
                psi = calc_psi(phi[i], hden[i], alpha, beta)
                lum_line = lum_line + eq_widths[i,j]*psi

                

    return
"""
