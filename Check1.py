import os
import platform
import subprocess
import psutil
import logging

# Set up logging
logging.basicConfig(filename='diagnostics.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def check_network_connectivity():
    try:
        logging.info("Checking network connectivity...")
        if platform.system() == "Windows":
            output = subprocess.check_output(["ping", "8.8.8.8", "-n", "4"], shell=True).decode()
        else:
            output = subprocess.check_output(["ping", "-c", "4", "8.8.8.8"]).decode()
        logging.info("Network connectivity: OK")
        logging.info(output)
    except subprocess.CalledProcessError:
        logging.error("Network connectivity: Failed")

def check_signal_strength():
    try:
        logging.info("Checking signal strength...")
        if platform.system() == "Windows":
            output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
            for line in output.split('\n'):
                if "Signal" in line:
                    signal_strength = line.split(":")[1].strip()
                    logging.info(f"Signal strength: {signal_strength}")
                    break
        elif platform.system() == "Linux":
            output = subprocess.check_output("iwconfig", shell=True).decode()
            for line in output.split('\n'):
                if "Link Quality" in line:
                    signal_strength = line.split("=")[1].split()[0]
                    logging.info(f"Signal strength: {signal_strength}")
                    break
        else:
            logging.warning("Signal strength check not supported on this OS")
    except Exception as e:
        logging.error(f"Error checking signal strength: {e}")

def check_packet_loss():
    try:
        logging.info("Checking packet loss...")
        if platform.system() == "Windows":
            output = subprocess.check_output(["ping", "8.8.8.8", "-n", "10"], shell=True).decode()
        else:
            output = subprocess.check_output(["ping", "8.8.8.8", "-c", "10"]).decode()
        logging.info(output)
        for line in output.split('\n'):
            if "loss" in line or "Lost" in line:
                packet_loss = line.split(",")[-1].strip()
                logging.info(f"Packet loss: {packet_loss}")
                break
    except Exception as e:
        logging.error(f"Error checking packet loss: {e}")

def check_system_resources():
    try:
        logging.info(f"CPU usage: {psutil.cpu_percent(interval=1)}%")
        logging.info(f"Memory usage: {psutil.virtual_memory().percent}%")
    except Exception as e:
        logging.error(f"Error checking system resources: {e}")

def check_disk_usage():
    try:
        logging.info("Checking disk usage...")
        disk_usage = psutil.disk_usage('/')
        logging.info(f"Disk usage: {disk_usage.percent}% used")
    except Exception as e:
        logging.error(f"Error checking disk usage: {e}")

def check_network_adapters():
    try:
        logging.info("Checking network adapters...")
        adapters = psutil.net_if_addrs()
        for adapter_name, adapter_info in adapters.items():
            logging.info(f"Adapter: {adapter_name}")
            for info in adapter_info:
                logging.info(f"  {info}")
    except Exception as e:
        logging.error(f"Error checking network adapters: {e}")

def check_active_processes():
    try:
        logging.info("Checking active processes...")
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            logging.info(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}")
    except Exception as e:
        logging.error(f"Error checking active processes: {e}")

def main():
    try:
        logging.info("Running diagnostics...")
        check_network_connectivity()
        check_signal_strength()
        check_packet_loss()
        check_system_resources()
        check_disk_usage()
        check_network_adapters()
        check_active_processes()
        logging.info("Diagnostics complete.")
    except Exception as e:
        logging.error(f"An error occurred during diagnostics: {e}")
    input("Press Enter to exit...")  # Keeps the console window open

if __name__ == "__main__":
    main()
