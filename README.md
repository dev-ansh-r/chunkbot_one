# ROS(Jazzy) Bot

This package template is build in jazzy and supported ros tools, By this date(2024-08-19) this package includes gazebo Harmonic support, and some pluguins supported by gazebo. There are few changes when compared to the ROS2 on ubuntu 22.04(Humble). The basic plugins used in humble(libgazebo_diff_drive.so) are not supported in jazzy. So, we have to use the plugins which are supported by jazzy(libgz_ros2_control.so).

- By this date there are not much of the plugins supported by jazzy, but still you can build a small robot and run it in the gazebo environment. although the libraries and documentation are very less compared to other ROS versions, So, if you are interested in building a robot in jazzy, prepare yourself to face some challenges but I assure you that would be just amazing.

## Resources

I prefer to use the official documentation for the ROS2, gazebo, and other tools.

- [ROS2 Documentation](https://docs.ros.org/en/jazzy/index.html)
- [Gazebo Documentation](https://gazebosim.org/docs/latest/ros_installation/)
- [Articulated Robotics](https://articulatedrobotics.xyz/category/build-a-mobile-robot-with-ros)
- [Reddit ROS2](https://www.reddit.com/r/ROS/comments/1cyvjfg/ros_2_jazzy_jalisco_has_been_released_details/)
- [YT ROS2 Jazzy](https://www.youtube.com/watch?v=b8VwSsbZYn0&pp=ygUMamF6enkgZ2F6ZWJv)
- [YT Gz SIM](https://www.youtube.com/watch?v=xsr7QmEWeu0&pp=ygUMamF6enkgZ2F6ZWJv)
- [YT ROS2 Jazzy](https://www.youtube.com/playlist?list=PLbFaOt0VQ7S_BlYTlfVKUo9u9h7mc4GAU)


## ROS Package template for the Jazzy robot

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `chunkbot_one` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).