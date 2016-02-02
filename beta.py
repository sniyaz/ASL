import numpy as np
from mayavi import mlab
import time 


def scalar(x, y, z):
	return x + 2*y + 3*z

x = np.array([1, 15, 30])
y = np.array([1, 15, 30])
z = np.array([1, 15, 30])


l = mlab.points3d(x, y, z, scalar, scale_factor=1)
mlab.show()

engine = mayavi.mlab.get_engine()
scene = engine.scene
vtk_scene = scene.scene
interactor = vtk_scene.interactor

while True:
	time.sleep(5.5)
	print(interactor.event_postion)