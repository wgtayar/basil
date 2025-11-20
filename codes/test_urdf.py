#!/usr/bin/env python3
import numpy as np
from pydrake.all import (
    RobotDiagramBuilder,
    StartMeshcat,
    MeshcatVisualizer,
    Simulator,
    JointActuatorIndex,
    RigidTransform, 
)

from underactuated import ConfigureParser

def main():
    meshcat = StartMeshcat()

    robot_builder = RobotDiagramBuilder(time_step=0.0)
    plant = robot_builder.plant()
    scene_graph = robot_builder.scene_graph()
    parser = robot_builder.parser()
    ConfigureParser(parser)
    X_WB = RigidTransform([0, 0, 0.0738])
    parser.AddModelsFromUrl("package://underactuated/models/blackbird.urdf")	
    parser.AddModelsFromUrl("package://underactuated/models/littledog/ground.urdf")

    base = plant.GetBodyByName("l_foot")
    plant.WeldFrames(plant.world_frame(), base.body_frame())
    
    plant.Finalize() # Finalize must happen before querying actuators

    print("num joints:", plant.num_joints())
    print("num actuators:", plant.num_actuators())
    
    # <--- 2. The Fix: Wrap 'i' in JointActuatorIndex(i)
    for i in range(plant.num_actuators()):
       a = plant.get_joint_actuator(JointActuatorIndex(i))
       print(i, a.name(), "acts on joint", a.joint().name())
   

    builder = robot_builder.builder()
    MeshcatVisualizer.AddToBuilder(builder, scene_graph, meshcat=meshcat)

    diagram = robot_builder.Build()
    context = diagram.CreateDefaultContext()

    # ForcedPublish to visualize
    diagram.ForcedPublish(context)
    
    print("Meshcat URL:", meshcat.web_url())
    # Keep the script running so you can see the visualization
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
