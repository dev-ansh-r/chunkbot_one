import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Define the package name
    package_name = 'chunkbot_one'

    # Include the Robot State Publisher to publish the robot state
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'rsp.launch.py'
        )]),
        launch_arguments={'use_sim_time': LaunchConfiguration('use_sim_time')}.items()
    )

    # Include the joint_state_publisher to publish joint states
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )

    # Launch Arguments for Gazebo
    arguments = [
        DeclareLaunchArgument('world', default_value='/home/devansh/chunkbot_ws/src/chunkbot_one/worlds/chunkbot.sdf',
                              description='Gazebo world file'),
        DeclareLaunchArgument('verbose', default_value='true',
                              description='Gazebo verbosity level'),
        DeclareLaunchArgument('use_sim_time', default_value='true',
                              description='Use simulation time')
    ]

    # Gazebo (now often referred to as GZ) launch description using ros_gz_sim
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
        launch_arguments=[
            ('gz_args', [LaunchConfiguration('world'),
                         ' -v ', LaunchConfiguration('verbose'),
                         ' -r']
            )
        ]
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

    return LaunchDescription(arguments + [
        rsp,
        joint_state_publisher,
        gazebo,
        spawn_entity
    ])
