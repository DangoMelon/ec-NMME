#!bin/bash -i

conda activate pangeo

# Create URL database
python createURL.py

cd models

FILES=$(ls *.txt)

for file in $FILES
do
    echo $file
done
