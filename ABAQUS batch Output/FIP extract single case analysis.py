#Set Abaqus Environment
from odbAccess import *
from abaqusConstants import *
import numpy as np
#initial starting ID:
n = 0
os.chdir(r"V:\ABAQUS\Steel_174PH\79\Models") # need to change !!!
#Generate output text files
FIPFile = open("FIP_distri.txt","w")
#end point

#Open ODB and Output File
odb = openOdb(path="No_%d_include.odb" % n, readOnly=True)
#Select Nodes of Interest
ref_node=odb.rootAssembly.instances["PART-1-1"].nodeSets["REF"]
ref_Int=odb.rootAssembly.instances["PART-1-1"].elements[1]
lastFrame= odb.steps['Step-1'].frames[-1]
allelements=len(odb.rootAssembly.instances["PART-1-1"].elements)
#print allelements
##initial value - doesnt matter because it will be overwritten
MaxElement1=MaxElement=odb.rootAssembly.instances["PART-1-1"].elements[1]
#Extract last 2 vals in CycleInd array to get last Cycle, here define to be constant due to tensile load
Ind1=40
Frame1= odb.steps['Step-1'].frames[Ind1]
maxVal=0.0
#Write FIP into p1 list and use numpy to get maximum and mean value.
p1=[]
for i in range(0,(allelements)):    
ref_Int=odb.rootAssembly.instances["PART-1-1"].elements[i]
for Value in Frame1.fieldOutputs['SDV147'].getSubset(region=ref_Int).values:
p1.append(Value.data)
FIPFile.write("%8f" % (p1))

odb.close()

#Close files
FIPFile.close()
print('Fatigue Analysis Complete, check FIP.txt for the details')