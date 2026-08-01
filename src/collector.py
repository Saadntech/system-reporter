"""get metrics from the system """  

import platform

import psutil  #import psutil library to get system metrics
import platform #import platform library to get system information
from datetime import datetime #import datetime library to get current date and time


def get_system_info():
    """get system information"""
    info ={
        "timestamp":datetime.now().isoformat(),
        "platform":{
            "system":platform.system(),
            "release":platform.release(),
            "machine":platform.machine(),
            "processor":platform.processor()
        },
        "cpu":{
            "cores_physical":psutil.cpu_count(logical=False), #get number of physical cores
            "cores_logical":psutil.cpu_count(logical=True), #get number of logical cores
            "usage_percent":psutil.cpu_percent(interval=1) #get cpu usage percentage
        },

        "memory":{
            "total_gb":round(psutil.virtual_memory().total / (1024 **3), 2),#get total memory in GB *
            "available_gb":round(psutil.virtual_memory().available / (1024 **3), 2),#get available memory in GB *
            "usage_percent":psutil.virtual_memory().percent #get memory usage percentage    
        },
        "disk":{
            "total_gb":round(psutil.disk_usage('/').total / (1024 **3), 2),#get total disk space in GB *
            "used_gb":round(psutil.disk_usage('/').used / (1024 **3), 2),#get used disk space in GB *
            "free_gb":round(psutil.disk_usage('/').free / (1024 **3), 2),#get free disk space in GB *
            "usage_percent":psutil.disk_usage('/').percent #get disk usage percentage
        }


    }
    return info