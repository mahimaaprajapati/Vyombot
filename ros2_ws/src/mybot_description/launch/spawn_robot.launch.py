from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    # get path of URDF
    this_dir = os.path.dirname(os.path.realpath(__file__))
    urdf_path = os.path.abspath(
        os.path.join(this_dir, "..", "urdf", "lunabot_fixed_standard.urdf")
    )

    # read URDF
    with open(urdf_path, 'r') as f:
        robot_desc = f.read()

    return LaunchDescription([

        # Publish URDF to ROS
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}],
            output='screen'
        ),

        # Spawn robot in Gazebo Fortress
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-string', robot_desc,
                '-name', 'my_robot',
                '-allow_renaming', 'true'
            ],
            output='screen'
        ),
    ])
