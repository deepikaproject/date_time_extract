from datetime import datetime

log_list = [
    '2020-11-30T09:42:10Z [info] Deploying disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:43:49Z [info] CASS: Instance Deployment started.',
    '2020-11-30T09:43:49Z [info] Config: Interval:10s, Quiet:false, Hostname:"localhost", Flush Interval:10s.',
    '2020-11-30T09:44:09Z [error] When writing to ["http:\localhost"]: Post "localhost": dial tcp 127.0.0.1:8086: connect: connection refused',
    '2020-11-30T09:44:10Z [warning] Error in plugin: warning getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:44:10Z [info] Deploying disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:45:10Z [info] CASS: Instance Deployment configured.',
    '2020-11-30T09:45:10Z [warning] Warning in plugin: error getting disk io info: open /proc/diskstats: no such file or directory.',
    '2020-11-30T09:45:20Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:47:10Z [info] Info in plugin: error getting disk io info: open /proc/diskstats: no such file or directory in Instance Deployment',
    '2020-11-30T09:49:10Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:51:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:54:10Z [info] CASS: Instance Deployment complete.',
    '2020-11-30T09:54:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:55:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:57:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
]


def parse_log_time(time):
    data = datetime.strptime(time[:-1],"%Y-%m-%dT%H:%M:%S")
    return data


def extract_datetime(log_list):
    for i in log_list:
        if (i.find('Instance Deployment started')) != -1:
            start_date = i.split(' ')[0]
            continue
        if (i.find('Instance Deployment complete.')) != -1:
            end_date = i.split(' ')[0]
            break
    else:
        raise Exception("deployment did not happened")

    return start_date, end_date


if __name__ == '__main__':
    start_time, end_time = extract_datetime(log_list)
    start_time = parse_log_time(start_time)
    end_time = parse_log_time(end_time)
    print(end_time - start_time)
