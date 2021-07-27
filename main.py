import datetime
import glob
import math
import time


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def process_chia_log(filename, search_str):
    index = 0
    prev_time = time.strptime("2021-01-01", '%Y-%m-%d')
    prev_delta = datetime.timedelta(hours=12, minutes=0, seconds=0)
    total_time = datetime.timedelta(hours=0, minutes=0, seconds=0)
    farming_attempts = 0
    total_days = 1
    longest = 0.0
    total_elapsed = 0.0
    proofs_total = 0

    try:
        # trying to open a file in read mode
        file = open(filename, "r")

    except FileNotFoundError:
        print("File does not exist")
        return 0
    except:
        print("Other error")
        return 0

    for line in file:

        # reading each line
        index = index + 1
        if search_str in line:

            # parse the line
            elements = line.split()
            # get date and time
            if int(elements[4]) > 0:

                dt = elements[0].split('.')
                if farming_attempts > 0:
                    # calc timebetween hits
                    timebetweenhits = dt_delta - prev_delta
                    # deal with day boundaries
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
                total_elapsed = total_elapsed + elapsed

                if elapsed >= longest:
                    longest = elapsed

                farming_attempts = farming_attempts + 1

    # print(index, "---" ,line)

    file.close()
    if farming_attempts > 0:
        minutes = (total_time.total_seconds() / farming_attempts) / 60
        seconds = total_time.total_seconds() / farming_attempts - round_down(minutes) * 60
        avg_elapsed = total_elapsed / farming_attempts
        print(
            "Chia log analysis results for %s (%d days): Avg time between proof attempts %02d:%02d, Lookup times: (avg/longest) %f / %f (s) , Proofs: (attempts/found) %d / %d" % (
                filename, total_days, round_down(minutes), round(seconds), avg_elapsed, longest, farming_attempts,
                proofs_total))
    else:
        print("No proof attempts found in ", filename)
    return farming_attempts


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("\n Chia Log File Analyzer (Version 0.1)\n ====================================\n")

    logpaths = glob.glob(pathname='c:\\Users\\paul_\\.chia\\mainnet\\log\\debug.log*', recursive=False)

    search_string = '1 plots were eligible'
    h = 0
    for logpath in logpaths:
        h = h + process_chia_log(logpath, search_string)

    print("Total proof attempts : ", h)
