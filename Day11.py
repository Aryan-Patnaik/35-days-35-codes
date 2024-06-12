import os

def create_incident_response_plan(file_path):
    # Define the incident response plan template as a multi-line string
    plan_template = """
    Incident Response Plan Template
    ==============================

    1. Introduction
    ----------------
    This Incident Response Plan (IRP) outlines the procedures for detecting, responding to, and recovering from security incidents. The goal is to minimize the impact on operations and ensure the timely restoration of services.

    2. Purpose
    ----------
    The purpose of this IRP is to provide a structured approach to managing and mitigating incidents to protect organizational assets, including data, systems, and personnel.

    3. Scope
    --------
    This plan applies to all systems, networks, and applications within the organization. It covers all types of security incidents, including but not limited to data breaches, malware infections, and unauthorized access.

    4. Roles and Responsibilities
    -----------------------------
    - Incident Response Team (IRT): The primary group responsible for managing incidents.
    - Incident Commander: Leads the incident response efforts.
    - IT Staff: Provides technical support and expertise.
    - Legal and Compliance: Ensures regulatory requirements are met.
    - Communication Team: Manages internal and external communications.

    5. Incident Classification
    -------------------------
    Incidents are classified based on their severity and impact:
    - Low: Minor incidents with minimal impact.
    - Medium: Incidents with moderate impact requiring prompt attention.
    - High: Major incidents with significant impact on operations.

    6. Incident Detection and Reporting
    -----------------------------------
    - Detection: Methods for detecting incidents include monitoring systems, user reports, and automated alerts.
    - Reporting: All incidents should be reported immediately to the Incident Response Team via [reporting mechanism].

    7. Incident Response Procedures
    -------------------------------
    a. Identification: Confirm the incident and gather initial details.
    b. Containment: Implement measures to limit the impact and spread of the incident.
    c. Eradication: Identify and eliminate the root cause of the incident.
    d. Recovery: Restore systems and operations to normal.
    e. Lessons Learned: Conduct a post-incident review to identify improvements.

    8. Communication Plan
    ---------------------
    - Internal Communication: Keep stakeholders informed throughout the incident lifecycle.
    - External Communication: Manage public relations and notify affected parties as required.

    9. Training and Awareness
    -------------------------
    Regular training sessions should be conducted to ensure all employees are aware of the incident response procedures and their roles in the process.

    10. Review and Update
    ---------------------
    This Incident Response Plan should be reviewed and updated annually or following a significant incident to ensure its effectiveness.

    Appendix A: Contact Information
    --------------------------------
    - Incident Response Team: [Contact details]
    - IT Support: [Contact details]
    - Legal and Compliance: [Contact details]
    - Communication Team: [Contact details]

    Appendix B: Incident Report Form
    --------------------------------
    - Incident Date and Time:
    - Reported By:
    - Description of Incident:
    - Systems Affected:
    - Actions Taken:
    """

    # Open the specified file in write mode
    with open(file_path, 'w') as file:
        # Write the incident response plan template to the file
        file.write(plan_template.strip())

    # Print a message indicating that the template has been created
    print(f"Incident Response Plan template created at {file_path}")

# Define the path to the file where the template will be saved
file_path = 'file1.txt'

# Call the function to create the incident response plan template
create_incident_response_plan(file_path)
