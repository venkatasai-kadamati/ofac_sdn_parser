import csv
from lxml import etree

tree = etree.parse("source_documents/sdn_advanced.xml")
root = tree.getroot()

# namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

ref_values = root.find(".//ns:ReferenceValueSets", ns)

with open(
    "ofac_sdn_parser/generated_csv/reference_values.csv", "w", newline=""
) as csvfile:
    writer = csv.writer(csvfile)

    # header row
    writer.writerow(
        [
            "Element",
            "ID",
            "CountryID",
            "Description",
            "AreaCodeTypeID",
            "OrganisationID",
            "LegalBasisShortRef",
            "LegalBasisTypeID",
            "SanctionsProgramID",
            "PartyTypeID",
            "ScriptCode",
            "Symmetrical",
        ]
    )

    for child in ref_values:
        if child.tag == "{http://www.un.org/sanctions/1.0}AliasTypeValues":
            for alias_type in child.findall(".//ns:AliasType", ns):
                writer.writerow(
                    [
                        "AliasType",
                        alias_type.attrib["ID"],
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]
                )
        elif child.tag == "{http://www.un.org/sanctions/1.0}AreaCodeValues":
            for area_code in child.findall(".//ns:AreaCode", ns):
                writer.writerow(
                    [
                        "AreaCode",
                        area_code.attrib["ID"],
                        area_code.attrib["CountryID"],
                        area_code.attrib["Description"],
                        area_code.attrib["AreaCodeTypeID"],
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]
                )
        elif child.tag == "{http://www.un.org/sanctions/1.0}CountryValues":
            for country in child.findall(".//ns:Country", ns):
                writer.writerow(
                    [
                        "Country",
                        country.attrib["ID"],
                        "",
                        country.text,
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]
                )
        elif child.tag == "{http://www.un.org/sanctions/1.0}DecisionMakingBodyValues":
            for decision_making_body in child.findall(".//ns:DecisionMakingBody", ns):
                writer.writerow(
                    [
                        "DecisionMakingBody",
                        decision_making_body.attrib["ID"],
                        "",
                        "",
                        "",
                        decision_making_body.attrib["OrganisationID"],
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]
                )
        elif child.tag == "{http://www.un.org/sanctions/1.0}LegalBasisValues":
            for legal_basis in child.findall(".//ns:LegalBasis", ns):
                writer.writerow(
                    [
                        "LegalBasis",
                        legal_basis.attrib["ID"],
                        "",
                        "",
                        "",
                        "",
                        legal_basis.attrib["LegalBasisShortRef"],
                        legal_basis.attrib["LegalBasisTypeID"],
                        legal_basis.attrib["SanctionsProgramID"],
                        "",
                        "",
                        "",
                    ]
                )
        elif child.tag == "{http://www.un.org/sanctions/1.0}PartySubTypeValues":
            for party_sub_type in child.findall(".//ns:PartySubType", ns):
                writer.writerow(
                    [
                        "PartySubType",
                        party_sub_type.attrib["ID"],
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        party_sub_type.attrib["PartyTypeID"],
                        "",
                        "",
                        "",
                    ]
                )
        elif child.tag == "{http://www.un.org/sanctions/1.0}ScriptValues":
            for script in child.findall(".//ns:Script", ns):
                writer.writerow(
                    [
                        "Script",
                        script.attrib["ID"],
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        script.attrib["ScriptCode"],
                        "",
                        "",
                    ]
                )
        elif child.tag == "{http://www.un.org/sanctions/1.0}RelationTypeValues":
            for relation_type in child.findall(".//ns:RelationType", ns):
                writer.writerow(
                    [
                        "RelationType",
                        relation_type.attrib["ID"],
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        relation_type.attrib["Symmetrical"],
                        "",
                    ]
                )
