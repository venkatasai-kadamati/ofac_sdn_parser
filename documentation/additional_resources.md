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
