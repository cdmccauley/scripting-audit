# review inserts
{ Write-Output "Writing output from a script block" }

$scriptBlock = { Write-Output "Writing output from a script block" }
$scriptBlock

Invoke-Command -ScriptBlock $scriptBlock

# guided practice inserts
$session = New-PSSession -ComputerName PLABDC01

$session

Invoke-Command -Session $session -ScriptBlock { Write-Output "Writing output from a script block" }

$getIP = { Get-NetIPAddress | Select-Object InterfaceAlias, IPAddress }

Invoke-Command -ScriptBlock $getIP

# not included in assignment
Invoke-Command -Session $session -ScriptBlock $getIP
