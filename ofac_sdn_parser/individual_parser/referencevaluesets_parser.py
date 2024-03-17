import xml.etree.ElementTree as ET

#
tree = ET.parse("sdn_advanced.xml")

root = tree.getroot()

ns = {"ns": "http://www.un.org/sanctions/1.0"}


alias_types = {}
for alias_type in root.find(".//ns:AliasTypeValues", ns).findall(".//ns:AliasType", ns):
    alias_id = alias_type.attrib["ID"]
    alias_name = alias_type.text
    alias_types[alias_id] = alias_name

# Parse AreaCodeValues
area_codes = {}
for area_code in root.find(".//ns:AreaCodeValues", ns).findall(".//ns:AreaCode", ns):
    area_code_id = area_code.attrib["ID"]
    country_id = area_code.attrib["CountryID"]
    description = area_code.attrib["Description"]
    area_code_type_id = area_code.attrib["AreaCodeTypeID"]
    area_codes[area_code_id] = {
        "CountryID": country_id,
        "Description": description,
        "AreaCodeTypeID": area_code_type_id,
    }

# Parse AreaCodeTypeValues
area_code_types = {}
for area_code_type in root.find(".//ns:AreaCodeTypeValues", ns).findall(
    ".//ns:AreaCodeType", ns
):
    area_code_type_id = area_code_type.attrib["ID"]
    area_code_type_name = area_code_type.text
    area_code_types[area_code_type_id] = area_code_type_name

# Parse CalendarTypeValues
calendar_types = {}
for calendar_type in root.find(".//ns:CalendarTypeValues", ns).findall(
    ".//ns:CalendarType", ns
):
    calendar_type_id = calendar_type.attrib["ID"]
    calendar_type_name = calendar_type.text
    calendar_types[calendar_type_id] = calendar_type_name

# Parse CountryValues
countries = {}
for country in root.find(".//ns:CountryValues", ns).findall(".//ns:Country", ns):
    country_id = country.attrib["ID"]
    iso2 = country.attrib["ISO2"]
    country_name = country.text
    countries[country_id] = {"ISO2": iso2, "Name": country_name}

# Parse CountryRelevanceValues
country_relevance = {}
for country_rel in root.find(".//ns:CountryRelevanceValues", ns).findall(
    ".//ns:CountryRelevance", ns
):
    country_rel_id = country_rel.attrib["ID"]
    country_rel_name = country_rel.text
    country_relevance[country_rel_id] = country_rel_name

# Parse DecisionMakingBodyValues
decision_making_bodies = {}
for decision_making_body in root.find(".//ns:DecisionMakingBodyValues", ns).findall(
    ".//ns:DecisionMakingBody", ns
):
    decision_making_body_id = decision_making_body.attrib["ID"]
    organisation_id = decision_making_body.attrib["OrganisationID"]
    decision_making_body_name = decision_making_body.text
    decision_making_bodies[decision_making_body_id] = {
        "OrganisationID": organisation_id,
        "Name": decision_making_body_name,
    }

# Parse DetailReferenceValues
detail_references = {}
for detail_reference in root.find(".//ns:DetailReferenceValues", ns).findall(
    ".//ns:DetailReference", ns
):
    detail_reference_id = detail_reference.attrib["ID"]
    detail_reference_name = detail_reference.text
    detail_references[detail_reference_id] = detail_reference_name

# Parse DetailTypeValues : TODO:
# detail_types = {}
# for detail_type in root.find('.//ns:DetailTypeValues', ns).findall('.//ns:DetailType', ns):
#     detail_type_id = detail_type.attrib['ID']
#     detail_type_name =

# __________________________________________

# Parse DocNameStatusValues
doc_name_status_values = {}
for doc_name_status in root.findall("ns:DocNameStatusValues/ns:DocNameStatus", ns):
    doc_name_status_id = doc_name_status.get("ID")
    doc_name_status_value = doc_name_status.text
    doc_name_status_values[doc_name_status_id] = doc_name_status_value

