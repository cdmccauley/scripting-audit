# display computer information for computer the script is being run on
Get-WmiObject -Class Win32_ComputerSystem

# display computer information for another computer on the domain, ComputerName should be different than output from above
Get-WmiObject -Class Win32_ComputerSystem -ComputerName "W10LAB03"