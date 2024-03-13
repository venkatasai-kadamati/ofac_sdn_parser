# TODO @pending Handle the nested comment element 
# TODO @pending Merge the profileRelationships.csv with the rest into a single csv 
# TODO @ongoin research about the namespace and how to handle it

# !  Python script for parsing xml file and writing the data to a CSV file
# ?? Parses ProfileRelationships top level element and its nested fragments to csv
# ** Target top-level element: Locations
# ** XML file : sdn_advanced.xml
# ** Using lxml & CSV module

# **--------------------------- SCRIPT START ---------------------------

import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('source_documents/sdn_advanced.xml')

# Get the root element
root = tree.getroot()

# Define the namespace
ns = {'ns': 'http://www.un.org/sanctions/1.0'}

# Find the Locations element
locations = root.find('.//ns:Locations', ns)

# Write the CSV file header
with open('ofac_sdn_parser/generated_csv/locations.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID', 'AreaCodeID', 'CountryID', 'CountryRelevanceID', 'Address', 'City', 'State', 'FeatureVersionID']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Write the CSV file data
for location in locations.findall('.//ns:Location', ns):
    data = {
        'ID': location.attrib['ID'],
        'AreaCodeID': '',
        'CountryID': '',
        'CountryRelevanceID': '',
        'Address': '',
        'City': '',
        'State': '',
        'FeatureVersionID': ''
    }

    # Get the LocationAreaCode element
    location_area_code = location.find('.//ns:LocationAreaCode', ns)
    if location_area_code is not None:
        data['AreaCodeID'] = location_area_code.attrib['AreaCodeID']

    # Get the LocationCountry element
    location_country = location.find('.//ns:LocationCountry', ns)
    if location_country is not None:
        data['CountryID'] = location_country.attrib['CountryID']
        data['CountryRelevanceID'] = location_country.attrib['CountryRelevanceID']

    # Get the LocationPart elements
    location_parts = location.findall('.//ns:LocationPart', ns)
    for location_part in location_parts:
        loc_part_type_id = location_part.attrib['LocPartTypeID']
        if loc_part_type_id == '1451':  # Address
            loc_part_value = location_part.find('.//ns:LocationPartValue', ns)
            if loc_part_value is not None:
                data['Address'] = loc_part_value.find('.//ns:Value', ns).text
        elif loc_part_type_id == '1454':  # City
            loc_part_value = location_part.find('.//ns:LocationPartValue', ns)
            if loc_part_value is not None:
                data['City'] = loc_part_value.find('.//ns:Value', ns).text
        elif loc_part_type_id == '1456':  # State
            loc_part_value = location_part.find('.//ns:LocationPartValue', ns)
            if loc_part_value is not None:
                data['State'] = loc_part_value.find('.//ns:Value', ns).text

    # Get the FeatureVersionReference element
    feature_version_reference = location.find('.//ns:FeatureVersionReference', ns)
    if feature_version_reference is not None:
        data['FeatureVersionID'] = feature_version_reference.attrib['FeatureVersionID']

    with open('ofac_sdn_parser/generated_csv/locations.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