# Parse EntryEventTypeValues
entry_event_type_values = {}
for entry_event_type in root.findall("ns:EntryEventTypeValues/ns:EntryEventType", ns):
    entry_event_type_id = entry_event_type.get("ID")
    entry_event_type_value = entry_event_type.text
    entry_event_type_values[entry_event_type_id] = entry_event_type_value

# Pending EntryLinkTypeValues TODO:
# Pending ExRefTypeValues TODO:

# Parse FeatureTypeValues
feature_type_values = {}
for feature_type in root.findall("ns:FeatureTypeValues/ns:FeatureType", ns):
    feature_type_id = feature_type.get("ID")
    feature_type_group_id = feature_type.get("FeatureTypeGroupID")
    feature_type_value = feature_type.text
    feature_type_values[feature_type_id] = {
        "FeatureTypeGroupID": feature_type_group_id,
        "Value": feature_type_value,
    }

# Parse FeatureTypeGroupValues
feature_type_group_values = {}
for feature_type_group in root.findall(
    "ns:FeatureTypeGroupValues/ns:FeatureTypeGroup", ns
):
    feature_type_group_id = feature_type_group.get("ID")
    feature_type_group_value = feature_type_group.text
    feature_type_group_values[feature_type_group_id] = feature_type_group_value

# Parse IDRegDocDateTypeValues
id_reg_doc_date_type_values = {}
for id_reg_doc_date_type in root.findall(
    "ns:IDRegDocDateTypeValues/ns:IDRegDocDateType", ns
):
    id_reg_doc_date_type_id = id_reg_doc_date_type.get("ID")
    id_reg_doc_date_type_value = id_reg_doc_date_type.text
    id_reg_doc_date_type_values[id_reg_doc_date_type_id] = id_reg_doc_date_type_value

# Parse IDRegDocTypeValues
id_reg_doc_type_values = {}
for id_reg_doc_type in root.findall("ns:IDRegDocTypeValues/ns:IDRegDocType", ns):
    id_reg_doc_type_id = id_reg_doc_type.get("ID")
    id_reg_doc_type_value = id_reg_doc_type.text
    id_reg_doc_type_values[id_reg_doc_type_id] = id_reg_doc_type_value

# Parse IdentityFeatureLinkTypeValues
identity_feature_link_type_values = {}
for identity_feature_link_type in root.findall(
    "ns:IdentityFeatureLinkTypeValues/ns:IdentityFeatureLinkType", ns
):
    identity_feature_link_type_id = identity_feature_link_type.get("ID")
    identity_feature_link_type_value = identity_feature_link_type.text
    identity_feature_link_type_values[identity_feature_link_type_id] = (
        identity_feature_link_type_value
    )

# Parse LegalBasisValues
legal_basis_values = {}
for legal_basis in root.findall("ns:LegalBasisValues/ns:LegalBasis", ns):
    legal_basis_id = legal_basis.get("ID")
    legal_basis_short_ref = legal_basis.get("LegalBasisShortRef")
    legal_basis_type_id = legal_basis.get("LegalBasisTypeID")
    sanctions_program_id = legal_basis.get("SanctionsProgramID")
    legal_basis_value = legal_basis.text
    legal_basis_values[legal_basis_id] = {
        "LegalBasisShortRef": legal_basis_short_ref,
        "LegalBasisTypeID": legal_basis_type_id,
        "SanctionsProgramID": sanctions_program_id,
        "Value": legal_basis_value,
    }

# Parse LegalBasisTypeValues : TODO:
# legal_basis_type_values = {}
# for legal_basis_type in root.findall('ns:LegalBasisTypeValues/ns:LegalBasisType', ns):
#     legal_basis_type_id =

# pending: ListValues TODO:
# pending: LocPartTypeValues TODO:
# pending: LocPartValueStatusValues TODO:
# pending: NamePartTypeValues TODO:
# pending: OrganizationValues TODO:

