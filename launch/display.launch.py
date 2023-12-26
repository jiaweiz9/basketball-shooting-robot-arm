from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get path to the xacro file
    xacro_file = os.path.join(get_package_share_directory('my_robot_arm'), 'urdf', 'my_arm.urdf.xacro')
    # Path where the URDF file will be saved
    urdf_file = os.path.join(get_package_share_directory('my_robot_arm'), 'urdf', 'my_arm.urdf')
    return LaunchDescription([
        # Convert xacro to URDF
        ExecuteProcess(
            cmd=['ros2', 'run', 'xacro', 'xacro', xacro_file, '-o', urdf_file],
            output='screen'
        ),
        # Publish robot state
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': 'my_arm.urdf'}]
        ),
        # Launch RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2'
        )
    ])