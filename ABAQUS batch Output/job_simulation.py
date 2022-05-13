# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by 15540847 on Fri Nov  9 14:12:25 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=241.399993896484, 
    height=229.216659545898)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('D:\FYP\Computational modelling\ABAQUS_6\Iterative_simulation2.cae')
#: The model database "E:\FYP\Computational modelling\ABAQUS_6\Iterative_simulation2.cae" has been opened.
i = 49
os.chdir('D:\FYP\Computational modelling\ABAQUS_6')
while i <= 80:
    mdb.Job(name='JOB_%d' % i, model='Model-%d' % i, description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='D:/FYP/Computational modelling/ABAQUS_6', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
        numGPUs=0)
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p = mdb.models['Model-%d' % i].parts['Part1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    a = mdb.models['Model-%d' % i].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    mdb.jobs['JOB_%d' % i].submit(consistencyChecking=OFF)
    #: The job input file "JOB_1.inp" has been submitted for analysis.
    #: Job JOB_1: Analysis Input File Processor completed successfully.
    #: Job JOB_1: Abaqus/Standard completed successfully.
    #: Job JOB_1 completed successfully.
    mdb.jobs['JOB_%d' % i].waitForCompletion()
    o3 = session.openOdb(name='D:/FYP/Computational modelling/ABAQUS_6/JOB_%d.odb' % i)
    #: Model: E:/FYP/Computational modelling/ABAQUS_6/JOB_1.odb
    #: Number of Assemblies:         1
    #: Number of Assembly instances: 0
    #: Number of Part instances:     1
    #: Number of Meshes:             2
    #: Number of Element Sets:       3
    #: Number of Node Sets:          8
    #: Number of Steps:              1
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=130.724, 
        farPlane=199.61, width=81.1455, height=45.7914, viewOffsetX=7.63632, 
        viewOffsetY=-1.40189)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=130.6, 
        farPlane=203.647, width=81.0686, height=45.7479, cameraPosition=(30.551, 
        -127.089, 141.758), cameraUpVector=(-0.132916, 0.848501, 0.512229), 
        cameraTarget=(-3.37075, -4.15431, 36.7989), viewOffsetX=7.62908, 
        viewOffsetY=-1.40056)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=136.873, 
        farPlane=196.466, width=84.9623, height=47.9452, cameraPosition=(-10.1171, 
        -148.054, 113.428), cameraUpVector=(0.267677, 0.701717, 0.660259), 
        cameraTarget=(-3.11381, -1.28733, 37.9921), viewOffsetX=7.9955, 
        viewOffsetY=-1.46783)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=133.537, 
        farPlane=197.61, width=82.8913, height=46.7765, cameraPosition=(-35.0283, 
        -140.804, 117.377), cameraUpVector=(0.125841, 0.746682, 0.65317), 
        cameraTarget=(-3.8657, -0.750564, 35.5592), viewOffsetX=7.8006, 
        viewOffsetY=-1.43205)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=140.19, 
        farPlane=190.958, width=28.5709, height=16.1229, viewOffsetX=4.16178, 
        viewOffsetY=-22.1474)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=156.105, 
        farPlane=189.242, width=31.8146, height=17.9533, cameraPosition=(-56.93, 
        -157.645, 79.1709), cameraUpVector=(0.102157, 0.554827, 0.82567), 
        cameraTarget=(-5.55964, -6.23248, 37.7505), viewOffsetX=4.63427, 
        viewOffsetY=-24.6618)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=152.077, 
        farPlane=193.27, width=65.3903, height=36.9005, viewOffsetX=7.13662, 
        viewOffsetY=-24.2105)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=164.434, 
        farPlane=190.242, width=70.7035, height=39.8988, cameraPosition=(-110.546, 
        -138.654, 34.5154), cameraUpVector=(0.228952, 0.219972, 0.948258), 
        cameraTarget=(-5.97978, -10.84, 37.6792), viewOffsetX=7.7165, 
        viewOffsetY=-26.1777)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=162.577, 
        farPlane=194.468, width=69.9048, height=39.4481, cameraPosition=(-121.391, 
        -130.034, 22.4773), cameraUpVector=(0.147306, 0.210101, 0.966519), 
        cameraTarget=(-9.08461, -9.69969, 36.1661), viewOffsetX=7.62934, 
        viewOffsetY=-25.882)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=162.674, 
        farPlane=194.37, width=69.9464, height=39.4716, cameraPosition=(-119.392, 
        -131.989, 23.2647), cameraUpVector=(0.214946, 0.147091, 0.965486), 
        cameraTarget=(-7.08534, -11.6552, 36.9536), viewOffsetX=7.63388, 
        viewOffsetY=-25.8974)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=165.055, 
        farPlane=195.32, width=70.9701, height=40.0493, cameraPosition=(-7.63538, 
        -179.239, 54.3339), cameraUpVector=(0.036777, 0.418299, 0.907565), 
        cameraTarget=(0.131754, -14.9703, 38.9713), viewOffsetX=7.74561, 
        viewOffsetY=-26.2764)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=164.987, 
        farPlane=197.386, width=70.9408, height=40.0328, cameraPosition=(22.469, 
        -178.74, 56.9981), cameraUpVector=(-0.113737, 0.425081, 0.897981), 
        cameraTarget=(0.214137, -16.1248, 38.5131), viewOffsetX=7.74241, 
        viewOffsetY=-26.2656)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=170.554, 
        farPlane=196.818, width=73.3344, height=41.3835, cameraPosition=(23.8287, 
        -182.11, 41.7785), cameraUpVector=(-0.138557, 0.343897, 0.928729), 
        cameraTarget=(-0.229467, -18.7734, 36.9893), viewOffsetX=8.00364, 
        viewOffsetY=-27.1518)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=171.498, 
        farPlane=211.68, width=73.7403, height=41.6125, cameraPosition=(53.3639, 
        -180.114, -0.188038), cameraUpVector=(-0.0709758, 0.123109, 0.989852), 
        cameraTarget=(6.14423, -25.3141, 32.7944), viewOffsetX=8.04794, 
        viewOffsetY=-27.3021)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=171.448, 
        farPlane=211.729, width=73.719, height=41.6005, cameraPosition=(55.2917, 
        -179.648, 0.386832), cameraUpVector=(-0.0124107, 0.140955, 0.989938), 
        cameraTarget=(8.07207, -24.8485, 33.3693), viewOffsetX=8.04561, 
        viewOffsetY=-27.2942)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.534, 
        farPlane=203.642, width=6.91165, height=3.90032, viewOffsetX=0.475654, 
        viewOffsetY=-36.2849)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.588, 
        farPlane=203.589, width=6.9137, height=3.90148, cameraPosition=(53.3465, 
        -180.238, 0.370255), cameraUpVector=(-0.0597339, 0.12647, 0.99017), 
        cameraTarget=(6.12684, -25.4383, 33.3527), viewOffsetX=0.475796, 
        viewOffsetY=-36.2957)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.571, 
        farPlane=203.974, width=6.91306, height=3.90112, cameraPosition=(55.2254, 
        -179.664, -0.608858), cameraUpVector=(-0.0661935, 0.11907, 0.990677), 
        cameraTarget=(6.28176, -25.5746, 33.1752), viewOffsetX=0.475752, 
        viewOffsetY=-36.2924)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.571, 
        farPlane=203.973, width=6.91307, height=3.90113, cameraPosition=(56.4654, 
        -179.277, -0.577023), cameraUpVector=(-0.0360512, 0.128563, 0.991046), 
        cameraTarget=(7.52176, -25.1877, 33.207), viewOffsetX=0.475753, 
        viewOffsetY=-36.2925)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.832, 
        farPlane=203.713, width=4.48948, height=2.53347, viewOffsetX=0.267199, 
        viewOffsetY=-36.4749)
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
        'Min. Principal'), )
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendBox=OFF, legendDecimalPlaces=1, legendNumberFormat=FIXED, state=OFF, 
        annotations=OFF)
    session.graphicsOptions.setValues(backgroundStyle=SOLID, 
        backgroundColor='#FFFFFF', translucencyMode=2)
    session.printOptions.setValues(vpBackground=ON, reduceColors=False)
    session.printToFile(
        fileName='D:/FYP/Computational modelling/ABAQUS_6/Images/Min_princ_%d' % i, 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
    i = i + 1

