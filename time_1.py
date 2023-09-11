#! /usr/bin/env python3
import time

current_time_millis = time.time()
while True:
    for i in range (1000000):
        i = i +1

    end_time_millis = time.time()

    print(end_time_millis - current_time_millis)


