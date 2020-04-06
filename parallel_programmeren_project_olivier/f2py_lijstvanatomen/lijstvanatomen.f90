!-------------------------------------------------------------------------------------------------
! Fortran source code for module parallel_programmeren_project_olivier.lijstvanatomen
!-------------------------------------------------------------------------------------------------
! Remarks:
!   . Enter Python documentation for this module in ``./lijstvanatomen.rst``.
!     You might want to check the f2py output for the interfaces of the C-wrapper functions.
!     It will be autmatically included in the parallel_programmeren_project_olivier documentation.
!   . Documument the Fortran routines in this file. This documentation will not be included
!     in the parallel_programmeren_project_olivier documentation (because there is no recent sphinx
!     extension for modern fortran.

subroutine add(x,y,z,n)
  ! Compute the
  !
  ! Python use:
  !    import Parallel-Programmeren-project-Olivier.lijstvanatomen as f90
  !    a      = np.array([1,2,3],dtype=np.float64)
  !    result = np.ndarray((2,), np.float64)
  !    f90.mean_and_stddev(result,a)
  !    avg = result[0]
  !    std = result[1]
    implicit none
  !-------------------------------------------------------------------------------------------------
    integer*4              , intent(in)    :: n
    real*8   , dimension(n), intent(in)    :: x,y
    real*8   , dimension(n), intent(inout) :: z
    ! intent is inout because we do not want to return an array to avoid needless copying
  !-------------------------------------------------------------------------------------------------
  ! declare local variables
    integer*4 :: i
  !-------------------------------------------------------------------------------------------------
    do i=1,n
        z(i) = x(i) + y(i)
    end do
end subroutine add

subroutine loopOverDeLijst(lijstVanAtomen,lengteLijst,dummy)
	!Dit zou over de lijst van atomen moeten loopen
	integer, intent(in) :: lengteLijst
	real(8), dimension(n,3),intent(in) :: lijstVanAtomen
	integer, intent(out) :: dummy

	do atoom1=1,lengteLijst
		do atoom2=1,lengteLijst
			if (atoom1 /= atoom2) then
				roep de Lennard-Jones potentiaal op van de pythonklasse lj.py
			else 
				pass
	end do
end subroutine loopOverDeLijst

	
