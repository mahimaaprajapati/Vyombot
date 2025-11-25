from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        # Bridge for Lidar
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/scan@sensor_msgs/msg/LaserScan@ignition.msgs.LaserScan'
            ],
            output='screen'
        ),

        # Bridge for RGB Camera
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/camera/image_raw@sensor_msgs/msg/Image@ignition.msgs.Image'
            ],
            output='screen'
        ),

        # Bridge for Depth Camera
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/camera/depth/image_raw@sensor_msgs/msg/Image@ignition.msgs.Image'
            ],
            output='screen'
        ),

        # Bridge for IMU
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/imu/data@sensor_msgs/msg/Imu@ignition.msgs.IMU'
            ],
            output='screen'
        ),

        # Bridge for cmd_vel → to move robot
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist'
            ],
            output='screen'
        ),

       # Bridge for odometry (VERY IMPORTANT)
       Node(
           package='ros_gz_bridge',
           executable='parameter_bridge',
           arguments=[
               '/odom@nav_msgs/msg/Odometry@ignition.msgs.Odometry'
           ],
           output='screen'
        ),


    ])
