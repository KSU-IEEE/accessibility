#!/usr/bin/env python3 

##################################
## TODO  
## Add Rosserial installer
##################################
import os 
import argparse

parser = argparse.ArgumentParser()

##################################
## Ros installer
##################################
def install_ros_melodic(): 
    # adding ros to apt list
    print("Installing ros.....\n")
    os.system('''sudo sh -c "echo 'deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main' > /etc/apt/sources.list.d/ros-latest.list"''')
    os.system("sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654")
    os.system('sudo apt-get update')

    # installing ros 
    os.system('sudo apt install ros-melodic-ros-base')
    os.system('echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc')
    os.system('source ~/.bashrc')

    # initializing roscore 
    os.system('sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential')
    os.system('sudo apt install python-rosdep')
    os.system('sudo rosdep init')
    os.system('rosdep update')

##################################
## apt dependencies
##################################
def add_all_apt(bool_add_ros):
    apt_list = ''
    apt_list = apt_list + add_ninja() + add_cmake() + add_rosserial(bool_add_ros) + add_arduino() + add_catkin(bool_add_ros)
    return apt_list

def add_ninja():
    return 'ninja-build '

def add_catkin(add_this):
    string = 'ros-melodic-catkin-* ' if add_this else ''
    return string

def add_cmake():
    return 'cmake '  

def add_rosserial(add_this):
    string = 'ros-melodic-rosserial-arduino ' if add_this else '' 
    return string 

def add_arduino():
    return "arduino"

##################################
## python dependencies
##################################
def add_all_python():
    # none yet
    python_list=''
    print("adding python deps")
    return python_list

##################################
## main script
##################################

# flags useable
parser.add_argument('-a', '--all', help='Install all dependencies', action='store_true')
parser.add_argument('-d', '--apt_deps', help='Install the apt-depends', action='store_true')
parser.add_argument('-rm', '--ros_melodic', help='Install ros-melodic', action='store_true')
parser.add_argument('-p', '--python_deps', help='Install the python dependencies (nothing yet)', action='store_true')
parser.add_argument('--exclude_ros', help='Exclude ros install and rosserial apt install', action='store_true')

args = parser.parse_args()  

include_ros = not args.exclude_ros
if(include_ros):
    print("Including ros packages in install")
else: 
    print("Not including ros pacakges in install")
apt_list=''
python_list=''
# based on flags, install ros or append lists
if args.all:
    if include_ros:
        install_ros_melodic()
    apt_list = add_all_apt(include_ros)
    python_list = add_all_python() 
else: 
    if args.apt_deps:
        apt_list = add_all_apt(include_ros)
    if args.ros_melodic and not include_ros:
        install_ros_melodic() 
    if args.python_deps:
        python = add_all_python()

# first install apt  
if apt_list != '':
    print("Install apt-dependencies: ")
    print(apt_list)
    os.system('sudo apt-get update') 
    
    cmd='sudo apt-get install ' + apt_list 
    os.system(cmd)
else:
    print("Apt-list is emtpy, not installing apt dependencies")

# then install python deps
if python_list != '':
    print("Installing python dependencies")
    cmd = 'pip install ' + python_list 
else:
    print("Python list is empty, not installing python dependencies (none yet, ignore this message)")  

print("List complete, exiting.......")
