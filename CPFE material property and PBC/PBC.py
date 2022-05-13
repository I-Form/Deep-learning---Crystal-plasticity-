# -*- coding: utf-8 -*-
"""
Created on 24.04.2020

@author: Yuhui
"""

#Generate strings with element numbers for sets
import csv
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
import random
import math 

#specify number of grains in model
NumInputs=3
displacement= 0.5# applied displacement

#Write new inputs in sequence.
for xx in range(0,NumInputs): 

#first empty files
open('"3D_" + str(xx) + "_step.inp"', 'w').close()
open('"3D_" + str(xx) + "_PBCs.inp"', 'w').close()
open('"3D_" + str(xx) + "_nodesets.inp"', 'w').close()
open('"3D_" + str(xx) + "_include.inp"', 'w').close()

InputFile="3D_" + str(xx) + "_nodes.inp"
PBCFile="3D_" + str(xx) + "_PBCs.inp"
SetFile="3D_" + str(xx) + "_nodesets.inp"
StepFile="3D_" + str(xx) + "_step.inp"
MatFile="3D_" + str(xx) + "_include.inp"

#Open input file and extract node data only)


with open(InputFile) as Data:
    f=Data.read()
err=0 #need this error counter to account for each line before*node
endIndex=0
y=0
for x in range(0,len(f)):
    if f[x]=='\n':
        err=err+1        
    if f[x]=='o' and f[x-1]=='N' and f[x-2]=='*':
        startIndex=x+err+1
        y=err
    if  f[x]=='*' and f[x-1]=='*':
        endIndex=x-113+y  # -113 because there is a comment at the end of the file and an additional node that doesnt fit 

with open(InputFile) as fin:
    fin.seek(startIndex)
    data = fin.read(endIndex- startIndex)
    
nodefile=open("nodefile.out",'w')
nodefile.write("%s" % data)
nodefile.close()
  




#Parameters=np.genfromtxt("Outputs.txt")
#numElements=int(Parameters[0])
#numSplitEls=int(Parameters[1])
Rows=[]

with open('nodefile.out', 'r') as f:
    reader = csv.reader(f, dialect='excel', delimiter=',')
    for row in reader:
#        print row
        Rows.append(row)
NodeLabels=[]
Xcoords=[]
Ycoords=[]        
Zcoords=[]
for x in range(0,len(Rows)):        
        label=int(Rows[x][0])
        xcoord=float(Rows[x][1])
        ycoord=float(Rows[x][2])
        zcoord=float(Rows[x][3])
        NodeLabels.append(label)
        Xcoords.append(xcoord)
        Ycoords.append(ycoord)
        Zcoords.append(zcoord)
        
Xmin=0
Ymin=0
Zmin=0
Xmax=int(max(Xcoords))
Ymax=int(max(Ycoords))
Zmax=int(max(Zcoords))  
#find nodes at free edges
FrontLFEycoords=[]
FrontLFEnodes=[]
FrontRFEycoords=[]
FrontRFEnodes=[]
FrontBFEnodes=[]
FrontBFExcoords=[]
FrontTFEnodes=[]
FrontTFExcoords=[]
BackLFEycoords=[]
BackLFEnodes=[]
BackRFEycoords=[]
BackRFEnodes=[]
BackBFEnodes=[]
BackBFExcoords=[]
BackTFEnodes=[]
BackTFExcoords=[]
BottomRightFEzcoords=[]
BottomLeftFEzcoords=[]
TopRightFEzcoords=[]
TopLeftFEzcoords=[]
BottomRightFEnodes=[]
BottomLeftFEnodes=[]
TopRightFEnodes=[]
TopLeftFEnodes=[]

Face1nodes=[]
Face1ycoords=[]
Face1xcoords=[]

Face2nodes=[]
Face2ycoords=[]
Face2zcoords=[]

Face3nodes=[]
Face3ycoords=[]
Face3xcoords=[]

Face4nodes=[]
Face4ycoords=[]
Face4zcoords=[]

Face5nodes=[]
Face5xcoords=[]
Face5zcoords=[]

Face6nodes=[]
Face6xcoords=[]
Face6zcoords=[]

#Find nodes at faces
for i in range (0,len(NodeLabels)):
        #FFace 1
    if Zcoords[i]==Zmin :
        node=NodeLabels[i]
        ycoord=Ycoords[i]
        xcoord=Xcoords[i]
        Face1nodes.append(node)
        Face1ycoords.append(ycoord)
        Face1xcoords.append(xcoord)
            #Face 2
    if Xcoords[i]==Xmin :
        node=NodeLabels[i]
        ycoord=Ycoords[i]
        zcoord=Zcoords[i]
        Face2nodes.append(node)
        Face2ycoords.append(ycoord)
        Face2zcoords.append(zcoord)
                #Face 3
    if Zcoords[i]==Zmax :
        node=NodeLabels[i]
        ycoord=Ycoords[i]
        xcoord=Xcoords[i]
        Face3nodes.append(node)
        Face3ycoords.append(ycoord)
        Face3xcoords.append(xcoord)  
        #face 4
    if Xcoords[i]==Xmax :
        node=NodeLabels[i]
        ycoord=Ycoords[i]
        zcoord=Zcoords[i]
        Face4nodes.append(node)
        Face4ycoords.append(ycoord)
        Face4zcoords.append(zcoord)
        #face 5
    if Ycoords[i]==Ymax :
        node=NodeLabels[i]
        zcoord=Zcoords[i]
        xcoord=Xcoords[i]
        Face5nodes.append(node)
        Face5xcoords.append(xcoord)
        Face5zcoords.append(zcoord)     
        #face 6
    if Ycoords[i]==Ymin :
        node=NodeLabels[i]
        zcoord=Zcoords[i]
        xcoord=Xcoords[i]
        Face6nodes.append(node)
        Face6xcoords.append(xcoord)
        Face6zcoords.append(zcoord)     
        














