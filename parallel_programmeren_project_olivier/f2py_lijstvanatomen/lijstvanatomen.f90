module f90

contains

	function lj(afstand)
		implicit None
		!Deze functie geeft de Lennard Jones potentiaal voor 2 atomen.
		!Deze functie heeft wel problemen als 2 atomen toevallig op dezelfde plek zitten, maar die kans is bijna 0,
		!en dan zou de configuratie toch weggegooit moeten worden.

		!variabelen
		real*8			:: afstand
		real*8			:: lj		!Output, de interactie energie tussen de twee atomen
		real*8			:: temp !Deze dient voor de tussenberekeningen.
			

		!function body
		!lj = 4.*((1./afstand)**12-(1./afstand)**6)
		temp = 1./afstand
		temp = temp*temp
		temp = temp*temp*temp
		lj = 4*temp*(temp-1.0)
		
	end function lj

	function loopOverDeLijst(lijstVanAtomen,lengteLijst)
		!Deze functie loopt over de lijst van atomen en geeft een totale energie voor de configuratie
		implicit None

		!variabelen
		integer*4, intent(in) 		  :: lengteLijst	 !De lengte van de lijstVanAtomen.
		real*8, dimension(3*lengteLijst),intent(in) :: lijstVanAtomen	 !De numpy lijst van atoomcoordinaten.
		real*8				  :: loopOverDeLijst 		 !De output van de functie

		integer*4			  :: atoom1,atoom2	 !Locale variabelen, geven het atoomnummer weer, uit de lijst.
		real*8 :: x1,y1,z1
		real*8 :: x2,y2,z2
		real*8 :: etot
		real*8 :: afstand
		!function body
		etot = 0
		do atoom1=1,lengteLijst
			x1 = lijstVanAtomen(atoom1)
			y1 = lijstVanAtomen(atoom1+lengteLijst)
			z1 = lijstVanAtomen(atoom1+lengteLijst*2)
			do atoom2=atoom1+1,lengteLijst
				x2 = lijstVanAtomen(atoom2)
				y2 = lijstVanAtomen(atoom2+lengteLijst)
				z2 = lijstVanAtomen(atoom2+lengteLijst*2)

				afstand = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
				etot = etot + lj(afstand)
			end do
		end do
		loopOverDeLijst = etot
		write(*,*) 'energie',etot
	end function loopOverDeLijst



end module f90
