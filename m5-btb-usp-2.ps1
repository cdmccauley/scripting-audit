# store computer information as HTML in variable
$info = Get-WMIObject -Class Win32_ComputerSystem | 
ConvertTo-Html -Property Name, UserName, Domain, Manufacturer, Model, TotalPhysicalMemory -Fragment

# store BIOS information as HTML in variable
$bios = Get-WMIObject -class Win32_BIOS | 
ConvertTo-HTML -Property Manufacturer, Name, SerialNumber, Version -Fragment

# store process information as HTML in variable
$proc = Get-Process |
ConvertTo-HTML -Property Id, Name -Fragment

# store <head> element inner HTML in variable
$head = "<title>System Information Summary, Generated $(Get-Date)</title>`n<style>td, th { border: 1px solid red; }</style>"

# store <body> element inner HTML in variable
$body = "<h2>System Information Summary, Generated $(Get-Date)</h2>`n<h3>System Info:</h3>$info`n<h3>BIOS Info:</h3>$bios`n<h3>Proc:</h3>$proc"

# save HTML to a file
ConvertTo-HTML -Head $head -Body $body |
Out-File ".\status-report.html"