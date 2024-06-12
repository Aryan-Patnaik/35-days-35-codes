import os
import subprocess
import platform

def run_command(command):
    try:
        # Execute the given command in the shell
        subprocess.check_call(command, shell=True)
        print(f"Executed: {command}")
    except subprocess.CalledProcessError as e:
        # Print an error message if the command fails
        print(f"Failed to execute: {command}\n{e}")

def setup_firewall():
    # Flush all current rules in the default table
    run_command("iptables -F")
    # Delete all user-defined chains in the default table
    run_command("iptables -X")
    # Flush all current rules in the nat table
    run_command("iptables -t nat -F")
    # Delete all user-defined chains in the nat table
    run_command("iptables -t nat -X")
    # Flush all current rules in the mangle table
    run_command("iptables -t mangle -F")
    # Delete all user-defined chains in the mangle table
    run_command("iptables -t mangle -X")
    # Flush all current rules in the raw table
    run_command("iptables -t raw -F")
    # Delete all user-defined chains in the raw table
    run_command("iptables -t raw -X")

    # Set default policy to drop all incoming traffic
    run_command("iptables -P INPUT DROP")
    # Set default policy to drop all forwarding traffic
    run_command("iptables -P FORWARD DROP")
    # Set default policy to allow all outgoing traffic
    run_command("iptables -P OUTPUT ACCEPT")

    # Allow unlimited traffic on the loopback interface for input
    run_command("iptables -A INPUT -i lo -j ACCEPT")
    # Allow unlimited traffic on the loopback interface for output
    run_command("iptables -A OUTPUT -o lo -j ACCEPT")

    # Allow incoming SSH traffic on port 22
    run_command("iptables -A INPUT -p tcp --dport 22 -j ACCEPT")

    # Allow incoming HTTP traffic on port 80
    run_command("iptables -A INPUT -p tcp --dport 80 -j ACCEPT")
    # Allow incoming HTTPS traffic on port 443
    run_command("iptables -A INPUT -p tcp --dport 443 -j ACCEPT")

    # Allow established and related connections for incoming traffic
    run_command("iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
    # Allow established and related connections for forwarding traffic
    run_command("iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")

    # Log dropped incoming packets with a rate limit (optional)
    run_command("iptables -A INPUT -m limit --limit 5/min -j LOG --log-prefix 'iptables INPUT drop: ' --log-level 7")
    # Log dropped forwarding packets with a rate limit (optional)
    run_command("iptables -A FORWARD -m limit --limit 5/min -j LOG --log-prefix 'iptables FORWARD drop: ' --log-level 7")

    print("Firewall setup completed.")

if __name__ == "__main__":
    # Check if the operating system is Windows
    if platform.system() == "Windows" or os.name == "nt":
        print("This script is designed to run on Unix-like systems and may not work properly on Windows.")
    else:
        # Check if the script is being run as root
        if os.getuid() != 0:
            print("This script must be run as root.")
        else:
            # Set up the firewall rules
            setup_firewall()
