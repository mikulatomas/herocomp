#!/bin/bash
for i in $(seq -w 01 40)
do
    echo "Translating $i example..."
    python3.6 herocomp/main.py heroc-examples/example$i.heroc > heroc-examples/example$i.s
    echo "Done"
done
