-- Script for table creation of Crimes Database

CREATE TABLE CrimeTypes(
	CrimeTypeID int Not Null Constraint pkCrimeTypeID Primary Key Identity,
	CrimeTypeName varchar(255) Not Null
);

GO

CREATE TABLE CrimeAgainst(
	CrimeAgainstID int Not Null Constraint pkCrimeAgainstID Primary Key Identity,
	CrimeAgainstType varchar(255) Not Null
);

GO

CREATE TABLE PopulationDensity(
	PopulationDensityID int Not Null Constraint pkPopulationDensityID Primary Key Identity,
	PopulationDensity float Not Null
);

GO

CREATE TABLE Neighborhood(
	NeighborhoodID int Not Null Constraint pkNeighborhoodID Primary Key Identity,
	PopulationDensityID int Not Null Constraint fkPopulationDensityID Foreign Key References PopulationDensity(PopulationDensityID)
);

GO

CREATE TABLE Crimes(
	CrimeID int Not Null Constraint pkCrimeID Primary Key Identity,
	CrimeTypeID int Not Null Constraint fkCrimeTypeID Foreign Key References CrimeTypes(CrimeTypeID),
	CrimeAgainstID int Not Null Constraint fkCrimeAgainstID Foreign Key References CrimeAgainst(CrimeAgainstID),
	NeighborhoodID int Not Null Constraint fkNeighborhoodID Foreign Key References Neighborhood(NeighborhoodID),
	CrimeStartTime datetime,
	CrimeEndTime datetime,
	CrimeReportedTime datetime
);
