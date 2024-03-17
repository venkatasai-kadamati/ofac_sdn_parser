import csv
from lxml import etree

# parse the XML file
tree = etree.parse("sdn_advanced.xml")
root = tree.getroot()

# define the namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

# create a CSV file and write the header row
with open("reference_values.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Element", "ID", "Name"])

    # loop through the child elements of ReferenceValueSets and extract data
    for elem in root.find(".//ns:ReferenceValueSets", ns):
        if elem.tag == ns["AliasTypeValues"]:
            for alias_type in elem.findall(".//ns:AliasType", ns):
                writer.writerow(["AliasType", alias_type.attrib["ID"], alias_type.text])
        elif elem.tag == ns["AreaCodeValues"]:
            for area_code in elem.findall(".//ns:AreaCode", ns):
                writer.writerow(
                    [
                        "AreaCode",
                        area_code.attrib["ID"],
                        area_code.attrib["Description"],
                    ]
                )
        elif elem.tag == ns["CountryValues"]:
            for country in elem.findall(".//ns:Country", ns):
                writer.writerow(["Country", country.attrib["ID"], country.text])
        elif elem.tag == ns["DecisionMakingBodyValues"]:
            for decision_making_body in elem.findall(".//ns:DecisionMakingBody", ns):
                writer.writerow(
                    [
                        "DecisionMakingBody",
                        decision_making_body.attrib["ID"],
                        decision_making_body.text,
                    ]
                )
        elif elem.tag == ns["DetailReferenceValues"]:
            for detail_reference in elem.findall(".//ns:DetailReference", ns):
                writer.writerow(
                    [
                        "DetailReference",
                        detail_reference.attrib["ID"],
                        detail_reference.text,
                    ]
                )
        elif elem.tag == ns["DocNameStatusValues"]:
            for doc_name_status in elem.findall(".//ns:DocNameStatus", ns):
                writer.writerow(
                    [
                        "DocNameStatus",
                        doc_name_status.attrib["ID"],
                        doc_name_status.text,
                    ]
                )
        elif elem.tag == ns["EntryEventTypeValues"]:
            for entry_event_type in elem.findall(".//ns:EntryEventType", ns):
                writer.writerow(
                    [
                        "EntryEventType",
                        entry_event_type.attrib["ID"],
                        entry_event_type.text,
                    ]
                )
        elif elem.tag == ns["FeatureTypeValues"]:
            for feature_type in elem.findall(".//ns:FeatureType", ns):
                writer.writerow(
                    ["FeatureType", feature_type.attrib["ID"], feature_type.text]
                )
        elif elem.tag == ns["LegalBasisValues"]:
            for legal_basis in elem.findall(".//ns:LegalBasis", ns):
                writer.writerow(
                    ["LegalBasis", legal_basis.attrib["ID"], legal_basis.text]
                )
        elif elem.tag == ns["ListValues"]:
            for list_value in elem.findall(".//ns:List", ns):
                writer.writerow(["List", list_value.attrib["ID"], list_value.text])
        elif elem.tag == ns["PartyTypeValues"]:
            for party_type in elem.findall(".//ns:PartyType", ns):
                writer.writerow(["PartyType", party_type.attrib["ID"], party_type.text])
        elif elem.tag == ns["RelationTypeValues"]:
            for relation_type in elem.findall(".//ns:RelationType", ns):
                writer.writerow(
                    ["RelationType", relation_type.attrib["ID"], relation_type.text]
                )
        elif elem.tag == ns["SanctionsProgramValues"]:
            for sanctions_program in elem.findall(".//ns:SanctionsProgram", ns):
                writer.writerow(
                    [
                        "SanctionsProgram",
                        sanctions_program.attrib["ID"],
                        sanctions_program.text,
                    ]
                )
        elif elem.tag == ns["SanctionsTypeValues"]:
            for sanctions_type in elem.findall(".//ns:SanctionsType", ns):
                writer.writerow(
                    ["SanctionsType", sanctions_type.attrib["ID"], sanctions_type.text]
                )
