/*
CREATE TABLE lekarze (
	ID_lekarza number PRIMARY KEY,
	specjalizacja varchar2(100) NOT NULL,
	tytul varchar2(100) NOT NULL,
	imie varchar2(30) NOT NULL,
	nazwisko varchar2(60) NOT NULL,
	miejscowosc varchar2(100) NOT NULL,
	kod_pocztowy number NOT NULL,
	ulica varchar2(100) NOT NULL,
	nr_domu number NOT NULL,
	nr_mieszkania number NOT NULL,
	nr_tel number NOT NULL,
	adres_email varchar2(100) NOT NULL,
	nr_pwz number NOT NULL);
    */
 /*insert into lekarze(ID_lekarza, specjalizacja,tytul, imie, nazwisko, miejscowosc, kod_pocztowy, ulica, nr_domu,
                        nr_mieszkania, nr_tel, adres_email, nr_pwz)
values (0, 'Psychiatra', 'Doktor', 'Marek', 'Hoffman', 'Turek', '62700', 'Inna',23,1,876654827,'costam@wp.pl', 8765432);
*/


CREATE TABLE pacjenci (
	ID_pacjenta number PRIMARY KEY,
	ID_lekarza number NOT NULL,
	PESEL number NOT NULL,
	imie varchar2(30) NOT NULL,
	nazwisko varchar2(60) NOT NULL,
	plec varchar2(1) check (plec in ('K','M')) NOT NULL,
	wiek number NOT NULL,
	miejscowosc varchar2(100) NOT NULL,
	kod_pocztowy number(5) NOT NULL,
	ulica varchar2(100) NOT NULL,
	nr_domu number NOT NULL,
	nr_mieszkania number NOT NULL,
	nr_tel number NOT NULL,
	adres_email varchar2(100) NOT NULL,
	oddzial_NFZ number NOT NULL); 
    
insert into pacjenci(ID_pacjenta,ID_lekarza,PESEL,imie, nazwisko, plec, wiek, miejscowosc, kod_pocztowy, ulica, nr_domu,
                        nr_mieszkania, nr_tel, adres_email, oddzial_nfz)
values (0, 0, 78965412354, 'Adam', 'Gilbert', 'M', 25, 'Wroc³aw',23456,'Dziwna',4,21,785412356,'costam@wp.pl', 1);

select * from pacjenci;

