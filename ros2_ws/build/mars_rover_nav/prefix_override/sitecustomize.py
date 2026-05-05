import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/gianluca/spaceros_tutorial/spaceros-bt-packages/ros2_ws/install/mars_rover_nav'
