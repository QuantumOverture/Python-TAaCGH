########################################## CORE ####################################################################################
from subprocess import call
import sys,readline,os
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


ParametersForEachScript = ["DO NOT USE THIS INDEX" ,"dataSet","dataSet numParts action segLength subdir", "dataSet","dataSet arms/sect","dataSet homDim partNum epsIncr action","param phenotype dataSet partNum action outliers subdir", "name_of_dataSet/file Parameter phenotype Parts Perm sig subdir","param phenotype dataSet action subdir","Parameter phenotype name_of_dataSet/file subdir perm sig seed","name_of_dataSet/file seglength phenotype permutation sig seed","Sorry, you need to manually edit this file","Sorry, you need to manually edit this file"]

ParameterHelp = ["DO NOT USE THIS INDEX",
#Script 1
[ "fileName without including the txt extension (e.g. \"set\")"],
#Script 2
["short name for dataSet (e.g. set)","number of parts to split the dictionary. Usually 8","arms, sections","Section size. In the case of arms --> fullarm, but segLength --> minimum number of probes to run a specific arm.","a directory within /dataSet dir to read the dictionaries.use arms if action=arms or sect if action=sections."],
#Script 3
["(sj, sim6, simC3 climent, etc.)"],
#Script 3B
["(sj, sim6, simC3 climent, etc.)","arms/sect"],
#Script 4
["(sj, climent, sim, etc.)","(usually 1 or 2, which computes B0 or (B0 and B1), respectively.","(a positive integer)","(usually 0.01 or 0.05)","(arms or sect) specify if you are running full arms or sections (as used in 2_cgh_dictionary_cytoband.R)"],
#Script 5
["(B0, B1, D, CC)","(ERBB2, basal, test, sim, etc)","(SET, etc)","(an integer with the part from the dictionary)","arms, sect (for sections)","yes, no","a directory within /dataSet dir to read the dictionaries"],
#Script 6
["Name of dataset/file","(B0, B1, etc)","(lumA, test, sim, rec, etc)","(in which the directory was split (TOTAL))","number of permutations used to modify 0 p-values (e.g. 1/10,000=0.0001, pvalue[0]=0.0001)","desired false discovery rate (fdr) for the significant sections","a directory within /file to send the results and read dictionaries, sig_pcalc files"],
#Script 7
["(B0, B1)","(ERBB2, basal, test, sim, etc)","(SET, etc)"," arms, sect (for sections)","(where the dictionaries where saved)"],
#Script 8
["(B0, B1, etc)","(lumA, test, sim, rec, etc)","Name of dataset/file","(where the dictionaries were saved and where the p-values were saved)","number of permutations used to modify 0 p-values","desired false discovery rate (fdr) for the sig. sections","any integer num for reproducible research"],
#Script 9
["Name of dataset/file"," Section size, use the same number used in the dictionary.This will be the minimum number of probes needed to run a specific arm","(lumA, rec, test, etc)","number of permutations used to modify 0 p-values","desired false discovery rate (fdr) for the significant sections","an integer as a seed to have reproducible research"]

]

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

def SetupParameterFile():
    ParameterFile = open("Parameter.txt","w")
    ParameterFile.write("PLEASE DO NOT EDIT THIS FINAL MANUALLY UNLESS YOU KNOW WHAT YOU ARE DOING!!\n")
    ParameterEdits = MakeMenu(["Yes","No"],"Would you like to pre-write the parameters for the scripts you will running[REQUIRED FOR AUTO MODE BUT NOT NECCESSARY FOR REGULAR MODE?")
    if( ParameterEdits == 1):
        EditEnabled = True
    else:
        EditEnabled = False
    
    for i in range(1,len(Line_Headers)-5):
        CurrentParameters = ParametersForEachScript[i].split(" ")
        ParameterFile.write(Line_Headers[i]+" ")
        if(EditEnabled):
            for j in range(0,len(CurrentParameters)):
                print(Line_Headers[i] +  ": Instructions -> " + ParameterHelp[i][j])
                Parameter = input("Please Enter Parameter for: "+CurrentParameters[j]+ " -> ")
                ParameterFile.write(Parameter+" ")
                print("\n")
            print("\n\n")
            ParameterFile.write("\n")
    ParameterFile.write("NumParts: \n")
    ParameterFile.write("Epsilon: \n")
    ParameterFile.write("Progress: \n")
    ParameterFile.close()

