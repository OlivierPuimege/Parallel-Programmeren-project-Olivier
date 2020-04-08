function lj(atoom1,atoom2) result(energie)
	!Deze functie geeft de Lennard Jones potentiaal voor 2 atomen.
	!Deze functie heeft wel problemen als 2 atomen toevallig op dezelfde plek zitten, maar die kans is bijna 0,
	!en dan zou de configuratie toch weggegooit moeten worden.
	
	!variabelen
	real*8, dimension(3), intent(in)	:: atoom1,atoom2	!Atoomnummers in de lijst
	real*8					:: afstand		!Locale variabele, geeft de afstand
	integer*4				:: epsilo,sigma		!epsilon is een functie in fortran, daarom epsilo
	real*8					:: x1,x2,y1,y2,z1,z2	!coördinaten voor de afstand
	real*8					:: energie		!Output, de interactie energie tussen de twee atomen
	
	!function body
	if (atoom1 /= atoom2) then
		x1 = atoom1(1)
		x2 = atoom2(1)

		y1 = atoom1(2)
		y2 = atoom2(2)

		z1 = atoom1(3)
		z2 = atoom2(3)

		afstand = ((x1-x2)**2.+(y1-y2)**2.+(z1-z2)**2.)**(1./2.)

		energie = 4.*epsilo*((sigma/afstand)**(1./12.)-(sigma/afstand)**(1./6.))

	else
		energie = 0 !Als de twee atomen dezelfde zijn, ik denk dat dit efficiënter is dan de loop ingewikkelder maken.

end function lj

function loopOverDeLijst(lijstVanAtomen,lengteLijst) result(etot)
	!Deze functie loopt over de lijst van atomen en geeft een totale energie voor de configuratie
	
	!variabelen
	integer*4, intent(in) 		  :: lengteLijst	 !De lengte van de lijstVanAtomen.
	real*8, dimension(n,3),intent(in) :: lijstVanAtomen	 !De numpy lijst van atoomcoordinaten.
	integer*4			  :: atoom1,atoom2	 !Locale variabelen, geven het atoomnummer weer, uit de lijst.
	real*8				  :: etot 		 !De output van de functie

	!function body	
	etot = 0 
	do atoom1=1,lengteLijst
		do atoom2=atoom1,lengteLijst
			etot = etot + lj(lijstVanAtomen(atoom1),lijstVanAtomen(atoom2)) 
	end do

end function loopOverDeLijst

! de bedoeling is dat je alle interactieenergien van atoomparen optelt en de totale energie teruggeeft.
! Vermits dat één enkel getal is, kan je dat met een function doen ipv een subroutine. => deze dinges of de lj?
! als je het met een subroutine doet moet je uiteraard een real(8), intent(out) gebruiken.
