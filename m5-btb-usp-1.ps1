# print uptime
# Get-CimInstance may be aliased as gcim, -ClassName can be ommitted
(Get-Date) - (Get-CimInstance -ClassName Win32_OperatingSystem).LastBootUpTime

# print computer name and last boot time
# Get-CimInstance may be aliased as gcim, Select-Object may be aliased as Select
Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object CSName, LastBootUpTime