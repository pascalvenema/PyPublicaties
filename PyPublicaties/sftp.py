import os
import paramiko
import xml.etree.ElementTree as ET
from skeleton import OfficielePublicatie

def setup_sftp():
    # Define the SFTP server information
    host = "bestanden.officielebekendmakingen.nl"
    port = 22  # Default SFTP port
    username = "anonymous"
    password = "anonymous@domain.com"

    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    # Now you have established the SFTP connection using SSH, and you can create an SFTP client
    sftp = ssh.open_sftp()

    return sftp

# Assuming setup_sftp() is defined as provided
def fetch_and_process_xml(year, month, day):
    sftp = setup_sftp()  # Connect to the SFTP server

    base_path = f"/{year}/{month}/{day}/"
    try:
        # List subdirectories for the given date
        for subcategory in sftp.listdir(base_path):
            subcategory_path = os.path.join(base_path, subcategory)
            for identifier in sftp.listdir(subcategory_path):
                file_path = os.path.join(subcategory_path, identifier, "metadata_owms.xml")
                with sftp.file(file_path, 'r') as file:
                    xml_content = file.read()
                    xml_root = ET.fromstring(xml_content)
                    publication_instance = OfficielePublicatie.from_xml_element(xml_root, namespaces={})
                    # At this point, publication_instance is populated with the XML data
                    # Process the instance as needed (e.g., storing, displaying)
                    print(publication_instance)  # Example action

    except Exception as e:
        print(f"Error processing files: {e}")
    finally:
        sftp.close()

# Remember to replace 'year', 'month', and 'day' with actual values
# fetch_and_process_xml(year='2023', month='05', day='12')

# OfficielePublicatie class and other necessary parts of the script should be defined as provided above.


