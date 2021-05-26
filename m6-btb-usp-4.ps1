# get file content from downloaded file and pipe it to powershell, -NoProfile can be ommitted
Get-Content .\downloaded-script.ps1 | PowerShell.exe -NoProfile

# the file content is:
# write-host "`nYou are logged in as: ${env:UserName} and working on ${env:ComputerName} that is part of the ${env:UserDomain} Windows domain.`n"