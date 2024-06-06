-- # Class: "MinimalMetadataMixin" Description: "A mixin with the minimal required slots of a class in this schema."
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "Dataset" Description: "Represents a Dataset"
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
--     * Slot: DatasetCollection_id Description: Autocreated FK slot
-- # Class: "DatasetCollection" Description: "A holder for Dataset objects"
--     * Slot: id Description: 
-- # Class: "Protocol" Description: "The information that specifies how to execute a planned process, in terms of what steps and actions must be taken and what preconditions must be met"
--     * Slot: id Description: 
-- # Class: "Characteristic" Description: "An attribute/characteristic of an entity (which could be a material entity, information or process)"
--     * Slot: id Description: 
--     * Slot: has_quantitative_value Description: A property to provide the qualitative value of a characteristic
--     * Slot: output_of_analysis Description: A property to provide the chemical analysis or assay that determined the characteristic
-- # Class: "MaterialEntity" Description: "Material entities are three-dimensional entities (entities extended in three spatial dimensions), as contrasted with the processes in which they participate, which are four-dimensional entities (entities extended also along the dimension of time)"
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "Sample" Description: "The material entity that is being evaluated to assay its attributes/characteristic."
--     * Slot: output_of_sampling_process Description: A property to link a sample to its creation process.
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
--     * Slot: has_characteristic_id Description: A property to provide a Characteristic of a Material Entity, such as a Sample, or a Process
-- # Class: "ChemicalEntity" Description: "Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity."
--     * Slot: iupac_name Description: A property to provide the IUPAC name of a Chemical Substance or Chemical Entity.
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "ChemicalSubstance" Description: "A MaterialEntity that is composed of multiple Chemical Entities of either the same or different kind"
--     * Slot: provenance Description: A property to provide a specific setting of a device
--     * Slot: space_group Description: A property to provide the space group of a Chemical Substance.
--     * Slot: iupac_name Description: A property to provide the IUPAC name of a Chemical Substance or Chemical Entity.
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "Device" Description: "A  used within an analysis with a specific function"
--     * Slot: has_part Description: A property to provide the part of a device
--     * Slot: has_manufacturer Description: A property to provide the vendor of a device
--     * Slot: has_serial_number Description: A property to provide the serial number of a device
--     * Slot: has_model_number Description: A property to provide the model number of a device
--     * Slot: has_function Description: A property to provide the specific function of a device
--     * Slot: has_setting Description: A property to provide a specific setting of a device
--     * Slot: has_visual_representation Description: A property to provide a visualization of a device, such as an image, scetch or schematic drawing.
--     * Slot: has_type Description: A property to provide the specific type of the class it is used on.
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "DevicePart" Description: "A device which function is to be a part of another device that is used within a chemical assay."
--     * Slot: has_part Description: A property to provide the part of a device
--     * Slot: has_manufacturer Description: A property to provide the vendor of a device
--     * Slot: has_serial_number Description: A property to provide the serial number of a device
--     * Slot: has_model_number Description: A property to provide the model number of a device
--     * Slot: has_function Description: A property to provide the specific function of a device
--     * Slot: has_setting Description: A property to provide a specific setting of a device
--     * Slot: has_visual_representation Description: A property to provide a visualization of a device, such as an image, scetch or schematic drawing.
--     * Slot: has_type Description: A property to provide the specific type of the class it is used on.
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "PlannedProcess" Description: "A process that is executed according to some plan or protocol"
--     * Slot: has_input Description: A property to provide the input of a process.
--     * Slot: has_output Description: A property to provide the output of a proces.
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "ChemicalAssay" Description: "The planned process to chemically assay a sample in order to determine some characteristic of it."
--     * Slot: has_sample Description: A property to provide the sample being evaluated in a ChemicalAssay
--     * Slot: has_device Description: A property to provide the device being used in a ChemicalAssay
--     * Slot: produces_dataset Description: A property to provide the dataset being produced by a ChemicalAnalysis or ChemicalAssay
--     * Slot: has_type Description: A property to provide the specific type of the class it is used on.
--     * Slot: has_input Description: A property to provide the input of a process.
--     * Slot: has_output Description: A property to provide the output of a proces.
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "ChemicalAnalysis" Description: "An interpretation of the data output of a ChemicalAssay"
--     * Slot: has_status Description: A property to provide the status of a ChemicalAnalysis
--     * Slot: based_on_assay_output Description: The status of a ChemicalAnalysis
--     * Slot: has_input Description: A property to provide the input of a process.
--     * Slot: has_output Description: A property to provide the output of a proces.
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "SamplePreparation" Description: "The process in which a sample is being generated or prepared for further analysis"
--     * Slot: has_input Description: A property to provide the input of a process.
--     * Slot: has_output Description: A property to provide the output of a proces.
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "ChemicalReaction" Description: "A process between multiple chemical entities of a different kind."
--     * Slot: id Description: A property to provide the unique identifier for a thing
--     * Slot: name Description: A property to provide the human-readable name for a thing
--     * Slot: description Description: A property to provide the human-readable description for a thing
-- # Class: "ChemicalSubstance_composed_of_chemical_entity" Description: ""
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: composed_of_chemical_entity Description: A property to provide the chemical entities of which a chemical substance is composed of.

CREATE TABLE "MinimalMetadataMixin" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DatasetCollection" (
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
CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalEntity" (
	iupac_name TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalSubstance" (
	provenance TEXT, 
	space_group TEXT, 
	iupac_name TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Device" (
	has_part TEXT, 
	has_manufacturer TEXT, 
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
	has_manufacturer TEXT, 
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
	has_input TEXT, 
	has_output TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalAssay" (
	has_sample TEXT, 
	has_device TEXT, 
	produces_dataset TEXT, 
	has_type TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalAnalysis" (
	has_status VARCHAR(11), 
	based_on_assay_output TEXT, 
	has_input TEXT, 
	has_output TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SamplePreparation" (
	has_input TEXT, 
	has_output TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalReaction" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
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
CREATE TABLE "Sample" (
	output_of_sampling_process TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_characteristic_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(output_of_sampling_process) REFERENCES "SamplePreparation" (id), 
	FOREIGN KEY(has_characteristic_id) REFERENCES "Characteristic" (id)
);
CREATE TABLE "ChemicalSubstance_composed_of_chemical_entity" (
	"ChemicalSubstance_id" TEXT, 
	composed_of_chemical_entity TEXT, 
	PRIMARY KEY ("ChemicalSubstance_id", composed_of_chemical_entity), 
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id)
);