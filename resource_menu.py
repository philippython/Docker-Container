"""
To run the code below psutil module most be installed

the module can be installed with the command below

>> pip install psutil

>> this script can be run using 

>> python resource_menu.py

"""
# Importing the required libraries
import platform
import psutil
 
# the code below gets percentage of each CPU core over 10 seconds 
print("="*40, "CPU Info", "="*40)
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
print("CPU Usage Per Core:")
# for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=10)):
#     print(f"Core {i + 1}: {percentage}%")

#  the code below gets the amount of CPU usage currently being used
print(f"Total CPU Usage: {psutil.cpu_percent()}%")


#  the code below gets name and version of the operating system
print(platform.system())
print(platform.version())

# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', f"{psutil.virtual_memory()[2]}%")
# Getting usage of virtual_memory in GB ( 4th field)
print('RAM Used (GB):', round(psutil.virtual_memory()[3]/1000000000, 2))


task = input("Enter any command below to perform respective operation\n --per usg all core : TO get all \
percentage usage of each CPU core over 10 seconds\n --ram usg : Get RAM in use \n --version \
name : Get name and version of Operating system \n --busy : check if Computer is busy \n Exit : To exit\n")

while task != "Exit":
    if task == "--busy":
        # the conditional statement compares CPU and RAM usage 
        if psutil.virtual_memory()[2] > 50 and psutil.cpu_percent() > 50:
            print("Computer is currently Busy")
        else:
            print("Computer is not busy and ready for operations")
    else:
        print(f"'{task}' is not recognized as an internal or external command,\
                operable program.")