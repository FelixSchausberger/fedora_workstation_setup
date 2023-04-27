set fish_greeting ""

zoxide init fish | source
starship init fish | source


##################################################
#Path
if test -d $HOME/.cargo/env 
    fish_add_path $HOME/.cargo/bin 
end

if test -d /opt/ros/humble
    bass source /opt/ros/humble/setup.bash 
    bass source /usr/share/colcon_cd/function/colcon_cd.sh 
    bass source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash

    bass export _colcon_cd_root=/opt/ros/humble/
    bass export GAZEBO_MODEL_PATH=/home/fesch/ScoutBot/simulation_ws/src/
    bass export ROS_PACKAGE_PATH=/opt/ros/humble/share
end

#Generated for envman.Do not edit.
test -s "$HOME/.config/envman/load.fish"; and source "$HOME/.config/envman/load.fish"
