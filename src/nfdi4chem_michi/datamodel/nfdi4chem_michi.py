# Auto generated from nfdi4chem_michi.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-05-29T11:59:04
# Schema: NFDI4Chem_MIChI
#
# id: https://w3id.org/NFDI4Chem/MIChI
# description: This is the LinkML metadata schema prototype for NFDI4Chem
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
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
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


class SampleId(NamedThingId):
    pass


class MaterialEntityId(NamedThingId):
    pass


class ChemicalEntityId(MaterialEntityId):
    pass


class ChemicalSubstanceId(MaterialEntityId):
    pass


class DeviceId(NamedThingId):
    pass


class DevicePartId(DeviceId):
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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

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


class Data(YAMLRoot):
    """
    Information about some entity produced by a planned process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["Data"]
    class_class_curie: ClassVar[str] = "michi:Data"
    class_name: ClassVar[str] = "Data"
    class_model_uri: ClassVar[URIRef] = MICHI.Data


class RawData(Data):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["RawData"]
    class_class_curie: ClassVar[str] = "michi:RawData"
    class_name: ClassVar[str] = "RawData"
    class_model_uri: ClassVar[URIRef] = MICHI.RawData


class Protocol(YAMLRoot):
    """
    The information that specifies how to execute a planned process, in terms of what steps and actions must be taken
    and what preconditions must be met
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000272"]
    class_class_curie: ClassVar[str] = "OBI:0000272"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = MICHI.Protocol


@dataclass
class Characteristic(YAMLRoot):
    """
    An attribute/characteristic of an entity (which could be a material entity, information or process)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["Characteristic"]
    class_class_curie: ClassVar[str] = "michi:Characteristic"
    class_name: ClassVar[str] = "Characteristic"
    class_model_uri: ClassVar[URIRef] = MICHI.Characteristic

    has_quantitative_value: Optional[str] = None
    output_of_analysis: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_quantitative_value is not None and not isinstance(self.has_quantitative_value, str):
            self.has_quantitative_value = str(self.has_quantitative_value)

        if self.output_of_analysis is not None and not isinstance(self.output_of_analysis, str):
            self.output_of_analysis = str(self.output_of_analysis)

        super().__post_init__(**kwargs)


@dataclass
class Sample(NamedThing):
    """
    The material entity that is being evaluated to assay its attributes/characteristic.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["Sample"]
    class_class_curie: ClassVar[str] = "michi:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = MICHI.Sample

    id: Union[str, SampleId] = None
    output_of_sampling_process: Optional[str] = None
    has_characteristic: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self.output_of_sampling_process is not None and not isinstance(self.output_of_sampling_process, str):
            self.output_of_sampling_process = str(self.output_of_sampling_process)

        if self.has_characteristic is not None and not isinstance(self.has_characteristic, str):
            self.has_characteristic = str(self.has_characteristic)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    """
    Material entities are three-dimensional entities (entities extended in three spatial dimensions), as contrasted
    with the processes in which they participate, which are four-dimensional entities (entities extended also along
    the dimension of time)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000040"]
    class_class_curie: ClassVar[str] = "BFO:0000040"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = MICHI.MaterialEntity

    id: Union[str, MaterialEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalEntity(MaterialEntity):
    """
    Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex,
    conformer etc., identifiable as a separately distinguishable entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["23367"]
    class_class_curie: ClassVar[str] = "CHEBI:23367"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = MICHI.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalSubstance(MaterialEntity):
    """
    A MaterialEntity that is composed of multiple Chemical Entities of either the same or different kind
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["59999"]
    class_class_curie: ClassVar[str] = "CHEBI:59999"
    class_name: ClassVar[str] = "ChemicalSubstance"
    class_model_uri: ClassVar[URIRef] = MICHI.ChemicalSubstance

    id: Union[str, ChemicalSubstanceId] = None
    provenance: Optional[str] = None
    composed_of_chemical_entity: Optional[str] = None
    space_group: Optional[str] = None
    iupac_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)

        if self.provenance is not None and not isinstance(self.provenance, str):
            self.provenance = str(self.provenance)

        if self.composed_of_chemical_entity is not None and not isinstance(self.composed_of_chemical_entity, str):
            self.composed_of_chemical_entity = str(self.composed_of_chemical_entity)

        if self.space_group is not None and not isinstance(self.space_group, str):
            self.space_group = str(self.space_group)

        if self.iupac_name is not None and not isinstance(self.iupac_name, str):
            self.iupac_name = str(self.iupac_name)

        super().__post_init__(**kwargs)


@dataclass
class Device(NamedThing):
    """
    A  used within an analysis with a specific function
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["Device"]
    class_class_curie: ClassVar[str] = "michi:Device"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = MICHI.Device

    id: Union[str, DeviceId] = None
    has_part: Optional[str] = None
    has_vendor: Optional[str] = None
    has_serial_number: Optional[str] = None
    has_model_number: Optional[str] = None
    has_function: Optional[str] = None
    has_setting: Optional[str] = None
    has_visual_representation: Optional[str] = None
    has_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        if self.has_part is not None and not isinstance(self.has_part, str):
            self.has_part = str(self.has_part)

        if self.has_vendor is not None and not isinstance(self.has_vendor, str):
            self.has_vendor = str(self.has_vendor)

        if self.has_serial_number is not None and not isinstance(self.has_serial_number, str):
            self.has_serial_number = str(self.has_serial_number)

        if self.has_model_number is not None and not isinstance(self.has_model_number, str):
            self.has_model_number = str(self.has_model_number)

        if self.has_function is not None and not isinstance(self.has_function, str):
            self.has_function = str(self.has_function)

        if self.has_setting is not None and not isinstance(self.has_setting, str):
            self.has_setting = str(self.has_setting)

        if self.has_visual_representation is not None and not isinstance(self.has_visual_representation, str):
            self.has_visual_representation = str(self.has_visual_representation)

        self.has_type = str(self.class_name)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "has_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass
