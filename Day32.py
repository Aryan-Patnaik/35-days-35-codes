import os  # Import the os module for interacting with the operating system
import shutil  # Import the shutil module for file and directory operations
import subprocess  # Import the subprocess module for running system commands
from git import Repo  # Import the Repo class from GitPython for cloning repositories
import bandit  # Import the bandit module for static code analysis
import bandit.core.manager  # Import the BanditManager class from bandit.core.manager
import bandit.core.config  # Import the BanditConfig class from bandit.core.config
import bandit.core.constants as b_constants  # Import constants from bandit.core.constants
import bandit.formatters.json as bandit_json  # Import the JSON formatter from bandit.formatters.json
import safety.formatter  # Import the safety.formatter module for formatting Safety reports
import safety.safety  # Import the safety.safety module for checking vulnerable dependencies
import safety.util  # Import the safety.util module for utility functions

REPO_URL = 'GITHUB REPO LINK'  # Replace with the target repository URL
CLONE_DIR = './cloned_repo'  # Directory to clone the repository into
BANDIT_REPORT = 'bandit_report.json'  # File to save the Bandit report
SAFETY_REPORT = 'safety_report.txt'  # File to save the Safety report

def clone_repository(url, to_path):
    if os.path.exists(to_path):  # Check if the directory already exists
        print(f"Directory {to_path} already exists. Deleting it.")
        shutil.rmtree(to_path)  # Delete the directory if it exists
    print(f"Cloning repository {url} to {to_path}")
    Repo.clone_from(url, to_path)  # Clone the repository to the specified path

def run_bandit(target_dir, report_file):
    print(f"Running Bandit on {target_dir}")
    b_conf = bandit.core.config.BanditConfig()  # Create a BanditConfig object
    b_mgr = bandit.core.manager.BanditManager(b_conf, 'file')  # Create a BanditManager object
    b_mgr.discover_files([target_dir], True)  # Discover files in the target directory
    b_mgr.run_tests()  # Run Bandit tests on the discovered files
    
    with open(report_file, 'w') as f:  # Open the report file for writing
        bandit_json.report(b_mgr, f, b_constants.verbose)  # Write the Bandit report in JSON format
    
    print(f"Bandit report saved to {report_file}")

def run_safety(target_dir, report_file):
    print(f"Running Safety on {target_dir}")
    requirements_files = []  # Initialize an empty list to hold paths to requirements.txt files
    for root, _, files in os.walk(target_dir):  # Walk through the target directory
        for file in files:
            if file == 'requirements.txt':  # Check if the file is requirements.txt
                requirements_files.append(os.path.join(root, file))  # Add the file path to the list
    vulnerabilities = safety.safety.check(requirements_files, key=None, db_mirror=None, cached=True)  # Check for vulnerabilities
    with open(report_file, 'w') as f:  # Open the report file for writing
        f.write(safety.formatter.SAFE.format_vulnerabilities(vulnerabilities))  # Write the Safety report
    print(f"Safety report saved to {report_file}")

def main():
    clone_repository(REPO_URL, CLONE_DIR)  # Clone the repository
    run_bandit(CLONE_DIR, BANDIT_REPORT)  # Run Bandit on the cloned repository
    run_safety(CLONE_DIR, SAFETY_REPORT)  # Run Safety on the cloned repository
    print("Secure code review completed.")

if __name__ == '__main__':
    main()  # Run the main function if the script is executed directly
