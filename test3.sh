#!/bin/bash
echo "####################################################"
echo "this shell is to print all the file in the directory"
echo "####################################################"

echo "请输入要列出文件的目录："
read directory
ls -al $directory
