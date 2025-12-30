-- Database: db_dolar

-- DROP DATABASE IF EXISTS db_dolar;

CREATE DATABASE db_dolar
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
    

-- Table: public.tb_dolar

-- DROP TABLE IF EXISTS public.tb_dolar;

CREATE TABLE IF NOT EXISTS public.tb_dolar
(
    year numeric NOT NULL,
    mount numeric NOT NULL,
    day numeric NOT NULL,
    value numeric(19,2) NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tb_dolar
    OWNER to postgres;

