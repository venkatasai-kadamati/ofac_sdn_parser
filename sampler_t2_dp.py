import csv
from lxml import etree

xml_file_path = "source_documents/sdn_advanced.xml"
csv_file_path = "parsed_output_t2.csv"


def parse_ofac_sdn_xml(xml_file_path, csv_file_path):
    tree = etree.parse(xml_file_path)
    root = tree.getroot()
    ns = {"ns": "http://www.un.org/sanctions/1.0"}

    fieldnames = [
        "Alias",
        "Documented Name",
    ]

    with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for distinct_party in root.findall(".//ns:DistinctParty", ns):
            for alias in distinct_party.findall(".//ns:Alias", ns):
                alias_value = alias.find(".//ns:NamePartValue", ns).text
                name_part_values = alias.findall(".//ns:NamePartValue", ns)

                if len(name_part_values) >= 2:
                    documented_name = name_part_values[1].text
                else:
                    documented_name = ""

                is_latin = all(
                    ord(char) < 128 for char in alias_value + documented_name
                )

                if not is_latin:
                    alias_value = f"Non-Latin: {alias_value}"
                    documented_name = f"Non-Latin: {documented_name}"

                writer.writerow(
                    {"Alias": alias_value, "Documented Name": documented_name}
                )


if __name__ == "__main__":
    parse_ofac_sdn_xml(xml_file_path, csv_file_path)
