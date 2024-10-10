import psutil
import time
import socket

threshold_percentage = 50
included_processes = ['CTFarm.exe']  # List of process names to include
computer_name = socket.gethostname()  # Get the computer name
log_file = f"{computer_name}.txt"  # Set the log file name using the computer name

def log_cpu_usage():
    with open(log_file, "a") as f:
        for process in psutil.process_iter(['name', 'cpu_percent']):
            process_name = process.info['name']
            cpu_percent = process.info['cpu_percent']
            if cpu_percent > threshold_percentage and process_name not in ['System Idle Process', 'python.exe']:
                f.write(f"{process_name} : {cpu_percent}%\n")

def main():
    while True:
        processes_exceeded_threshold = False  # Flag to track if any process exceeds the threshold
        for process in psutil.process_iter(['name', 'cpu_percent']):
            process_name = process.info['name']
            cpu_percent = process.info['cpu_percent']
            if process_name != 'Idle' and process_name in included_processes:
                print(f"Process to be monitored: {process_name} (CPU Usage: {cpu_percent}%)")
            
            if cpu_percent > threshold_percentage:
                processes_exceeded_threshold = True
        
        if processes_exceeded_threshold:
            log_cpu_usage()

        time.sleep(1)  # Adjust sleep duration to 1 second for more frequent checking

if __name__ == "__main__":
    main()