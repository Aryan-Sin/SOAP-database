-- This file contains the DDL script for the SOAP database

CREATE TABLE gsa_offices (
    office_name     	varchar(100),
    city            	varchar(100) NOT NULL,
    tol_sq_foot     	numeric(10,2) NOT NULL CHECK (tol_sq_foot >= 0),
    PRIMARY KEY (office_name)
);

CREATE TABLE agencies (
	agency_id			varchar(10),
	agency_name			varchar(100) NOT NULL,
	agency_address		varchar(100) NOT NULL,
	city				varchar(100) NOT NULL,
	phone_number		numeric(10,0) NOT NULL,
	PRIMARY KEY (agency_id)
);

CREATE TABLE rental_agreements (
	ra_id				varchar(10),
	office_name			varchar(100) NOT NULL,
	rent_amnt			numeric(10,2) NOT NULL CHECK (rent_amnt >= 0),
	end_year			numeric(4,0) NOT NULL CHECK (end_year > 1701 AND end_year < 2100),
	end_month			numeric(2,0) NOT NULL CHECK (end_month >= 1 AND end_month <= 12),
	end_day				numeric(2,0) NOT NULL CHECK (end_day >= 1 AND end_day <= 31),
	PRIMARY KEY (ra_id),
	FOREIGN KEY (office_name) REFERENCES gsa_offices(office_name)
);

CREATE TABLE ra_agencies (
    ra_id           	varchar(10) NOT NULL,
    agency_id       	varchar(10) NOT NULL,
	PRIMARY KEY (ra_id, agency_id),
    FOREIGN KEY (ra_id) REFERENCES rental_agreements(ra_id)
                ON DELETE CASCADE, 
    FOREIGN KEY (agency_id) REFERENCES agencies(agency_id) 
);