# Parse PartySubTypeValues
party_sub_type_values = {}
for party_sub_type in root.findall("ns:PartySubTypeValues/ns:PartySubType", ns):
    party_sub_type_id = party_sub_type.get("ID")
    party_type_id = party_sub_type.get("PartyTypeID")
    party_sub_type_values[party_sub_type_id] = {"PartyTypeID": party_type_id}

# Parse PartyTypeValues
party_type_values = {}
for party_type in root.findall("ns:PartyTypeValues/ns:PartyType", ns):
    party_type_id = party_type.get("ID")
    party_type_value = party_type.text
    party_type_values[party_type_id] = party_type_value

# Parse RelationQualityValues
relation_quality_values = {}
for relation_quality in root.findall("ns:RelationQualityValues/ns:RelationQuality", ns):
    relation_quality_id = relation_quality.get("ID")
    relation_quality_value = relation_quality.text
    relation_quality_values[relation_quality_id] = relation_quality_value

# Parse RelationTypeValues
relation_type_values = {}
for relation_type in root.findall("ns:RelationTypeValues/ns:RelationType", ns):
    relation_type_id = relation_type.get("ID")
    symmetrical = relation_type.get("Symmetrical")
    relation_type_value = relation_type.text
    relation_type_values[relation_type_id] = {
        "Symmetrical": symmetrical,
        "Value": relation_type_value,
    }

# Parse ReliabilityValues
reliability_values = {}
for reliability in root.findall("ns:ReliabilityValues/ns:Reliability", ns):
    reliability_id = reliability.get("ID")
    reliability_value = reliability.text
    reliability_values[reliability_id] = reliability_value

# Parse SanctionsProgramValues
sanctions_program_values = {}
for sanctions_program in root.findall(
    "ns:SanctionsProgramValues/ns:SanctionsProgram", ns
):
    sanctions_program_id = sanctions_program.get("ID")
    subsidiary_body_id = sanctions_program.get("SubsidiaryBodyID")
    sanctions_program_value = sanctions_program.text
    sanctions_program_values[sanctions_program_id] = {
        "SubsidiaryBodyID": subsidiary_body_id,
        "Value": sanctions_program_value,
    }

# Parse SanctionsTypeValues
sanctions_type_values = {}
for sanctions_type in root.findall("ns:SanctionsTypeValues/ns:SanctionsType", ns):
    sanctions_type_id = sanctions_type.get("ID")
    sanctions_type_value = sanctions_type.text
    sanctions_type_values[sanctions_type_id] = sanctions_type_value

# Parse ScriptValues
script_values = {}
for script in root.findall("ns:ScriptValues/ns:Script", ns):
    script_id = script.get("ID")
    script_code = script.get("ScriptCode")
    script_value = script.text
    script_values[script_id] = {"ScriptCode": script_code, "Value": script_value}

# Parse ScriptStatusValues
script_status_values = {}
for script_status in root.findall("ns:ScriptStatusValues/ns:ScriptStatus", ns):
    script_status_id = script_status.get("ID")
    script_status_value = script_status.text
    script_status_values[script_status_id] = script_status_value

# Parse SubsidiaryBodyValues
subsidiary_body_values = {}
for subsidiary_body in root.findall("ns:SubsidiaryBodyValues/ns:SubsidiaryBody", ns):
    subsidiary_body_id = subsidiary_body.get("ID")
    notional = subsidiary_body.get("Notional")
    decision_making_body_id = subsidiary_body.get("DecisionMakingBodyID")
    subsidiary_body_value = subsidiary_body.text
    subsidiary_body_values[subsidiary_body_id] = {
        "Notional": notional,
        "DecisionMakingBodyID": decision_making_body_id,
        "Value": subsidiary_body_value,
    }


# pending: SupInfoTypeValues TODO:

# Parse ValidityValues
validity_values = {}
for validity in root.findall("ns:ValidityValues/ns:Validity", ns):
    validity_id = validity.get("ID")
    validity_value = validity.text
    validity_values[validity_id] = validity_value

print(validity_values)