def ShowMenu():
    ParameterFile = open("Parameter.txt", "r")
    
    Lines = ParameterFile.readlines()
    #Script 1 -- USER CHOOSES TO RUN AS NOT A NECCESSARY SCRIPT --
    #for j in GetDataSetNames():
    #    if os.path("Research\Data\\"+j).index(j+"_lowess.txt") == -1:
    #        Lines[1] = "[OUTPUT FILE MISSING]"+Lines[1]
    #if param:

    #Script 2  --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    OutputFound = []
    for i in next(os.walk('Research/Data'))[1]:
        CurrentSubDirects = next(os.walk('Research/Data/'+i))[1]
               
        if('sect' in CurrentSubDirects):
            CurrentFiles =  next(os.walk('Research/Data/'+i+'/sect'))[2]
        elif('arms' in CurrentSubDirects):
            CurrentFiles =  next(os.walk('Research/Data/'+i+'/arms'))[2]
        else:
            continue
         
        if ((i+'_sect_dict_cyto.txt') in CurrentFiles or (i+'_arms_dict_cyto.txt') in CurrentFiles ):
            OutputFound.append(i)
    if len(OutputFound) == 0:
        Lines[2] = "[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[2]
    else:
        Lines[2] = "[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[2]
    
    #Script 3  --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    OutputFound = []
    for i in next(os.walk('Research/Data'))[1]:
        CurrentSubDirects = next(os.walk('Research/Data/'+i))[1]
        CurrentFiles =  next(os.walk('Research/Data/'+i))[2]

        if ((i+'_data.txt') in CurrentFiles):
            OutputFound.append(i)
    if len(OutputFound) == 0:
        Lines[3] = "[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[3]
    else:
        Lines[3] = "[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[3]
    
    #Script 3B  -->  next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    # lines[0].split('\t')
    OutputFound = []
    for i in next(os.walk('Research/Data'))[1]:
        CurrentSubDirects = next(os.walk('Research/Data/'+i))[1]
               
        if('sect' in CurrentSubDirects):
            CurrentFiles =  next(os.walk('Research/Data/'+i+'/sect'))[2]
            CytoFile = open("Research/Data/"+i+"/sect/"+i+"_sect_dict_cyto.txt","r")
        elif('arms' in CurrentSubDirects):
            CurrentFiles =  next(os.walk('Research/Data/'+i+'/arms'))[2]
            CytoFile = open("Research/Data/"+i+"/arms/"+i+"_arms_dict_cyto.txt","r")
        else:
            continue
         
        if (((i+'_sect_dict_cyto.txt') in CurrentFiles or (i+'_arms_dict_cyto.txt') in CurrentFiles)):
            lines = CytoFile.readlines()
            if(len(lines[0].split('\t'))==14):
                OutputFound.append(i)
        CytoFile.close()

    if len(OutputFound) == 0:
        Lines[4] = "[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[4]
    else:
        Lines[4] = "[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[4]
    #Script 4 --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    # ~/Research/Results/dataSet/action/2D/Homology/  (action: arms or sect)
    # ~/Research/Results/SET/2D/Homology/
    OutputFound = []
    for i in next(os.walk('Research/Results'))[1]:
        if(os.path.isdir('Research/Results/'+i+'/arms/2D/Homology') or os.path.isdir('Research/Results/'+i+'/sect/2D/Homology')):
            if(os.path.isdir('Research/Results/'+i+'/2D/Homology')):
                OutputFound.append('Results/'+i)
            else:
                continue
        else:
            continue
             
    if len(OutputFound) == 0:
        Lines[5] = "[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[5]
    else:
        Lines[5] = "[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[5]
    #Script 5 --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    # ~/Research/Results/SET/significance/pvals
    OutputFound = []
    for i in next(os.walk('Research/Results'))[1]:
        if(os.path.isdir('Research/Results/'+i+'/significance/pvals')):
            OutputFound.append('Result/'+i)
        else:
            continue
             
    if len(OutputFound) == 0:
        Lines[6] = "[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[6]
    else:
        Lines[6] = "[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[6]
   #Script 6 --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    OutputFound = []

            
    for i in Lines:
        print(i)

    

    

    ParameterFile.close()

def ParameterFileExists():
    return os.path.exists("./Parameter.txt")

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
    # meant to be run outside (directly) Research folder
    #Example Script Call --> ScriptCalls["Script3B"]()
    while ( true ):
        ShowMenu() 
        # Make sure you clear the menu at correct times

        TargetScript =  ReadScriptTarget() # Will have a make menu call and outputs the script user wants to run and has animation telling user what scripts they should run --> outputs tuple that tell us whether user is running or clear the effects of a script
        if(TargetScript[0] == 'Run'):
            RunScript(TargetScript) # Error checking and script call
        elif (TargetScript[0] == 'Delete'):
            DeleteScript(TargetScript) # Delete trace of script
        elif( TargetScript[0] == 'Exit'):
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
#Clear()
#SetupParameterFile() 
#print(ParameterFileExists())
ShowMenu()
