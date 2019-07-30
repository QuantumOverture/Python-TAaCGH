########################################## CORE ####################################################################################
import from subprocess import call
# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py --> getch() function only

#ScriptNumber = ["DO NOT USE THIS INDEX",Script1(),Script2(),Script3(),Script3B(),Script4(),Script5(),Script5(),Script6(),Script7(),Script8(),Script9(),Script10(),Script11()]

Line_Headers = [ "DO NOT USE THIS INDEX","1_impute_aCGH.R","2_cgh_dictionary_cytoband.R","3_Transposed_aCGH.R","3b_dist_Q05.R","4_hom_stats_parts.py","5_sig_pcalc_parts.R","6_FDR.R","7_vis_curves.R","8_probesFDR.R","9_mean_diff.perm.R","10_class_pat_CM.R","11_class_pat_seg.R","Script_4_run","Script_5_run"]

import sys, termios, tty, os, time
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
########################################### END OF CORE ############################################################################





################################################ SCRIPTS ###########################################################################
# sample set
def Script2():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript2():
    pass
# Also have function to clear stuff from screen and output R stuff into a file(with the subprocess capturing?) for screen removal
################################################ END OF SCRIPTS ###################################################################




################################################ UTILITIES #######################################################################
def ChooseSpecificScript():
    for i in range(1,len(Line_Headers)):
        print("Enter "+str(i)+" for: "+Line_Headers[i])

    print("")
    CurrentScript = input("Enter number corresponding to a script you want to run:")
    try:
        CurrentScript = int(CurrentScript)
    except ValueError:
        pass

    while( (type(CurrentScript) is str) or (CurrentScript<1 or CurrentScript>14) ):
        for i in range(1,len(Line_Headers)):
            print("Enter "+str(i)+" for: "+Line_Headers[i])

        print("")
        CurrentScript = input("Enter a number(between 1 and 14 inclusive) corresponding you want to run: ")
        try:
            CurrentScript = int(CurrentScript)
        except ValueError:
            pass
    ScriptNumber[CurrentScript]
    return CurrentScript # For saving your phase progress 

def MakeMenu():



################################################ END UTILITIES #######################################################################

########################################## MODES ####################################################################################
def RegularMode():
    counter = 1

    # While not for error checking
    while counter<14:
        print("Enter r for: run selected Script")
        print("Enter q for: Save and quit progress")
        print("Enter the number for the corresponding script you want to run")  
        Phase = input("Would you like to run "+ Line_Headers[counter])
########################################## END OF MODES ####################################################################################








