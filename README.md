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
  https://answers.ros.org/question/192369/moveit-rviz-plugin-error/
  
---------
(carpeta: catkin_ws)

source ~/catkin_ws/devel/setup.bash

echo 'source ~/catkin_ws/devel/setup.bash' >> ~/.bashrc

roslaunch moveo_moveit_config demo.launch
https://www.youtube.com/watch?v=l4dtSRvlAjg
https://www.youtube.com/watch?v=xHh6kd5aQxA
https://github.com/jesseweisberg/moveo_ros

--------------------------
para probar el demo:

si estoy en windows y tengo WSL instalado con Ubuntu-20.04:

wsl -d Ubuntu-20.04

mkdir -p ~/catkin_ws/src       ....(no tiene por que ser "catkin_ws" puede ser "mi_carpeta_ws" pero almenos que tengas otra carpeta igual usar catkin_ws)

cd ~/catkin_ws

catkin_make                    .....esto comprobara que todas las dependencias esten bien y que codigos tengan lo necesario para compilas etc etc etc...

cd src/

git clone https://github.com/jesseweisberg/moveo_ros.git

..Una vez hecho esto recien se van a poder seguir los pasos que muestra en el repositorio original..

roslaunch moveo_moveit_config demo.launch

