#! /usr/bin/env python3

from generate_insert_statement import generate_insert
from load_csv import load_csv_main

data = load_csv_main()

for i in data:
    print(generate_insert('boss_hog', i))

