import numpy as np
def cdsim():
  x=np.linspace(-5,5,200)  #creation of grid
  y=np.linspace(-5,5,200) 
  X,Y=np.meshgrid(x,y) 
  
  R = 1.5 #this calculates fluid velocity at every instant
  rad_sq = X**2 + Y**2 + 0.1
  U = 1.0 - (R**2 * (X**2 - Y**2) / (rad_sq**2))
  V = - (R**2 * (2 * X * Y) / (rad_sq**2))
  
  inside_obstacle = (X**2 + Y**2) < R**2 #now we made it so that the obstacle (cylinder) is entirely empty
  U[inside_obstacle] = 0
  V[inside_obstacle] = 0
  
  spd = np.sqrt(U**2 + V**2) #overall fluid speed (scalar!)
  
  row_indices, col_indices = np.indices((200, 200))
  
  data={ #allows ggplot to work
        "x":X.flatten(),
        "y":Y.flatten(),
        "u":U.flatten(),
        "v":V.flatten(),
        "speed":spd.flatten(),
        "row":row_indices.flatten(),
        "col":col_indices.flatten()
  }
  return data