class DevicePart(Device):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["DevicePart"]
    class_class_curie: ClassVar[str] = "michi:DevicePart"
    class_name: ClassVar[str] = "DevicePart"
    class_model_uri: ClassVar[URIRef] = MICHI.DevicePart

    id: Union[str, DevicePartId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DevicePartId):
            self.id = DevicePartId(self.id)

        super().__post_init__(**kwargs)
        self.has_type = str(self.class_name)


@dataclass
class PlannedProcess(YAMLRoot):
    """
    A process that is executed according to some plan or protocol
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "OBI:0000011"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = MICHI.PlannedProcess

    has_input: Optional[str] = None
    has_output: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_input is not None and not isinstance(self.has_input, str):
            self.has_input = str(self.has_input)

        if self.has_output is not None and not isinstance(self.has_output, str):
            self.has_output = str(self.has_output)

        super().__post_init__(**kwargs)


class ChemicalReaction(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["ChemicalReaction"]
    class_class_curie: ClassVar[str] = "michi:ChemicalReaction"
    class_name: ClassVar[str] = "ChemicalReaction"
    class_model_uri: ClassVar[URIRef] = MICHI.ChemicalReaction


@dataclass
class ChemicalAssay(PlannedProcess):
    """
    The planned process to chemically assay a sample in order to determine some characteristic of it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "OBI:0000070"
    class_name: ClassVar[str] = "ChemicalAssay"
    class_model_uri: ClassVar[URIRef] = MICHI.ChemicalAssay

    has_sample: Optional[str] = None
    has_device: Optional[str] = None
    produces_dataset: Optional[str] = None
    has_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_sample is not None and not isinstance(self.has_sample, str):
            self.has_sample = str(self.has_sample)

        if self.has_device is not None and not isinstance(self.has_device, str):
            self.has_device = str(self.has_device)

        if self.produces_dataset is not None and not isinstance(self.produces_dataset, str):
            self.produces_dataset = str(self.produces_dataset)

        self.has_type = str(self.class_name)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalAnalysis(PlannedProcess):
    """
    An interpretation of the data output of a ChemicalAssay
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["ChemicalAnalysis"]
    class_class_curie: ClassVar[str] = "michi:ChemicalAnalysis"
    class_name: ClassVar[str] = "ChemicalAnalysis"
    class_model_uri: ClassVar[URIRef] = MICHI.ChemicalAnalysis

    has_status: Optional[str] = None
    based_on_assay_output: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_status is not None and not isinstance(self.has_status, str):
            self.has_status = str(self.has_status)

        if self.based_on_assay_output is not None and not isinstance(self.based_on_assay_output, str):
            self.based_on_assay_output = str(self.based_on_assay_output)

        super().__post_init__(**kwargs)


class SamplePreparation(PlannedProcess):
    """
    The process in which a sample is being generated or prepared for further analysis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICHI["SamplePreparation"]
    class_class_curie: ClassVar[str] = "michi:SamplePreparation"
    class_name: ClassVar[str] = "SamplePreparation"
    class_model_uri: ClassVar[URIRef] = MICHI.SamplePreparation


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

slots.has_input = Slot(uri=MICHI.has_input, name="has_input", curie=MICHI.curie('has_input'),
                   model_uri=MICHI.has_input, domain=None, range=Optional[str])

slots.has_output = Slot(uri=MICHI.has_output, name="has_output", curie=MICHI.curie('has_output'),
                   model_uri=MICHI.has_output, domain=None, range=Optional[str])

slots.has_sample = Slot(uri=MICHI.has_sample, name="has_sample", curie=MICHI.curie('has_sample'),
                   model_uri=MICHI.has_sample, domain=None, range=Optional[str])

