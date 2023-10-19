#!/bin/bash

for referencemonitor in reference_monitor_*
do
    echo $referencemonitor under test
    for testcase in dh3382_*
    do
        python repy.py restrictions.default encasementlib.r2py $referencemonitor $testcase
    done
done