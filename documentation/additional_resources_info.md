### Resources

> This section consists of all supporting references and material useful for better contextual understanding

1. XSD extract - https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xml
2. Technical XSD schema definition - https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xsd
3. Explanatory XSD schema definition - https://ofac.treasury.gov/media/10391/download?inline

4. Why LXML over other

   - Memory Efficiency: lxml has features like iterparse, which allows processing of XML documents in an iterative manner. This prevents loading the entire XML file into memory at once, making it ideal for large files. Superior to ElementTree.

5. Namespaces

   - You can't just choose any namespace you like when parsing an existing XML file. Your code must use the namespace that the XML document was designed with.
   - Namespaces look like URLs but don't necessarily point to an actual webpage. They serve as unique identifiers.

6. Approachs

   - (✔) Direct parsing into CSV # working and using this method
     - We have identified that this is better based on the business use case and requirement.
   - (❌) Intermediate parsing into JSON then CSV
     - Chose this when the document is having highly nested and uncertain structure with cross references, JSON has an inbuilt approach to define the relations between various nested data and do better transformations.

7. Parsing Methodology

   - code for parsing <ReferenceValueSets> top level element is different from the code for parsing the <SanctionsEntries> top level element.

   - The reason for this is that the structure of the XML data under these two top level elements is different, and therefore requires different parsing strategies.

   - For example, under the <ReferenceValueSets> top level element, there are multiple child elements, each representing a different type of reference data (e.g., <AliasTypeValues>, <AreaCodeValues>, <CountryValues>, etc.). Each of these child elements has a consistent structure, with a set of child elements representing individual records. In this case, we can iterate over each child element and extract the data for each record using a consistent approach.

   - In contrast, under the <SanctionsEntries> top level element, there is a single child element <SanctionsEntry> that contains multiple child elements representing different types of data (e.g., <EntryEvent>, <SanctionsMeasure>, etc.). Each of these child elements has a different structure and requires a different approach to extract the data.

   - Therefore, the code for parsing the <SanctionsEntries> top level element is more complex, as it needs to handle the different child elements and their respective structures. The code uses a combination of find() and findall() methods to locate the relevant child elements, and then extracts the data using a combination of attribute values and text content.

8. date of birth

   - if present, is likely to be embedded within textual content in a few possible places:
     DocumentedNamePart: Inside <Alias> or potentially other identity sections.
     Feature: Occasionally within a <Feature> element, but the feature type would not be specifically dedicated to DoB.

9. Latin vs non latin words

- A Latin word is a word that is written using the Latin alphabet. The Latin alphabet is the most widely used alphabet in the world, and it is used to write many different languages, including English, French, Spanish, German, and Italian.

- A non-Latin word is a word that is not written using the Latin alphabet. There are many different non-Latin alphabets in the world, including the Arabic alphabet, the Chinese alphabet, and the Cyrillic alphabet.

- Here are some examples of Latin and non-Latin words:

  Latin words:
  English: hello\* French: bonjour
  Spanish: hola
  German: hallo
  Italian: ciao

  Non-Latin words:
  Arabic: مرحبا (marhaba)
  Chinese: 你好 (nǐ hǎo)
  Cyrillic: привет (privet)

  \*\* Solution: Byte Order Mark (BOM) - multi encoding
