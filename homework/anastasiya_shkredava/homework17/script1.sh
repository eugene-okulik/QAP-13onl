#!/bin/bash

PS3="Хотите установить Python?"
echo
select answ in "Да" "Нет"
do
if [[ $answ == "Да" ]]
then
echo "Вы выбрали установить python"
elif [[ $answ == "Нет" ]]
then
echo "Все-равно установим"
else
echo "А такого варианта ответа нет =)"
fi
break
done
