#!/bin/bash

while true; do
    read -p "Введите слово: " word

    if [ "$word" = "." ]; then
        echo "Сценарий завершен."
        exit 0
    fi

    if [ ${#word} -le 5 ]; then
        echo "ok"
    else
        echo "Слово слишком длинное"
    fi
done
