"""Working practice with libraries subprocess, os, sys"""
import subprocess
import os
import argparse

# Create parser for arguments
parser = argparse.ArgumentParser()
parser.add_argument('--file-folder',
                    action='store',
                    default='D:\\PyCharm_projects\\System_status\\files_folder',
                    help='Work directory with files')
args = parser.parse_args()

# Getting system name
system_name = os.name
print(system_name)

# Getting current directory
current_folder = os.getcwd()
print(current_folder)

# Getting list of file from working directory
files_list = os.listdir(args.file_folder)
print(files_list)

# Getting system information
stdout_info = subprocess.Popen(['systeminfo'], stdout=subprocess.PIPE)
print("System Information: ")
stdin_info = subprocess.Popen(['findstr', '/C:OS Name', '/C:OS Version'], stdin=stdout_info.stdout)
result_info = stdin_info.communicate()

# Getting process list
stdout_proc = subprocess.Popen(['tasklist', '/NH'], stdout=subprocess.PIPE)
print('System Process: ')
stdin_proc = subprocess.Popen(['sort'], stdin=stdout_proc.stdout)
result_proc = stdin_proc.communicate()

# Getting network interfaces
print('Network Interfaces: ')
network_interfaces = subprocess.Popen('ipconfig')
network_interfaces.wait()





