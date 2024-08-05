CREATE TABLE gsa_offices (
    office_name     	varchar(100) not null,
    city            	varchar(100) not null,
    tol_sq_foot     	numeric(10,2) check (tol_sq_foot >= 0),
    primary key (office_name)
);


CREATE TABLE agencies (
	agency_id			varchar(10) not null,
	agencies_name		varchar(100) not null,
	agencies_address	varchar(100) not null,
	city				varchar(100) not null,
	phone_number		numeric(10) not null,
	primary key (agency_id)
);


CREATE TABLE rental_agreements (
	ra_id				varchar(10) not null,
	office_name			varchar(100) not null,
	rent_amnt			numeric(10,2) not null,
	end_date			date not null,
	primary key (ra_id),
	foreign key (office_name) references gsa_offices(office_name)
);

CREATE TABLE ra_agencies (
    ra_id           	varchar(10) not null,
    agency_id       	varchar(10) not null,
    foreign key (ra_id) references rental_agreements(ra_id), 
    foreign key (agency_id) references agencies(agency_id) 
);