#n should possibly be n-1
for n in range (0,len(NodeLabels)):
    #Front Free Edges
    if Xcoords[n]==Xmin and Zcoords[n]==Zmin :
        node=NodeLabels[n]
        coord=Ycoords[n]
        FrontLFEnodes.append(node)
        FrontLFEycoords.append(coord)
    if Xcoords[n]==Xmax and Zcoords[n]==Zmin : #Should be limit of cell referencing previous file
        node1=NodeLabels[n]
        coord=Ycoords[n]
        FrontRFEnodes.append(node1)
        FrontRFEycoords.append(coord)
    if Ycoords[n]==Ymin and Zcoords[n]==Zmin : #Should be limit of cell referencing previous file
        node2=NodeLabels[n]
        coord=Xcoords[n]
        FrontBFEnodes.append(node2)
        FrontBFExcoords.append(coord)
    if Ycoords[n]==Ymax and Zcoords[n]==Zmin : #Should be limit of cell referencing previous file
        node3=NodeLabels[n]
        coord=Xcoords[n]
        FrontTFEnodes.append(node3)
        FrontTFExcoords.append(coord)
    #Back Free Edges    
    if Xcoords[n]==Xmin and Zcoords[n]==Zmax :
        node=NodeLabels[n]
        coord=Ycoords[n]
        BackLFEnodes.append(node)
        BackLFEycoords.append(coord)
    if Xcoords[n]==Xmax and Zcoords[n]==Zmax : #Should be limit of cell referencing previous file
        node1=NodeLabels[n]
        coord=Ycoords[n]
        BackRFEnodes.append(node1)
        BackRFEycoords.append(coord)
    if Ycoords[n]==Ymin and Zcoords[n]==Zmax : #Should be limit of cell referencing previous file
        node2=NodeLabels[n]
        coord=Xcoords[n]
        BackBFEnodes.append(node2)
        BackBFExcoords.append(coord)
    if Ycoords[n]==Ymax and Zcoords[n]==Zmax : #Should be limit of cell referencing previous file
        node3=NodeLabels[n]
        coord=Xcoords[n]
        BackTFEnodes.append(node3)
        BackTFExcoords.append(coord)
        
        
        
    if Ycoords[n]==Ymax and Xcoords[n]==Xmax : #Should be limit of cell referencing previous file
        node3=NodeLabels[n]
        coord=Zcoords[n]
        TopRightFEnodes.append(node3)
        TopRightFEzcoords.append(coord)
    if Ycoords[n]==Ymax and Xcoords[n]==Xmin : #Should be limit of cell referencing previous file
        node3=NodeLabels[n]
        coord=Zcoords[n]
        TopLeftFEnodes.append(node3)
        TopLeftFEzcoords.append(coord)   
    if Ycoords[n]==Ymin and Xcoords[n]==Xmin : #Should be limit of cell referencing previous file
        node3=NodeLabels[n]
        coord=Zcoords[n]
        BottomLeftFEnodes.append(node3)
        BottomLeftFEzcoords.append(coord) 
    if Ycoords[n]==Ymin and Xcoords[n]==Xmax : #Should be limit of cell referencing previous file
        node3=NodeLabels[n]
        coord=Zcoords[n]
        BottomRightFEnodes.append(node3)
        BottomRightFEzcoords.append(coord)             
print 'No. of nodes on Front left free edge:\n', len(FrontLFEnodes)        
print 'No. of nodes on Front right free edge:\n', len(FrontRFEnodes)        
print 'No. of nodes on Front top free edge:\n', len(FrontTFEnodes)        
print 'No. of nodes on Front bottom free edge:\n', len(FrontBFEnodes)  
print 'No. of nodes on Back left free edge:\n', len(BackLFEnodes)        
print 'No. of nodes on Back right free edge:\n', len(BackRFEnodes)        
print 'No. of nodes on Back top free edge:\n', len(BackTFEnodes)        
print 'No. of nodes on Back bottom free edge:\n', len(BackBFEnodes)  
     
#organise nodes in ascending order
#Sort left free edge
sLFEycoords=sorted(FrontLFEycoords)  
sLFEnodes=[]  
for y in range(0,len(sLFEycoords)):
    for j in range(0,len(FrontLFEycoords)):
        if sLFEycoords[y] == FrontLFEycoords[j]:
            node=FrontLFEnodes[j]
            sLFEnodes.append(node)
FrontLFEnodes=sLFEnodes #sorted in ascending order
FrontLFEycoords=sLFEycoords
#Sort right free edge
sRFEycoords=sorted(FrontRFEycoords)  
sRFEnodes=[]  
for y in range(0,len(sRFEycoords)):
    for j in range(0,len(FrontRFEycoords)):
        if sRFEycoords[y] == FrontRFEycoords[j]:
            node=FrontRFEnodes[j]
            sRFEnodes.append(node)
FrontRFEnodes=sRFEnodes #sorted in ascending order
FrontRFEycoords=sRFEycoords
#Sort top free edge        
sTFExcoords=sorted(FrontTFExcoords)  
sTFEnodes=[]  
for y in range(0,len(sTFExcoords)):
    for j in range(0,len(FrontTFExcoords)):
        if sTFExcoords[y] == FrontTFExcoords[j]:
            node=FrontTFEnodes[j]
            sTFEnodes.append(node)
FrontTFEnodes=sTFEnodes #sorted in ascending order
FrontTFExcoords=sTFExcoords     
#Sort bottom free edge        
sBFExcoords=sorted(FrontBFExcoords)  
sBFEnodes=[]  
for y in range(0,len(sBFExcoords)):
    for j in range(0,len(FrontBFExcoords)):
        if sBFExcoords[y] == FrontBFExcoords[j]:
            node=FrontBFEnodes[j]
            sBFEnodes.append(node)
