# Abaqus/CAE Release 2017 for CNN-CPFE job
# Author: 17235804 Yuhui

#Set Abaqus Environment
import odbAccess
from abaqus import *
from abaqusConstants import *
import numpy
import visualization
import xyPlot
import displayGroupOdbToolset as dgo


    
def find_cross_point(x,y,k,b):
    '''
    :param x: an array of x
    :param y: an array of y
    :param k: the slope of the line
    :param b: the intercept of the line
    :return: x_c and y_c, the coordinate of cross point
    '''
    if len(x) != len(y):
        exit("Error! The length of x and y are not equal!")
    l = len(x)
    pre = x[0]
    pre_value = y[0] - (x[0] * k + b)
    for i in range(1,l):
        now = x[i]
        now_value = y[i] - (x[i] * k + b)
        if now_value == 0:
            return x[i],y[i]
        elif now_value * pre_value > 0:
            pre = x[i]
            pre_value = y[i]
            continue
        elif now_value * pre_value < 0:
            k_fit = (y[i] - y[i-1])/(x[i]-x[i-1])
            b_fit = y[i] - x[i] * k_fit
            x_c = (b_fit - b) / (k - k_fit)
            y_c = k * (b_fit - b)/(k - k_fit) + b
            return x_c, y_c

if __name__ == "__main__":
            #initial starting ID:
    i = 0
    os.chdir(r"V:\ABAQUS\Steel_174PH\79\Models") # need to change !!!
    #Generate outputs file for CNN learning
    YieldFile = open("YieldStress.txt","a+")
    #end point
    while i <= 1:
        #job submission from inp
        mdb.JobFromInputFile(name='No_%d_include' % i, \
            inputFileName='V:\\ABAQUS\\Steel_174PH\\79\\Models\\No_%d_include.inp' % i, \
            type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, \
            memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, \
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, \
            userSubroutine='V:\\ABAQUS\\Steel_174PH\\79\\Models\\HuangUMAT-Kin-withstop.for', \
            scratch='', resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, \
            numDomains=4, activateLoadBalancing=False, multiprocessingMode=DEFAULT, \
            numCpus=4, numGPUs=0)
        mdb.jobs['No_%d_include' % i].submit(consistencyChecking=OFF)
        mdb.jobs['No_%d_include' % i].waitForCompletion()
        #export SDV147 contour plot
        odb = session.openOdb(name='V:/ABAQUS/Steel_174PH/79/Models/No_%d_include.odb' % i)
        session.viewports['Viewport: 1'].setValues( \
            displayedObject=odb)
        session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF, \
            title=OFF, state=OFF, annotations=OFF, compass=OFF)
        session.graphicsOptions.setValues(backgroundStyle=SOLID, \
            backgroundColor='#FFFFFF')
        session.viewports['Viewport: 1'].setValues(displayedObject=odb)
        session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
        session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=( \
            CONTOURS_ON_DEF, ))
        session.viewports['Viewport: 1'].view.fitView()
        session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable( \
            variableLabel='SDV147', outputPosition=INTEGRATION_POINT, )
        session.viewports['Viewport: 1'].view.setValues(nearPlane=246.852, \
            farPlane=321.068, width=146.168, height=92.4765, viewOffsetX=-19.7784, \
            viewOffsetY=-0.241455)
        session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
            outsideLimitsMode=SPECTRUM, minValue=0)
        session.printToFile(fileName='V:/ABAQUS/Steel_174PH/79/DM/Energy_%d' % i, \
            format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
        session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
            variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(
            INVARIANT, 'Mises'), )
        session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
            minAutoCompute=OFF, minValue=0)
        session.printToFile(fileName='V:/ABAQUS/Steel_174PH/79/DM/vonMises_%d' % i, \
            format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
        #calculate and write yield stress values.
        StressFile = open("CPStressTimetrace_%d.out" % i,"w")

        #ref_Node=odb.rootAssembly.nodeSets["REF"]
        ref_Node=odb.rootAssembly.instances["PART-1-1"].nodeSets["REF"]
        #Loop Through Each Frame in Step 1
        mySteps = odb.steps
        numSteps = len(mySteps)
        for currentFrame in mySteps["Step-1"].frames:
        #
        #Get Stress
            ALLSTRESS=[]
            for stressValue in currentFrame.fieldOutputs["RF"].getSubset(region=ref_Node).values:
        #If Statement to Probe just 1 int point
                Stress=(stressValue.data[1])/(100*1)  #surface area of the top surface RVE (x*y)
            #Write Result to File
                StressFile.write("%8f\n " % (Stress))

        StressFile.close()
        odb.close()
        y=[]
        y_file = open("CPStressTimetrace_%d.out" % i,"r")
        for line in y_file.readlines():
            line = line.strip()
            if len(line) != 0:
                y.append(float(line))
        x=[]
        x_file = open("CPStrainTimetrace.out","r")
        for line in x_file.readlines():
            line = line.strip()
            if len(line) != 0:
                x.append(float(line))

        k = (y[1]/x[1] + y[2]/x[2] + y[3]/x[3] + y[4]/x[4] + y[5]/x[5]) / 5
        b = -0.002 * k

        x_c, y_c = find_cross_point(x,y,k,b)
        Result = y_c
        YieldFile.write("%8f\n " % (Result))
        YieldFile.close()
        print('%d jobs finished' % i)
        #RVELength=100

        i = i + 1
        #close files
    

YieldFile.close()
print('Postprocessing Complete, check YieldStress.txt for the details')
##
#