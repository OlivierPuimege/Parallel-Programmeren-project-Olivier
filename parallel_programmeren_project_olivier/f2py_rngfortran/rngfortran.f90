module rngmodule

contains
        
	
        function rng(seed)
	    
            implicit none
            integer*8 :: rng ! De output
	    integer*8, parameter    :: a=1478586353_8 !een willekeurig gekozen getal
    	    integer*8, parameter    :: b=1987654321_8 !een ander willekeurig gekozen getal
	    !integer*8, parameter   :: m=2_8**31-1 !De originele m
	    !integer*8, parameter    :: m=1/(2_8**31-1)
	    integer*8               :: seed !De input, deze waarde bepaalt alle volgende waardes.
	    integer*8               :: x
      
            ! modify the state
	    x = (a*seed*b+b)
	    
            !x = modulo( b*x+a, m )!formule van bert
            ! assign result
            rng = x

        end function rng

end module rngmodule
