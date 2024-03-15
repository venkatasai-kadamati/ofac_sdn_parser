import csv
from lxml import etree

tree = etree.parse("source_documents/sdn_advanced.xml")

root = tree.getroot()

ns = {"ns": "http://www.un.org/sanctions/1.0"}

with open(
    "ofac_sdn_parser/generated_csv/idregdocuments.csv",
    "w",
    newline="",
    encoding="utf-8-sig",
) as csvfile:
    fieldnames = [
        "ID",
        "IDRegDocTypeID",
        "IdentityID",
        "IssuedBy_CountryID",
        "ValidityID",
        "IDRegistrationNo",
        "IssuingAuthority",
        "DocumentedNameID",
        "DocumentDate_IDRegDocDateTypeID",
        "DocumentDate_Start_From_Year",
        "DocumentDate_Start_From_Month",
        "DocumentDate_Start_From_Day",
        "DocumentDate_Start_To_Year",
        "DocumentDate_Start_To_Month",
        "DocumentDate_Start_To_Day",
        "DocumentDate_End_From_Year",
        "DocumentDate_End_From_Month",
        "DocumentDate_End_From_Day",
        "DocumentDate_End_To_Year",
        "DocumentDate_End_To_Month",
        "DocumentDate_End_To_Day",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

for idregdocuments in root.findall(".//ns:IDRegDocuments", ns):
    for idregdocument in idregdocuments.findall(".//ns:IDRegDocument", ns):
        data = {
            "ID": idregdocument.attrib["ID"],
            "IDRegDocTypeID": idregdocument.attrib["IDRegDocTypeID"],
            "IdentityID": idregdocument.attrib["IdentityID"],
            "IssuedBy_CountryID": idregdocument.get("IssuedBy-CountryID"),
            "ValidityID": idregdocument.attrib["ValidityID"],
            "IDRegistrationNo": idregdocument.find(".//ns:IDRegistrationNo", ns).text,
            "IssuingAuthority": idregdocument.find(".//ns:IssuingAuthority", ns).text,
            "DocumentedNameID": idregdocument.find(
                ".//ns:DocumentedNameReference", ns
            ).attrib["DocumentedNameID"],
            "DocumentDate_IDRegDocDateTypeID": "",
            "DocumentDate_Start_From_Year": "",
            "DocumentDate_Start_From_Month": "",
            "DocumentDate_Start_From_Day": "",
            "DocumentDate_Start_To_Year": "",
            "DocumentDate_Start_To_Month": "",
            "DocumentDate_Start_To_Day": "",
            "DocumentDate_End_From_Year": "",
            "DocumentDate_End_From_Month": "",
            "DocumentDate_End_From_Day": "",
            "DocumentDate_End_To_Year": "",
            "DocumentDate_End_To_Month": "",
            "DocumentDate_End_To_Day": "",
        }

        documentdate = idregdocument.find(".//ns:DocumentDate", ns)
        if documentdate is not None:
            data["DocumentDate_IDRegDocDateTypeID"] = documentdate.attrib[
                "IDRegDocDateTypeID"
            ]

            dateperiod = documentdate.find(".//ns:DatePeriod", ns)
            if dateperiod is not None:
                start = dateperiod.find(".//ns:Start", ns)
                if start is not None:
                    data["DocumentDate_Start_From_Year"] = start.find(
                        ".//ns:From/ns:Year", ns
                    ).text
                    data["DocumentDate_Start_From_Month"] = start.find(
                        ".//ns:From/ns:Month", ns
                    ).text
                    data["DocumentDate_Start_From_Day"] = start.find(
                        ".//ns:From/ns:Day", ns
                    ).text
                    data["DocumentDate_Start_To_Year"] = start.find(
                        ".//ns:To/ns:Year", ns
                    ).text
                    data["DocumentDate_Start_To_Month"] = start.find(
                        ".//ns:To/ns:Month", ns
                    ).text
                    data["DocumentDate_Start_To_Day"] = start.find(
                        ".//ns:To/ns:Day", ns
                    ).text

                end = dateperiod.find(".//ns:End", ns)
                if end is not None:
                    data["DocumentDate_End_From_Year"] = end.find(
                        ".//ns:From/ns:Year", ns
                    ).text
                    data["DocumentDate_End_From_Month"] = end.find(
                        ".//ns:From/ns:Month", ns
                    ).text
                    data["DocumentDate_End_From_Day"] = end.find(
                        ".//ns:From/ns:Day", ns
                    ).text
                    data["DocumentDate_End_To_Year"] = end.find(
                        ".//ns:To/ns:Year", ns
                    ).text
                    data["DocumentDate_End_To_Month"] = end.find(
                        ".//ns:To/ns:Month", ns
                    ).text
                    data["DocumentDate_End_To_Day"] = end.find(
                        ".//ns:To/ns:Day", ns
                    ).text

        with open(
            "ofac_sdn_parser/generated_csv/idregdocuments.csv",
            "a",
            newline="",
            encoding="utf-8-sig",
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)
