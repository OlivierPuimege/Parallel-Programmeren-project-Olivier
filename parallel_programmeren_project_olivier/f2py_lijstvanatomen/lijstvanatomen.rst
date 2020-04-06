This file documents a python module built from Fortran code with f2py.
You should document the Python interfaces, *NOT* the Fortran interfaces.

Module parallel_programmeren_project_olivier.lijstvanatomen
*********************************************************************

Module :py:mod:`lijstvanatomen` built from fortran code in :file:`f2py_lijstvanatomen/lijstvanatomen.f90`.

.. function:: add(x,y,z)
   :module: parallel_programmeren_project_olivier.lijstvanatomen
   
   Compute the sum of *x* and *y* and store the result in *z* (overwrite).

   :param x: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param y: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param z: 1D Numpy array with ``dtype=numpy.float64`` (output)
