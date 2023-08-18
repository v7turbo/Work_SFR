set input=D:\for_Miheev\bmw.txt
:: расположение выходного файа
set output=result.txt    
setlocal enabledelayedexpansion
for /f "delims=-" %%a in (!input!) do (
    set tok1=%%a
    echo !tok1:~0,3!-!tok1:~3,3!-!tok1:~6,6!>>!output!)