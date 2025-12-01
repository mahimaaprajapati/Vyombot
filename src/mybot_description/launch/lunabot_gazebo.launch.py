from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg = get_package_share_directory('mybot_description')
    urdf = os.path.join(pkg, 'urdf', 'lunabot_sensors.urdf')

    robot_desc = ParameterValue(
        Command(['xacro ', urdf]),
        value_type=str
    )

    state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_desc}],
        output='screen'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        )
    )

    spawn = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'lunabot'],
        output='screen'
    )

    spawn_delay = TimerAction(period=5.0, actions=[spawn])

    return LaunchDescription([
        gazebo,
        state_pub,
        spawn_delay
    ])
