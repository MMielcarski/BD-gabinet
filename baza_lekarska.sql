/******### LEKARZE ###******************************************************* */
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
    COMMENT ON TABLE Lekarze IS 'Dane lekarza';
    
/*******### PACJENCI### ************************************************************/    
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
	oddzial_NFZ number NOT NULL,
    przebyte_choroby   varchar2(1000),
    przewlekle_choroby varchar2(1000), 
    pobyty_w_szpitalu  varchar2(1000), 
    zabiegi            varchar2(1000), 
    szczepienia        varchar2(1000), 
    uczulenia          varchar2(1000), 
    obciazenia         varchar2(1000) ); 
    COMMENT ON TABLE Lekarze IS 'Dane pacjena wraz z opisem stanu zdrowia';
    
/****### ODDZIALY NFZ ###************************************************************ */    
CREATE TABLE oddzialy_NFZ (
  ID_oddzialu_NFZ number(2) PRIMARY KEY, 
  Nazwa           varchar2(60) NOT NULL);
  COMMENT ON TABLE oddzialy_NFZ IS 'Prawdziwe dane dotyczące oddziałów NFZ w Polsce'
  
     
/***### WIZYTY ###******************************************************************* */
CREATE TABLE wizyty (
	ID_wizyty number PRIMARY KEY,
	ID_pacjenta number NOT NULL,
	data_wizyty date DEFAULT '1999-01-01' NOT NULL,
	wywiad varchar2(1000) NULL,
	rozpoznanie varchar2(1000) NULL,
	zalecenia varchar2(1000) NULL,
	zlecone_badania varchar2(1000) NULL,
	id_leki number NULL,
	zwolnienia varchar2(1000) NULL ); 
    COMMENT ON TABLE wizyty IS 'Opis wizyty (lekarz zdaje relacje z wizyty danego pacjenta)';
       

/* ### LEKI ### */
create table baza_lekow(
    ID_leku number primary key,
    nazwa varchar2(100) not null,
    postac varchar2(100) not null,
    sklad varchar2(500) not null,
    dawka varchar2(200) not null,
    czy_refundowany varchar2(1) check (czy_refundowany in ('t','n')) not null,
    procent_refundacji number(3) null,
    czy_na_recepte varchar2(1) check (czy_na_recepte in ('t','n')) not null );
    COMMENT ON TABLE baza_lekow IS 'Baza istniejących leków wraz z parametrami';

/*  ### PRZEPISANE LEKI ### */
create table przepisane_leki(
    ID_wpisu number primary key,
    ID_wizyty number not null,
    ID_leku number not null,
    ilosc number not null);

/******REFERENCJE**************************************************************************************/
/*Każdy pacjent ma sowjego lekarza*/
alter table pacjenci
add constraint fk_pacjent_lekarz foreign key (id_lekarza)
references lekarze(id_lekarza)

/*Kazdy pacjent jest przypisany do danego oddzialu NFZ*/
alter table pacjenci
add constraint fk_pacjent_oddzial foreign key (oddzial_NFZ)
references oddzialy_nfz(id_oddzialu_NFZ);

/*Każda wizyta ma przypisanego pacjenta*/
alter table wizyty
add constraint fk_wizyta_pacjent foreign key (id_pacjenta)
references pacjenci(id_pacjenta);

/* Każdy przepisany lek musi isnieć w bazie leków*/
alter table przepisane_leki
add constraint fk_przepisaneleki_baza foreign key (id_leku)
references baza_lekow(id_leku);

/* Wszystkie przepisane jednorazowo leki muszą być przypisane do jednej wizyty*/
alter table przepisane_leki
add constraint fk_przepisaneleki_wizyta foreign key (id_wizyty)
references wizyty(id_wizyty); 


/*******WPISY TESTOWE******************************************************************************/
insert into oddzialy_NFZ(ID_oddzialu_NFZ, Nazwa)
values(1, 'Dolośląski');
insert into oddzialy_NFZ(ID_oddzialu_NFZ, Nazwa)
values(2, 'Kujawsko-Pomorski');

insert into baza_lekow(ID_leku,nazwa,postac,sklad,dawka,czy_refundowany,procent_refundacji,czy_na_recepte)
values (1,'Rutinoscorbin','tabletka powlekana','witamina C','50','n',null,'n');
insert into baza_lekow(ID_leku,nazwa,postac,sklad,dawka,czy_refundowany,procent_refundacji,czy_na_recepte)
values (2,'Euthyrox','tabletka','anabactriosunicos',150,'n',null,'t');


insert into lekarze(ID_lekarza, specjalizacja,tytul, imie, nazwisko, miejscowosc, kod_pocztowy, ulica, nr_domu,
                        nr_mieszkania, nr_tel, adres_email, nr_pwz)
values (0, 'Psychiatra', 'Doktor', 'Marek', 'Hoffman', 'Turek', '62700', 'Inna',23,1,876654827,'costam@wp.pl', 8765432);

insert into pacjenci(ID_pacjenta,ID_lekarza,PESEL,imie, nazwisko, plec, wiek, miejscowosc, kod_pocztowy, ulica, nr_domu,
                        nr_mieszkania, nr_tel, adres_email, oddzial_nfz, przebyte_choroby, przewlekle_choroby,
                         pobyty_w_szpitalu, zabiegi, szczepienia, uczulenia, obciazenia)
values (0, 0, 78965412354, 'Adam', 'Gilbert', 'M', 25, 'Wroc³aw',23456,'Dziwna',4,21,785412356,'costam@wp.pl', 1, 
        'świńka','niedoczynność tarczycy', 'Zapalenie płuc', 'BRAK', '20.05.1986 Różyczka', 'Laktoza', 'BRAK');
  
       
insert into przepisane_leki(id_wpisu,id_wizyty, id_leku,ilosc)
values (1,0,1,2);
          
insert into wizyty(id_wizyty,id_pacjenta, data_wizyty, wywiad, rozpoznanie, zalecenia, zlecone_badania, id_leki, zwolnienia)
values (0,0, TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'), 'historia choroby', 'diagnoza','siedziec w domu' ,'zrobic badanie krwi', 1, 'zwolniony z w-fu');
         




