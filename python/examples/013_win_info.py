import wmi
from datetime import datetime as dt


win_info = {}

c = wmi.WMI()
cs = c.Win32_ComputerSystem()[0]
win_info['sys_model'] = cs.Model
win_info['sys_name'] = cs.Name
win_info['sys_domain'] = cs.Domain
win_info['sys_user'] = cs.UserName
os = c.Win32_OperatingSystem()[0]
win_info['os_name'] = os.Caption
win_info['os_version'] = os.Version
win_info['os_boot'] = dt.strptime(os.LastBootUpTime[:14], '%Y%m%d%H%M%S')
win_info['os_time'] = dt.strptime(os.LocalDateTime[:14], '%Y%m%d%H%M%S')
win_info['os_status'] = os.Status
disks = c.Win32_DiskDrive()
win_info['disks'] = []
win_info['disks_SN'] = []
win_info['disks_SMART'] = []
for disk in disks:
    win_info['disks'].append(disk.Caption)
    win_info['disks_SN'].append(disk.SerialNumber)
    win_info['disks_SMART'].append(disk.Status)



for k, v in win_info.items():
    print(k, v)
