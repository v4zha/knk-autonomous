# Description: Output format for the knk_drive module
TRAJECTORY_SIZE = 10
# x,y,z
model_plan = {
    'position': [0, 0, 0],
    'velocity': [0, 0, 0],
    'acceleration': [0, 0, 0],
    'rotation': [0, 0, 0],
    'rotation_rate': [0, 0, 0],
}

lines_xy = {
    # uses coor yz
    'left_far': [[0, 0]*TRAJECTORY_SIZE],
    'left_near': [[0, 0]*TRAJECTORY_SIZE],
    'right_near': [[0, 0]*TRAJECTORY_SIZE],
    'right_far': [[0, 0]*TRAJECTORY_SIZE],
}

model_lane = {
    'mean': lines_xy,
    'std': lines_xy,
    'prob': lines_xy
}

edge = {
    'left': [[0, 0]*TRAJECTORY_SIZE],
    'right': [[0, 0]*TRAJECTORY_SIZE],
}

model_edges = {
    'mean': edge,
    'std': edge
}

model_pose = {
    # x,y
    "velocity_mean":[0,0],
    "velocity_std":[0,0],
    "rotation_mean":[0,0],
    "rotation_std":[0,0],
}

model_out = {
    'plans': [[model_plan]],
    'lane': model_lane,
    'road_edges': model_edges,
    'pose': model_pose
}
