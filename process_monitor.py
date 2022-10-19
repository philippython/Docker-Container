import psutil
import time
import wmi

# Initializing the wmi constructor
wmi_object = wmi.WMI()

# the lists below tracks processes 
processor_list = []
cpu_usage = []

# a code to notify user that the code is running
print('='*30, "Processing", '='*30)

def processor():
    
    # the total running process is appended to the processor_list evry 20 seconds to keep track
    total_running_processes = len(wmi_object.Win32_Process())
    processor_list.append(total_running_processes)

    cpu_usage.append(psutil.cpu_percent())

        


    # this code below compares current running process and the running process 20seconds earlier
    if len(processor_list) == 1: 
        print('CPU usage (GB) in %:', cpu_usage[0])
        print("We have %s processes running................." % (processor_list[0]))
    
    if len(processor_list) > 1:
        difference_in_processes = abs(processor_list[-1] - processor_list[-2])
        diff_in_cpu_usage = abs(cpu_usage[-1] - cpu_usage[-2])
        prev_ten_percent_usage = cpu_usage[-2] * 0.1
        
        #  checks if the change in ram usage is above 10% the previous
        if diff_in_cpu_usage > prev_ten_percent_usage:
            for process in wmi_object.Win32_Process():

                try:
                    p = psutil.Process(process.ProcessId)
                except psutil.NoSuchProcess:
                    pass
                else:
                    each_process_usage = p.cpu_percent()
                    if each_process_usage > 1 :
                        print(f"Process {process} is using more than 1 % of CPU ")
                

        if processor_list[-1] > processor_list[-2] :
            print('CPU usage (GB) in %:', cpu_usage[-1])
            print("We have %s more processes than 20 seconds earlier........." % (difference_in_processes))
        
        elif processor_list[-1] == processor_list[-2] :
            print('CPU usage (GB) in %:', cpu_usage[-1])
            print("We have no new processes than 20 seconds earlier............")

        else:
            print('CPU usage (GB) in %:', cpu_usage[-1])
            print("We have %s less processes than 20 seconds earlier..........." % (difference_in_processes))

    time.sleep(20)

    processor()


processor()

