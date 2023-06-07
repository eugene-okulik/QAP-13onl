#!/bin/bash

word=""


while [[ $word != "." ]]
do
echo
echo "Enter something"
read word

if [[ ${#word} -le 5 ]]
then echo "Lendth of phrase = ${#word}. It's ok :)"
else echo "Phrase is too long :("
fi

done

echo "Bye"