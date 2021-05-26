# $SearchPath = Read-Host "Please enter path to search"
$SearchPath = ".\*.png"
Get-ChildItem $SearchPath -Recurse -ErrorAction SilentlyContinue | 
Select-Object Name, FullName | 
ConvertTo-Csv |
Tee-Object -FilePath ".\search-path.csv"