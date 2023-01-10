--------------------------------------------------------
-- Archivo creado  - lunes-noviembre-21-2022   
--------------------------------------------------------
DROP TABLE "JAVAP"."ANIMALES" cascade constraints;
--------------------------------------------------------
--  DDL for Table ANIMALES
--------------------------------------------------------

  CREATE TABLE "JAVAP"."ANIMALES" 
   (	"ID" NUMBER(8,0), 
	"NOMBRE" VARCHAR2(10 BYTE), 
	"ESPECIE" VARCHAR2(10 BYTE), 
	"FECHA_NACIMIENTO" DATE, 
	"SEXO" CHAR(1 BYTE), 
	"ALTURA" FLOAT(126), 
	"PESO" FLOAT(126), 
	"DESCRIPCION" LONG
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into JAVAP.ANIMALES
SET DEFINE OFF;
Insert into JAVAP.ANIMALES (ID,NOMBRE,ESPECIE,FECHA_NACIMIENTO,SEXO,ALTURA,PESO,DESCRIPCION) values ('4','Winnie','Oso',to_date('07/04/04','DD/MM/RR'),'H','1','90','Winnie the Pooh');
Insert into JAVAP.ANIMALES (ID,NOMBRE,ESPECIE,FECHA_NACIMIENTO,SEXO,ALTURA,PESO,DESCRIPCION) values ('6','Tantor','Elefante',to_date('17/07/06','DD/MM/RR'),'M','2,05','800','Elefante amigo de Tarzan');
Insert into JAVAP.ANIMALES (ID,NOMBRE,ESPECIE,FECHA_NACIMIENTO,SEXO,ALTURA,PESO,DESCRIPCION) values ('5','Dumbo','Elefante',to_date('01/06/08','DD/MM/RR'),'M','1,2','500','Elefante volador');
Insert into JAVAP.ANIMALES (ID,NOMBRE,ESPECIE,FECHA_NACIMIENTO,SEXO,ALTURA,PESO,DESCRIPCION) values ('7','Baloo','Oso',to_date('20/11/90','DD/MM/RR'),'M','1,8','150','El libro de la selva');
Insert into JAVAP.ANIMALES (ID,NOMBRE,ESPECIE,FECHA_NACIMIENTO,SEXO,ALTURA,PESO,DESCRIPCION) values ('8','Sardina','Caballo',to_date('05/06/05','DD/MM/RR'),'M','1,8','300','Caballo de Geralt de Rivia');
Insert into JAVAP.ANIMALES (ID,NOMBRE,ESPECIE,FECHA_NACIMIENTO,SEXO,ALTURA,PESO,DESCRIPCION) values ('1','Kiara','Perro',to_date('05/04/14','DD/MM/RR'),'H','0,5','18','Husky Siberiano Gris y blanco');
Insert into JAVAP.ANIMALES (ID,NOMBRE,ESPECIE,FECHA_NACIMIENTO,SEXO,ALTURA,PESO,DESCRIPCION) values ('2','Dyna','Perro',to_date('05/10/20','DD/MM/RR'),'H','0,5','18','Husky Siberiano Blanco y Rubio');
Insert into JAVAP.ANIMALES (ID,NOMBRE,ESPECIE,FECHA_NACIMIENTO,SEXO,ALTURA,PESO,DESCRIPCION) values ('3','Tara','Perro',to_date('10/10/15','DD/MM/RR'),'H','0,5','18','Husky Siberiano Gris y Blanco');
