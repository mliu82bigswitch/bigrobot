#!/bin/sh
# Move logs into data.<date_stamp> directory.
# There are quite a bit of logs generated, so rm_logs.sh should occasionally
# be used to empty the logs to recover the disk space.

if [ ! -x ../bin/gobot ]; then
    echo "Error: This script must be executed in the bigrobot/catalog/ directory."
    exit 1
fi

ts=`date "+%Y-%m-%d_%H%M%S"`
dest=.data.$ts

mkdir $dest
mv -f raw_data.* debug.log dev_commands.log syslog.txt report.html output.xml log.html bigrobot_listener.log myrobot.log bigrobot_logs* *.txt.gz $dest 2> /dev/null

