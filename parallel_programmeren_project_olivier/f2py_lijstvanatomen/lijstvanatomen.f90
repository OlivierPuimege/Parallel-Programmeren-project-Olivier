module f90

contains

	function lj(afstand)
		implicit None
		!Deze functie geeft de Lennard Jones potentiaal voor 2 atomen.
		!Deze functie heeft wel problemen als 2 atomen toevallig op dezelfde plek zitten, maar die kans is bijna 0,
		!en dan zou de configuratie toch weggegooit moeten worden.

		!variabelen
		real*8					:: afstand
	!	real*8	  			:: epsilo,sigma		!epsilon is een functie in fortran, daarom epsilo
		real*8					:: lj		!Output, de interactie energie tussen de twee atomen

		!function body
		lj = 4.*((1./afstand)**12-(1./afstand)**6)
		write(*,*) 'lj',afstand
	end function lj

	function loopOverDeLijst(lijstVanAtomen,lengteLijst)
	!	!Deze functie loopt over de lijst van atomen en geeft een totale energie voor de configuratie
		implicit None

		!variabelen
		integer*4, intent(in) 		  :: lengteLijst	 !De lengte van de lijstVanAtomen.
		real*8, dimension(lengteLijst,3),intent(in) :: lijstVanAtomen	 !De numpy lijst van atoomcoordinaten.
		real*8				  :: loopOverDeLijst 		 !De output van de functie

		integer*4			  :: atoom1,atoom2	 !Locale variabelen, geven het atoomnummer weer, uit de lijst.
		real*8 :: x1,y1,z1
		real*8 :: x2,y2,z2
		real*8 :: etot
		real*8 :: afstand
	!	!function body
		etot = 0
		do atoom1=1,lengteLijst
			x1 = lijstVanAtomen(atoom1,1)
			y1 = lijstVanAtomen(atoom1,2)
			z1 = lijstVanAtomen(atoom1,3)
			do atoom2=atoom1,lengteLijst
				x2 = lijstVanAtomen(atoom2,1)
				y2 = lijstVanAtomen(atoom2,2)
				z2 = lijstVanAtomen(atoom2,3)

				afstand = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
				etot = etot + lj(afstand)
			end do
		end do
		loopOverDeLijst = etot
	end function loopOverDeLijst

! de bedoeling is dat je alle interactieenergien van atoomparen optelt en de totale energie teruggeeft.
! Vermits dat één enkel getal is, kan je dat met een function doen ipv een subroutine. => deze dinges of de lj?
! als je het met een subroutine doet moet je uiteraard een real(8), intent(out) gebruiken.
end module f90