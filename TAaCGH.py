########################################## CORE ####################################################################################
from subprocess import call
from subprocess import Popen
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

# Script Set : 2 
def Script2(ParameterFileUse):
    if(ParameterFileUse == True):
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ScriptParameters = Lines[2].split(" ") 
        ParameterFile.close()
        
        call('(cd Research/TAaCGH && R --vanilla --args '+ScriptParameters[1]+' '+ScriptParameters[2]+' '+ScriptParameters[3]+' '+ScriptParameters[4]+' '+ScriptParameters[5]+' < Research/TAaCGH/2_cgh_dictionary_cytoband.R)',shell=True)
        SetNumParts(ScriptParameters[2]) 
        SetSegLength(ScriptParameters[3])
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script2(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 2 ======================")
    else:
        DataSet = ""
        while(DataSet == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[2][0])
            print("Current Directories: "+str(next(os.walk("Research/Data"))[1]))
            DataSet = input("Please enter a valid data set: ")
            print(" ")
        print("\n\n")

        NumParts = ""
        while( type(NumParts) is not int):
            print("Help: "+ParameterHelp[2][1])
            NumParts = input("Please enter an integer for the NumParts parameter: ")
            try:
                NumParts = int(NumParts)
            except:
                pass
            print(" ")
        SetNumParts(NumParts)
        print("\n\n")

        Action = ""
        while(Action != "sections" and Action !='arms'):
            print("Help: "+ParameterHelp[2][4])
            Action = input("Please enter either \"sections\" or \"arms\" for the action parameter: ")
            print(" ")
        print("\n\n")

        SegLength = ""
        while(type(SegLength) is not int):
            print("Help: "+ParameterHelp[2][3])
            SegLength = input("Please enter an integer for the SegLength parameter: ")
            try:
                SegLength = int(SegLength)
            except:
                pass
            print(" ")
        SetSegLength(SegLength)
        print("\n\n")
        
        Subdir = input("Please enter the name for the subdir associated with this script(sect or arms or other): ")
        print(" ")
        print("\n\n")

        call('(cd Research/TAaCGH && R --vanilla --args '+DataSet+' '+str(NumParts)+' '+Action+' '+str(SegLength)+' '+Subdir+' < 2_cgh_dictionary_cytoband.R)',shell=True)
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script2(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 2 ======================")
 
def ClearScript2():
    OutputFound = []
    for i in next(os.walk('Research/Data'))[1]:
        CurrentSubDirects = next(os.walk('Research/Data/'+i))[1]

        for j in CurrentSubDirects:
            if ((i+'_sect_dict_cyto.txt') in next(os.walk('Research/Data/'+i+'/'+j))[2] or (i+'_arms_dict_cyto.txt') in next(os.walk('Research/Data/'+i+'/'+j))[2]):
                OutputFound.append(i+'/'+j)
    print("Output of Script 2 found in the following Research/Data directories: "+str(OutputFound))
    if(len(OutputFound)!=0):
        DeleteThis = MakeMenu(OutputFound,"Choose one directory to delete:")
        call("rm -r Research/Data/"+OutputFound[DeleteThis-1],shell=True)
        
    


# Script Set : 3
def Script3(ParameterFileUse):
    if(ParameterFileUse == True):
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ScriptParameters = Lines[3].split(" ") 
        ParameterFile.close()
        
        call('(cd Research/TAaCGH && R --slave --args '+ScriptParameters[1]+'  < 3_Transposed_aCGH.R)',shell=True)
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script3(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 3 ======================")
    else:
        DataSet = ""
        while(DataSet == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[3][0])
            print("Current Directories: "+str(next(os.walk("Research/Data"))[1]))
            DataSet = input("Please enter a valid data set: ")
            print(" ")
        print("\n\n")
        
        call('(cd Research/TAaCGH && R --slave --args '+DataSet+'  < 3_Transposed_aCGH.R)',shell=True)
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script3(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 3 ======================")
 

def ClearScript3():
    OutputFound = []
    for i in next(os.walk('Research/Data'))[1]:
        CurrentSubDirects = next(os.walk('Research/Data/'+i))[1]
        CurrentFiles =  next(os.walk('Research/Data/'+i))[2]

        if ((i+'_data.txt') in CurrentFiles):
            OutputFound.append(i)
    print("Output of Script 3 found in the following Research/Data directories: "+str(OutputFound))
    if(len(OutputFound)!=0):
        DeleteThis = MakeMenu(OutputFound,"Choose one directory to delete:")
        call("rm  Research/Data/"+OutputFound[DeleteThis-1]+"/"+OutputFound[DeleteThis-1]+"_data.txt",shell=True)
    

# Script Set : 3B
def Script3B(ParameterFileUse):
     if(ParameterFileUse == True):
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ScriptParameters = Lines[4].split(" ") 
        ParameterFile.close()
        
        call('(cd Research/TAaCGH && R --slave --args '+ScriptParameters[1]+' '+ScriptParameters[2]+' < 3b_dist_Q05.R)',shell=True)
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script3B(ParameterFileUse)
        else:
            CytoFile = open("Research/Data/"+DataSet+"/"+Subdir+"/"+DataSet+"_"+Subdir+"_dict_cyto.txt","r")
            CytoLines = CytoFile.readlines()
            MinOfAvg05 = float("inf")
            for i in range(0,len(CytoLines)):
                if i == 0:
                    continue
                else:
                    CytoLines[i] = CytoLines[i][:CytoLines[i].rindex('\t')] + CytoLines[i][CytoLines[i].rindex('\t')+1:] 
                    CytoLines[i] = CytoLines[i][:CytoLines[i].rindex('\t')] +'|'+CytoLines[i][CytoLines[i].rindex('\t')+1:] 

                    PossibleMin = float(CytoLines[i][CytoLines[i].rindex('\t')+1 : CytoLines[i].rindex('|')])
                    if(PossibleMin < MinOfAvg05):
                        MinOfAvg05 = PossibleMin 


            CytoFile.close()    
            SetEpsilon(MinOfAvg05)
                
            print("====================== COMPLETED SCRIPT 3B ======================")
     else:
        DataSet = ""
        while(DataSet == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[4][0])
            print("Current Directories: "+str(next(os.walk("Research/Data"))[1]))
            DataSet = input("Please enter a valid data set: ")
            print(" ")
        print("\n\n")
        
        Subdir = ""
        while(Subdir == "" or os.path.isdir('Research/Data/'+DataSet+'/'+Subdir) == False):
            print("Help: "+ParameterHelp[4][1])
            print("Current Directories: "+str(next(os.walk("Research/Data/"+DataSet))[1]))
            Subdir = input("Please enter a valid sub directory with the cyto dictonary files: ")
            print(" ")
        print("\n\n")
        
        call('(cd Research/TAaCGH && R --slave --args '+DataSet+' '+Subdir+' < 3b_dist_Q05.R)',shell=True)
        print("\n")
        
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script3B(ParameterFileUse)
        else:
            CytoFile = open("Research/Data/"+DataSet+"/"+Subdir+"/"+DataSet+"_"+Subdir+"_dict_cyto.txt","r")
            CytoLines = CytoFile.readlines()
            MinOfAvg05 = float("inf")
            for i in range(0,len(CytoLines)):
                if i == 0:
                    continue
                else:
                    CytoLines[i] = CytoLines[i][:CytoLines[i].rindex('\t')] + CytoLines[i][CytoLines[i].rindex('\t')+1:] 
                    CytoLines[i] = CytoLines[i][:CytoLines[i].rindex('\t')] +'|'+CytoLines[i][CytoLines[i].rindex('\t')+1:] 

                    PossibleMin = float(CytoLines[i][CytoLines[i].rindex('\t')+1 : CytoLines[i].rindex('|')])
                    if(PossibleMin < MinOfAvg05):
                        MinOfAvg05 = PossibleMin 


            CytoFile.close()    
            SetEpsilon(MinOfAvg05)

            print("====================== COMPLETED SCRIPT 3B ======================")
 

def ClearScript3B():
    OutputFound = []
    CurrentFiles = []
    for i in next(os.walk('Research/Data'))[1]:
        CurrentSubDirects = next(os.walk('Research/Data/'+i))[1]
        for j in CurrentSubDirects:      
            print('Research/Data/'+i+'/'+j+'/'+i+'_'+j+'_dict_cyto.txt')
            if( os.path.isfile('Research/Data/'+i+'/'+j+'/'+i+'_'+j+'_dict_cyto.txt')):
                CytoFile = open('Research/Data/'+i+'/'+j+'/'+i+'_'+j+'_dict_cyto.txt',"r")
                lines = CytoFile.readlines()
                if(len(lines[0].split('\t'))==10):
                    OutputFound.append('Research/Data/'+i+'/'+j+'/'+i+'_'+j+'_dict_cyto.txt')
                CytoFile.close()
            else:
                continue
         
    print("Output of Script 3B found in the following files: "+str(OutputFound))
    if len(OutputFound) != 0:
        DeleteThis = MakeMenu(OutputFound,"Choose one directory to clear 3B output")
        CytoFile = open(OutputFound[DeleteThis-1],"r+")
        Current_Lines = CytoFile.readlines()
        for i in range(0,len(Current_Lines)):
            Current_Lines[i] = '\t'.join(Current_Lines[i].split('\t')[0:7])+'\n'
        CytoFile.truncate(0)
        CytoFile.writelines(Current_Lines)
        CytoFile.close()



# Script Set : 4
def Script4(ParameterFileUse,UseDefaultEpsilon):
    # USE POPEN IN SUBPROCESS!!!
    if(ParameterFileUse == True):
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ScriptParameters = Lines[5].split(" ") 
        ParameterFile.close()
        Epsilon = ""
        if(not UseDefaultEpsilon):
             while( type(Epsilon) is not float):
                print("Help: "+ParameterHelp[5][3])
                Epsilon = input("Please enter an floating point for the Epsilon parameter: ")
                try:
                    Epsilon = float(Epsilon)
                except:
                    pass
        else:
            Epsilon = ScriptParameter[3]
        ScriptCalls = []
        for i in range(1,int(ScriptParameter[2])+1 ):
            ScriptCalls.append(Popen(['python','4_hom_stats_parts.py',ScriptParameter[0],ScriptParameter[1],str(i),str(Epsilon),ScriptParameter[4],],cwd='Research/TAaCGH',shell=False))
	
        for j in ScriptCalls:
            j.wait()
        
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script4(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 4 ======================")
    else:
        DataSet = ""
        while(DataSet == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[5][0])
            print("Current Directories: "+str(next(os.walk("Research/Data"))[1]))
            DataSet = input("Please enter a valid data set: ")
            print(" ")
        print("\n\n")


        HomDim = ""
        while(HomDim != 1 and HomDim!=2):
            print("Help: "+ParameterHelp[5][1])
            HomDim = input("Please enter a valid integer[1 or 2]: ")
            print(" ")
            try:
                HomDim = int(HomDim)
            except:
                pass
        print("\n\n")

        NumParts = ""
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ParameterFile.close()
        SkipStep = False
        if(len(Lines[12].split(" ")) == 2):
            print("Number of Parts is set to: "+str(Lines[12].split(" ")[1]))
            Option = MakeMenu(["Yes","No"],"Would you like to use this value[HIGHLY RECOMMENDED]?")
            if(Option == 1):
                NumParts = int(Lines[12].split(" ")[1].replace("\n",""))
                SkipStep = True
        
        if(SkipStep == False):
            while( type(NumParts) is not int):
                print("Help: "+ParameterHelp[5][2])
                NumParts = input("Please enter an integer for the NumParts parameter: ")
                try:
                    NumParts = int(NumParts)
                except:
                    pass
            print(" ")
            SetNumParts(NumParts)	
        print("\n\n")

        Epsilon = ""
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ParameterFile.close()
        SkipStep = False
        if(len(Lines[13].split(" ")) == 2):
            print("Epsilon is set to: "+str(Lines[13].split(" ")[1]))
            Option = MakeMenu(["Yes","No"],"Would you like to use this value[HIGHLY RECOMMENDED]?")
            if(Option == 1):
                Epsilon = float(Lines[13].split(" ")[1].replace("\n",""))
                SkipStep = True
        
        if(SkipStep == False):
            while( type(Epsilon) is not float):
                print("Help: "+ParameterHelp[5][3])
                Epsilon = input("Please enter an floating point for the Epsilon parameter: ")
                try:
                    Epsilon = float(Epsilon)
                except:
                    pass
            print(" ")
            SetEpsilon(Epsilon)
        print("\n\n")


        Action = ""
        while(Action != "sect" and Action !='arms'):
            print("Help: "+ParameterHelp[5][4])
            Action = input("Please enter either \"sect\" or \"arms\" for the action parameter: ")
            print(" ")
        print("\n\n")

        ScriptCalls = []
        for i in range(1,NumParts+1 ):
            ScriptCalls.append(Popen(['python','4_hom_stats_parts.py',DataSet,str(HomDim),str(i),str(round(Epsilon,2)),Action],cwd='Research/TAaCGH',shell=False))
	
        for j in ScriptCalls:
            j.wait()
        
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script4(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 4 ======================")
 

def ClearScript4():

    CytoFileHeaders = GetCytoFileStartAndEnd() # Format [ [dataset/sect_or_arms_etc.,start,end,Number of header lines],...   ]
    OutputFound = []
    for i in CytoFileHeaders:
        StartPart = i[1].split(",")
        EndPart = i[2].split(",")

        if(os.path.isfile("Research/Results/"+i[0]+"/2D/Homology/"+"B0_2D_"+i[0].replace("/","_")+"_"+StartPart[0]+StartPart[1]+"_seg"+StartPart[2]+".txt") and os.path.isfile("Research/Results/"+i[0]+"/2D/Homology/"+"B0_2D_"+i[0].replace("/","_")+"_"+EndPart[0]+EndPart[1]+"_seg"+EndPart[2]+".txt") ):
            OutputFound.append("Research/Results/"+i[0]+"/2D/Homology/")
        elif(os.path.isfile("Research/Results/"+i[0]+"/2D/Homology/"+"B1_2D_"+i[0].replace("/","_")+"_"+StartPart[0]+StartPart[1]+"_seg"+StartPart[2]+".txt") and os.path.isfile("Research/Results/"+i[0]+"/2D/Homology/"+"B1_2D_"+i[0].replace("/","_")+"_"+EndPart[0]+EndPart[1]+"_seg"+EndPart[2]+".txt") ):
            OutputFound.append("Research/Results/"+i[0]+"/2D/Homology/")

             
    if len(OutputFound) != 0:
       DeleteThis = MakeMenu(OutputFound,"Choose one directory to clear 4 output")
       call("rm -r "+OutputFound[DeleteThis-1],shell=True)        


# Script Set : 5
def Script5(ParameterFileUse):
      if(ParameterFileUse == True):
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ScriptParameters = Lines[6].split(" ") 
        ParameterFile.close()
        
        ScriptCalls = []
        for i in range(1,int(ScriptParameters[3])+1):
            ScriptCalls.append(Popen(['R','--vanilla',"--args",ScriptParameters[0], ScriptParameters[1] ,ScriptParameters[2] ,str(i),ScriptParameters[4] ,ScriptParameters[5] ,ScriptParameters[6], "<","5_sig_pcalc_parts.R"],cwd='Research/TAaCGH',shell=False))
	
        for j in ScriptCalls:
            j.wait()
        
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script5(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 5 ======================")
      else:
        Param = ""
        while(Param not in ("B0", "B1", "D", "CC")):
            print("Help: "+ParameterHelp[6][0])
            Param = input("Please enter a valid param: ")
            print(" ")
        print("\n\n")


        Phenotype = ""
        while(Phenotype == ""):
            print("Help: "+ParameterHelp[6][1])
            Phenotype = input("Please enter a valid phenotype: ")
            print(" ")
        print("\n\n")

        DataSet = ""
        while(DataSet == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[6][2])
            print("Current Directories: "+str(next(os.walk("Research/Data"))[1]))
            DataSet = input("Please enter a valid data set: ")
            print(" ")
        print("\n\n") 
        
        NumParts = ""
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ParameterFile.close()
        SkipStep = False
        if(len(Lines[12].split(" ")) == 2):
            print("Number of Parts is set to: "+str(Lines[12].split(" ")[1]))
            Option = MakeMenu(["Yes","No"],"Would you like to use this value[HIGHLY RECOMMENDED]?")
            if(Option == 1):
                NumParts = int(Lines[12].split(" ")[1].replace("\n",""))
                SkipStep = True
        
        if(SkipStep == False):
            while( type(NumParts) is not int):
                print("Help: "+ParameterHelp[6][3])
                NumParts = input("Please enter an integer for the NumParts parameter: ")
                try:
                    NumParts = int(NumParts)
                except:
                    pass
            print(" ")
            SetNumParts(NumParts)	
        print("\n\n")

        Action = ""
        while(Action != "sect" and Action !='arms'):
            print("Help: "+ParameterHelp[6][4])
            Action = input("Please enter either \"sect\" or \"arms\" for the action parameter: ")
            print(" ")
        print("\n\n")
        
        Outlier = ""
        while(Outlier == ""):
            print("Help: "+ParameterHelp[6][5])
            Outlier = input("Please enter a valid option for outlier: ")
            print(" ")
        print("\n\n") 

        Subdir = ""
        while(Subdir == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[6][6])
            Subdir = input("Please enter a valid subdir: ")
            print(" ")
        print("\n\n") 
        
        ScriptCalls = []
        for i in range(1,NumParts+1 ):
            ScriptCalls.append(Popen(['R --vanilla --args '+" ".join([Param,Phenotype,DataSet,str(i),Action,Outlier,Subdir])+" < 5_sig_pcalc_parts.R"],cwd='Research/TAaCGH',shell=True))
        for j in ScriptCalls:
            j.wait()
        
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script5(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 5 ======================")
 
        
def ClearScript5():
    OutputFound = []
    for i in next(os.walk('Research/Results'))[1]:
        if(os.path.isdir('Research/Results/'+i+'/significance/pvals')):
            OutputFound.append('Research/Results/'+i+'/significance/pvals')
        else:
            continue
             
    print("Output of Script 5 found in the following Research/Data directories: "+str(OutputFound))
    if(len(OutputFound)!=0):
        DeleteThis = MakeMenu(OutputFound,"Choose one directory to delete:")
        call("rm  -r "+ OutputFound[DeleteThis-1],shell=True)
    

# Script Set : 6
def Script6(ParameterFileUse):
   if(ParameterFileUse == True):
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ScriptParameters = Lines[7].split(" ") 
        ParameterFile.close()
        
        call("R --slave --args "+ScriptParameters[0]+" "+ScriptParameters[1]+" "+ScriptParameters[2]+" "+ScriptParameters[3]+" "+ScriptParameters[4]+" "+ScriptParameters[5]+" "+ScriptParameters[6]+"< 6_FDR.R",shell=True,cwd = "Research/TAaCGH")
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script6(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 6 ======================")
   else:
        File = ""
        while(File == ""):
            print("Help: "+ParameterHelp[7][0])
            File = input("Please enter a valid file: ")
            print(" ")
        print("\n\n")


        Parameter = ""
        while(Parameter == ""):
            print("Help: "+ParameterHelp[7][1])
            Parameter = input("Please enter a valid parameter: ")
            print(" ")
        print("\n\n")

        Phenotype = ""
        while(Phenotype == ""):
            print("Help: "+ParameterHelp[7][2])
            Phenotype = input("Please enter a valid phenotype: ")
            print(" ")
        print("\n\n") 
        
        NumParts = ""
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ParameterFile.close()
        SkipStep = False
        if(len(Lines[12].split(" ")) == 2):
            print("Number of Parts is set to: "+str(Lines[12].split(" ")[1]))
            Option = MakeMenu(["Yes","No"],"Would you like to use this value[HIGHLY RECOMMENDED]?")
            if(Option == 1):
                NumParts = int(Lines[12].split(" ")[1].replace("\n",""))
                SkipStep = True
        
        if(SkipStep == False):
            while( type(NumParts) is not int):
                print("Help: "+ParameterHelp[7][3])
                NumParts = input("Please enter an integer for the NumParts parameter: ")
                try:
                    NumParts = int(NumParts)
                except:
                    pass
            print(" ")
            SetNumParts(NumParts)	
        print("\n\n")

        Perm = ""
        while(Perm == ""):
            print("Help: "+ParameterHelp[7][4])
            Perm = input("Please enter a valid perm: ")
            print(" ")
        print("\n\n")
        
        Sig = ""
        while(Sig == ""):
            print("Help: "+ParameterHelp[7][5])
            Sig = input("Please enter a valid data set: ")
            print(" ")
        print("\n\n") 

        Subdir = ""
        while(Subdir == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[7][6])
            Subdir = input("Please enter a valid subdir: ")
            print(" ")
        print("\n\n") 
        

        call("R --slave --args "+File+" "+Parameter+" "+Phenotype+" "+NumParts+" "+Perm+" "+Sig+" "+Subdir +"< 6_FDR.R",shell=True,cwd = "Research/TAaCGH")
        
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script6(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 6 ======================")
 

def ClearScript6():
    DataSets = next(os.walk('Research/Data'))[1]
    SubDirects = [] # DataSet index correspondes to its subdirectory in subdirects list
    for i in DataSets:
        SubDirects.append(next(os.walk('Research/Data/'+i))[1])
    
    OutputFound = []
    for i in range(0,len(DataSets)):
        for j in SubDirects[i]:
            if(os.path.isfile('Research/Data/'+DataSets[i]+'/'+j+'/'+DataSets[i]+'_FDR.txt') and os.path.isfile('Research/Data/'+DataSets[i]+'/'+j+'/'+DataSets[i]+'_FDRsigtxt') ):
                    OutputFound.append('Research/Data/'+DataSets[i]+'/'+j+'/'+DataSets[i])

    if len(OutputFound) != 0:
        DeleteThis =  MakeMenu(OutputFound,"Choose one directory to delete:")
        call("rm "+OutputFound[DeleteThis-1]+"_FDR.txt",shell=True) 
        call("rm "+OutputFound[DeleteThis-1]+"_FDRsig.txt",shell=True) 


# Script Set : 7
def Script7(ParameterFileUse):
   if(ParameterFileUse == True):
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ScriptParameters = Lines[8].split(" ") 
        ParameterFile.close()
        
        call("R --slave --args "+ScriptParameters[0]+" "+ScriptParameters[1]+" "+ScriptParameters[2]+" "+ScriptParameters[3]+" "+ScriptParameters[4]+"< 7_vis_curves.R",shell=True,cwd = "Research/TAaCGH")
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script7(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 7 ======================")
   else:

        Parameter = ""
        while(Parameter != "B0" and Parameter != "B1"):
            print("Help: "+ParameterHelp[8][0])
            Parameter = input("Please enter a valid parameter: ")
            print(" ")
        print("\n\n")

        Phenotype = ""
        while(Phenotype == ""):
            print("Help: "+ParameterHelp[8][1])
            Phenotype = input("Please enter a valid phenotype: ")
            print(" ")
        print("\n\n") 
        
        DataSet = ""
        while(DataSet == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[8][2])
            print("Current Directories: "+str(next(os.walk("Research/Data"))[1]))
            DataSet = input("Please enter a valid data set: ")
            print(" ")
        print("\n\n") 
        
        Action = ""
        while(Action != "sect" and Action !='arms'):
            print("Help: "+ParameterHelp[8][3])
            Action = input("Please enter either \"sect\" or \"arms\" for the action parameter: ")
            print(" ")
        print("\n\n")
        
 
        Subdir = ""
        while(Subdir == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[8][4])
            Subdir = input("Please enter a valid subdir: ")
            print(" ")
        print("\n\n") 
        

        call("R --slave --args "+Parameter+" "+Phenotype+" "+DataSet+" "+Action+" "+Subdir +"<7_vis_curves.R",shell=True,cwd = "Research/TAaCGH")
        
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script7(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 7 ======================")
 
def ClearScript7():
    CurrentResults = next(os.walk('Research/Results'))[1]
    OutputFound = []
    for i in CurrentResults:
        CurrentSubDirects = next(os.walk('Research/Results/'+i))[1]
        for j in CurrentSubDirects:
            if(os.path.isdir('Research/Results/'+i+'/'+j+'/vis/curves/B0')):
                OutputFound.append('Research/Results/'+i+'/'+j+'/vis/curves/B0')
            elif(os.path.isdir('Research/Results/'+i+'/'+j+'/vis/curves/B1')):
                OutputFound.append('Research/Results/'+i+'/'+j+'/vis/curves/B1')

    if len(OutputFound) != 0:
        DeleteThis = MakeMenu(OutputFound,"Choose one directory to delete:")
        call("rm -r "+OutputFound[DeleteThis-1],shell=True)


# Script Set : 8 
def Script8(ParameterFileUse):
   if(ParameterFileUse == True):
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ScriptParameters = Lines[9].split(" ") 
        ParameterFile.close()
        
        call("R --slave --args "+ScriptParameters[0]+" "+ScriptParameters[1]+" "+ScriptParameters[2]+" "+ScriptParameters[3]+" "+ScriptParameters[4]+" "+ScriptParameters[5]+" "+ScriptParameter[6]+"< 8_probesFDR.R",shell=True,cwd = "Research/TAaCGH")
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script8(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 8 ======================")
   else:

        Parameter = ""
        while(Parameter != "B0" and Parameter != "B1"):
            print("Help: "+ParameterHelp[9][0])
            Parameter = input("Please enter a valid parameter: ")
            print(" ")
        print("\n\n")

        Phenotype = ""
        while(Phenotype == ""):
            print("Help: "+ParameterHelp[9][1])
            Phenotype = input("Please enter a valid phenotype: ")
            print(" ")
        print("\n\n") 
        
        DataSet = ""
        while(DataSet == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[9][2])
            print("Current Directories: "+str(next(os.walk("Research/Data"))[1]))
            DataSet = input("Please enter a valid data set: ")
            print(" ")
        print("\n\n") 
        
        Subdir = ""
        while(Subdir == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[9][3])
            Subdir = input("Please enter a valid subdir: ")
            print(" ")
        print("\n\n") 
        
        Perm = ""
        while( type(Perm) is not int):
            print("Help: "+ParameterHelp[9][4])
            Perm = input("Please enter an integer for the Perm parameter: ")
            try:
                Perm  = int(Perm)
            except:
                pass
            print(" ")
        print("\n\n")

        Sig = ""
        while( type(Sig) is not float):
            print("Help: "+ParameterHelp[9][5])
            Sig = input("Please enter an integer for the Sig parameter: ")
            try:
                Sig  = float(Sig)
            except:
                pass
            print(" ")
        print("\n\n")


        Seed  = ""
        while( type(Seed) is not int):
            print("Help: "+ParameterHelp[9][6])
            Seed = input("Please enter an integer for the Seed parameter: ")
            try:
                Seed = int(Seed)
            except:
                pass
            print(" ")
        print("\n\n")

        call("R --slave --args "+Parameter+" "+Phenotype+" "+DataSet+" "+Subdir+" "+str(Perm) +" "+str(Sig)+" "+str(Seed)+" <8_probesFDR.R",shell=True,cwd = "Research/TAaCGH")
        
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script8(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 8 ======================")

def ClearScript8():
    OutputFound = []
    for i in CurrentResults:
       #Results/SET/significance/pvals
       if( os.path.isfile('Research/Results/'+i+'/significance/pvals/'+i+'_Probes_FDR.txt') and os.path.isfile('Research/Results/'+i+'/significance/pvals/'+i+'_Probes_FDRsig.txt')):
           OutputFound.append(['Research/Results/'+i+'/significance/pvals/'+i+'_Probes_FDR.txt','Research/Results/'+i+'/significance/pvals/'+i+'_Probes_FDRsig.txt'])

    if len(OutputFound) != 0:
        DeleteThis = MakeMenu(OutputFound,"Choose one file group to delete:")
        call("rm "+OutputFound[DeleteThis-1][0] +" "+OutputFound[DeleteThis-1][1],shell=True)


 
# Script Set : 9 
def Script9(ParameterFileUse):
   if(ParameterFileUse == True):
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ScriptParameters = Lines[10].split(" ") 
        ParameterFile.close()
        
        call("R --slave --args "+ScriptParameters[0]+" "+ScriptParameters[1]+" "+ScriptParameters[2]+" "+ScriptParameters[3]+" "+ScriptParameters[4]+" "+ScriptParameters[5]+"< 9_mean_diff_perm_NoOut.R",shell=True,cwd = "Research/TAaCGH")
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script9(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 9 ======================")
   else:


        DataSet = ""
        while(DataSet == "" or os.path.isdir('Research/Data/'+DataSet) == False):
            print("Help: "+ParameterHelp[10][0])
            print("Current Directories: "+str(next(os.walk("Research/Data"))[1]))
            DataSet = input("Please enter a valid data set: ")
            print(" ")
        print("\n\n") 
 
        SegLength = ""
        ParameterFile = open("Parameter.txt","r")
        Lines = ParameterFile.readlines()
        ParameterFile.close()
        SkipStep = False
        if(len(Lines[14].split(" ")) == 2):
            print("SeglLength is set to: "+str(Lines[14].split(" ")[1]))
            Option = MakeMenu(["Yes","No"],"Would you like to use this value[HIGHLY RECOMMENDED]?")
            if(Option == 1):
                SegLength = int(Lines[14].split(" ")[1].replace("\n",""))
                SkipStep = True
        
        if(SkipStep == False):
            while( type(SegLength) is not int):
                print("Help: "+ParameterHelp[10][1])
                SegLength = input("Please enter an integer for the SegLength parameter: ")
                try:
                    SegLength = int(SegLength)
                except:
                    pass
            print(" ")
            SetSegLength(SegLength)	
        print("\n\n")


        Phenotype = ""
        while(Phenotype == ""):
            print("Help: "+ParameterHelp[10][2])
            Phenotype = input("Please enter a valid phenotype: ")
            print(" ")
        print("\n\n")

        
        Perm = ""
        while( type(Perm) is not int):
            print("Help: "+ParameterHelp[10][3])
            Perm = input("Please enter an integer for the Perm parameter: ")
            try:
                Perm  = int(Perm)
            except:
                pass
            print(" ")
        print("\n\n")

        Sig = ""
        while( type(Sig) is not float):
            print("Help: "+ParameterHelp[10][4])
            Sig = input("Please enter an integer for the Sig parameter: ")
            try:
                Sig  = float(Sig)
            except:
                pass
            print(" ")
        print("\n\n")


        Seed  = ""
        while( type(Seed) is not int):
            print("Help: "+ParameterHelp[10][5])
            Seed = input("Please enter an integer for the Seed parameter: ")
            try:
                Seed = int(Seed)
            except:
                pass
            print(" ")
        print("\n\n")

        call("R --slave --args "+DataSet+" "+SegLength+" "+Phenotype+" "+str(Perm)+" "+str(sig) +" "+str(Seed)+" <9_mean_diff_perm_NoOut.R",shell=True,cwd = "Research/TAaCGH")
        
        print("\n")
        RunAgain = MakeMenu(["Yes","No"],"Would you like to run again?")
        if(RunAgain == 1):
            Script9(ParameterFileUse)
        else:
            print("====================== COMPLETED SCRIPT 9 ======================")


def ClearScript9():
   OutputFound = []
   # List files in ~/Reseach/Results/SET/CenterMass
   for i in next(os.walk('Research/Results'))[1]:
        if(os.path.isdir('Research/Results/'+i+'/CenterMass')):
            OutputFound.append('Research/Results/'+i+'/CenterMass')
    
        if len(OutputFound) != 0:
            DeleteThis = MakeMenu(OutputFound,"Choose one directory to delete:")
            call("rm -r "+OutputFound[DeleteThis-1],shell=True)

# use List Comprehension for Script calls



ScriptCalls = {
        "Script2":Script2,
        "Script3":Script3,
        "Script3B":Script3B,
        "Script4":Script4,
        "Script5":Script5,
        "Script6":Script6,
        "Script7":Script7,
        "Script8":Script8,
        "Script9":Script9,
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
    ParameterFile.write("Script 1 not part of suite\n")
    for i in range(2,len(Line_Headers)-4):
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
    ParameterFile.write("10_class_pat_CM.R\n")
    ParameterFile.write("11_class_pat_seg.R\n")
    ParameterFile.write("NumParts: \n")
    ParameterFile.write("Epsilon: \n")
    ParameterFile.write("SegLength: \n")
    ParameterFile.close()

def ShowMenu():
    ParameterFile = open("Parameter.txt", "r")
    Lines = ParameterFile.readlines()
    #Script 1 -- USER CHOOSES TO RUN AS NOT A NECCESSARY SCRIPT --
    # Core Data Below --> For performance
    CytoFileHeaders = GetCytoFileStartAndEnd() # Format [ [dataset/sect_or_arms_etc.,start,end,Number of header lines],...   ]
    DataSets = next(os.walk('Research/Data'))[1]
    SubDirects = [] # DataSet index correspondes to its subdirectory in subdirects list
    CurrentFiles = [] # DataSet index correspondes to files in main data set folder
    CurrentResults = next(os.walk('Research/Results'))[1]
    for i in DataSets:
        SubDirects.append(next(os.walk('Research/Data/'+i))[1])
        CurrentFiles.append(next(os.walk('Research/Data/'+i))[2])


    #Script 2  --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    OutputFound = []
    for i in range(0,len(DataSets)):
              # "Chrom"  "Arm"  "Beg"  "End"  "Length"  "Segment"  
        for j in SubDirects[i]:
            if ((DataSets[i]+'_'+j+'_dict_cyto.txt') in next(os.walk('Research/Data/'+DataSets[i]+'/'+j))[2]):
                OutputFound.append(DataSets[i]+'/'+j)
    if len(OutputFound) == 0:
        print("First Script Is Not Part of the Suite"+'\n'+"[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[1])
    else:
        print("First Script Is Not Part of the Suite"+'\n'+"[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[1])
    
    #Script 3  --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    OutputFound = []
    for i in range(0,len(DataSets)):
        if ((DataSets[i]+'_data.txt') in CurrentFiles[i]):
            OutputFound.append(DataSets[i])
    if len(OutputFound) == 0:
        print("[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[2])
    else:
        print("[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[2])
    
    #Script 3B  -->  next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    # lines[0].split('\t')
    OutputFound = []
    for i in CytoFileHeaders:
        if( i[3] == 14):
            OutputFound.append(i[0]) 

    if len(OutputFound) == 0:
        print("[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[3])
    else:
        print("[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[3]) 
    #Script 4 --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    # Research/Results/horlings/sect/2D/Homology/ B0_2D_horlings_sect_2p_seg2.txt 
    OutputFound = []
    for i in CytoFileHeaders:
        StartPart = i[1].split(",")
        EndPart = i[2].split(",")

        if(os.path.isfile("Research/Results/"+i[0]+"/2D/Homology/"+"B0_2D_"+i[0].replace("/","_")+"_"+StartPart[0]+StartPart[1]+"_seg"+StartPart[2]+".txt") and os.path.isfile("Research/Results/"+i[0]+"/2D/Homology/"+"B0_2D_"+i[0].replace("/","_")+"_"+EndPart[0]+EndPart[1]+"_seg"+EndPart[2]+".txt") ):
            OutputFound.append(i[0])
        elif(os.path.isfile("Research/Results/"+i[0]+"/2D/Homology/"+"B1_2D_"+i[0].replace("/","_")+"_"+StartPart[0]+StartPart[1]+"_seg"+StartPart[2]+".txt") and os.path.isfile("Research/Results/"+i[0]+"/2D/Homology/"+"B1_2D_"+i[0].replace("/","_")+"_"+EndPart[0]+EndPart[1]+"_seg"+EndPart[2]+".txt") ):
            OutputFound.append(i[0])

             
    if len(OutputFound) == 0:
        print("[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[4])
    else:
        print("[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[4])
    #Script 5 --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    # ~/Research/Results/SET/significance/pvals
    OutputFound = []
    for i in CurrentResults:
        if(os.path.isdir('Research/Results/'+i+'/significance/pvals')):
            OutputFound.append('Result/'+i)
        else:
            continue
             
    if len(OutputFound) == 0:
        print("[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[5])
    else:
        print("[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[5])
   #Script 6 --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    OutputFound = []
    for i in range(0,len(DataSets)):
        for j in SubDirects[i]:
            if(os.path.isfile('Research/Data/'+DataSets[i]+'/'+j+'/'+DataSets[i]+'_FDR.txt') and os.path.isfile('Research/Data/'+DataSets[i]+'/'+j+'/'+DataSets[i]+'_FDRsigtxt') ):
                    OutputFound.append(DataSets[i]+"/"+j)

    if len(OutputFound) == 0:
        print("[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[6])
    else:
        print("[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[6])
   #Script 7 --> next(os.walk('./pythonTAaCGH'))[2] (Files but  1 is directories)
    OutputFound = []
    for i in CurrentResults:
        CurrentSubDirects = next(os.walk('Research/Results/'+i))[1]
        for j in CurrentSubDirects:
            if(os.path.isdir('Research/Results/'+i+'/'+j+'/vis/curves/B0') or os.path.isdir('Research/Results/'+i+'/'+j+'/vis/curves/B1')):
                OutputFound.append(i+"/"+j)

    if len(OutputFound) == 0:
        print("[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[7])
    else:
        print("[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[7])
   #Script 8 
    OutputFound = []
    for i in CurrentResults:
       #Results/SET/significance/pvals
       if( os.path.isfile('Research/Results/'+i+'/significance/pvals/'+i+'_Probes_FDR.txt') and os.path.isfile('Research/Results/'+i+'/significance/pvals/'+i+'_Probes_FDRsig.txt')):
           OutputFound.append(i+"/"+j)

    if len(OutputFound) == 0:
        print("[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[8])
    else:
        print("[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[8])
   #Script 9
    OutputFound = []
   # List files in ~/Reseach/Results/SET/CenterMass
    for i in CurrentResults:
        if(os.path.isdir('Research/Results/'+i+'/CenterMass')):
            OutputFound.append(os.walk('Research/Results/'+i+'/CenterMass')[2])
    
        if len(OutputFound) == 0:
            print("[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[9])
        else:
            print("[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[9])
    OutputFound = []
    OutputFound2 = []
   # Script 10
    for i in CurrentResults:
        if(os.path.isfile('Research/Data/'+i+'/'+i+'_phen.txt')):
            PhenFile = open('Research/Data/'+i+'/'+i+'_phen.txt','r')
            NumberOfCols = (PhenFile.readlines())[0].count('\t')+1
            PhenFile.close()
            if( NumberOfCols == 16):
                OutputFound.append(i)
            elif ( NumberOfCols == 17):
                OutputFound2.append(i)
        if len(OutputFound) == 0:
            print("[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[10])
        else:
            print("[OUTPUT FOUND IN: "+str(OutputFound)+"] --> "+Lines[10])
        
        if len(OutputFound2) == 0:
            print("[OUTPUT FILES MISSING - HAVE YOU RUN THE SCRIPT?] --> "+Lines[11])
        else:
            print("[OUTPUT FOUND IN: "+str(OutputFound2)+"] --> "+Lines[11])
            

    print(Lines[12]+'\n'+Lines[13])

    

    ParameterFile.close()

def ParameterFileExists():
    return os.path.exists("./Parameter.txt")


def SetNumParts(NewNum):
    ParameterFile = open("Parameter.txt","r+")
    Lines = ParameterFile.readlines()
    ParameterFile.truncate(0)
    Lines[12] = "NumParts: " + str(NewNum)+'\n'
    ParameterFile.writelines(Lines)
    ParameterFile.close()

def SetEpsilon(NewNum):
    ParameterFile = open("Parameter.txt","r+")
    Lines = ParameterFile.readlines()
    ParameterFile.truncate(0)
    Lines[13] = "Epsilon: " + str(NewNum)+'\n'
    ParameterFile.writelines(Lines)
    ParameterFile.close()

def SetSegLength(NewNum):
    ParameterFile = open("Parameter.txt","r+")
    Lines = ParameterFile.readlines()
    ParameterFile.truncate(0)
    Lines[14] = "SegLength: " + str(NewNum)+'\n'
    ParameterFile.writelines(Lines)
    ParameterFile.close()


def GetCytoFileStartAndEnd():
    # Format [ [dataset/sect_or_arms_etc.,start,end],...   ]
    Result = []
    for i in next(os.walk('Research/Data'))[1]:
        for j in next(os.walk('Research/Data/'+i))[1]:
            if(os.path.isfile('Research/Data/'+i+'/'+j+'/'+i+'_'+j+'_dict_cyto.txt')):
                CytoFile = open('Research/Data/'+i+'/'+j+'/'+i+'_'+j+'_dict_cyto.txt',"r")
                Lines = CytoFile.readlines()
                One = Lines[1].split('\t')
                Last = Lines[len(Lines)-1].split('\t')
                Result.append([i+'/'+j,One[0]+","+One[1][1]+","+One[5],Last[0]+","+Last[1][1]+","+Last[5],Lines[0].count('\t')+1])
                CytoFile.close()

    return Result
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
#Script2(False)
#call('cat Parameter.txt',shell=True)
#Script3(False)
#call('cat Parameter.txt',shell=True)
#Script3B(False)
#call('cat Parameter.txt',shell=True)
#GetCytoFileStartAndEnd()
#Script2(False)
#ClearScript2()
#ClearScript3B()
#ClearScript4()
#ShowMenu()
Script9(False)
