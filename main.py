from os import chdir

from pathlib import Path

import time
import math
import datetime


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def process_chia_log(filename, search_str):
    index = 0
    prev_time = time.strptime("2021-01-01", '%Y-%m-%d')
    prev_delta = datetime.timedelta(hours=12, minutes=0, seconds=0)
    total_time = datetime.timedelta(hours=0, minutes=0, seconds=0)
    hits = 0
    total_days = 1
    longest = 0.0
    proofs_total = 0
    file = open(filename, "r")
    for line in file:

        # reading each line
        index = index + 1
        if search_str in line:

            # parse the line
            elements = line.split()
            # get date and time
            if int(elements[4]) > 0:

                dt = elements[0].split('.')
                if hits > 0:
                    # calc timebetween hits
                    timebetweenhits = dt_delta - prev_delta
                    #deal with day boundaries
                    if timebetweenhits.days >= 0:
                        # only count deltas that do not cross day boundary
                        total_time = total_time + timebetweenhits
                    else:
                        # ignore day boundary but increase day count
                        total_days = total_days + 1
                    prev_time = dateTimeObject
                    prev_delta = datetime.timedelta(hours=prev_time.tm_hour, minutes=prev_time.tm_min,
                                                seconds=prev_time.tm_sec)
                dateTimeObject = time.strptime(dt[0], '%Y-%m-%dT%H:%M:%S')
                dt_delta = datetime.timedelta(hours=dateTimeObject.tm_hour, minutes=dateTimeObject.tm_min,
                                              seconds=dateTimeObject.tm_sec)
                # get elapsed time
                elapsed = float(elements[15])
                proofs_total = proofs_total + int(elements[12])

                if elapsed >= longest:
                    longest = elapsed

                hits = hits + 1

    # print(index, "---" ,line)

    file.close()
    minutes = (total_time.total_seconds() / hits) / 60
    seconds = total_time.total_seconds() / hits - round_down(minutes) * 60

    print(
        "Chia log analysis results : Average time between proof attempts %d:%d, longest attempt %f , total proof attempts = %d total proofs found = %d over %d days" % (
            round_down(minutes), round(seconds), longest, hits, proofs_total, total_days))

    return hits


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logpath = "c:\\Users\\paul_\\.chia\\mainnet\\log\\debug.log"
    search_string = '1 plots were eligible'
    h = process_chia_log(logpath, search_string)
