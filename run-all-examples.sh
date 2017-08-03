#!/bin/bash
for i in $(seq -w 01 40)
do
    echo "Compiling example $i"
    gcc -m64 -o heroc-examples/example$i heroc-examples/example$i.s heroc-examples/herocio.c
    echo "Running example $i"
    heroc-examples/example$i > heroc-examples/example$i.out.txt
done
