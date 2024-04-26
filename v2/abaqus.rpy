# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-13.57.30 176069
# Run by rhk12 on Fri Apr 26 12:28:02 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=257.421539306641, 
    height=156.66667175293)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName='/storage/work/rhk12/classes/me563/sp24/app14/v1/truck_v2024_v1.cae')
#: The model database "/storage/work/rhk12/classes/me563/sp24/app14/v1/truck_v2024_v1.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Job-1'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12405.2, 
    farPlane=23031.3, width=9469.26, height=4989.59, cameraPosition=(12035.1, 
    10031.5, 11124.3), cameraUpVector=(-0.962238, 0.196214, 0.188674))
session.viewports['Viewport: 1'].view.setValues(nearPlane=12300.6, 
    farPlane=23217.3, width=9389.43, height=4947.52, cameraPosition=(14243.3, 
    11753.6, 4943.3), cameraUpVector=(-0.371903, -0.392146, 0.841374), 
    cameraTarget=(1805.47, -198.136, 894.639))
session.viewports['Viewport: 1'].view.setValues(nearPlane=12555.2, 
    farPlane=22845.8, width=9583.81, height=5049.95, cameraPosition=(11802.7, 
    14146.7, 3766.01), cameraUpVector=(-0.284674, -0.388911, 0.87619), 
    cameraTarget=(1799.88, -192.652, 891.941))
session.viewports['Viewport: 1'].view.setValues(nearPlane=12976, 
    farPlane=22425, width=6612.65, height=3484.37, viewOffsetX=-129.741, 
    viewOffsetY=105.622)
mdb.save()
#: The model database has been saved to "/storage/work/rhk12/classes/me563/sp24/app14/v1/truck_v2024_v1.cae".
a = mdb.models['Job-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
mdb.models['Job-1'].predefinedFields['IC-1'].setValues(velocity1=0.0, 
    velocity2=15111.1, velocity3=0.0, omega=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13133.3, 
    farPlane=22390.8, width=10025, height=5282.44, cameraPosition=(11029.2, 
    3020.82, 15676.3), cameraUpVector=(-0.921728, -0.303343, 0.241663))
session.viewports['Viewport: 1'].view.setValues(nearPlane=13168, 
    farPlane=22356.1, width=10051.5, height=5296.4, cameraPosition=(11029.2, 
    3020.82, 15676.3), cameraUpVector=(-0.633653, -0.756755, 0.160643), 
    cameraTarget=(1805.47, -198.135, 894.637))
session.viewports['Viewport: 1'].view.setValues(nearPlane=12494, 
    farPlane=22878.5, width=9537.07, height=5025.32, cameraPosition=(10731.2, 
    13818.6, 7080.66), cameraUpVector=(-0.330465, -0.55122, 0.766126), 
    cameraTarget=(1804.74, -171.516, 873.447))
mdb.save()
#: The model database has been saved to "/storage/work/rhk12/classes/me563/sp24/app14/v1/truck_v2024_v1.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.save()
#: The model database has been saved to "/storage/work/rhk12/classes/me563/sp24/app14/v1/truck_v2024_v1.cae".
mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-1.inp".
