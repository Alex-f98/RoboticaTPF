# RoboticaTPF (EN PROGRESO)
El paso a paso para la elavoracion de control de movimiento para el robot  Moveo (BCN3D) 5Dof mediante ROS _1 con MoveIt.
-----------
#Distribucion de linux
se utiliza ubunto 20.04, tener en cuenta que la version de ROS esta ligada a la version de ubunto y recientemente a windows.

#Version de ROS
Para Ubuntu 20.04 se usa ROS Noetic el mismo puede ser descargado de la siguiente pagina:
https://wiki-ros-org.translate.goog/noetic/Installation/Ubuntu?_x_tr_sch=http&_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=op

#Simulador
Las simulaciones estan hechas con MoveIt 1 Noetic, al igual que ROS con Linux tambien MoveIt está ligada a una version de ROS, los pasos para la instalacion del mismo se encuentra en el siguiente link:
https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html

Nota1: Si se esta usando ROS o moveit por primera vez es recomendable seguir los tutoriales iniciales para comprender mejor como funciona este trabajo.
  para el caso de moveit basta con seguir su tutorial hasta "Move Group Python Interface".
Nota2: Puede que haya fallos al momento de la instalacion de MoveIt, en mi caso los solucione con los siguiente Links:
  https://answers.ros.org/question/374436/error-cannot-launch-node-of-type-moveit_ros_move_groupmove_group-moveit_ros_move_group/
  
---------
(carpeta: catkin_ws)

source ~/catkin_ws/devel/setup.bash

echo 'source ~/catkin_ws/devel/setup.bash' >> ~/.bashrc

roslaunch moveo_moveit_config demo.launch
