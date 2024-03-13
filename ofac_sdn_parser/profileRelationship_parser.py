import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('source_documents/sdn_advanced.xml')

# Get the root element
root = tree.getroot()

# Define the namespace
ns = {'ns': 'http://www.un.org/sanctions/1.0'}

# Find the ProfileRelationships element
profile_relationships = root.find('.//ns:ProfileRelationships', ns)

# Write the CSV file header
with open('profile_relationships.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID', 'From-ProfileID', 'To-ProfileID', 'RelationTypeID', 'RelationQualityID', 'Former', 'SanctionsEntryID']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Write the CSV file data
for profile_relationship in profile_relationships.findall('.//ns:ProfileRelationship', ns):
    data = {
        'ID': profile_relationship.attrib['ID'],
        'From-ProfileID': profile_relationship.attrib['From-ProfileID'],
        'To-ProfileID': profile_relationship.attrib['To-ProfileID'],
        'RelationTypeID': profile_relationship.attrib['RelationTypeID'],
        'RelationQualityID': profile_relationship.attrib['RelationQualityID'],
        'Former': profile_relationship.attrib['Former'],
        'SanctionsEntryID': profile_relationship.attrib['SanctionsEntryID']
    }
    with open('profile_relationships.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
