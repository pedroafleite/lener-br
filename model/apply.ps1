$InputFiles = Get-ChildItem 'C:\Users\Pedro\Documents\Python Scripts\notas-trabalhistas\input\'
$OutputPath = 'C:\Users\Pedro\Documents\Python Scripts\notas-trabalhistas\output\'

ForEach($File in $InputFiles) {
    Get-Content $File |
        python evaluateText.py $InputFiles | Out-File -FilePath $OutputPath -Encoding utf8 |
            Out-File (Join-Path -Path $OutputPath -ChildPath $File.Name)
}