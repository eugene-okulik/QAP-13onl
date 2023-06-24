@echo off
setlocal enabledelayedexpansion

echo Хотите установить Python?
echo 1) Да
echo 2) Нет

set /p choice=Выберите вариант (1 или 2): 

if "!choice!"=="1" (
    echo Вы выбрали установить Python.
) else (
    echo Все-равно установим.
)