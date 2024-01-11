```sh
# enable archive log
docker-compose exec -i oracle sqlplus /nolog <<- EOF
    CONNECT sys/oracle AS SYSDBA
	-- Turn on Archivelog Mode
	SHUTDOWN IMMEDIATE
	STARTUP MOUNT
	ALTER DATABASE ARCHIVELOG;
	ALTER DATABASE FLASHBACK ON;
	ALTER DATABASE OPEN;
	-- Should show "Database log mode: Archive Mode"
	ARCHIVE LOG LIST
	exit;
EOF

# interactive session
docker-compose exec -i oracle sqlplus sys/oracle@//localhost:1521/ORCLCDB as sysdba


# docker-compose exec -i oracle sqlplus sys/oracle@//localhost:1521/ORCLCDB as sysdba
```sql
ALTER SESSION SET CONTAINER=CDB$ROOT;
CREATE ROLE C##CDC_PRIVS;
CREATE USER C##MYUSER IDENTIFIED BY password CONTAINER=ALL;
ALTER USER C##MYUSER QUOTA UNLIMITED ON USERS;
ALTER USER C##MYUSER SET CONTAINER_DATA = (CDB$ROOT, ORCLPDB1) CONTAINER=CURRENT;
GRANT C##CDC_PRIVS to C##MYUSER CONTAINER=ALL;

GRANT CREATE SESSION TO C##CDC_PRIVS CONTAINER=ALL;
GRANT EXECUTE ON SYS.DBMS_LOGMNR TO C##CDC_PRIVS CONTAINER=ALL;
GRANT LOGMINING TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$LOGMNR_CONTENTS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$DATABASE TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$THREAD TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$PARAMETER TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$NLS_PARAMETERS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$TIMEZONE_NAMES TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_INDEXES TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_OBJECTS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_USERS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_CATALOG TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_CONSTRAINTS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_CONS_COLUMNS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_TAB_COLS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_IND_COLUMNS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_ENCRYPTED_COLUMNS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_LOG_GROUPS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_TAB_PARTITIONS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON SYS.DBA_REGISTRY TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON SYS.OBJ$ TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON DBA_TABLESPACES TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON DBA_OBJECTS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON SYS.ENC$ TO C##CDC_PRIVS CONTAINER=ALL;
GRANT CONNECT TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON DBA_PDBS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON CDB_TABLES TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON CDB_TAB_PARTITIONS TO C##CDC_PRIVS CONTAINER=ALL;

ALTER SESSION SET CONTAINER=ORCLPDB1;
GRANT SELECT ANY TABLE TO C##CDC_PRIVS;

ALTER SESSION SET CONTAINER=CDB$ROOT;
-- The following privileges are required additionally for 19c and 21c compared to 12c.
GRANT SELECT ON V_$ARCHIVED_LOG TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$LOG TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$LOGFILE TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$INSTANCE to C##CDC_PRIVS CONTAINER=ALL;

-- Need this only if using Full Supplemental Logging for only a select few tables
-- GRANT SELECT ON DBA_SUPPLEMENTAL_LOGGING TO C##CDC_PRIVS CONTAINER=ALL;

ALTER SESSION SET CONTAINER=cdb$root;
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

ALTER SESSION SET CONTAINER=ORCLPDB1;
GRANT FLASHBACK ON <schema>.<table> TO C##CDC_PRIVS

```

# docker-compose exec -i oracle sqlplus sys/oracle@//localhost:1521/ORCLCDB as sysdba
```sql
ALTER SESSION SET CONTAINER=CDB$ROOT;
CREATE ROLE C##CDC_PRIVS;
CREATE USER C##MYUSER IDENTIFIED BY password CONTAINER=ALL;
ALTER USER C##MYUSER QUOTA UNLIMITED ON USERS;
ALTER USER C##MYUSER SET CONTAINER_DATA = (CDB$ROOT, ORCLPDB1) CONTAINER=CURRENT;
GRANT C##CDC_PRIVS to C##MYUSER CONTAINER=ALL;

GRANT CREATE SESSION TO C##CDC_PRIVS CONTAINER=ALL;
GRANT EXECUTE ON SYS.DBMS_LOGMNR TO C##CDC_PRIVS CONTAINER=ALL;
GRANT LOGMINING TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$LOGMNR_CONTENTS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$DATABASE TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$THREAD TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$PARAMETER TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$NLS_PARAMETERS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$TIMEZONE_NAMES TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_INDEXES TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_OBJECTS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_USERS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_CATALOG TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_CONSTRAINTS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_CONS_COLUMNS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_TAB_COLS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_IND_COLUMNS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_ENCRYPTED_COLUMNS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_LOG_GROUPS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON ALL_TAB_PARTITIONS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON SYS.DBA_REGISTRY TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON SYS.OBJ$ TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON DBA_TABLESPACES TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON DBA_OBJECTS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON SYS.ENC$ TO C##CDC_PRIVS CONTAINER=ALL;
GRANT CONNECT TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON DBA_PDBS TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON CDB_TABLES TO C##CDC_PRIVS CONTAINER=ALL;

GRANT CREATE TABLE TO C##MYUSER container=all;
GRANT CREATE SEQUENCE TO C##MYUSER container=all;
GRANT CREATE TRIGGER TO C##MYUSER container=all;
GRANT FLASHBACK ANY TABLE TO C##MYUSER container=all;

-- The following privileges are required additionally for 19c compared to 12c.
GRANT SELECT ON V_$ARCHIVED_LOG TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$LOG TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$LOGFILE TO C##CDC_PRIVS CONTAINER=ALL;
GRANT SELECT ON V_$INSTANCE to C##CDC_PRIVS CONTAINER=ALL;
GRANT EXECUTE ON SYS.DBMS_LOGMNR TO C##CDC_PRIVS;
GRANT EXECUTE ON SYS.DBMS_LOGMNR_D TO C##CDC_PRIVS;
GRANT EXECUTE ON SYS.DBMS_LOGMNR_LOGREP_DICT TO C##CDC_PRIVS;

-- Enable Supplemental Logging for All Columns
ALTER SESSION SET CONTAINER=cdb$root;
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

-- Check Database Instance Version
GRANT SELECT ON V_$INSTANCE to C##CDC_PRIVS;

GRANT CREATE materialized view to C##CDC_PRIVS container=all;

-- grant select to materialized view
GRANT SELECT ON C##MYUSER.CustomerPolicyClaimsMV TO C##CDC_PRIVS;
```


# ksqldb queries

```sql
CREATE STREAM REDOLOG WITH (KAFKA_TOPIC='redo-log-topic', VALUE_FORMAT='AVRO');
CREATE STREAM CUSTOMERS WITH (KAFKA_TOPIC='ORCLCDB.C__MYUSER.CUSTOMERS', VALUE_FORMAT='AVRO');
CREATE STREAM CLAIMS WITH (KAFKA_TOPIC='ORCLCDB.C__MYUSER.CLAIMS', VALUE_FORMAT='AVRO');
CREATE STREAM POLICIES WITH (KAFKA_TOPIC='ORCLCDB.C__MYUSER.POLICIES', VALUE_FORMAT='AVRO');
CREATE STREAM CUSTOMERPOLICYCLAIMSMV WITH (KAFKA_TOPIC='ORCLCDB.C__MYUSER.CUSTOMERPOLICYCLAIMSMV', VALUE_FORMAT='AVRO');
```