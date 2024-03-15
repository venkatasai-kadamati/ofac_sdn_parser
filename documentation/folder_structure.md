> source_documents

- consists sdn_advanced.xml, sdn.xml and additional generated minified xml files
- Generated minified xml are standalone top level elements with

> ofac_sdn_parser

- consists of script and generated csv
- individual_parser consists of all the python scripts, separate script for each top level element
- generated_csv consists of all the output parsed csv's, separate for each top level element

> documentation

- consists of progress tracking and action items.
- details edge cases, additional resources and folder structure

### Folder Structure (Tree)

```(sql)
rootdir
├───documentation
├───ofac_sdn_parser
│   ├───generated_csv
│   └───individual_parser
├───source_documents
│   └───topLevelElement_minified
└───utility
```
