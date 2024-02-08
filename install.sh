#!/bin/bash

echo "> Creating a new conda environment..."
conda env create -f environment.yml -p ./hmacenv

# Asking for user input
echo "> Do you want to enroll your device now? (y/N)"
read enroll
if [ "$enroll" = "Y" ] || [ "$enroll" = "y" ]; then
    echo "> Enrolling your device..."
    cd src/bins || exit
    ./first_run
else
    echo "> Skipping enrollment..."
    echo "> To (re)enroll your device later, run the following command:"
    echo "> cd src/bins && ./first_run"
fi
