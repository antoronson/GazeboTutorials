import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/antoronson/GitTrade/GazeboTutorials/ROS2_Tutorials/ros2_ws/install/py_srvcli'