FrontBFEnodes=sBFEnodes #sorted in ascending order
FrontBFExcoords=sBFExcoords 


#organise nodes in ascending order
#Sort left free edge
sLFEycoords=sorted(BackLFEycoords)  
sLFEnodes=[]  
for y in range(0,len(sLFEycoords)):
    for j in range(0,len(BackLFEycoords)):
        if sLFEycoords[y] == BackLFEycoords[j]:
            node=BackLFEnodes[j]
            sLFEnodes.append(node)
BackLFEnodes=sLFEnodes #sorted in ascending order
BackLFEycoords=sLFEycoords
#Sort right free edge
sRFEycoords=sorted(BackRFEycoords)  
sRFEnodes=[]  
for y in range(0,len(sRFEycoords)):
    for j in range(0,len(BackRFEycoords)):
        if sRFEycoords[y] == BackRFEycoords[j]:
            node=BackRFEnodes[j]
            sRFEnodes.append(node)
BackRFEnodes=sRFEnodes #sorted in ascending order
BackRFEycoords=sRFEycoords
#Sort top free edge        
sTFExcoords=sorted(BackTFExcoords)  
sTFEnodes=[]  
for y in range(0,len(sTFExcoords)):
    for j in range(0,len(BackTFExcoords)):
        if sTFExcoords[y] == BackTFExcoords[j]:
            node=BackTFEnodes[j]
            sTFEnodes.append(node)
BackTFEnodes=sTFEnodes #sorted in ascending order
BackTFExcoords=sTFExcoords     
#Sort bottom free edge        
sBFExcoords=sorted(BackBFExcoords)  
sBFEnodes=[]  
for y in range(0,len(sBFExcoords)):
    for j in range(0,len(BackBFExcoords)):
        if sBFExcoords[y] == BackBFExcoords[j]:
            node=BackBFEnodes[j]
            sBFEnodes.append(node)
BackBFEnodes=sBFEnodes #sorted in ascending order
BackBFExcoords=sBFExcoords 



#organise nodes in ascending order
sBottomLeftzcoords=sorted(BottomLeftFEzcoords)  
sLFEnodes=[]  
for y in range(0,len(sBottomLeftzcoords)):
    for j in range(0,len(sBottomLeftzcoords)):
        if sBottomLeftzcoords[y] == BottomLeftFEzcoords[j]:
            node=BottomLeftFEnodes[j]
            sLFEnodes.append(node)
BottomLeftFEnodes=sLFEnodes #sorted in ascending order
BottomLeftFEzcoords=sBottomLeftzcoords
#organise nodes in ascending order
sBottomRightzcoords=sorted(BottomRightFEzcoords)  
sLFEnodes=[]  
for y in range(0,len(sBottomRightzcoords)):
    for j in range(0,len(sBottomRightzcoords)):
        if sBottomRightzcoords[y] == BottomRightFEzcoords[j]:
            node=BottomRightFEnodes[j]
            sLFEnodes.append(node)
BottomRightFEnodes=sLFEnodes #sorted in ascending order
BottomRightFEzcoords=sBottomRightzcoords
#organise nodes in ascending order
sTopRightzcoords=sorted(TopRightFEzcoords)  
sLFEnodes=[]  
for y in range(0,len(sTopRightzcoords)):
    for j in range(0,len(sTopRightzcoords)):
        if sTopRightzcoords[y] == TopRightFEzcoords[j]:
            node=TopRightFEnodes[j]
            sLFEnodes.append(node)
TopRightFEnodes=sLFEnodes #sorted in ascending order
TopRightFEzcoords=sTopRightzcoords
#organise nodes in ascending order
sBottomLeftzcoords=sorted(BottomLeftFEzcoords)  
sLFEnodes=[]  
for y in range(0,len(sBottomLeftzcoords)):
    for j in range(0,len(sBottomLeftzcoords)):
        if sBottomLeftzcoords[y] == BottomLeftFEzcoords[j]:
            node=BottomLeftFEnodes[j]
            sLFEnodes.append(node)
BottomLeftFEnodes=sLFEnodes #sorted in ascending order
BottomLeftFEzcoords=sBottomLeftzcoords
#check for equal number of nodes on opposite free edges
if len(FrontLFEnodes)- len(FrontRFEnodes)==0 and len(FrontBFEnodes)-len(FrontTFEnodes)==0 and len(BackLFEnodes)- len(BackRFEnodes)==0 and len(BackBFEnodes)-len(BackTFEnodes)==0  :
    print '\nElement mesh is suitable for periodic BCs\n'  
else:
    print  '********** WARNING ********\nElement mesh is NOT suitable for periodic BCs'
    
#find corner nodes
for x in range(0,len(NodeLabels)):
    if Xcoords[x]==Xmin and Ycoords[x]==Ymin and Zcoords[x]==Zmin:
        FrontBLnode=NodeLabels[x]
    if Xcoords[x]==Xmin and Ycoords[x]==Ymax and Zcoords[x]==Zmin:
        FrontTLnode=NodeLabels[x]
    if Xcoords[x]==Xmax and Ycoords[x]==Ymax and Zcoords[x]==Zmin:
        FrontTRnode=NodeLabels[x]
    if Xcoords[x]==Xmax and Ycoords[x]==Ymin and Zcoords[x]==Zmin:
        FrontBRnode=NodeLabels[x]   
    if Xcoords[x]==Xmin and Ycoords[x]==Ymin and Zcoords[x]==Zmax:
        BackBLnode=NodeLabels[x]
    if Xcoords[x]==Xmin and Ycoords[x]==Ymax and Zcoords[x]==Zmax:
        BackTLnode=NodeLabels[x]
    if Xcoords[x]==Xmax and Ycoords[x]==Ymax and Zcoords[x]==Zmax:
        BackTRnode=NodeLabels[x]
    if Xcoords[x]==Xmax and Ycoords[x]==Ymin and Zcoords[x]==Zmax:
        BackBRnode=NodeLabels[x]       
