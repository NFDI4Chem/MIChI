-- # Class: "NamedThing" Description: "A generic grouping for any identifiable entity"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Dataset" Description: "Represents a Dataset"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: DatasetCollection_id Description: Autocreated FK slot
-- # Class: "DatasetCollection" Description: "A holder for Dataset objects"
--     * Slot: id Description: 
-- # Class: "Data" Description: "Information about some entity produced by a planned process."
--     * Slot: id Description: 
-- # Class: "RawData" Description: ""
--     * Slot: id Description: 
-- # Class: "Protocol" Description: "The information that specifies how to execute a planned process, in terms of what steps and actions must be taken and what preconditions must be met"
--     * Slot: id Description: 
-- # Class: "Characteristic" Description: "An attribute/characteristic of an entity (which could be a material entity, information or process)"
--     * Slot: id Description: 
--     * Slot: has_quantitative_value Description: 
--     * Slot: output_of_analysis Description: 
-- # Class: "Sample" Description: "The material entity that is being evaluated to assay its attributes/characteristic."
--     * Slot: output_of_sampling_process Description: 
--     * Slot: has_characteristic Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "MaterialEntity" Description: "Material entities are three-dimensional entities (entities extended in three spatial dimensions), as contrasted with the processes in which they participate, which are four-dimensional entities (entities extended also along the dimension of time)"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "ChemicalEntity" Description: "Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity."
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "ChemicalSubstance" Description: "A MaterialEntity that is composed of multiple Chemical Entities of either the same or different kind"
--     * Slot: provenance Description: 
--     * Slot: composed_of_chemical_entity Description: 
--     * Slot: space_group Description: 
--     * Slot: iupac_name Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Device" Description: "A  used within an analysis with a specific function"
--     * Slot: has_part Description: 
--     * Slot: has_vendor Description: 
--     * Slot: has_serial_number Description: 
--     * Slot: has_model_number Description: 
--     * Slot: has_function Description: 
--     * Slot: has_setting Description: 
--     * Slot: has_visual_representation Description: 
--     * Slot: has_type Description: A property to provide the specific type of the class it is used on.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "DevicePart" Description: ""
--     * Slot: has_part Description: 
--     * Slot: has_vendor Description: 
--     * Slot: has_serial_number Description: 
--     * Slot: has_model_number Description: 
--     * Slot: has_function Description: 
--     * Slot: has_setting Description: 
--     * Slot: has_visual_representation Description: 
--     * Slot: has_type Description: A property to provide the specific type of the class it is used on.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "PlannedProcess" Description: "A process that is executed according to some plan or protocol"
--     * Slot: id Description: 
--     * Slot: has_input Description: 
--     * Slot: has_output Description: 
-- # Class: "ChemicalReaction" Description: ""
--     * Slot: id Description: 
-- # Class: "ChemicalAssay" Description: "The planned process to chemically assay a sample in order to determine some characteristic of it."
--     * Slot: id Description: 
--     * Slot: has_sample Description: 
--     * Slot: has_device Description: 
--     * Slot: produces_dataset Description: 
--     * Slot: has_type Description: A property to provide the specific type of the class it is used on.
--     * Slot: has_input Description: 
--     * Slot: has_output Description: 
-- # Class: "ChemicalAnalysis" Description: "An interpretation of the data output of a ChemicalAssay"
--     * Slot: id Description: 
--     * Slot: has_status Description: 
--     * Slot: based_on_assay_output Description: 
--     * Slot: has_input Description: 
--     * Slot: has_output Description: 
-- # Class: "SamplePreparation" Description: "The process in which a sample is being generated or prepared for further analysis"
--     * Slot: id Description: 
--     * Slot: has_input Description: 
--     * Slot: has_output Description: 

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DatasetCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Data" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "RawData" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Protocol" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Characteristic" (
	id INTEGER NOT NULL, 
	has_quantitative_value TEXT, 
	output_of_analysis TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sample" (
	output_of_sampling_process TEXT, 
	has_characteristic TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalSubstance" (
	provenance TEXT, 
	composed_of_chemical_entity TEXT, 
	space_group TEXT, 
	iupac_name TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Device" (
	has_part TEXT, 
	has_vendor TEXT, 
	has_serial_number TEXT, 
	has_model_number TEXT, 
	has_function TEXT, 
	has_setting TEXT, 
	has_visual_representation TEXT, 
	has_type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DevicePart" (
	has_part TEXT, 
	has_vendor TEXT, 
	has_serial_number TEXT, 
	has_model_number TEXT, 
	has_function TEXT, 
	has_setting TEXT, 
	has_visual_representation TEXT, 
	has_type TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PlannedProcess" (
	id INTEGER NOT NULL, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalReaction" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalAssay" (
	id INTEGER NOT NULL, 
	has_sample TEXT, 
	has_device TEXT, 
	produces_dataset TEXT, 
	has_type TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalAnalysis" (
	id INTEGER NOT NULL, 
	has_status TEXT, 
	based_on_assay_output TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SamplePreparation" (
	id INTEGER NOT NULL, 
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Dataset" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"DatasetCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DatasetCollection_id") REFERENCES "DatasetCollection" (id)
);