slots.has_device = Slot(uri=MICHI.has_device, name="has_device", curie=MICHI.curie('has_device'),
                   model_uri=MICHI.has_device, domain=None, range=Optional[str])

slots.produces_dataset = Slot(uri=MICHI.produces_dataset, name="produces_dataset", curie=MICHI.curie('produces_dataset'),
                   model_uri=MICHI.produces_dataset, domain=None, range=Optional[str])

slots.has_quantitative_value = Slot(uri=MICHI.has_quantitative_value, name="has_quantitative_value", curie=MICHI.curie('has_quantitative_value'),
                   model_uri=MICHI.has_quantitative_value, domain=None, range=Optional[str])

slots.output_of_analysis = Slot(uri=MICHI.output_of_analysis, name="output_of_analysis", curie=MICHI.curie('output_of_analysis'),
                   model_uri=MICHI.output_of_analysis, domain=None, range=Optional[str])

slots.has_status = Slot(uri=MICHI.has_status, name="has_status", curie=MICHI.curie('has_status'),
                   model_uri=MICHI.has_status, domain=None, range=Optional[str])

slots.based_on_assay_output = Slot(uri=MICHI.based_on_assay_output, name="based_on_assay_output", curie=MICHI.curie('based_on_assay_output'),
                   model_uri=MICHI.based_on_assay_output, domain=None, range=Optional[str])

slots.has_type = Slot(uri=MICHI.has_type, name="has_type", curie=MICHI.curie('has_type'),
                   model_uri=MICHI.has_type, domain=None, range=Optional[str])

slots.has_part = Slot(uri=MICHI.has_part, name="has_part", curie=MICHI.curie('has_part'),
                   model_uri=MICHI.has_part, domain=None, range=Optional[str])

slots.has_vendor = Slot(uri=MICHI.has_vendor, name="has_vendor", curie=MICHI.curie('has_vendor'),
                   model_uri=MICHI.has_vendor, domain=None, range=Optional[str])

slots.has_serial_number = Slot(uri=MICHI.has_serial_number, name="has_serial_number", curie=MICHI.curie('has_serial_number'),
                   model_uri=MICHI.has_serial_number, domain=None, range=Optional[str])

slots.has_model_number = Slot(uri=MICHI.has_model_number, name="has_model_number", curie=MICHI.curie('has_model_number'),
                   model_uri=MICHI.has_model_number, domain=None, range=Optional[str])

slots.has_function = Slot(uri=MICHI.has_function, name="has_function", curie=MICHI.curie('has_function'),
                   model_uri=MICHI.has_function, domain=None, range=Optional[str])

slots.has_setting = Slot(uri=MICHI.has_setting, name="has_setting", curie=MICHI.curie('has_setting'),
                   model_uri=MICHI.has_setting, domain=None, range=Optional[str])

slots.has_visual_representation = Slot(uri=MICHI.has_visual_representation, name="has_visual_representation", curie=MICHI.curie('has_visual_representation'),
                   model_uri=MICHI.has_visual_representation, domain=None, range=Optional[str])

slots.provenance = Slot(uri=MICHI.provenance, name="provenance", curie=MICHI.curie('provenance'),
                   model_uri=MICHI.provenance, domain=None, range=Optional[str])

slots.composed_of_chemical_entity = Slot(uri=MICHI.composed_of_chemical_entity, name="composed_of_chemical_entity", curie=MICHI.curie('composed_of_chemical_entity'),
                   model_uri=MICHI.composed_of_chemical_entity, domain=None, range=Optional[str])

slots.space_group = Slot(uri=MICHI.space_group, name="space_group", curie=MICHI.curie('space_group'),
                   model_uri=MICHI.space_group, domain=None, range=Optional[str])

slots.iupac_name = Slot(uri=MICHI.iupac_name, name="iupac_name", curie=MICHI.curie('iupac_name'),
                   model_uri=MICHI.iupac_name, domain=None, range=Optional[str])

slots.output_of_sampling_process = Slot(uri=MICHI.output_of_sampling_process, name="output_of_sampling_process", curie=MICHI.curie('output_of_sampling_process'),
                   model_uri=MICHI.output_of_sampling_process, domain=None, range=Optional[str])

slots.has_characteristic = Slot(uri=MICHI.has_characteristic, name="has_characteristic", curie=MICHI.curie('has_characteristic'),
                   model_uri=MICHI.has_characteristic, domain=None, range=Optional[str])

slots.datasetCollection__entries = Slot(uri=MICHI.entries, name="datasetCollection__entries", curie=MICHI.curie('entries'),
                   model_uri=MICHI.datasetCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, DatasetId], Union[dict, Dataset]], List[Union[dict, Dataset]]]])