print 'Front Bottom left node: ', FrontBLnode     
print 'Front Top left node: ', FrontTLnode  
print 'Front Top right node: ', FrontTRnode  
print 'Front Bottom right node: ', FrontBRnode
print 'Back Bottom left node: ', BackBLnode     
print 'Back Top left node: ', BackTLnode  
print 'Back Top right node: ', BackTRnode  
print 'Back Bottom right node: ', BackBRnode       




Edge1nodes=FrontRFEnodes
Edge2nodes=FrontBFEnodes
Edge3nodes=FrontLFEnodes
Edge4nodes=FrontTFEnodes
Edge5nodes=TopLeftFEnodes
Edge6nodes=BottomLeftFEnodes
Edge7nodes=BackLFEnodes
Edge8nodes=BackTFEnodes
Edge9nodes=BackRFEnodes
Edge10nodes=BackBFEnodes
Edge11nodes=TopRightFEnodes
Edge12nodes=BottomRightFEnodes
#Edge5nodes=Edge5nodes[::-1]
EdgeNodes=(Edge1nodes,Edge2nodes,Edge3nodes,Edge4nodes,Edge5nodes,Edge6nodes,Edge7nodes,Edge8nodes,Edge9nodes,Edge10nodes,Edge11nodes,Edge12nodes)
AllEdgeNodes=[]
for x in EdgeNodes:
    for n in x:
        AllEdgeNodes.append(n)
AllEdgeNodes = list(set(AllEdgeNodes))        
CN1=FrontBRnode
CN2=FrontBLnode
CN3=FrontTLnode
CN4=FrontTRnode
CN5=BackTLnode
CN6=BackBLnode
CN7=BackTRnode
CN8=BackBRnode




#remove corner nodes from face sets

Face1nodes.remove(CN1)
Face1nodes.remove(CN2)
Face1nodes.remove(CN3)
Face1nodes.remove(CN4)

Face2nodes.remove(CN6)
Face2nodes.remove(CN2)
Face2nodes.remove(CN3)
Face2nodes.remove(CN5)

Face3nodes.remove(CN6)
Face3nodes.remove(CN7)
Face3nodes.remove(CN8)
Face3nodes.remove(CN5)

Face4nodes.remove(CN4)
Face4nodes.remove(CN7)
Face4nodes.remove(CN8)
Face4nodes.remove(CN1)

Face5nodes.remove(CN3)
Face5nodes.remove(CN5)
Face5nodes.remove(CN7)
Face5nodes.remove(CN4)

Face6nodes.remove(CN2)
Face6nodes.remove(CN6)
Face6nodes.remove(CN1)
Face6nodes.remove(CN8)






##find matching nodes on each face


#face 1 and face 3
sFace3nodes=[]
sFace1nodes=[]
for j in range(0,len(Face3nodes)):
    for i in range(0,len(Face1nodes)):
        if  Face3ycoords[j]== Face1ycoords[i] and Face3xcoords[j]== Face1xcoords[i]:
            snode1=Face3nodes[j]
            snode2=Face1nodes[i]            
            sFace3nodes.append(snode1)
            sFace1nodes.append(snode2)
#face 2 and face 4
sFace2nodes=[]
sFace4nodes=[]
for j in range(0,len(Face4nodes)):
    for i in range(0,len(Face2nodes)):
        if  Face4ycoords[j]== Face2ycoords[i] and Face4zcoords[j]== Face2zcoords[i]:
            snode1=Face4nodes[j]
            snode2=Face2nodes[i]            
            sFace4nodes.append(snode1)
            sFace2nodes.append(snode2)            
#face 5 and face 6
sFace5nodes=[]
sFace6nodes=[]
for j in range(0,len(Face6nodes)):
    for i in range(0,len(Face5nodes)):
        if  Face6xcoords[j]== Face5xcoords[i] and Face6zcoords[j]== Face5zcoords[i]:
            snode1=Face6nodes[j]
            snode2=Face5nodes[i]            
            sFace6nodes.append(snode1)
            sFace5nodes.append(snode2)                 

Face1nodes=sFace1nodes
Face2nodes=sFace2nodes
Face3nodes=sFace3nodes
Face4nodes=sFace4nodes
Face5nodes=sFace5nodes
Face6nodes=sFace6nodes

print len(Face1nodes)
print len(Face2nodes)
print len(Face3nodes)
print len(Face4nodes)
print len(Face5nodes)
print len(Face6nodes)




 #create equation strings
Equationstring=""
#Replace the below:
#Face1PBC1='*EQUATION\n3\n    Face3,3,1,     CN6,3,-1,        Face1,3,-1\n'
#Face2PBC1='*EQUATION\n3\n    Face4,1,1,     CN1,1,-1,        Face2,1,-1\n'
#Face6PBC1='*EQUATION\n3\n    Face5,2,1,     CN3,2,-1,        Face6,2,-1\n'

#with:
for q in range(0,len(Face1nodes)):
    for k in range(0,len(Face3nodes)):
        if Xcoords[Face1nodes[q]-1] == Xcoords[Face3nodes[k]-1] and Ycoords[Face1nodes[q]-1] == Ycoords[Face3nodes[k]-1]:
            text='*EQUATION\n3\n    %s,3,1,  %s,3,-1,     %s,3,-1\n' %(Face3nodes[k],CN6,Face1nodes[q])
            Equationstring+=str(text)
