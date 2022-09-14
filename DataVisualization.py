#shoongi
#400312914

import numpy as np
import open3d as o3d
if __name__ == "__main__":
    #Remember the goals of modularization
    #   -- smaller problems, reuse, validation, debugging
    #To simulate the data from the sensor lets create a new file with test data 


    with open("measurements.xyz","r") as f:
        length = len(f.readlines())                         
    
    #Read the test data in from the file we created        
    print("Read in the prism point cloud data (pcd)")
    pcd = o3d.io.read_point_cloud("measurements.xyz", format="xyz")

    #Lets see what our point cloud data looks like numerically       
    print("The PCD array:")
    print(np.asarray(pcd.points))

    #Lets see what our point cloud data looks like graphically       
    print("Lets visualize the PCD: (spawns seperate interactive window)")
    o3d.visualization.draw_geometries([pcd])

    #OK, good, but not great, lets add some lines to connect the vertices
    #   For creating a lineset we will need to tell the packahe which vertices need connected
    #   Remember each vertex actually contains one x,y,z coordinate

    #Give each vertex a unique number
    yz_slice_vertex = []
    for x in range(0,length):
        yz_slice_vertex.append([x])

    #Define coordinates to connect lines in each yz slice        
    lines = []  
    for x in range(0,length,16):
        lines.append([yz_slice_vertex[x], yz_slice_vertex[x+1]])
        lines.append([yz_slice_vertex[x+1], yz_slice_vertex[x+2]])
        lines.append([yz_slice_vertex[x+2], yz_slice_vertex[x+3]])
        lines.append([yz_slice_vertex[x+3], yz_slice_vertex[x+4]])
        lines.append([yz_slice_vertex[x+4], yz_slice_vertex[x+5]])
        lines.append([yz_slice_vertex[x+5], yz_slice_vertex[x+6]])
        lines.append([yz_slice_vertex[x+6], yz_slice_vertex[x+7]])
        lines.append([yz_slice_vertex[x+7], yz_slice_vertex[x+8]])
        lines.append([yz_slice_vertex[x+8], yz_slice_vertex[x+9]])
        lines.append([yz_slice_vertex[x+9], yz_slice_vertex[x+10]])
        lines.append([yz_slice_vertex[x+10], yz_slice_vertex[x+11]])
        lines.append([yz_slice_vertex[x+11], yz_slice_vertex[x+12]])
        lines.append([yz_slice_vertex[x+12], yz_slice_vertex[x+13]])
        lines.append([yz_slice_vertex[x+13], yz_slice_vertex[x+14]])
        lines.append([yz_slice_vertex[x+14], yz_slice_vertex[x+15]])
        lines.append([yz_slice_vertex[x+15], yz_slice_vertex[x]])

    #Define coordinates to connect lines between current and next yz slice        
    
    for x in range(0,length-16-1,16):
        lines.append([yz_slice_vertex[x], yz_slice_vertex[x+16]])
        lines.append([yz_slice_vertex[x+1], yz_slice_vertex[x+17]])
        lines.append([yz_slice_vertex[x+2], yz_slice_vertex[x+18]])
        lines.append([yz_slice_vertex[x+3], yz_slice_vertex[x+19]])
        lines.append([yz_slice_vertex[x+4], yz_slice_vertex[x+20]])
        lines.append([yz_slice_vertex[x+5], yz_slice_vertex[x+21]])
        lines.append([yz_slice_vertex[x+6], yz_slice_vertex[x+22]])
        lines.append([yz_slice_vertex[x+7], yz_slice_vertex[x+23]])
        lines.append([yz_slice_vertex[x+8], yz_slice_vertex[x+24]])
        lines.append([yz_slice_vertex[x+9], yz_slice_vertex[x+25]])
        lines.append([yz_slice_vertex[x+10], yz_slice_vertex[x+26]])
        lines.append([yz_slice_vertex[x+11], yz_slice_vertex[x+27]])
        lines.append([yz_slice_vertex[x+12], yz_slice_vertex[x+28]])
        lines.append([yz_slice_vertex[x+13], yz_slice_vertex[x+29]])
        lines.append([yz_slice_vertex[x+14], yz_slice_vertex[x+30]])
        lines.append([yz_slice_vertex[x+15], yz_slice_vertex[x+31]])
    
    #This line maps the lines to the 3d coordinate vertices
    line_set = o3d.geometry.LineSet(points=o3d.utility.Vector3dVector(np.asarray(pcd.points)),lines=o3d.utility.Vector2iVector(lines))

    #Lets see what our point cloud data with lines looks like graphically       
    o3d.visualization.draw_geometries([line_set])