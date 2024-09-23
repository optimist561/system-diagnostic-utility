System Diagnostic Utility

-------------------------

This Python program is designed to perform a variety of system diagnostic checks, 
providing insights into network performance, system resources, and hardware status. 
It logs detailed information into a file called diagnostics.log for easy review and troubleshooting.

-------------------------

Requirements:
Python 3.x
psutil library (install using pip install psutil)

-------------------------

Features:

-------------------------

Network Connectivity Check:

Pings Google's DNS server (8.8.8.8) to verify internet connectivity and logs the result.
-------------------------
Signal Strength Check:

Retrieves and logs the signal strength of Wi-Fi adapters (supported on Windows and Linux).
-------------------------
Packet Loss Check:

Measures and logs packet loss by sending multiple ping requests.
-------------------------
System Resource Monitoring:

Logs CPU and memory usage to help identify performance bottlenecks.
-------------------------
Disk Usage Check:

Logs the percentage of disk space currently in use on the system.
-------------------------
Network Adapter Information:

Lists all network adapters and their configuration details (IP addresses, MAC addresses, etc.).
-------------------------
Active Processes Check:

Logs all active processes running on the system, including their process ID (PID), name, and user.
-------------------------
Logging:

All diagnostic information is stored in a file named diagnostics.log for further analysis.

-------------------------

INSTRUCTIONS:

-------------------------

1. Run the program using Python.

2.Follow the on-screen prompts as the diagnostics run.

3.After diagnostics complete, review the results in the diagnostics.log file.

