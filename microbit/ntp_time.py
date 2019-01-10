import ntplib
from time import ctime

ntp_client = ntplib.NTPClient()

# Provide the respective ntp server ip in below function
response = ntp_client.request('uk.pool.ntp.org', version=3)

print(ctime(response.tx_time))
