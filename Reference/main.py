####################################################
#
# Strucutre of looping instructionsets
#
####################################################

##########################
# Initial definitions
##########################

class main:
    def __init__(self):
        self.exit=0;

    def condition(self,main):
        if(main==True):
            self.exit=1
        else:
            self.exit=0

##########################
# Main loop
##########################
program = main()

while (program.exit==0): # Check to see if quit actions have been triggered
    program.condition(True) # process actions to change exit state
    time.sleep(1) # determine the refresh rate of the program IE how long it will try to run in the background
