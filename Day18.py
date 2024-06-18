import re
import sys
from collections import defaultdict

log_file_path = "security.log"

LOG_PATTERNS = {
    "syslog": re.compile(r'(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+(?P<hostname>\S+)\s+(?P<process>\S+)\[\d+\]:\s+(?P<message>.+)'),
    "apache": re.compile(r'(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<request>[^"]+)"\s+(?P<status>\d+)\s+(?P<size>\d+)')
}

def parse_log_line(line, pattern):
    match = pattern.match(line)
    if match:
        return match.groupdict()
    return None

def analyze_logs(parsed_logs):
    analysis_results = defaultdict(int)
    
    for log in parsed_logs:
        message = log.get("message", "")
        if "failed login" in message.lower():
            analysis_results["failed_login_attempts"] += 1
        analysis_results["total_logs"] += 1
    
    return analysis_results

def main(log_file_path):
    parsed_logs = []

    try:
        with open(log_file_path, "r") as log_file:
            for line in log_file:
                for pattern_name, pattern in LOG_PATTERNS.items():
                    parsed_log = parse_log_line(line, pattern)
                    if parsed_log:
                        parsed_logs.append(parsed_log)
                        break
    except FileNotFoundError:
        print(f"Log file {log_file_path} not found.")
        sys.exit(1)

    analysis_results = analyze_logs(parsed_logs)
    
    print("Analysis Results:")
    for key, value in analysis_results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main(log_file_path)
