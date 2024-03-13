# TODO @pending Handle the nested comment element
# TODO @pending Merge the profileRelationships.csv with the rest into a single csv
# TODO @ongoin research about the namespace and how to handle it

# !  Python script for parsing xml file and writing the data to a CSV file
# ?? Parses ProfileRelationships top level element and its nested fragments to csv
# ** Target top-level element: ProfileRelationships
# ** XML file : sdn_advanced.xml
# ** Using lxml & CSV module

# **--------------------------- SCRIPT START ---------------------------
import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse("source_documents/sdn_advanced.xml")

# Get the root element
root = tree.getroot()

# namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

profile_relationships = root.find(".//ns:ProfileRelationships", ns)

# Write csv header
with open(
    "ofac_sdn_parser/generated_csv/profile_relationships.csv", "w", newline=""
) as csvfile:
    fieldnames = [
        "ID",
        "From-ProfileID",
        "To-ProfileID",
        "RelationTypeID",
        "RelationQualityID",
        "Former",
        "SanctionsEntryID",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# write csv data
for profile_relationship in profile_relationships.findall(
    ".//ns:ProfileRelationship", ns
):
    data = {
        "ID": profile_relationship.attrib["ID"],
        "From-ProfileID": profile_relationship.attrib["From-ProfileID"],
        "To-ProfileID": profile_relationship.attrib["To-ProfileID"],
        "RelationTypeID": profile_relationship.attrib["RelationTypeID"],
        "RelationQualityID": profile_relationship.attrib["RelationQualityID"],
        "Former": profile_relationship.attrib["Former"],
        "SanctionsEntryID": profile_relationship.attrib["SanctionsEntryID"],
    }
    with open(
        "ofac_sdn_parser/generated_csv/profile_relationships.csv", "a", newline=""
    ) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
