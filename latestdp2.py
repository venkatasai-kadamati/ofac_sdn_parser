import csv
from lxml import etree


xml_file_path = "source_documents/sdn_advanced.xml"
csv_file_path = "output2.csv"


def parse_ofac_sdn_xml(xml_file_path, csv_file_path):
    tree = etree.parse(xml_file_path)
    root = tree.getroot()
    ns = {"ns": "http://www.un.org/sanctions/1.0"}

    fieldnames = [
        "FixedRef",
        "ProfileID",
        "PartySubTypeID",
        "IdentityID",
        "FixedRef",
        "Primary",
        "AliasFixedRef",
        "AliasTypeID",
        "Primary",
        "LowQuality",
        "DocumentedNameID",
        "FixedRef",
        "DocNameStatusID",
        "NamePartValue",
        "NamePartGroupID",
        "ScriptID",
        "ScriptStatusID",
        "Acronym",
        "FeatureID",
        "FeatureTypeID",
        "FeatureVersionID",
        "ReliabilityID",
        "Comment",
        "DateOfBirth",
    ]

    with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for distinct_party in root.findall(".//ns:DistinctParty", ns):
            data = {
                "FixedRef": distinct_party.attrib["FixedRef"],
                "ProfileID": "",
                "PartySubTypeID": "",
                "IdentityID": "",
                "FixedRef": "",
                "Primary": "",
                "AliasFixedRef": "",
                "AliasTypeID": "",
                "Primary": "",
                "LowQuality": "",
                "DocumentedNameID": "",
                "FixedRef": "",
                "DocNameStatusID": "",
                "NamePartValue": "",
                "NamePartGroupID": "",
                "ScriptID": "",
                "ScriptStatusID": "",
                "Acronym": "",
                "FeatureID": "",
                "FeatureTypeID": "",
                "FeatureVersionID": "",
                "ReliabilityID": "",
                "Comment": "",
                "DateOfBirth": "",
            }

            profile = distinct_party.find(".//ns:Profile", ns)
            if profile is not None:
                data["ProfileID"] = profile.attrib["ID"]
                data["PartySubTypeID"] = profile.attrib["PartySubTypeID"]

                identity = profile.find(".//ns:Identity", ns)
                if identity is not None:
                    data["IdentityID"] = identity.attrib["ID"]
                    data["FixedRef"] = identity.attrib["FixedRef"]
                    data["Primary"] = identity.attrib["Primary"]

                    aliases = identity.findall(".//ns:Alias", ns)
                    for alias in aliases:
                        data["AliasFixedRef"] = alias.attrib["FixedRef"]
                        data["AliasTypeID"] = alias.attrib["AliasTypeID"]
                        data["Primary"] = alias.attrib["Primary"]
                        data["LowQuality"] = alias.attrib["LowQuality"]

                        documented_name = alias.find(".//ns:DocumentedName", ns)
                        if documented_name is not None:
                            data["DocumentedNameID"] = documented_name.attrib["ID"]
                            data["FixedRef"] = documented_name.attrib["FixedRef"]
                            data["DocNameStatusID"] = documented_name.attrib[
                                "DocNameStatusID"
                            ]

                            documented_name_part = documented_name.find(
                                ".//ns:DocumentedNamePart", ns
                            )
                            if documented_name_part is not None:
                                name_part_value = documented_name_part.find(
                                    ".//ns:NamePartValue", ns
                                )
                                if name_part_value is not None:
                                    data["NamePartValue"] = name_part_value.text
                                    data["NamePartGroupID"] = name_part_value.attrib[
                                        "NamePartGroupID"
                                    ]
                                    data["ScriptID"] = name_part_value.attrib[
                                        "ScriptID"
                                    ]
                                    data["ScriptStatusID"] = name_part_value.attrib[
                                        "ScriptStatusID"
                                    ]
                                    data["Acronym"] = name_part_value.attrib["Acronym"]

                features = profile.findall(".//ns:Feature", ns)
                for feature in features:
                    if (
                        feature.attrib["FeatureTypeID"] == "8"
                    ):  # Assuming "8" is the FeatureTypeID for Date of Birth
                        feature_version = feature.find(".//ns:FeatureVersion", ns)
                        if feature_version is not None:
                            date_period = feature_version.find(".//ns:DatePeriod", ns)
                            if date_period is not None:
                                start_date = date_period.find(".//ns:Start/ns:From", ns)
                                if start_date is not None:
                                    data["DateOfBirth"] = (
                                        f"{start_date.find('ns:Year', ns).text}-{start_date.find('ns:Month', ns).text}-{start_date.find('ns:Day', ns).text}"
                                    )

                writer.writerow(data)


if __name__ == "__main__":
    parse_ofac_sdn_xml(xml_file_path, csv_file_path)
