-- DailyM8 creates --

create table Users
(
    Users_id     serial
        constraint Users_pk
            primary key,
    Users_name   varchar(60) not null,
    Users_bdate  date        not null,
    Users_gender char        not null,
    Users_email  varchar(60),
    Users_matricula varchar(15),
    Users_password varchar(30) not null
);

create table Reservas 
(
    res_id     serial
        constraint res_pk
            primary key,
    res_name   varchar(60) not null,
    res_date  date        not null,
    res_type char        not null,
    res_Users_name  varchar(60)        not null
);

create table Estabelecimento
(
    spot_id     serial
        constraint spot_pk
            primary key,
    spot_name   varchar(60) not null,
    spot_date  date        not null,
    spot_res_id int     not null,
    spot_type varchar(40)    not null
          
);

-- Equipamentos Em Cada Praia--

create table Epraia
(
    ep_id     serial
        constraint ep_pk
            primary key,
    ep_name   varchar(60) not null,
    ep_type char        not null
          
);

create table Estacionamento
(
    est_id     serial
        constraint est_pk
            primary key,
    est_name   varchar(60) not null,
    est_lugares int(500) ,
    est_Users_matricula varchar(15),
    est_type char    not null

          
);

