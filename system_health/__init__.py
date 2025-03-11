import shutil
import psutil


def check_disk_usage(disk_path):
    usage_tuple = shutil.disk_usage(disk_path)
    free = round(usage_tuple.free / usage_tuple.total * 100, 2)
    # print(
    #     f'Full storage is (bytes) : {usage_tuple.total}\nUsed storage is (bytes) : {usage_tuple.used}\nFree storage is (bytes) : {usage_tuple.free}')
    # print(f'Disk free percentage is : {free:.2f}%')
    return free > 20


def check_cpu_usage(interval):
    cpu_usage = psutil.cpu_percent(interval=interval, percpu=False)
    # cpu_usage = psutil.cpu_percent(interval=interval, percpu=True)
    # print(f'Average per cpu usage : {cpu_usage}')
    return cpu_usage < 75


def expand_float(float_num, width=4):
    """format value to width digits"""
    d = f"{float_num:.{width - 1}f}".index(".")
    if d >= width:
        return f"{float_num:.0f}"  # Show no decimal, but round
    return f"{float_num:.{width - d}f}"  # Show width - d decimal digits