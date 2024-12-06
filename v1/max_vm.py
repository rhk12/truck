from odbAccess import *
import sys

# Specify your ODB file
odb_path = 'Job-1.odb'
odb = openOdb(path=odb_path)

# Iterate over all steps
for step_name, step in odb.steps.items():
    print("Processing Step: {}".format(step_name))
    # Iterate over all frames in the step
    for i, frame in enumerate(step.frames):
        stress_field = frame.fieldOutputs['S']  # Von Mises stress
        # Find the maximum Von Mises stress in this frame
        max_stress = max(val.mises for val in stress_field.values)
        print("Frame {}: Maximum Von Mises Stress = {:.2f} MPa".format(i, max_stress))

odb.close()
