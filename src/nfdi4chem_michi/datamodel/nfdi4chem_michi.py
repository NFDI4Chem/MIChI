# Auto generated from nfdi4chem_michi.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-05-28T11:49:37
# Schema: MIChI
#
# id: https://w3id.org/StroemPhi/NFDI4Chem_MIChI
# description: This is the metadata schema for NFDI4Chem
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MICHI = CurieNamespace('michi', 'https://w3id.org/NFDI4Chem/MIChI')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MICHI


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class DatasetId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MICHI.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(NamedThing):
    """
    Represents a Dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["Dataset"]
    class_class_curie: ClassVar[str] = "michi:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = MICHI.Dataset

    id: Union[str, DatasetId] = None
    primary_email: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        super().__post_init__(**kwargs)


@dataclass
class DatasetCollection(YAMLRoot):
    """
    A holder for Dataset objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["DatasetCollection"]
    class_class_curie: ClassVar[str] = "michi:DatasetCollection"
    class_name: ClassVar[str] = "DatasetCollection"
    class_model_uri: ClassVar[URIRef] = MICHI.DatasetCollection

    entries: Optional[Union[Dict[Union[str, DatasetId], Union[dict, Dataset]], List[Union[dict, Dataset]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Dataset, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


class Sample(YAMLRoot):
    """
    The material entity that is being evaluated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["Sample"]
    class_class_curie: ClassVar[str] = "michi:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = MICHI.Sample


class Molecule(YAMLRoot):
    """
    A molecular entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["Molecule"]
    class_class_curie: ClassVar[str] = "michi:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = MICHI.Molecule


class ChemicalSubstance(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["ChemicalSubstance"]
    class_class_curie: ClassVar[str] = "michi:ChemicalSubstance"
    class_name: ClassVar[str] = "Chemical_Substance"
    class_model_uri: ClassVar[URIRef] = MICHI.ChemicalSubstance


class Analysis(YAMLRoot):
    """
    The planned process to analyse/assay a sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0001209"]
    class_class_curie: ClassVar[str] = "OBI:0001209"
    class_name: ClassVar[str] = "Analysis"
    class_model_uri: ClassVar[URIRef] = MICHI.Analysis


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MICHI.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MICHI.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MICHI.description, domain=None, range=Optional[str])

slots.datasetCollection__entries = Slot(uri=MICHI.entries, name="datasetCollection__entries", curie=MICHI.curie('entries'),
                   model_uri=MICHI.datasetCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, DatasetId], Union[dict, Dataset]], List[Union[dict, Dataset]]]])

slots.primary_email = Slot(uri=MICHI.primary_email, name="primary_email", curie=MICHI.curie('primary_email'),
                   model_uri=MICHI.primary_email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.Dataset_primary_email = Slot(uri=MICHI.primary_email, name="Dataset_primary_email", curie=MICHI.curie('primary_email'),
                   model_uri=MICHI.Dataset_primary_email, domain=Dataset, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))