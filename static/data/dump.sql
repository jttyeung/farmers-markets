--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.5
-- Dumped by pg_dump version 9.5.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: brands; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE brands (
    brand_id character varying(5) NOT NULL,
    name character varying(50) NOT NULL,
    founded integer,
    headquarters character varying(50),
    discontinued integer
);


ALTER TABLE brands OWNER TO vagrant;

--
-- Name: models; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE models (
    model_id integer NOT NULL,
    year integer NOT NULL,
    brand_id character varying(5) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE models OWNER TO vagrant;

--
-- Name: models_model_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE models_model_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE models_model_id_seq OWNER TO vagrant;

--
-- Name: models_model_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE models_model_id_seq OWNED BY models.model_id;


--
-- Name: model_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY models ALTER COLUMN model_id SET DEFAULT nextval('models_model_id_seq'::regclass);


--
-- Data for Name: brands; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY brands (brand_id, name, founded, headquarters, discontinued) FROM stdin;
for	Ford	1903	Dearborn, MI	\N
chr	Chrysler	1925	Auburn Hills, Michigan	\N
cit	Citroen	1919	Saint-Ouen, France	\N
hil	Hillman	1907	Ryton-on-Dunsmore, England	1981
che	Chevrolet	1911	Detroit, Michigan	\N
cad	Cadillac	1902	New York City, NY	\N
bmw	BMW	1916	Munich, Bavaria, Germany	\N
aus	Austin	1905	Longbridge, England	1987
fai	Fairthorpe	1954	Chalfont St Peter, Buckinghamshire	1976
stu	Studebaker	1852	South Bend, Indiana	1967
pon	Pontiac	1926	Detroit, MI	2010
bui	Buick	1903	Detroit, MI	\N
ram	Rambler	1901	Kenosha, Washington	1969
ply	Plymouth	1928	Auburn Hills, Michigan	2001
tes	Tesla	2003	Palo Alto, CA	\N
\.


--
-- Data for Name: models; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY models (model_id, year, brand_id, name) FROM stdin;
1	1909	for	Model T
2	1926	chr	Imperial
3	1948	cit	2CV
4	1950	hil	Minx Magnificent
5	1953	che	Corvette
6	1954	che	Corvette
7	1954	cad	Fleetwood
8	1955	che	Corvette
9	1955	for	Thunderbird
10	1956	che	Corvette
11	1957	che	Corvette
12	1957	bmw	600
13	1958	che	Corvette
14	1958	bmw	600
15	1958	for	Thunderbird
16	1959	aus	Mini
17	1959	che	Corvette
18	1959	bmw	600
19	1960	che	Corvair
20	1960	che	Corvette
21	1960	fai	Rockette
22	1961	aus	Mini Cooper
23	1961	stu	Avanti
24	1961	pon	Tempest
25	1961	che	Corvette
26	1962	pon	Grand Prix
27	1962	che	Corvette
28	1962	stu	Avanti
29	1962	bui	Special
30	1963	aus	Mini
31	1963	aus	Mini Cooper S
32	1963	ram	Classic
33	1963	for	E-Series
34	1963	stu	Avanti
35	1963	pon	Grand Prix
36	1963	che	Corvair 500
37	1963	che	Corvette
38	1964	che	Corvette
39	1964	for	Mustang
40	1964	for	Galaxie
41	1964	pon	LeMans
42	1964	pon	Bonneville
43	1964	pon	Grand Prix
44	1964	ply	Fury
45	1964	stu	Avanti
46	1964	aus	Mini Cooper
\.


--
-- Name: models_model_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('models_model_id_seq', 46, true);


--
-- Name: brands_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY brands
    ADD CONSTRAINT brands_pkey PRIMARY KEY (brand_id);


--
-- Name: models_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY models
    ADD CONSTRAINT models_pkey PRIMARY KEY (model_id);


--
-- Name: models_brand_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY models
    ADD CONSTRAINT models_brand_id_fkey FOREIGN KEY (brand_id) REFERENCES brands(brand_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

