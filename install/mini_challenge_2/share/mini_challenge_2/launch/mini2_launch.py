from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():

    controller_node = Node(
        package='mini_challenge_2',
        executable='Controller',
        output='screen',
    )

    point_generator_node = Node(
        package='mini_challenge_2',
        executable='PointGenerator',
        output='screen',
    )
    
    odometry_node = Node(
        package='mini_challenge_2',
        executable='Odometry',
        output='screen',
    )

    l_d = LaunchDescription([controller_node, point_generator_node, odometry_node])
    return l_d