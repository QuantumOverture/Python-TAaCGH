########################################## CORE ####################################################################################
from subprocess import call
import sys,readline
# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py --> getch() function only


def delete_lines(lines):
    for i in range(0,lines+1):
        #cursor up one line
        sys.stdout.write('\x1b[1A')
        #delete last line
        sys.stdout.write('\x1b[2K')


########################################### END OF CORE ############################################################################





################################################ SCRIPTS ###########################################################################
# Script Set : 1 
def Script1():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript1():
    pass

# Script Set : 2 
def Script2():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript2():
    pass

# Script Set : 3
def Script3():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript3():
    pass

# Script Set : 3B
def Script3B():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript3B():
    pass

# Script Set : 4
def Script4():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript4():
    pass

# Script Set : 5
def Script5():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript5():
    pass

# Script Set : 6
def Script6():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript6():
    pass

# Script Set : 7
def Script7():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript7():
    pass

# Script Set : 8 
def Script8():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript8():
    pass

# Script Set : 9 
def Script9():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript9():
    pass

# Script Set : 10 
def Script10():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript10():
    pass

# Script Set : 11
def Script11():
    call('ls',shell=True)
    test = input("Enter a file name ")
    call('cat '+test,shell=True)
def ClearScript11():
    pass

# use List Comprehension for Script calls

ScriptCalls = {
        "Script1":Script1,
        "Script2":Script2,
        "Script3":Script3,
        "Script3B":Script3B,
        "Script4":Script4,
        "Script5":Script5,
        "Script6":Script6,
        "Script7":Script7,
        "Script8":Script8,
        "Script9":Script9,
        "Script10":Script10,
        "Script11":Script11
} 



Line_Headers = [ "DO NOT USE THIS INDEX","1_impute_aCGH.R","2_cgh_dictionary_cytoband.R","3_Transposed_aCGH.R","3b_dist_Q05.R","4_hom_stats_parts.py","5_sig_pcalc_parts.R","6_FDR.R","7_vis_curves.R","8_probesFDR.R","9_mean_diff.perm.R","10_class_pat_CM.R","11_class_pat_seg.R","Script_4_run","Script_5_run"]


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

def MakeMenu(OptionList,Prompt):
    counter = 1
    for i in OptionList:
        print("Enter "+str(counter)+" for : "+i)
        counter+=1
    UserInput = input(Prompt+": ")
    try:
        UserInput = int(UserInput)
    except:
        pass
    counter = len(OptionList)+1
    while( type(UserInput) is not int or (UserInput<1 or UserInput>len(OptionList)) ):
        UserInput = input("[INCORRECT FORMAT OR OUT OF BOUND - PLEASE ENTER AGAIN]"+Prompt+": ")
        counter+=1
        try:
            UserInput = int(UserInput)
        except:
            pass
    delete_lines(counter)
    return int(UserInput)



################################################ END UTILITIES #######################################################################

########################################## MODES ####################################################################################
def Setup():
    print("SET UP STARTED")
    # Create Core Directories
    call('mkdir Research',shell=True)
    call('mkdir Research/Data',shell=True)
    DataSetNameSetup = MakeMenu(["Yes","No"],"Would you like to make a directory(or multiple directories) for a Data set(s) within the Data directory?")
    if(DataSetNameSetup == 1):
        ContinueMakingDirectories = True
        while( ContinueMakingDirectories ):
            Name = input("Please enter a name for the Data Set directory:")
            print("You Entered:" + Name)
            call('mkdir Research/Data/'+Name,shell=True)
            Option = MakeMenu(["Yes","No"], "Would you like to make more Data Set directories?")
            if(Option == 2):
                ContinueMakingDirectories = False
    
    call('mkdir Research/TAaCGH',shell=True)
    call('mkdir Research/Results',shell=True)


    # Add Read and Execute Permissions to Core Scripts (needed for cp command and running of scripts)
    call('chmod +rx TAaCGH-master_June_24_2019/1_impute_aCGH.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/2_cgh_dictionary_cytoband.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/3_Transposed_aCGH.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/3b_dist_Q05.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/4_hom_stats_parts.py',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/5_sig_pcalc_parts.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/6_FDR.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/7_vis_curves.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/8_probesFDR.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/9_mean_diff_perm_NoOut.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/10_class_pat_CM.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/11_class_pat_seg.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/functions_cgh.py',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/functions_data_processing.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/functions_io.py',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/functions_sig.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/plex.jar',shell=True)

    #chmod +rx TAaCGH-master_June_24_2019/Readme.pdf
    call('chmod +rx TAaCGH-master_June_24_2019/ind_prof_origpat_local_sect.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/ind_prof_origpat_local.R',shell=True)
    call('chmod +rx TAaCGH-master_June_24_2019/vis_avg_betti_curves.R',shell=True)

    # Copy files from downloaded directory to required directory
    call('cp TAaCGH-master_June_24_2019/1_impute_aCGH.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/2_cgh_dictionary_cytoband.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/3_Transposed_aCGH.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/3b_dist_Q05.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/4_hom_stats_parts.py Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/5_sig_pcalc_parts.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/6_FDR.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/7_vis_curves.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/8_probesFDR.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/9_mean_diff_perm_NoOut.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/10_class_pat_CM.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/11_class_pat_seg.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/functions_cgh.py Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/functions_data_processing.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/functions_io.py Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/functions_sig.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/plex.jar Research/TAaCGH',shell=True)
    #cp TAaCGH-master_June_24_2019/Readme.pdf Research/TAaCGH
    call('cp TAaCGH-master_June_24_2019/ind_prof_origpat_local_sect.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/ind_prof_origpat_local.R Research/TAaCGH',shell=True)
    call('cp TAaCGH-master_June_24_2019/vis_avg_betti_curves.R Research/TAaCGH',shell=True)
     #cp TAaCGH-master_June_24_2019/ Research/TAaCGH
    call('touch Parameter.txt',shell=True)
    
    SetupParameterFile() # neccessary for auto mode notification here as well
   

def RegularMode():  

    if (not ParameterFileExists()):
        print("PLEASE RUN THE SETUP COMMAND BEFORE RUNNING SCRIPTS!")

    #Example Script Call --> ScriptCalls["Script3B"]()
    while ( true ):
        ShowMenu() 
        # Make sure you clear the menu at correct times

        TargetScript =  ReadScriptTarget() # Will have a make menu call and outputs the script user wants to run and has animation telling user what scripts they should run --> outputs tuple that tell us whether user is running or clear the effects of a script
        if(TargetScript[0] == 'Run'):
            RunScript(TargetScript) # Error checking and script call --> call has saveprogress call when output is given
        elif (TargetScript[0] == 'Delete'):
            DeleteScript(TargetScript) # Delete trace of script
        elif( TargetScript[0] == 'Exit'):
            SaveProgress()
            exit(0)
        else:
            print("INCORRECT COMMAND")


def AutoMode():
  if (not ParameterFileExists()):
        print("PLEASE RUN THE SETUP COMMAND BEFORE RUNNING SCRIPTS!")

def Clear():
    FinalCheck = MakeMenu(["Yes","No"],"Are you sure you want to delete the Research folder (and all its contents) and Parameter.txt?")
    if( FinalCheck == 1):
        print("Deletion Started")
        call('rm -r Research',shell=True)
        call('rm Parameter.txt',shell=True)
        print("Deletion Complete")
    elif( FinalCheck == 2):
        print("Deletion Aborted")
        exit(0)

########################################## END OF MODES ####################################################################################


#Setup()
#RegularMode()
Clear()


