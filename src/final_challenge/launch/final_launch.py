from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():

    vision_node = Node(
        package='final_launch',
        executable='Vision',
        output='screen',
    )

    controller_node = Node(
        package='final_launch',
        executable='Controller',
        output='screen',
    )

    odometry_node = Node(
        package='final_launch',
        executable='Odometry',
        output='screen',
    )

    signal_node = Node(
        package='final_launch',
        executable='Signal',
        output='screen',
    )

    l_d = LaunchDescription([vision_node, controller_node, odometry_node, signal_node])
    return l_d