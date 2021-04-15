
foreach($file in Get-ChildItem "Slides" -Filter *.md)
{
    pandoc -s $_ -o "output\$($_.Name + ".pdf")" 
}


pandoc -s Module00.md -o Module00.pdf 
pandoc -s Module01.md -o Module01.pdf   
pandoc -s Module02.md -o Module02.pdf   
pandoc -s Module03.md -o Module03.pdf   
pandoc -s Module04.md -o Module04.pdf   
pandoc -s Module05.md -o Module05.pdf
pandoc -s Module06.md -o Module06.pdf 
pandoc -s Module07.md -o Module07.pdf   
pandoc -s Module08.md -o Module08.pdf   
pandoc -s Module09.md -o Module09.pdf   
pandoc -s Module10.md -o Module10.pdf   
pandoc -s Module11.md -o Module11.pdf
pandoc -s Module12.md -o Module12.pdf

pandoc -s Slides\Module00.md -o Slides\Module00.html 
pandoc -s Slides\Module01.md -o Slides\Module01.html   
pandoc -s Slides\Module02.md -o Slides\Module02.html   
pandoc -s Slides\Module03.md -o Slides\Module03.html   
pandoc -s Slides\Module04.md -o Slides\Module04.html   
pandoc -s Slides\Module05.md -o Slides\Module05.html
pandoc -s Slides\Module06.md -o Slides\Module06.html 
pandoc -s Slides\Module07.md -o Slides\Module07.html   
pandoc -s Slides\Module08.md -o Slides\Module08.html   
pandoc -s Slides\Module09.md -o Slides\Module09.html   
pandoc -s Slides\Module10.md -o Slides\Module10.html   
pandoc -s Slides\Module11.md -o Slides\Module11.html
pandoc -s Slides\Module12.md -o Slides\Module12.html

Rename-Item -Path "slides\module1.md" -NewName "Module01.md" -Force
Rename-Item -Path "slides\module2.md" -NewName "Module02.md" -Force
Rename-Item -Path "slides\module3.md" -NewName "Module03.md" -Force
Rename-Item -Path "slides\module4.md" -NewName "Module04.md" -Force
Rename-Item -Path "slides\module5.md" -NewName "Module05.md" -Force
Rename-Item -Path "slides\module6.md" -NewName "Module06.md" -Force
Rename-Item -Path "slides\module7.md" -NewName "Module07.md" -Force
Rename-Item -Path "slides\module8.md" -NewName "Module08.md" -Force
Rename-Item -Path "slides\module9.md" -NewName "Module09.md" -Force