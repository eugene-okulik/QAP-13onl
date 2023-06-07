#!/bin/bash

echo "Хотите установить Python?"
echo "1. Да"
echo "2. Нет"

read -p "Выберите действие: " choice

if [ "$choice" == "1" ]; then
	echo "Вы выбрали установить Python"
elif [ "$choice" == "2" ]; then
	echo "Всё равно установим :р"
else
	echo "Неправильный выбор"
fi
