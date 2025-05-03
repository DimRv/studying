CREATE TABLE funcs(
	id serial PRIMARY KEY,
	title varchar(30) NOT NULL,
	s_desc varchar(30) NOT NULL,
	l_desc text NOT NULL
);

CREATE TABLE params(
	id serial PRIMARY KEY,
	title varchar(30) NOT NULL,
	s_desc varchar(30) NOT NULL
);

CREATE table func_params(
	f_id integer NOT NULL,
	p_id integer NOT NULL,
	FOREIGN KEY (f_id) REFERENCES funcs(id),
	FOREIGN KEY (p_id) REFERENCES params(id)
);