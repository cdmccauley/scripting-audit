$SearchPath = Read-Host "Please enter path to search"
Get-ChildItem $SearchPath -Recurse -ErrorAction SilentlyContinue | 
Select Name, FullName | 
ConvertTo-Csv |
Tee-Object -FilePath "C:\search-path.csv"