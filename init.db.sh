#!/bin/bash

set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
-- CREATE DATABASE rgb_db
-- USE rgb_db

CREATE TABLE IF NOT EXISTS entries(
uuid CHAR(36) PRIMARY KEY, 
name VARCHAR(255), 
date DATE, 
start TIME(HH:MI)
end TIME(HH:MI)
comment VARCHAR(255));
EOSQL