for q in range(0,len(Face4nodes)):
    for k in range(0,len(Face2nodes)):
        if Ycoords[Face4nodes[q]-1] == Ycoords[Face2nodes[k]-1] and Zcoords[Face4nodes[q]-1] == Zcoords[Face2nodes[k]-1]:
            text='*EQUATION\n3\n    %s,1,1,  %s,1,-1,     %s,1,-1\n' %(Face4nodes[q],CN1,Face2nodes[k])
            Equationstring+=str(text)          
for q in range(0,len(Face5nodes)):
    for k in range(0,len(Face6nodes)):
        if Xcoords[Face5nodes[q]-1] == Xcoords[Face6nodes[k]-1] and Zcoords[Face5nodes[q]-1] == Zcoords[Face6nodes[k]-1]:
            text='*EQUATION\n3\n    %s,2,1,  %s,2,-1,     %s,2,-1\n' %(Face5nodes[q],CN3,Face6nodes[k])
            Equationstring+=str(text)            
            





#####################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################
#                                                       NEW PBCs for faces
######################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################

#create face sets wthout edge nodes    
Face1NEnodes=Face1nodes
Face2NEnodes=Face2nodes
Face3NEnodes=Face3nodes
Face4NEnodes=Face4nodes
Face5NEnodes=Face5nodes
Face6NEnodes=Face6nodes


#remove edge nodes from faces for next PBC

for i in AllEdgeNodes:
    try:
        Face1NEnodes.remove(i)
    except ValueError:
        pass
    try:
        Face2NEnodes.remove(i)
    except ValueError:
        pass
    try:
        Face3NEnodes.remove(i)
    except ValueError:
        pass
    try:
        Face4NEnodes.remove(i)
    except ValueError:
        pass
    try:
        Face5NEnodes.remove(i)
    except ValueError:
        pass
    try:
        Face6NEnodes.remove(i)
    except ValueError:
        pass    
    






 



#Replace the below:


#Face1PBC2='*EQUATION\n2\n    FaceNE3,2,1,     FaceNE1,2,-1\n'
#Face1PBC3='*EQUATION\n2\n    FaceNE3,1,1,     FaceNE1,1,-1\n'
#Face2PBC2='*EQUATION\n2\n    FaceNE4,2,1,     FaceNE2,2,-1\n'
#Face2PBC3='*EQUATION\n2\n    FaceNE4,3,1,     FaceNE2,3,-1\n'
#Face6PBC2='*EQUATION\n2\n    FaceNE5,1,1,     FaceNE6,1,-1\n'
#Face6PBC3='*EQUATION\n2\n    FaceNE5,3,1,     FaceNE6,3,-1\n'



#need to sort into order
for q in range(0,len(Face1NEnodes)-1):
    for k in range(0,len(Face3NEnodes)-1):
        if Xcoords[Face1NEnodes[q]-1] == Xcoords[Face3NEnodes[k]-1] and Ycoords[Face1NEnodes[q]-1] == Ycoords[Face3NEnodes[k]-1]:
            text1='*EQUATION\n2\n    %s,2,1,     %s,2,-1\n' %(Face3NEnodes[k],Face1NEnodes[q])
            text2='*EQUATION\n2\n    %s,1,1,     %s,1,-1\n' %(Face3NEnodes[k],Face1NEnodes[q])
            text=text1+text2
            Equationstring+=str(text)  
for k in range(0,len(Face5NEnodes)-1):
    for q in range(0,len(Face6NEnodes)-1):
        if Xcoords[Face5NEnodes[k]-1] == Xcoords[Face6NEnodes[q]-1] and Zcoords[Face5NEnodes[k]-1] == Zcoords[Face6NEnodes[q]-1]:
            text1='*EQUATION\n2\n    %s,1,1,     %s,1,-1\n' %(Face5NEnodes[k],Face6NEnodes[q])
            text2='*EQUATION\n2\n    %s,3,1,     %s,3,-1\n' %(Face5NEnodes[k],Face6NEnodes[q])
            text=text1+text2
            Equationstring+=str(text) 
for k in range(0,len(Face4NEnodes)-1):
    for q in range(0,len(Face2NEnodes)-1):
        if Zcoords[Face2NEnodes[q]-1] == Zcoords[Face4NEnodes[k]-1] and Ycoords[Face2NEnodes[q]-1] == Ycoords[Face4NEnodes[k]-1]:
            text1='*EQUATION\n2\n    %s,2,1,     %s,2,-1\n' %(Face4NEnodes[k],Face2NEnodes[q])
            text2='*EQUATION\n2\n    %s,3,1,     %s,3,-1\n' %(Face4NEnodes[k],Face2NEnodes[q])
            text=text1+text2
            Equationstring+=str(text)
            


           
            
#insert strings into input file    
#edit input file
#with open(PBCFile) as Data:
#    f=Data.read()  
#err=0
#StartIndex=0
#with open(PBCFile, "r+") as f:
#    f.seek(StartIndex)
#    data = f.read()
#f.close()      
#with open(PBCFile, "r+") as f:
#     old = f.read() # read everything in the file
#     f.seek(StartIndex) # rewind
#     f.write(Equationstring + data) # write the new line before        
# 

#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################



###############################################################################
###############################################################################
#                    PERIODIIC BOUNDARY CONDITIONS                            #
###############################################################################
###############################################################################    

#Apply periodic boundary conditions to each face of RVE

#Face 1

#Ensure the left and right sides do not rotate with respect to each other
Face1textstring=""
for k in range(1,len(Edge3nodes)-1): #neglect corner nodes
    text='*EQUATION\n3\n    %s,1,1,     %s,1,-1,        %s,1,-1\n' %(Edge1nodes[k],CN1,Edge3nodes[k])
    Face1textstring+=str(text) # concatenate strings
