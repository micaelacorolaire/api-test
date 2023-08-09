--
--TOC entry 2 (class 3079 OID 62771)
--NAME:uuid-ossp;Type:EXTENSION;Schema: -;Owner
--
CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;
--
--TOC entry 3420(class 0 oid 0)
--dependencies:2
--name:EXTENSION"uuid-ossp";Type:Comment;Schema: -; Owner:
--
COMMENT ON EXTENSION "uuid-ossp"IS "generate universally unique identifiers(UUIDs);"

CREATE TABLE public.animals(
    id uuid DEFAULT public.uuid_generate_v4()NOT NULL,
    name character varying NOT NULL
);
CREATE TABLE public.login(
    id uuid DEFAULT public.uuid_generate_v4()NOT NULL,
    name character varying NOT NULL
);

CREATE TABLE public.race(
    id uuid DEFAULT public.uuid_generate_v4()NOT NULL;
    name character varying NOT NULL
);


CREATE TABLE public.species(
    id uuid DEFAULT public.uuid_generate_v4()NOT NULL;
    name character varying NOT NULL);


CREATE TABLE public.userdatacomplete(
    id uuid DEFAULT public.uuid_generate_v4()NOT NULL;
    name character varying NOT NULL);

CREATE TABLE public.animals(
    id uuid DEFAULT public.uuid_generate_v4()NOT NULL;
    id_race uuid NOT NULL,
    id_animal uuid  NOT NULL,
    age smallint NOT NULL,
    hair_color CHARACTER NOT NULL,
    eyes_color CHARACTER NOT NULL,
    weight CHARACTER NOT NULL,
    character CHARACTER NOT NULL,
    teeth CHARACTER NOT NULL,
    size INTERGER NOT NULL,
    diseases CHARACTER NOT NULL,
    disabilities CHARACTER NOT NULL,
    picturepath character varying NOT NULL,
);



CREATE TABLE public.login(
        id uuid DEFAULT public.uuid_generate_v4()NOT NULL,
        public.login(
                id uuid DEFAULT public.uuid_generate_v4()NOT NULL;
                google_id character varying NOT NULL,
                user_email character varying NOT NULL,
                user_password character varying NOT NULL,)
CREATE TABLE public.race(
        id uuid DEFAULT public.uuid_generate_v4()NOT NULL,
        race_name character varying NOT NULL;
)

CREATE TABLE public.species(
        id_species uuid DEFAULT public.uuid_generate_v4()NOT NULL,
        species_name character varying NOT NULL,

)

CREATE public.userdatacomplete(
        user_id uuid DEFAULT public.uuid_generate_v4()NOT NULL
        user_name character varying NOT NULL,
        user_lastname character varying NOT NULL,
        user_numberphone interger  varying NOT NULL,
        user_email character varying NOT NULL,
        other_phone interger varying NOT NULL,
        user_photo character varying NOT NULL , 
        user_age interger varying NOT NULL,
        where_live character varying NOT NULL,
        user_name character varying NOT NULL,


        )
)

ALTER TABLE only public.animals
    add constraint animals_pkey primary key (id_animal);

ALTER TABLE only public.login
    add constraint login_pkey primary_key (id_login);

ALTER TABLE only public.race
    add constraint race_pkey primary_key(id_race);

ALTER TABLE only public.species
    add constrain species_pkey primary_key(id_species);

ALTER TABLE only public.userdatacomplete
    add constrain userdatacomplete userdatacomplete_pkey primary_key(id_userdatacomplete);



ALTER TABLE ONLY animals
    add constrain id_animals_fkey foreing key (id_race) references public.race(race)
ALTER TABLE ONLY login
    add constrain id_login_fkey foreing key (??) references public.login(id_login)
                                             
ALTER TABLE ONLY race
    add constrain id_race_fkey foreign key (id_species) references public.race(species)

ALTER TABLE ONLY userdatacomplete
    add constrain user_id_pkey foreign key(user_id)references public.userdatacomplete(user_id)







