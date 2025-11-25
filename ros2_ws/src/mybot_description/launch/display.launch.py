from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    # get path of THIS file
    this_dir = os.path.dirname(os.path.realpath(__file__))

    # go from:
    # share/mybot_description/launch  → (..)
    # share/mybot_description/
    # then enter urdf/
    urdf_path = os.path.join(
        this_dir,
        '..',
        'urdf',
        'lunabot_fixed_standard.urdf'
    )

    # resolve absolute path
    urdf_path = os.path.abspath(urdf_path)

    # read URDF file
    with open(urdf_path, 'r') as infp:
        robot_description_content = infp.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description_content}],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        )
    ])
