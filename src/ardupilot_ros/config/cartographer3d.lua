-- Copyright 2016 The Cartographer Authors
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--      http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.

include "map_builder.lua"
include "trajectory_builder.lua"

options = {
  map_builder = MAP_BUILDER,
  trajectory_builder = TRAJECTORY_BUILDER,
  map_frame = "map",
  tracking_frame = "base_scan",
  -- tracking_frame = "camera_depth_frame"
  published_frame = "odom",
  odom_frame = "odom",
  provide_odom_frame = false,
  publish_frame_projected_to_2d = false,
  use_odometry = true,
  use_nav_sat = false,
  use_landmarks = false,
  num_laser_scans = 0,
  num_multi_echo_laser_scans = 0,
  num_subdivisions_per_laser_scan = 1,
  num_point_clouds = 1,
  lookup_transform_timeout_sec = 0.2,
  submap_publish_period_sec = 0.3,
  pose_publish_period_sec = 5e-3,
  trajectory_publish_period_sec = 30e-3,
  rangefinder_sampling_ratio = 1.,
  odometry_sampling_ratio = 1.,
  fixed_frame_pose_sampling_ratio = 1.,
  imu_sampling_ratio = 1.,
  landmarks_sampling_ratio = 1.,
}



-- MAX_3D_LASER_RANGE = 3.5
-- TRAJECTORY_BUILDER_3D.min_range = 0.1
-- TRAJECTORY_BUILDER_2D.min_z = 0.1
-- TRAJECTORY_BUILDER_2D.max_z = 1.5
-- TRAJECTORY_BUILDER_3D.use_online_correlative_scan_matching = true		--houjia
-- TRAJECTORY_BUILDER_3D.max_range = MAX_3D_RANGE
-- TRAJECTORY_BUILDER_3D.low_resolution_adaptive_voxel_filter.max_range = MAX_3D_RANGE
-- TRAJECTORY_BUILDER_3D.low_resolution_adaptive_voxel_filter.min_num_points = 500
-- TRAJECTORY_BUILDER_3D.high_resolution_adaptive_voxel_filter.max_range = MAX_3D_RANGE
-- TRAJECTORY_BUILDER_3D.high_resolution_adaptive_voxel_filter.min_num_points = 250
-- TRAJECTORY_BUILDER_3D.submaps.high_resolution_max_range = MAX_3D_RANGE

-- MAP_BUILDER.use_trajectory_builder_3d = true
-- MAP_BUILDER.num_background_threads = 30

-- TRAJECTORY_BUILDER_3D.motion_filter.max_time_seconds = 0.25
-- TRAJECTORY_BUILDER_3D.motion_filter.max_angle_radians = math.rad(0.1)
-- TRAJECTORY_BUILDER_3D.submaps.high_resolution = 0.035
-- TRAJECTORY_BUILDER_3D.submaps.low_resolution = 0.2

-- TRAJECTORY_BUILDER_3D.ceres_scan_matcher.occupied_space_weight_0 = 10.
-- TRAJECTORY_BUILDER_3D.ceres_scan_matcher.occupied_space_weight_1 = 15.
-- TRAJECTORY_BUILDER_3D.ceres_scan_matcher.translation_weight = 4.
-- TRAJECTORY_BUILDER_3D.ceres_scan_matcher.rotation_weight = 1e3
-- TRAJECTORY_BUILDER_3D.ceres_scan_matcher.only_optimize_yaw = true

-- POSE_GRAPH.constraint_builder.sampling_ratio = 0.2
-- POSE_GRAPH.optimization_problem.ceres_solver_options.max_num_iterations = 10
-- POSE_GRAPH.constraint_builder.min_score = 0.48
-- POSE_GRAPH.constraint_builder.log_matches = true
-- POSE_GRAPH.constraint_builder.fast_correlative_scan_matcher_3d.min_rotational_score = 0.
-- POSE_GRAPH.constraint_builder.fast_correlative_scan_matcher_3d.linear_xy_search_window = 2.

-- POSE_GRAPH.optimization_problem.huber_scale = 1e1
-- POSE_GRAPH.optimization_problem.acceleration_weight = 1e-1
-- POSE_GRAPH.optimization_problem.rotation_weight = 1e3

TRAJECTORY_BUILDER_2D.min_z = 0.1
TRAJECTORY_BUILDER_2D.max_z = 1.0
TRAJECTORY_BUILDER_3D.num_accumulated_range_data = 1   	--1
TRAJECTORY_BUILDER_3D.min_range = 1.3			--houjia
TRAJECTORY_BUILDER_3D.max_range = 25.			--houjia
TRAJECTORY_BUILDER_3D.use_online_correlative_scan_matching = true		--houjia
--TRAJECTORY_BUILDER_3D.submaps.num_range_data=90.

MAP_BUILDER.use_trajectory_builder_3d = true
MAP_BUILDER.num_background_threads = 7
POSE_GRAPH.optimization_problem.huber_scale = 5e2
POSE_GRAPH.optimize_every_n_nodes = 60
POSE_GRAPH.constraint_builder.sampling_ratio = 0.03
POSE_GRAPH.optimization_problem.ceres_solver_options.max_num_iterations = 10
POSE_GRAPH.constraint_builder.min_score = 0.62
POSE_GRAPH.constraint_builder.global_localization_min_score = 0.66

return options
