module rngmodule

contains
        
	
        function rng(seed,aantalatomen,aantalstappen)
	    
            implicit none
            integer*8, intent(in)              :: seed,aantalatomen,aantalstappen 
	    integer*8, dimension(3*aantalatomen):: rng ! De output
	    integer*8, parameter    :: a=1478586353_8 !een willekeurig gekozen getal
    	    integer*8, parameter    :: b=1987654321_8 !een ander willekeurig gekozen getal
	    integer*8, parameter   :: m=2_8**31-1 
	    
	    integer*8	:: atomen,stappen,z
 	    integer*8, dimension(3*aantalatomen) ::x
      
            !kleine variant van de Middle Square Weyl Sequence PRNG
	    z = seed		
	    do stappen=1,aantalstappen
		do atomen=1,3*aantalatomen			
			rng(atomen) = modulo(z*z*a + b ,m)
			z = rng(atomen)			
		end do
	    end do

        end function rng

end module rngmodule
