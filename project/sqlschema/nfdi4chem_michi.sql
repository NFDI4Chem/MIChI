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
-- # Class: "Sample" Description: "The material entity that is being evaluated."
--     * Slot: id Description: 
-- # Class: "Molecule" Description: "A molecular entity"
--     * Slot: id Description: 
-- # Class: "Chemical_Substance" Description: ""
--     * Slot: id Description: 
-- # Class: "Analysis" Description: ""
--     * Slot: id Description: 

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
CREATE TABLE "Sample" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Molecule" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Chemical_Substance" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Analysis" (
	id INTEGER NOT NULL, 
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