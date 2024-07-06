import json
from datetime import datetime

# Define the main function to develop the physical security plan
def develop_security_plan():
    # Step 1: Define security objectives
    security_objectives = {
        "protect_assets": "Ensure the protection of physical and digital assets",
        "protect_personnel": "Ensure the safety and security of all personnel",
        "prevent_intrusion": "Prevent unauthorized access to facilities",
        "emergency_response": "Establish effective emergency response procedures"
    }

    # Step 2: Identify assets and areas to protect
    assets = [
        {"name": "Main Office Building", "type": "Building", "value": "High"},
        {"name": "Data Center", "type": "Facility", "value": "Critical"},
        {"name": "Employee Workstations", "type": "Equipment", "value": "Medium"},
        {"name": "Server Room", "type": "Room", "value": "Critical"},
        {"name": "Parking Lot", "type": "Area", "value": "Low"},
    ]

    # Step 3: Conduct risk assessment
    risk_assessment = [
        {"asset": "Main Office Building", "threat": "Unauthorized access", "vulnerability": "Single entry point"},
        {"asset": "Data Center", "threat": "Theft", "vulnerability": "Insufficient surveillance"},
        {"asset": "Employee Workstations", "threat": "Vandalism", "vulnerability": "Unrestricted access"},
        {"asset": "Server Room", "threat": "Fire", "vulnerability": "Lack of fire suppression system"},
        {"asset": "Parking Lot", "threat": "Vehicle theft", "vulnerability": "Poor lighting"}
    ]

    # Step 4: Develop countermeasures
    countermeasures = {
        "Unauthorized access": ["Install access control systems", "Implement visitor management"],
        "Theft": ["Enhance surveillance with CCTV", "Install alarm systems"],
        "Vandalism": ["Increase security patrols", "Implement restricted access policies"],
        "Fire": ["Install fire suppression systems", "Conduct regular fire drills"],
        "Vehicle theft": ["Improve lighting", "Install security cameras"]
    }

    # Step 5: Create emergency response plan
    emergency_response_plan = {
        "fire": {
            "actions": ["Activate fire alarm", "Evacuate building", "Call fire department"],
            "contacts": ["Fire department: 911", "Building manager: 555-1234"]
        },
        "intrusion": {
            "actions": ["Alert security personnel", "Lockdown facility", "Notify police"],
            "contacts": ["Police: 911", "Security manager: 555-5678"]
        },
        "medical": {
            "actions": ["Call emergency services", "Provide first aid", "Notify family"],
            "contacts": ["Ambulance: 911", "HR: 555-9101"]
        }
    }

    # Step 6: Develop training and awareness programs
    training_programs = [
        {"program": "Fire Safety Training", "frequency": "Annually"},
        {"program": "Access Control Training", "frequency": "Bi-annually"},
        {"program": "Emergency Response Drills", "frequency": "Quarterly"},
        {"program": "Workplace Safety Training", "frequency": "Annually"},
    ]

    # Combine all elements into the security plan
    security_plan = {
        "objectives": security_objectives,
        "assets": assets,
        "risk_assessment": risk_assessment,
        "countermeasures": countermeasures,
        "emergency_response_plan": emergency_response_plan,
        "training_programs": training_programs,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Save the plan to a JSON file
    with open('physical_security_plan.json', 'w') as file:
        json.dump(security_plan, file, indent=4)
    
    # Print confirmation message
    print("Physical security plan developed and saved as 'physical_security_plan.json'.")

# Run the main function
if __name__ == "__main__":
    develop_security_plan()
