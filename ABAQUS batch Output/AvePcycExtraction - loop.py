# -*- coding: utf-8 -*-
"""
Created on 29.07 16:30:07 2020

@author: littlelazy
"""
#Set Abaqus Environment
from odbAccess import *
from abaqusConstants import *
import numpy as np

#Open ODB and Output File
odb = openOdb(path="No_0_include.odb", readOnly=True)


#Select Nodes of Interest
ref_node=odb.rootAssembly.instances["PART-1-1"].nodeSets["REF"]
ref_Int=odb.rootAssembly.instances["PART-1-1"].elements[1]
lastFrame= odb.steps['Step-1'].frames[-1]
allelements=len(odb.rootAssembly.instances["PART-1-1"].elements)
print allelements


#determine number of cycles
displacement=[]
for frame in odb.steps['Step-1'].frames:
    for disp in frame.fieldOutputs['U'].getSubset(region=ref_node).values:
        val=disp.data[1] #displacement at each frame     
        displacement.append(val)
            
#find last cycle
CycleInd=[]            
for k in range(0, (len(displacement)-1)):
    if displacement[k-1]<displacement[k] and displacement[k+1]<displacement[k] :
        print "Cycle"
        CycleInd.append(k)      
    

#CycleInd.append(len(displacement)-1)


#number of cycles in analysis
numCycs=len(CycleInd)
print ("Number of Cycles: ",numCycs)


##initial value - doesnt matter because it will be overwritten
MaxElement1=MaxElement=odb.rootAssembly.instances["PART-1-1"].elements[1]
#
#


###############################################################################
#                   Last Cycle
###############################################################################
#Extract last 2 vals in CycleInd array to get last Cycle
for i in range(0,len(CycleInd)):
    Ind1=CycleInd[-(i+1)]
    Ind2=CycleInd[-(i)]



    p2=[]
    Frame1= odb.steps['Step-1'].frames[Ind1]
    Frame2= odb.steps['Step-1'].frames[Ind2]
    maxVal=0.0
    for i in range(0,(allelements)):
        ref_Int=odb.rootAssembly.instances["PART-1-1"].elements[i]
        for Value in Frame2.fieldOutputs['SDV146'].getSubset(region=ref_Int).values:
            p2.append(Value.data)
        # # establish location of max p (which element it occurs in) 
        # if Value.data > maxVal:
            # MaxElement=odb.rootAssembly.instances["PART-1-1"].elements[i]
            # for val in Frame1.fieldOutputs['COORD'].getSubset(region=MaxElement).values:
                # MaxElement1=odb.rootAssembly.instances["PART-1-1"].elements[i]

    p1=[]
    for i in range(0,(allelements)):    
        ref_Int=odb.rootAssembly.instances["PART-1-1"].elements[i]
        for Value in Frame1.fieldOutputs['SDV146'].getSubset(region=ref_Int).values:
            p1.append(Value.data)
    Avep2=np.mean(p2)
    Avep1=np.mean(p1)
    pCYC1=Avep2-Avep1

    # interested in mean value of pcyc - Averaged value
    print ('Averaged Pcyc difference per Cycle=', pCYC1)
#    print ('Element with max Pcyc:', MaxElement)




#odb.close()            
print('Post-Processing Complete')