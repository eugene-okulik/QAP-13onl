#!/bin/bash

word=""


while [[ $word != "." ]]
do
echo "Enter the word"
read word
if [[ ${#word} -le 5 && ${#word} -gt 0 && $word != "." ]]
then
echo "ok"
elif [[ ${#word} -gt 5 ]]
then
echo "слово слишком длинное"
elif [[ ${#word} -eq 0 ]]
then
echo "You did not enter the word"
fi
done