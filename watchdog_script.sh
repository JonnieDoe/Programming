#!/bin/bash

#
# INFO: depending on Linux distro some parameters for commands might not actually work; usually Debian family OS is OK 
#
# Strict check for apache2 service every 2 minutes. 
# You can place the script in cron for user root
# */2 * * * * /bin/bash /root/watchdog.sh 
#
# OR
# Put the script to run at startup and it will run in the background for indefinitely until the condition of 4 failed start attempts is trigegred 
#

# Debugging
# set -e

# Logging file location
script_location="/var/run/process_check.log"

# Check if file exists otherwise create it; if it exists delete its content
if [[ ! -f ${script_location} ]]; then 
	touch ${script_location}
else
	> ${script_location}
fi

# Keep checking every 2 minutes
while true; do

	# Every pasing clear the content of the file
        > ${script_location}
	
	# Get Apache2 process and network connection check status; the commands get all instances of running apache2 an counts them
	# apache_proc=$(/bin/ps axw | /bin/grep /usr/sbin/apache2 | /bin/grep -v "grep" | wc -l)

	# On some distros there might be more than 1 instance of Apache2 running and is OK, so get network status
	apache_net=$(/bin/netstat -tlnp | /bin/grep "apache2" | wc -l)

	if [[ ${apache_net} -eq 1 ]]; then
		date +"Status: Apache2 process is running! - %a %b %e %H:%M:%S %Z %Y" >> /var/run/process_check.log

		# Check port 80 (default for Apache2)
		nc -z localhost 80

		if [[ $? -eq 0 ]]; then
			date +"Status: Apache2 port is opened! - %a %b %e %H:%M:%S %Z %Y" >> /var/run/process_check.log
		else
			date +"Status: Apache2 is not responding! Please investigate - %a %b %e %H:%M:%S %Z %Y" >> /var/run/process_check.log
		fi
	else
		date +"Status: Apache2 is down! - %a %b %e %H:%M:%S %Z %Y" >> /var/run/process_check.log
		echo "Trying to start Apache2: ... " >> /var/run/process_check.log
 
 		# First attempt to start Apache2
		/usr/sbin/service apache2 start &> /dev/null 

		if [[ $? -eq 0 ]]; then
			date +"Status: Apache2 started OK! - %a %b %e %H:%M:%S %Z %Y" >> /var/run/process_check.log
		else
			counter=3

			# Subsequent attempt (3) to start Apache2 
			until [ ${counter} -lt 1 ]; do
				/usr/sbin/service apache2 start &> /dev/null

				if [[ $? -eq 0 ]]; then
					date +"Status: Apache2 started OK! - %a %b %e %H:%M:%S %Z %Y" >> /var/run/process_check.log

					break
				else
					date +"Status: Apache2 failed to start! - %a %b %e %H:%M:%S %Z %Y" >> /var/run/process_check.log

					let counter-=1

					if [[ ${counter} -eq 0 ]]; then
						exit 1
					fi
				fi

				# Wait 15 seconds for another retry
				sleep 15
			done 
		fi
	fi

	sleep 120

done

exit 0
