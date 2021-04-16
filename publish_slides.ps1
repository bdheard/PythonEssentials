Set-Location -Path "Slides"

pandoc -s Module00.md -o ..\output\Module00.pdf 
pandoc -s Module01.md -o ..\output\Module01.pdf   
pandoc -s Module02.md -o ..\output\Module02.pdf   
pandoc -s Module03.md -o ..\output\Module03.pdf   
pandoc -s Module04.md -o ..\output\Module04.pdf   
pandoc -s Module05.md -o ..\output\Module05.pdf
pandoc -s Module06.md -o ..\output\Module06.pdf 
pandoc -s Module07.md -o ..\output\Module07.pdf   
pandoc -s Module08.md -o ..\output\Module08.pdf   
pandoc -s Module09.md -o ..\output\Module09.pdf   
pandoc -s Module10.md -o ..\output\Module10.pdf   
pandoc -s Module11.md -o ..\output\Module11.pdf
pandoc -s Module12.md -o ..\output\Module12.pdf

Set-Location -Path ..

pandoc -t revealjs -s Slides\Module00.md -o output\Module00.html
pandoc -t revealjs -s Slides\Module01.md -o output\Module01.html
pandoc -t revealjs -s Slides\Module02.md -o output\Module02.html
pandoc -t revealjs -s Slides\Module03.md -o output\Module03.html
pandoc -t revealjs -s Slides\Module04.md -o output\Module04.html
pandoc -t revealjs -s Slides\Module05.md -o output\Module05.html
pandoc -t revealjs -s Slides\Module06.md -o output\Module06.html
pandoc -t revealjs -s Slides\Module07.md -o output\Module07.html
pandoc -t revealjs -s Slides\Module08.md -o output\Module08.html
pandoc -t revealjs -s Slides\Module09.md -o output\Module09.html
pandoc -t revealjs -s Slides\Module10.md -o output\Module10.html
pandoc -t revealjs -s Slides\Module11.md -o output\Module11.html
pandoc -t revealjs -s Slides\Module12.md -o output\Module12.html

# Rename-Item -Path "slides\module1.md" -NewName "Module01.md" -Force
# Rename-Item -Path "slides\module2.md" -NewName "Module02.md" -Force
# Rename-Item -Path "slides\module3.md" -NewName "Module03.md" -Force
# Rename-Item -Path "slides\module4.md" -NewName "Module04.md" -Force
# Rename-Item -Path "slides\module5.md" -NewName "Module05.md" -Force
# Rename-Item -Path "slides\module6.md" -NewName "Module06.md" -Force
# Rename-Item -Path "slides\module7.md" -NewName "Module07.md" -Force
# Rename-Item -Path "slides\module8.md" -NewName "Module08.md" -Force
# Rename-Item -Path "slides\module9.md" -NewName "Module09.md" -Force