#Ensure the top and bottom sides do not rotate with respect to each other
for k in range(1,len(Edge4nodes)-1): #neglect corner nodes
    text='*EQUATION\n3\n    %s,2,1,     %s,2,-1,        %s,2,-1\n' %(Edge4nodes[k],CN3,Edge2nodes[k])
    Face1textstring+=str(text) # concatenate strings
#Ensure left and right sides deform equally in the y direction (no shear)
for k in range(1,len(Edge3nodes)-1):
    text='*EQUATION\n2\n    %s,2,1,     %s,2,-1\n' %(Edge1nodes[k],Edge3nodes[k])
    Face1textstring+=str(text) # concatenate strings    
#Ensure top and bottom sides deform equally in the x direction (no shear)
for k in range(1,len(Edge4nodes)-1):
    text='*EQUATION\n2\n    %s,1,1,     %s,1,-1\n' %(Edge4nodes[k],Edge2nodes[k])
    Face1textstring+=str(text) # concatenate strings      
#Ensure corner nodes displace evenly in respective directions
Face1textstring+='*EQUATION\n 2\n   %s,2,1,     %s,2,-1\n' %(CN4,CN3)
Face1textstring+='*EQUATION\n 2\n   %s,1,1,     %s,1,-1\n' %(CN4,CN1)  
 
#create strings of node numbers for set creation
Face1string=""
count=0
for node in Face1nodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face1string+=a
    count=count+1    

Face2string=""
count=0
for node in Face2nodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face2string+=a
    count=count+1   
    
Face3string=""
count=0
for node in Face3nodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face3string+=a
    count=count+1        

Face4string=""
count=0
for node in Face4nodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face4string+=a
    count=count+1       

Face5string=""
count=0
for node in Face5nodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face5string+=a
    count=count+1       

Face6string=""
count=0
for node in Face6nodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face6string+=a
    count=count+1  




#create strings of node numbers for set creation
Face1NEstring=""
count=0
for node in Face1NEnodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face1NEstring+=a
    count=count+1    

Face2NEstring=""
count=0
for node in Face2NEnodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face2NEstring+=a
    count=count+1   
    
Face3NEstring=""
count=0
for node in Face3NEnodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face3NEstring+=a
    count=count+1        

Face4NEstring=""
count=0
for node in Face4NEnodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face4NEstring+=a
    count=count+1       

Face5NEstring=""
count=0
for node in Face5NEnodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face5NEstring+=a
    count=count+1       

Face6NEstring=""
count=0
for node in Face6NEnodes:
    if count<=10:        
        a=(str(node)+',')
    if count>10:
        a=(str(node) +',' + '\n')
        count=0
    Face6NEstring+=a
    count=count+1  

    
 
#Displacement BCs
FrontBRSET=('SET%s') %FrontBRnode
FrontBLSET=('SET%s') %FrontBLnode
FrontTRSET=('SET%s') %FrontTRnode
FrontTLSET=('SET%s') %FrontTLnode
BackBRSET=('SET%s') %BackBRnode
BackBLSET=('SET%s') %BackBLnode
BackTRSET=('SET%s') %BackTRnode
BackTLSET=('SET%s') %BackTLnode
#Pin BL node and fix TL node in x dircection and fix BR node in y direction
BC1=' ** BOUNDARY CONDITIONS \n *Boundary\n %s,1,3\n %s,3,3\n %s,2,3\n %s,1,1\n %s,2,2\n %s,1,2\n %s,3,3\n %s,1,1\n'  %(FrontBLSET,FrontTLSET,FrontBRSET,BackTLSET,BackBRSET, BackBLSET, FrontTRSET,FrontTLSET )
#Create set for application of cyclic displacement
SetforBCs='*Nset, nset=Ref \n %s,\n*Nset, nset=%s \n %s,\n*Nset, nset=%s \n %s,\n*Nset, nset=%s \n %s,\n*Nset, nset=%s \n %s,\n*Nset, nset=%s \n %s,\n*Nset, nset=%s \n %s,\n*Nset, nset=%s \n %s,\n' %(FrontTLnode,FrontBLSET,FrontBLnode,FrontTLSET,FrontTLnode,FrontBRSET,FrontBRnode,BackTLSET,BackTLnode,BackBRSET, BackBRnode,BackBLSET, BackBLnode, FrontTRSET,FrontTRnode  )
# sets for face nodes
Face1Set=('*Nset, nset=Face1 \n' + Face1string +'\n')
Face2Set=('*Nset, nset=Face2 \n' + Face2string+'\n')
Face3Set=('*Nset, nset=Face3 \n' + Face3string+'\n')
Face4Set=('*Nset, nset=Face4 \n' + Face4string+'\n')
Face5Set=('*Nset, nset=Face5 \n' + Face5string+'\n')
Face6Set=('*Nset, nset=Face6 \n' + Face6string+'\n')
# sets for face nodes without edge nodes
Face1NESet=('*Nset, nset=FaceNE1 \n' + Face1NEstring +'\n')
Face2NESet=('*Nset, nset=FaceNE2 \n' + Face2NEstring+'\n')
Face3NESet=('*Nset, nset=FaceNE3 \n' + Face3NEstring+'\n')
Face4NESet=('*Nset, nset=FaceNE4 \n' + Face4NEstring+'\n')
Face5NESet=('*Nset, nset=FaceNE5 \n' + Face5NEstring+'\n')
Face6NESet=('*Nset, nset=FaceNE6 \n' + Face6NEstring+'\n')
#sets for corner nodes
CN1Set=('*Nset, nset=CN1 \n' + (str(CN1)+'\n'))
CN2Set=('*Nset, nset=CN2\n' + (str(CN2)+'\n'))
CN3Set=('*Nset, nset=CN3\n' + (str(CN3)+'\n'))
CN4Set=('*Nset, nset=CN4 \n' + (str(CN4)+'\n'))
CN5Set=('*Nset, nset=CN5 \n' + (str(CN5)+'\n'))
CN6Set=('*Nset, nset=CN6 \n' + (str(CN6)+'\n'))
CN7Set=('*Nset, nset=CN7 \n' + (str(CN7)+'\n'))
CN8Set=('*Nset, nset=CN8 \n' + (str(CN8)+'\n'))
FaceSets=Face1Set + Face2Set + Face3Set + Face4Set+ Face5Set +Face6Set+Face1NESet + Face2NESet + Face3NESet + Face4NESet+ Face5NESet +Face6NESet
CNSets=CN1Set+CN3Set+CN3Set+CN4Set+CN5Set+CN6Set+CN7Set+CN8Set
#numElements=np.genfromtxt("Outputs.txt")
#SetforAllgrains='*Elset, elset=ALLgrains,instance=RVEInstance , generate\n 1, %s, 1 \n' %(int(numElements))

