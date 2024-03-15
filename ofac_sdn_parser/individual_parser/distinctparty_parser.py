import csv
from lxml import etree

# Parse the XML file
tree = etree.parse("source_documents/sdn_advanced.xml")

# Get the root element
root = tree.getroot()

# Define the namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

# Write the CSV file header
with open(
    "ofac_sdn_parser/generated_csv/distinct_party.csv",
    "w",
    newline="",
    encoding="utf-8-sig",
) as csvfile:
    fieldnames = [
        "FixedRef",
        "ProfileID",
        "PartySubTypeID",
        "IdentityID",
        "FixedRef",
        "Primary",
        "False",
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
        "VersionLocationID",
        "NamePartTypeID",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Write the CSV file data
for distinct_party in root.findall(".//ns:DistinctParty", ns):
    data = {
        "FixedRef": distinct_party.attrib["FixedRef"],
        "ProfileID": "",
        "PartySubTypeID": "",
        "IdentityID": "",
        "FixedRef": "",
        "Primary": "",
        "False": "",
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
        "VersionLocationID": "",
        "NamePartTypeID": "",
    }

    # Get the Profile element
    profile = distinct_party.find(".//ns:Profile", ns)
    if profile is not None:
        data["ProfileID"] = profile.attrib["ID"]
        data["PartySubTypeID"] = profile.attrib["PartySubTypeID"]

        # Get the Identity element
        identity = profile.find(".//ns:Identity", ns)
        if identity is not None:
            data["IdentityID"] = identity.attrib["ID"]
            data["FixedRef"] = identity.attrib["FixedRef"]
            data["Primary"] = identity.attrib["Primary"]
            data["False"] = identity.attrib["False"]

            # Get the Alias elements
            aliases = identity.findall(".//ns:Alias", ns)
            for alias in aliases:
                data["AliasFixedRef"] = alias.attrib["FixedRef"]
                data["AliasTypeID"] = alias.attrib["AliasTypeID"]
                data["Primary"] = alias.attrib["Primary"]
                data["LowQuality"] = alias.attrib["LowQuality"]

                # Get the DocumentedName element
                documented_name = alias.find(".//ns:DocumentedName", ns)
                if documented_name is not None:
                    data["DocumentedNameID"] = documented_name.attrib["ID"]
                    data["FixedRef"] = documented_name.attrib["FixedRef"]
                    data["DocNameStatusID"] = documented_name.attrib["DocNameStatusID"]

                    # Get the DocumentedNamePart element
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
                            data["ScriptID"] = name_part_value.attrib["ScriptID"]
                            data["ScriptStatusID"] = name_part_value.attrib[
                                "ScriptStatusID"
                            ]
                            data["Acronym"] = name_part_value.attrib["Acronym"]

            # Get the NamePartGroups element
            name_part_groups = identity.find(".//ns:NamePartGroups", ns)
            if name_part_groups is not None:
                master_name_part_groups = name_part_groups.findall(
                    ".//ns:MasterNamePartGroup", ns
                )
                for master_name_part_group in master_name_part_groups:
                    name_part_group = master_name_part_group.find(
                        ".//ns:NamePartGroup", ns
                    )
                    if name_part_group is not None:
                        data["NamePartGroupID"] = name_part_group.attrib["ID"]
                        data["NamePartTypeID"] = name_part_group.attrib[
                            "NamePartTypeID"
                        ]

            # Get the Feature element
            feature = profile.find(".//ns:Feature", ns)
            if feature is not None:
                data["FeatureID"] = feature.attrib["ID"]
                data["FeatureTypeID"] = feature.attrib["FeatureTypeID"]

                # Get the FeatureVersion element
                feature_version = feature.find(".//ns:FeatureVersion", ns)
                if feature_version is not None:
                    data["FeatureVersionID"] = feature_version.attrib["ID"]
                    data["ReliabilityID"] = feature_version.attrib["ReliabilityID"]
                    data["Comment"] = (
                        feature_version.find(".//ns:Comment", ns).text
                        if feature_version.find(".//ns:Comment", ns) is not None
                        else ""
                    )
                    version_location = feature_version.find(".//ns:VersionLocation", ns)
                    if version_location is not None:
                        data["VersionLocationID"] = version_location.attrib[
                            "LocationID"
                        ]

    with open(
        "ofac_sdn_parser/generated_csv/distinct_party.csv",
        "a",
        newline="",
        encoding="utf-8-sig",
    ) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
