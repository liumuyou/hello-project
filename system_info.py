import platform
import os
import sys


def get_os_info():
    info = {}
    info['System'] = platform.system()
    info['Node Name'] = platform.node()
    info['Release'] = platform.release()
    info['Version'] = platform.version()
    info['Machine'] = platform.machine()
    info['Processor'] = platform.processor()
    return info


def get_python_info():
    info = {}
    info['Python Version'] = sys.version
    info['Python Compiler'] = platform.python_compiler()
    info['Python Implementation'] = platform.python_implementation()
    info['Python Build'] = platform.python_build()
    return info


def get_cpu_info():
    info = {}
    info['CPU Count'] = os.cpu_count()
    info['Architecture'] = platform.architecture()[0]
    return info


def get_memory_info():
    info = {}
    try:
        if sys.platform == 'darwin':
            mem_info = os.popen('sysctl -n hw.memsize').read().strip()
            total_mem = int(mem_info) / (1024 ** 3)
            info['Total Memory'] = f"{total_mem:.2f} GB"
            
            vm_stat_output = os.popen('vm_stat').read()
            for line in vm_stat_output.split('\n'):
                if 'Pages free' in line:
                    free_pages = int(line.split(':')[1].strip().replace('.', ''))
                if 'page size' in line:
                    page_size = int(line.split('(')[1].split(' ')[3])
            free_bytes = free_pages * page_size
            info['Free Memory'] = f"{free_bytes / (1024 ** 3):.2f} GB"
        elif sys.platform == 'linux':
            meminfo = {}
            with open('/proc/meminfo') as f:
                for line in f:
                    key, value = line.strip().split(':')
                    meminfo[key] = value.strip()
            total_mem = int(meminfo['MemTotal'].split()[0]) / 1024 / 1024
            free_mem = int(meminfo['MemFree'].split()[0]) / 1024 / 1024
            info['Total Memory'] = f"{total_mem:.2f} GB"
            info['Free Memory'] = f"{free_mem:.2f} GB"
        elif sys.platform == 'win32':
            import ctypes
            kernel32 = ctypes.windll.kernel32
            total_mem = ctypes.c_ulonglong(0)
            kernel32.GetPhysicallyInstalledSystemMemory(ctypes.pointer(total_mem))
            info['Total Memory'] = f"{total_mem.value / 1024 / 1024:.2f} GB"
    except Exception as e:
        info['Error'] = str(e)
    return info


def get_disk_info():
    info = {}
    try:
        if sys.platform == 'darwin':
            disk = os.popen('df -h /').read().splitlines()[-1].split()
            info['Total Disk'] = disk[1]
            info['Used Disk'] = disk[2]
            info['Available Disk'] = disk[3]
            info['Usage Percent'] = disk[4]
        elif sys.platform == 'linux':
            disk = os.popen('df -h /').read().splitlines()[-1].split()
            info['Total Disk'] = disk[1]
            info['Used Disk'] = disk[2]
            info['Available Disk'] = disk[3]
            info['Usage Percent'] = disk[4]
        elif sys.platform == 'win32':
            import ctypes
            free_bytes = ctypes.c_ulonglong(0)
            total_bytes = ctypes.c_ulonglong(0)
            ctypes.windll.kernel32.GetDiskFreeSpaceExW('C:\\', None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
            info['Total Disk'] = f"{total_bytes.value / (1024 ** 3):.2f} GB"
            info['Available Disk'] = f"{free_bytes.value / (1024 ** 3):.2f} GB"
    except Exception as e:
        info['Error'] = str(e)
    return info


def get_network_info():
    info = {}
    try:
        hostname = platform.node()
        info['Hostname'] = hostname
        
        if sys.platform == 'darwin' or sys.platform == 'linux':
            ip_output = os.popen('ifconfig | grep inet | grep -v 127.0.0.1 | grep -v inet6').read().strip()
            ips = [line.split()[1] for line in ip_output.split('\n') if line]
            info['IP Addresses'] = ', '.join(ips) if ips else 'Not found'
        elif sys.platform == 'win32':
            ip_output = os.popen('ipconfig | findstr IPv4').read().strip()
            ips = [line.split(':')[-1].strip() for line in ip_output.split('\n') if line]
            info['IP Addresses'] = ', '.join(ips) if ips else 'Not found'
    except Exception as e:
        info['Error'] = str(e)
    return info


def print_info(title, info):
    print(f"\n{'='*50}")
    print(f"  {title}")
    print(f"{'='*50}")
    for key, value in info.items():
        print(f"  {key}: {value}")


def main():
    print("\n" + "🤖 SYSTEM INFORMATION TOOL".center(50, "="))
    
    print_info("Operating System", get_os_info())
    print_info("Python Environment", get_python_info())
    print_info("CPU Information", get_cpu_info())
    print_info("Memory Information", get_memory_info())
    print_info("Disk Information", get_disk_info())
    print_info("Network Information", get_network_info())
    
    print(f"\n{'='*50}")
    print("  Information collected successfully!")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()