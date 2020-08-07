def story():
    print("""
WELCOME TO THE TOURNAMENT.
You have selected your fighter based on their special attributes and will now face your opponents in a fight to the DEATH.
Each turn you will have the opportunity to choose attack or use an item, and your opponent will be able to attack you.
After each round that you win, you will gain items that you can use to boost your health or give yourself extra attack power.
""")

def ending_story():
    print("""
    Peace out girl scout
    """)
    

def title():    
    print("""
    
@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@@@   @@@  @@@  @@@   @@@@@@   @@@       
@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@  @@@@ @@@  @@@@@@@@  @@@       
  @@!    @@!       @@!  @@@  @@! @@! @@!  @@!  @@!@!@@@  @@!  @@@  @@!       
  !@!    !@!       !@!  @!@  !@! !@! !@!  !@!  !@!!@!@!  !@!  @!@  !@!       
  @!!    @!!!:!    @!@!!@!   @!! !!@ @!@  !!@  @!@ !!@!  @!@!@!@!  @!!       
  !!!    !!!!!:    !!@!@!    !@!   ! !@!  !!!  !@!  !!!  !!!@!!!!  !!!       
  !!:    !!:       !!: :!!   !!:     !!:  !!:  !!:  !!!  !!:  !!!  !!:       
  :!:    :!:       :!:  !:!  :!:     :!:  :!:  :!:  !:!  :!:  !:!   :!:      
   ::     :: ::::  ::   :::  :::     ::    ::   ::   ::  ::   :::   :: ::::  
   :     : :: ::    :   : :   :      :    :    ::    :    :   : :  : :: : :  
                                                                             
                                                                             
@@@  @@@   @@@@@@   @@@@@@@@@@   @@@@@@@    @@@@@@   @@@@@@@                 
@@@  @@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@                 
@@!  !@@  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@    @@!                   
!@!  @!!  !@!  @!@  !@! !@! !@!  !@   @!@  !@!  @!@    !@!                   
@!@@!@!   @!@  !@!  @!! !!@ @!@  @!@!@!@   @!@!@!@!    @!!                   
!!@!!!    !@!  !!!  !@!   ! !@!  !!!@!!!!  !!!@!!!!    !!!                   
!!: :!!   !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!    !!:                   
:!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!    :!:                   
 ::  :::  ::::: ::  :::     ::    :: ::::  ::   :::     ::                   
 :   :::   : :  :    :      :    :: : ::    :   : :     :                    
                                                                                         
""")

def fight_text():
    print("""
                                             
@@@@@@@@  @@@   @@@@@@@@  @@@  @@@  @@@@@@@  
@@@@@@@@  @@@  @@@@@@@@@  @@@  @@@  @@@@@@@  
@@!       @@!  !@@        @@!  @@@    @@!    
!@!       !@!  !@!        !@!  @!@    !@!    
@!!!:!    !!@  !@! @!@!@  @!@!@!@!    @!!    
!!!!!:    !!!  !!! !!@!!  !!!@!!!!    !!!    
!!:       !!:  :!!   !!:  !!:  !!!    !!:    
:!:       :!:  :!:   !::  :!:  !:!    :!:    
 ::        ::   ::: ::::  ::   :::     ::    
 :        :     :: :: :    :   : :     :
 """)

def game_over():
    print("""
                                                                                       
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : :                                                                                                    
    """)

def victory():
    print("""
                                                               
@@@  @@@  @@@   @@@@@@@  @@@@@@@   @@@@@@   @@@@@@@   @@@ @@@  
@@@  @@@  @@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@ @@@  
@@!  @@@  @@!  !@@         @@!    @@!  @@@  @@!  @@@  @@! !@@  
!@!  @!@  !@!  !@!         !@!    !@!  @!@  !@!  @!@  !@! @!!  
@!@  !@!  !!@  !@!         @!!    @!@  !@!  @!@!!@!    !@!@!   
!@!  !!!  !!!  !!!         !!!    !@!  !!!  !!@!@!      @!!!   
:!:  !!:  !!:  :!!         !!:    !!:  !!!  !!: :!!     !!:    
 ::!!:!   :!:  :!:         :!:    :!:  !:!  :!:  !:!    :!:    
  ::::     ::   ::: :::     ::    ::::: ::  ::   :::     ::    
   :      :     :: :: :     :      : :  :    :   : :     :

""")

def fatality():
    print("""    

@@@ @@@   @@@@@@   @@@  @@@  @@@  @@@@@@@   @@@@@@@@  
@@@ @@@  @@@@@@@@  @@@  @@@   @@  @@@@@@@@  @@@@@@@@  
@@! !@@  @@!  @@@  @@!  @@@  @!   @@!  @@@  @@!       
!@! @!!  !@!  @!@  !@!  @!@       !@!  @!@  !@!       
 !@!@!   @!@  !@!  @!@  !@!       @!@!!@!   @!!!:!    
  @!!!   !@!  !!!  !@!  !!!       !!@!@!    !!!!!:    
  !!:    !!:  !!!  !!:  !!!       !!: :!!   !!:       
  :!:    :!:  !:!  :!:  !:!       :!:  !:!  :!:       
   ::    ::::: ::  ::::: ::       ::   :::   :: ::::  
   :      : :  :    : :  :         :   : :  : :: ::   
                                                      
                                                      
@@@@@@@   @@@@@@@@   @@@@@@   @@@@@@@                 
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@                
@@!  @@@  @@!       @@!  @@@  @@!  @@@                
!@!  @!@  !@!       !@!  @!@  !@!  @!@                
@!@  !@!  @!!!:!    @!@!@!@!  @!@  !@!                
!@!  !!!  !!!!!:    !!!@!!!!  !@!  !!!                
!!:  !!!  !!:       !!:  !!!  !!:  !!!                
:!:  !:!  :!:       :!:  !:!  :!:  !:!                
 :::: ::   :: ::::  ::   :::   :::: ::                
:: :  :   : :: ::    :   : :  :: :  :   

                """)

def loading():
    print("""
$$\                                $$\ $$\                                 
$$ |                               $$ |\__|                                
$$ |      $$$$$$\   $$$$$$\   $$$$$$$ |$$\ $$$$$$$\   $$$$$$\              
$$ |     $$  __$$\  \____$$\ $$  __$$ |$$ |$$  __$$\ $$  __$$\             
$$ |     $$ /  $$ | $$$$$$$ |$$ /  $$ |$$ |$$ |  $$ |$$ /  $$ |            
$$ |     $$ |  $$ |$$  __$$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |            
$$$$$$$$\\$$$$$$  |\$$$$$$$ |\$$$$$$$ |$$ |$$ |  $$ |\$$$$$$$ |$$\ $$\ $$\ 
\________|\______/  \_______| \_______|\__|\__|  \__| \____$$ |\__|\__|\__|
                                                     $$\   $$ |            
                                                     \$$$$$$  |            
                                                      \______/
                                                                                                    
""")