#Set Abaqus Environment
from odbAccess import *
from abaqusConstants import *
import numpy as np

#initial starting ID:
n = 0
os.chdir(r"V:\ABAQUS\Steel_174PH\95\Models") # need to change !!!
#Generate output text files
aveFIPFile = open("aveFIP.txt","a+")
maxFIPFile = open("maxFIP.txt","a+")
#end point
while n <= 199:
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
	p2 = p1.copy()
	p2.sort(reverse=True)
    #print(p2[2])
	avep1=p2[2]
	maxp1=max(p1)
	aveFIPFile.write("%8f\n " % (avep1))
	maxFIPFile.write("%8f\n " % (maxp1))
	
	print('%d FIPs obtained' % n)
	odb.close()
	n=n+1

#Close files
aveFIPFile.close()
maxFIPFile.close()

print('Fatigue Analysis Complete, check FIP.txt for the details')