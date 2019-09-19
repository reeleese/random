#!/bin/bash

echo mmm1.c
gcc mmm1.c
./a.out
./a.out | md5sum
echo

echo mmm2.c
gcc mmm2.c
./a.out
./a.out | md5sum
echo

echo mmm3.c
gcc mmm3.c
./a.out
./a.out | md5sum
echo

echo mmm4.c
gcc mmm4.c
./a.out
./a.out | md5sum
echo

echo mmm5.c
gcc mmm5.c
./a.out
./a.out | md5sum
echo

echo mmm6.c
gcc mmm6.c
./a.out
./a.out | md5sum
echo

echo mmm7.c
gcc mmm7.c
./a.out
./a.out | md5sum
echo

echo mmm.py
python3 mmm.py
python3 mmm.py | md5sum
