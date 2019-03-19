/*alter table pacjenci
add constraint fk_pacjent_oddzial foreign key (oddzial_nfz)
references oddzialy_nfz(id_oddzialu);*/

alter table oddzialy_nfz
add constraint pk_oddzialy primary key (id_oddzialu);
