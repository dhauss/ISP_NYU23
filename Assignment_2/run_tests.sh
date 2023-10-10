#! /bin/bash

for i in 1 2 3 4
do
    python repy.py restrictions.default encasementlib.r2py reference_monitor_dh3382.r2py reference_monitor_attack${i}_dh3382.r2py
done   
