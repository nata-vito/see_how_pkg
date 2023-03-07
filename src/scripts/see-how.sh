#!/bin/bash

Help()
{
   # Display Help
   echo "Script developed to assist in the execution of the SEE-HOW ros package. "
   echo
   echo "Syntax: ./see-ho.sh [-s|-l|-r|-c|-h]"
   echo "options:"
   echo "-s     Package initialization ."
   echo "-l     Print /Left topic data."
   echo "-r     Print /Right topic data."
   echo "-c     Print /camera topic data."
   echo "-h     Print this Help."
   echo
}

if [ "$1" = "-s" ]; then
    source ~root/ws/devel/setup.bash 
    roslaunch see_how_pkg see_how.launch
elif [ "$1" = "-l" ]; then
    source ~root/ws/devel/setup.bash
    rostopic echo /Left
elif [ "$1" = "-r" ]; then
    source ~root/ws/devel/setup.bash
    rostopic echo /Right
elif [ "$1" = "-c" ]; then
    source ~root/ws/devel/setup.bash
    rostopic echo /camera
elif [ "$1" = "-h" ]; then
    Help
fi