###############################################################################
###############################################################################
#                    PERIODIIC BOUNDARY CONDITIONS                            #
###############################################################################
###############################################################################    
Face1PBC1='*EQUATION\n3\n    Face3,3,1,     CN6,3,-1,        Face1,3,-1\n'
Face2PBC1='*EQUATION\n3\n    Face4,1,1,     CN1,1,-1,        Face2,1,-1\n'
Face6PBC1='*EQUATION\n3\n    Face5,2,1,     CN3,2,-1,        Face6,2,-1\n'



#corner node bcs
FaceCornerBC1='*EQUATION\n2\n    CN4,2,1,     CN3,2,-1\n'
FaceCornerBC2='*EQUATION\n2\n    CN5,2,1,     CN3,2,-1\n'
FaceCornerBC3='*EQUATION\n2\n    CN7,2,1,     CN3,2,-1\n'


#pbcs to prevent shear/rigid body rotation
Face1PBC2='*EQUATION\n2\n    FaceNE3,2,1,     FaceNE1,2,-1\n'
Face1PBC3='*EQUATION\n2\n    FaceNE3,1,1,     FaceNE1,1,-1\n'
Face2PBC2='*EQUATION\n2\n    FaceNE4,2,1,     FaceNE2,2,-1\n'
Face2PBC3='*EQUATION\n2\n    FaceNE4,3,1,     FaceNE2,3,-1\n'
Face6PBC2='*EQUATION\n2\n    FaceNE5,1,1,     FaceNE6,1,-1\n'
Face6PBC3='*EQUATION\n2\n    FaceNE5,3,1,     FaceNE6,3,-1\n'

Face1PBC=Face1PBC1+Face1PBC2+Face1PBC3
Face2PBC=Face2PBC1+Face2PBC2+Face2PBC3
Face6PBC=Face6PBC1+Face6PBC2+Face6PBC3


#edges in z direction - each node z disp = Edge6
TopString=""
for k in range(1,len(Edge6nodes)-1):
    text='*EQUATION\n2\n    %s,3,1,     %s,3,-1\n' %(Edge12nodes[k],Edge6nodes[k])
    TopString+=str(text)
for k in range(1,len(Edge6nodes)-1):
    text='*EQUATION\n2\n    %s,3,1,     %s,3,-1\n' %(Edge11nodes[k],Edge6nodes[k])
    TopString+=str(text)
for k in range(1,len(Edge6nodes)-1):
    text='*EQUATION\n2\n    %s,3,1,     %s,3,-1\n' %(Edge5nodes[k],Edge6nodes[k])
    TopString+=str(text)
    
for k in range(1,len(Edge2nodes)-1):
    text='*EQUATION\n2\n    %s,1,1,     %s,1,-1\n' %(Edge10nodes[k],Edge2nodes[k])
    TopString+=str(text)   
for k in range(1,len(Edge2nodes)-1):
    text='*EQUATION\n2\n    %s,1,1,     %s,1,-1\n' %(Edge8nodes[k],Edge2nodes[k])
    TopString+=str(text)    
for k in range(1,len(Edge2nodes)-1):
    text='*EQUATION\n2\n    %s,1,1,     %s,1,-1\n' %(Edge4nodes[k],Edge2nodes[k])
    TopString+=str(text)    
    
for k in range(1,len(Edge3nodes)-1):
    text='*EQUATION\n2\n    %s,2,1,     %s,2,-1\n' %(Edge1nodes[k],Edge3nodes[k])
    TopString+=str(text)    
for k in range(1,len(Edge3nodes)-1):
    text='*EQUATION\n2\n    %s,2,1,     %s,2,-1\n' %(Edge7nodes[k],Edge3nodes[k])
    TopString+=str(text)    
for k in range(1,len(Edge3nodes)-1):
    text='*EQUATION\n2\n    %s,2,1,     %s,2,-1\n' %(Edge9nodes[k],Edge3nodes[k])
    TopString+=str(text)        
    
#^^ to be written to before *End Instance    

