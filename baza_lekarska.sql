/*  ### ODDZIALY ### */
create table oddzialy_nfz(
    ID_oddzialu number primary key,
    nazwa_oddzialu varchar2(60) not null
);


/*  ### LEKI ### */
create table leki(
    ID_leku number primary key,
    nazwa varchar2(100) not null,
    postac varchar2(100) not null,
    sklad varchar2(500) not null,
    dawka varchar2(200) not null,
    czy_refundowany varchar2(1) check (czy_refundowany in ('t','n')) not null,
    procent_refundacji number(3) null,
    czy_na_recepte varchar2(1) check (czy_na_recepte in ('t','n')) not null
);

create table przepisane_leki(
    ID_wpisu number primary key,
    ID_leku number not null,
    ID_pacjenta number not null,
    data_przepisania date not null
);

alter table przepisane_leki
add constraint fk_przepis_lek foreign key (id_leku)
references leki(id_leku);


/*  ### STANY ZDROWIA ### */
create table stany_zdrowia_pacjentow(
    ID_stanu_zdrowia number primary key,
    ID_pacjenta number not null,
    data_akceptacji date null,
    przebyte_choroby varchar2(1000) null,
    przewlekle_choroby varchar2(1000) null,
    pobyty_w_szpitalu varchar2(1000) null,
    zabiegi varchar2(1000) null,
    szczepienia varchar2(1000) null,
    uczulenia varchar2(1000) null,
    obciazenia varchar2(1000) null);


/*  ### WIZYTY ### */
CREATE TABLE wizyty (
	ID_wizyty number PRIMARY KEY,
	data_wizyty date NOT NULL,
	wywiad varchar2(1000) NULL,
	rozpoznanie varchar2(1000) NULL,
	zalecenia varchar2(1000) NULL,
	zlecone_badania varchar2(1000) NULL,
	leki varchar2(1000) NULL,
	zwolnienia varchar2(1000) NULL,
	ID_pacjenta number NOT NULL); 
    
insert into wizyty(id_wizyty, data_wizyty, wywiad, rozpoznanie, zalecenia, zlecone_badania, leki, zwolnienia, id_pacjenta)
values (0, TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'), 'historia choroby', 'diagnoza','siedziec w domu' ,'zrobic badanie krwi', 'espumisan', 'zwolniony z w-fu', 0);
    
alter table wizyty
add constraint fk_wizyta_pacjent foreign key (id_pacjenta)
references pacjenci(id_pacjenta);
    
/*  ### LEKARZE ### */
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
    
insert into lekarze(ID_lekarza, specjalizacja,tytul, imie, nazwisko, miejscowosc, kod_pocztowy, ulica, nr_domu,
                        nr_mieszkania, nr_tel, adres_email, nr_pwz)
values (0, 'Psychiatra', 'Doktor', 'Marek', 'Hoffman', 'Turek', '62700', 'Inna',23,1,876654827,'costam@wp.pl', 8765432);


/*  ### PACJENCI ### */
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

alter table pacjenci
add constraint fk_pacjent_oddzial foreign key (oddzial_nfz)
references oddzialy_nfz(id_oddzialu);

