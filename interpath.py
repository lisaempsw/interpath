import psutil
import time
import os

def display_system_usage():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Get memory usage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    # Get disk usage
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent

    # Get network stats
    net_info = psutil.net_io_counters()
    bytes_sent = net_info.bytes_sent
    bytes_recv = net_info.bytes_recv

    # Display the system usage stats
    os.system('cls' if os.name == 'nt' else 'clear')
    print("System Usage Statistics:")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")
    print(f"Bytes Sent: {bytes_sent}")
    print(f"Bytes Received: {bytes_recv}")

def display_task_info():
    # Display running processes
    print("\nRunning Tasks:")
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, CPU: {proc.info['cpu_percent']}%, Memory: {proc.info['memory_percent']}%")

def main():
    while True:
        display_system_usage()
        display_task_info()
        time.sleep(5)

if __name__ == "__main__":
    main()