#!/usr/bin/env bash
echo "checking if ros cmds against ${1} ...."
if [ "$EXTRA_ROS_PATH" = ${1} ]
then
    echo "correct rospath already set, not touching .bashrc"
    return
else 
    if [ -z "${EXTRA_ROS_PATH}" ]
    then
        echo "add srcros alias"
        echo "alias srcros='source ${1}'" >> ~/.bashrc
    else 
        echo ""
    fi
    echo "setting rospath in .bashrc"
    echo "export EXTRA_ROS_PATH='${1}'" >> ~/.bashrc 
    source ~/.bashrc 
    return
fi