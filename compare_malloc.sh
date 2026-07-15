#!/usr/bin/env bash

WORKDIR="Work"

for method in "tup" "dict" "ntup" "cls"; do
    echo $method
    python ./$WORKDIR/readrides.py $method
done
