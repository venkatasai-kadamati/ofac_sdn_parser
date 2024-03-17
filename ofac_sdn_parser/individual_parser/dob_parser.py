import csv
from lxml import etree

# Parse the XML file
tree = etree.parse("source_documents/sdn_advanced.xml")
root = tree.getroot()

# Define the namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

# Assuming the necessary imports and setup code are at the top of your file

# Find the Parties element
parties = root.find(".//ns:Parties", ns)

# Check if parties is not None
if parties is not None:
    # Create a CSV writer object
    with open(
        "ofac_sdn_parser/generated_csv/dob_parties.csv", "w", newline=""
    ) as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["ID", "Name", "DateOfBirth"])

        # Loop through the child elements of Parties and write the data to the CSV
        for party in parties.findall(".//ns:Party", ns):
            # Get the ID and Name of the party
            party_id = party.attrib["ID"]
            name = party.find(".//ns:Name", ns).text

            # Find the Detail element with DetailTypeID of "1430" (DATE)
            dob_detail = party.find('.//ns:Detail[ns:DetailTypeID="1430"]', ns)

            # If a DOB detail is found, extract the date value
            if dob_detail is not None:
                dob = dob_detail.find(".//ns:Value", ns).text
            else:
                dob = ""

            # Write the data to the CSV
            writer.writerow([party_id, name, dob])
else:
    print("No Parties element found in the XML.")
