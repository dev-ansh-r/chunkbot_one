import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Define the package name
    package_name = 'chunkbot_one'

    # Include the Robot State Publisher to publish the robot state
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'rsp.launch.py'
        )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Gazebo (now often referred to as GZ) launch description using ros_gz_sim
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
        launch_arguments={'gz_args': 'empty.sdf'}.items()
    )

    # Spawn Entity in Gazebo using ros_gz_sim's create tool
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-entity', 'chunkbot_one',
            '-topic', 'robot_description',
            '-x', '0', '-y', '0', '-z', '0.1'
        ],
        output='screen',
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity
    ])
