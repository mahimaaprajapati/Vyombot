from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description():

    # ---------------------------
    # 1. Load Lunabot URDF
    # ---------------------------
    urdf_path = os.path.join(
        get_package_share_directory('mybot_description'),
        'urdf',
        'lunabot_sensors.urdf'
    )

    with open(urdf_path, 'r') as f:
        robot_desc = f.read()

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {'robot_description': robot_desc},
            {'use_sim_time': True}
        ],
        output='screen'
    )

    # ---------------------------
    # 2. Load Gazebo with moon.world
    # ---------------------------
    world_path = os.path.join(
        get_package_share_directory('lunabot_simulation'),
        'worlds',
        'moon.world'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ),
        launch_arguments={'world': world_path}.items()
    )

    # ---------------------------
    # 3. Spawn Rover on Moon Terrain
    # ---------------------------
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'lunabot',
            '-x', '0',
            '-y', '0',
            '-z', '1.5'    # safe height above rough terrain
        ],
        output='screen'
    )

    spawn_delayed = TimerAction(
        period=5.0,
        actions=[spawn_robot]
    )

    # ---------------------------
    # Launch Everything
    # ---------------------------
    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_delayed
    ])
