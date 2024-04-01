import csv
from lxml import etree

xml_file_path = "source_documents/sdn_advanced.xml"
csv_file_path = "parsed_output_t2.csv"

script_values_xml = """
<ScriptValues>
      <Script ID="160" ScriptCode="Arab">Arabic</Script>
      <Script ID="230" ScriptCode="Armn">Armenian</Script>
      <Script ID="501" ScriptCode="Hans">Chinese Simplified</Script>
      <Script ID="502" ScriptCode="Hant">Chinese Traditional</Script>
      <Script ID="220" ScriptCode="Cyrl">Cyrillic</Script>
      <Script ID="240" ScriptCode="Geor">Georgian</Script>
      <Script ID="200" ScriptCode="Grek">Greek</Script>
      <Script ID="125" ScriptCode="Hebrew">Hebrew</Script>
      <Script ID="413" ScriptCode="Japanese">Japanese</Script>
      <Script ID="215" ScriptCode="Latin">Latin</Script>
      <Script ID="287" ScriptCode="Korean">Korean</Script>
</ScriptValues>
"""


def parse_ofac_sdn_xml(xml_file_path, csv_file_path):
    tree = etree.parse(xml_file_path)
    root = tree.getroot()
    ns = {"ns": "http://www.un.org/sanctions/1.0"}

    # Create a dictionary for script IDs and their corresponding script codes
    script_root = etree.fromstring(script_values_xml)
    script_dict = {
        script.get("ID"): script.get("ScriptCode")
        for script in script_root.findall("Script")
    }

    fieldnames = [
        "Alias",
        "Documented Name",
        "Script Code",
        "Script ID",
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

                # Get the script ID and script code
                script_id = name_part_values[0].get("ScriptID")
                script_code = script_dict.get(script_id, "Unknown")

                is_latin = all(
                    ord(char) < 128 for char in alias_value + documented_name
                )

                if not is_latin:
                    alias_value = f"Non-Latin: {alias_value}"
                    documented_name = f"Non-Latin: {documented_name}"

                writer.writerow(
                    {
                        "Alias": alias_value,
                        "Documented Name": documented_name,
                        "Script Code": script_code,
                        "Script ID": script_id,
                    }
                )


if __name__ == "__main__":
    parse_ofac_sdn_xml(xml_file_path, csv_file_path)
