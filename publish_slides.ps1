Set-Location -Path "Slides"

#pandoc -s Module00.md Module01.md Module02.md Module03.md Module04.md Module05.md Module06.md Module07.md Module08.md Module09.md Module10.md Module11.md Module12.md -o ..\output\PythonEssentials.pdf 

pandoc -t revealjs -s Module00.md -o ..\output\Module00.html
pandoc -t revealjs -s Module01.md -o ..\output\Module01.html
pandoc -t revealjs -s Module02.md -o ..\output\Module02.html
pandoc -t revealjs -s Module03.md -o ..\output\Module03.html
pandoc -t revealjs -s Module04.md -o ..\output\Module04.html
pandoc -t revealjs -s Module05.md -o ..\output\Module05.html
pandoc -t revealjs -s Module06.md -o ..\output\Module06.html
pandoc -t revealjs -s Module07.md -o ..\output\Module07.html
pandoc -t revealjs -s Module08.md -o ..\output\Module08.html
pandoc -t revealjs -s Module09.md -o ..\output\Module09.html
pandoc -t revealjs -s Module10.md -o ..\output\Module10.html
pandoc -t revealjs -s Module11.md -o ..\output\Module11.html
pandoc -t revealjs -s Module12.md -o ..\output\Module12.html


# Rename-Item -Path "labs\Lab1.md" -NewName "Lab01.md" -Force
# Rename-Item -Path "labs\Lab2.md" -NewName "Lab02.md" -Force
# Rename-Item -Path "labs\Lab3.md" -NewName "Lab03.md" -Force
# Rename-Item -Path "labs\Lab4.md" -NewName "Lab04.md" -Force
# Rename-Item -Path "labs\Lab5.md" -NewName "Lab05.md" -Force
# Rename-Item -Path "labs\Lab6.md" -NewName "Lab06.md" -Force
# Rename-Item -Path "labs\Lab7.md" -NewName "Lab07.md" -Force
# Rename-Item -Path "labs\Lab8.md" -NewName "Lab08.md" -Force
# Rename-Item -Path "labs\Lab9.md" -NewName "Lab09.md" -Force