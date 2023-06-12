#!/bin/bash

echo "Хотите установить Python? 1) Да 2) Нет"
read user_choice

case $user_choice in
"Да")
echo "Вы выбрали установить python";;
"Нет")
echo "Все-равно установим";;
*)
echo "Что-то пошло не так, попробуйте снова. Выберите Да или Нет.";;
esac