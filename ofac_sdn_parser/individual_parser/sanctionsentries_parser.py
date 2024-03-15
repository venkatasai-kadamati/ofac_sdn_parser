import csv
from lxml import etree

# Parse the XML file
tree = etree.parse("source_documents/sdn_advanced.xml")

# Get the root element
root = tree.getroot()

# Define the namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

# Find the SanctionsEntries element
sanctions_entries = root.find(".//ns:SanctionsEntries", ns)

# Write the CSV file header
with open(
    "ofac_sdn_parser/generated_csv/sanctions_entries.csv", "w", newline=""
) as csvfile:
    fieldnames = [
        "ID",
        "ProfileID",
        "ListID",
        "EntryEventTypeID",
        "LegalBasisID",
        "Comment",
        "Year",
        "Month",
        "Day",
        "SanctionsMeasureID",
        "SanctionsTypeID",
        "SanctionsMeasureComment",
        "YearFixed",
        "MonthFixed",
        "DayFixed",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Write the CSV file data
for sanctions_entry in sanctions_entries.findall(".//ns:SanctionsEntry", ns):
    data = {
        "ID": sanctions_entry.attrib["ID"],
        "ProfileID": sanctions_entry.attrib["ProfileID"],
        "ListID": sanctions_entry.attrib["ListID"],
        "EntryEventTypeID": "",
        "LegalBasisID": "",
        "Comment": "",
        "Year": "",
        "Month": "",
        "Day": "",
        "SanctionsMeasureID": "",
        "SanctionsTypeID": "",
        "SanctionsMeasureComment": "",
        "YearFixed": "",
        "MonthFixed": "",
        "DayFixed": "",
    }

    # Get the EntryEvent element
    entry_event = sanctions_entry.find(".//ns:EntryEvent", ns)
    if entry_event is not None:
        data["EntryEventTypeID"] = entry_event.attrib["EntryEventTypeID"]
        data["LegalBasisID"] = entry_event.attrib["LegalBasisID"]
        data["Comment"] = (
            entry_event.find(".//ns:Comment", ns).text
            if entry_event.find(".//ns:Comment", ns) is not None
            else ""
        )
        date = entry_event.find(".//ns:Date", ns)
        if date is not None:
            data["Year"] = date.find(".//ns:Year", ns).text
            data["Month"] = date.find(".//ns:Month", ns).text
            data["Day"] = date.find(".//ns:Day", ns).text

    # Get the SanctionsMeasure elements
    sanctions_measures = sanctions_entry.findall(".//ns:SanctionsMeasure", ns)
    for sanctions_measure in sanctions_measures:
        data["SanctionsMeasureID"] = sanctions_measure.attrib["ID"]
        data["SanctionsTypeID"] = sanctions_measure.attrib["SanctionsTypeID"]
        data["SanctionsMeasureComment"] = (
            sanctions_measure.find(".//ns:Comment", ns).text
            if sanctions_measure.find(".//ns:Comment", ns) is not None
            else ""
        )
        date_period = sanctions_measure.find(".//ns:DatePeriod", ns)
        if date_period is not None:
            data["YearFixed"] = date_period.attrib["YearFixed"]
            data["MonthFixed"] = date_period.attrib["MonthFixed"]
            data["DayFixed"] = date_period.attrib["DayFixed"]

        with open(
            "ofac_sdn_parser/generated_csv/sanctions_entries.csv", "a", newline=""
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)