##Ensure top and bottom sides deform equally in the y direction (no shear)
#TopString=""
#for k in range(1,len(Edge4nodes)-1):
#    text='*EQUATION\n2\n    %s,2,1,     %s,2,-1\n' %(Edge4nodes[k],CN3)
#    TopString+=str(text)
#for k in range(1,len(Edge5nodes)-1):
#    text='*EQUATION\n2\n    %s,2,1,     %s,2,-1\n' %(Edge5nodes[k],CN3)
#    TopString+=str(text)  
#for k in range(1,len(Edge8nodes)-1):
#    text='*EQUATION\n2\n    %s,2,1,     %s,2,-1\n' %(Edge8nodes[k],CN3)
#    TopString+=str(text)
#for k in range(1,len(Edge11nodes)-1):
#    text='*EQUATION\n2\n    %s,2,1,     %s,2,-1\n' %(Edge11nodes[k],CN3)
#    TopString+=str(text)       
#Concatenate into one text string
INPmods=""
SingleNodePBCS=()
Seq=(FaceCornerBC1, FaceCornerBC2, FaceCornerBC3) #,Face2PBC,Face6PBC
INPmods=INPmods.join(Seq)
  

#

#EDIT INPUT FILE - PBCss

#write PBCs


#insert strings into input file    
#edit input file
with open(PBCFile) as Data:
    f=Data.read()  
err=0
StartIndex=0
with open(PBCFile, "r+") as f:
    f.seek(StartIndex)
    data = f.read()
f.close()      
with open(PBCFile, "r+") as f:
     old = f.read() # read everything in the file
     f.seek(StartIndex) # rewind
     f.write(TopString+Equationstring+INPmods) # write the new line before        
 


#######################################################################################
#######################################################################################
#                       END OF PERIODIC BOUNDARY CONDITIONs
#######################################################################################
########################################################################################
#
#
########################################################################################
########################################################################################
##           $            Add sets to set file for application of BCs
########################################################################################

#add amplitude for cyclic loading
Amp='*Amplitude, name=Amp1, definition=EQUALLY SPACED, fixed interval=1.\n0.,              1.,              0.,             -1.,              0.,              1.,              0.,             -1.\n0.,              1.,              0.,             -1.,              0.,              1.,              0.,             -1.\n0.,              1.,              0.,             -1.,              0.,              1.,              0.,             -1.\n0.,              1.,              0.,             -1.,              0.,              1.,              0.,             -1.\n0.,              1.,              0.,             -1.,              0.,              1.,              0.,             -1.\n0.,              1.,              0.,             -1.,              0.,              1.,              0.,             -1.\n'

StartIndex=0
#Add sets to nodeset  file    
with open(SetFile) as Data:
    f=Data.read()
err=0

with open(SetFile, "r+") as f:
    f.seek(StartIndex)
    data = f.read()
f.close()      
with open(SetFile, "r+") as f:
     old = f.read() # read everything in the file
     f.seek(StartIndex) # rewind
     f.write(SetforBCs +FaceSets+CNSets +Amp ) # write the new line before        
 
#
########################################################################################
########################################################################################
##                       END OF SET addition
########################################################################################
#########################################################################################
#



################################################################################
##$ USER MATERIAL - INPUT FILE MODIFICATIONS    
################################################################################    
#################################################################################

#
##Generate summary input file
#
    
    DataCards=""
    m='**Heading\n'
    mat='"No"+ str(xx)\n'
    ElasticModulii1='"*Include, Input = 3D_" + str(xx) + "_nodes.inp" \n'
    ElasticModulii2='"*Include, Input = 3D_" + str(xx) + "_nodesets.inp"\n'
    ElasticModulii3='"*Include, Input = 3D_" + str(xx) + "_elems.inp"\n'
    PotAcSlipSys='"*Include, Input = 3D_" + str(xx) + "_elset.inp"\n'
    NormandSlipDir1=' "*Include, Input = 3D_" + str(xx) + "_sects.inp"\n'
    NormandSlipDir2=' "*Include, Input = 3D_" + str(xx) + "_PBCs.inp"\n'
    NormandSlipDir3=' "*Include, Input = 3D_" + str(xx) + "_elems.inp"\n'
    InitialOrientation1='"*Include, Input = 3D_" + str(xx) + "_Vectors.inp"\n'
    InitialOrientation2='"*Include, Input = 3D_" + str(xx) + "_step.inp"\n'
    RateDep1='**\n'
    RateDep2='** ----------------------------------------------------------------\n'
    RateDep3='**'
    Seq=(m,mat,ElasticModulii1,ElasticModulii2,ElasticModulii3,PotAcSlipSys,NormandSlipDir1,NormandSlipDir2,NormandSlipDir3,InitialOrientation1,InitialOrientation2,RateDep1,RateDep2,
                  RateDep3)
    DataCards=DataCards.join(Seq)
    #edit inp file

    StartIndex=0

    with open(MatFile, "r+") as f:
        f.seek(StartIndex)
        data = f.read()

    with open(MatFile, "r+") as f:
        old = f.read() # read everything in the file
        f.seek(StartIndex) # rewind
        f.write(DataCards+data) # write the new line before        

#########################################################################################
#


#################################################################################
###$ Create Step and apply BCs
#################################################################################    
##################################################################################

Stepstring='** STEP: Step-1\n*Step, name=Step-1, nlgeom=YES, inc=100000\n*Static\n0.001, 1., 1e-06, 0.1\n*Restart, write, frequency=0\n*Output, field, time interval=0.05\n*Node Output\nRF, U\n*Element Output, directions=YES\nS, SDV147 \n*Output, history, variable=PRESELECT\n'
EndStep='*End Step'
StartIndex=0
#Cyclic displacement
CycDisp='*Boundary\nRef, 2, 2, %s\n' % displacement
####edit INP file
with open(StepFile, "r+") as f:
    f.seek(StartIndex)
    data = f.read()
f.close()  
   
with open(StepFile, "r+") as f:
     old = f.read() # read everything in the file
     f.seek(StartIndex) # rewind
     f.write(Stepstring +CycDisp +BC1+EndStep) # write the new line before        
 
 


#
#print "\n\nFinshed Editing Input File\n\n"  
#
