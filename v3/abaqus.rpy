# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-13.57.30 176069
# Run by rhk12 on Fri Apr 26 12:33:48 2024
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
    pathName='/storage/work/rhk12/classes/me563/sp24/app14/v3/truck_v2024_v3.cae')
#: The model database "/storage/work/rhk12/classes/me563/sp24/app14/v3/truck_v2024_v3.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Job-1'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13394.6, 
    farPlane=21980.4, width=12523.5, height=5387.52, cameraPosition=(7973.59, 
    5129.41, 16627), cameraUpVector=(-0.998324, -0.0480473, 0.032269))
session.viewports['Viewport: 1'].view.setValues(nearPlane=13077.3, 
    farPlane=21813.9, width=12226.9, height=5259.91, cameraPosition=(-2347.1, 
    16824.6, -1538.7), cameraUpVector=(-0.579108, -0.384258, 0.719013), 
    cameraTarget=(1823.44, -218.5, 926.27))
session.viewports['Viewport: 1'].view.setValues(nearPlane=12044, 
    farPlane=23233.2, width=11260.8, height=4844.29, cameraPosition=(15812.9, 
    9914.5, 3956.75), cameraUpVector=(-0.245199, -0.498505, 0.831486), 
    cameraTarget=(1539.67, -110.521, 840.396))
session.viewports['Viewport: 1'].view.setValues(nearPlane=13078.5, 
    farPlane=22068.3, width=12228, height=5260.4, cameraPosition=(7035.48, 
    16206.6, 4958.08), cameraUpVector=(-0.490993, -0.393452, 0.777253), 
    cameraTarget=(1579.32, -138.948, 835.872))
session.viewports['Viewport: 1'].view.setValues(nearPlane=12042.5, 
    farPlane=23187.8, width=11259.4, height=4843.69, cameraPosition=(15165.8, 
    10258, 5353.98), cameraUpVector=(-0.491531, -0.282188, 0.823873), 
    cameraTarget=(1512.29, -89.9071, 832.608))
session.viewports['Viewport: 1'].view.setValues(nearPlane=12817.1, 
    farPlane=22359.4, width=11983.6, height=5155.25, cameraPosition=(8845.46, 
    15515, 4864.47), cameraUpVector=(-0.239941, -0.482795, 0.842222), 
    cameraTarget=(1549.32, -120.704, 835.476))
session.viewports['Viewport: 1'].view.setValues(nearPlane=13171.4, 
    farPlane=22005.2, width=8389.3, height=3609.01, viewOffsetX=-141.532, 
    viewOffsetY=-172.691)
mdb.save()
#: The model database has been saved to "/storage/work/rhk12/classes/me563/sp24/app14/v3/truck_v2024_v3.cae".
a = mdb.models['Job-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13154.3, 
    farPlane=22377.9, width=12298.9, height=5290.9, cameraPosition=(11152.6, 
    2842.43, 15636.5), cameraUpVector=(-0.942183, -0.229568, 0.244111))
session.viewports['Viewport: 1'].view.setValues(width=12098.2, height=5204.57, 
    viewOffsetX=-4.96394, viewOffsetY=37.9957)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12891.6, 
    farPlane=22331.4, width=11812.2, height=5081.52, cameraPosition=(7688.66, 
    15021.5, 7803.31), cameraUpVector=(-0.375842, -0.574919, 0.726781), 
    cameraTarget=(1764.64, -162.701, 854.735), viewOffsetX=-4.84658, 
    viewOffsetY=37.0974)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12699.3, 
    farPlane=22616.9, width=11636, height=5005.72, cameraPosition=(10419.5, 
    15117, 3064.51), cameraUpVector=(-0.258552, -0.367127, 0.893515), 
    cameraTarget=(1739.16, -174.066, 879.911), viewOffsetX=-4.77428, 
    viewOffsetY=36.544)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13300.5, 
    farPlane=22015.7, width=7207.29, height=3100.52, viewOffsetX=-142.275, 
    viewOffsetY=87.7316)
mdb.models['Job-1'].predefinedFields['IC-1'].setValues(velocity1=0.0, 
    velocity2=35111.1, velocity3=0.0, omega=0.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13247.9, 
    farPlane=22085.1, width=7178.8, height=3088.26, cameraPosition=(10660.5, 
    14935.6, 3376.55), cameraUpVector=(-0.255819, -0.386236, 0.886216), 
    cameraTarget=(1738.76, -168.106, 882.99), viewOffsetX=-141.712, 
    viewOffsetY=87.3847)
mdb.save()
#: The model database has been saved to "/storage/work/rhk12/classes/me563/sp24/app14/v3/truck_v2024_v3.cae".
mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-1.inp".
mdb.save()
#: The model database has been saved to "/storage/work/rhk12/classes/me563/sp24/app14/v3/truck_v2024_v3.cae".
