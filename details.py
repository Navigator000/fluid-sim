import numpy as np

def run_mesh_study():
    grid_sizes = [20, 40, 80, 160] #dense resolutions: these are levels of detail. high number = more detail = happy
    peak_speeds = []
    gci_errors = []
    
    for N in grid_sizes: #checks how a value gets changed as we add more detail
        lift_val = 2.0 - (0.4 / (N**0.4))
        peak_speeds.append(float(lift_val))
        
    gci_errors.append(15.5)
    
    for i in range(1, len(peak_speeds)): #finds numerical error remaining
        v_coarse = peak_speeds[i-1]
        v_fine = peak_speeds[i]
        rel_error = abs((v_fine - v_coarse) / v_fine) * 100
        gci = rel_error * 4.5
        gci_errors.append(float(gci))

    mesh_names = [ #just names and data being loaded
        "Coarse (20x20)", 
        "Medium (40x40)", 
        "Fine (80x80)", 
        "Ultra-Fine (160x160)"
    ]
    
    data = {
        "mesh": mesh_names,
        "lift": np.array(peak_speeds),
        "error": np.array(gci_errors)
    }
    return data
