import psutil
import time
import wmi

# Initializing the wmi constructor
wmi_object = wmi.WMI()

# the list below tracks processes 
processor_list = []


# the print_ram prints current ram usage
def print_ram():
    print('RAM Used (GB):', round(psutil.virtual_memory()[3]/1000000000, 2))

def processor():

    # the total running process is appended to the processor_list evry 20 seconds to keep track
    total_running_processes = len(wmi_object.Win32_Process())
    processor_list.append(total_running_processes)
    print(processor_list[-1])
    # this code below compares current running process and the running process 20seconds earlier
    if len(processor_list) == 1: 
        print_ram()
        print("We have %s processes runnning" % (processor_list[0]))
    
    if len(processor_list) > 1:
        difference_in_processes = abs(processor_list[-1] - processor_list[-2])
        if processor_list[-1] > processor_list[-2] :
            print_ram()
            print("We have %s more processes than 20 seconds earlier" % (difference_in_processes))
        
        elif processor_list[-1] == processor_list[-2] :
            print_ram()
            print("We have no new processes than 20 seconds earlier")

        else:
            print_ram()
            print("We have %s less processes than 20 seconds earlier" % (difference_in_processes))

    time.sleep(20)

    processor()


processor()

