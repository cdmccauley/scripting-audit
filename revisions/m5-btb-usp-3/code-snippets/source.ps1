{ Write-Output "writing from a script block" }

$scriptBlock = { Write-Output "writing from a script block" }
$scriptBlock

Invoke-Command $scriptBlock

