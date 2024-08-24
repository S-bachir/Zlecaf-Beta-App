DROP TABLE IF EXISTS utilisateur CASCADE;
CREATE TABLE utilisateur (
	pseudo_user VARCHAR(10),
	mdp_hash VARCHAR,
	CONSTRAINT pk_pseudo_user PRIMARY KEY(pseudo_user)
);

DROP TABLE IF EXISTS super_utilisateur CASCADE;
CREATE TABLE super_utilisateur (
	pseudo_super_user VARCHAR(10),
	mdp_hash VARCHAR,
	CONSTRAINT pk_pseudo_super_user PRIMARY KEY(pseudo_super_user)
);





DROP TABLE IF EXISTS article CASCADE; 
CREATE TABLE article(
	id_article INT,
	nom_article VARCHAR,
	nb_avis_article INT,
	prix_article FLOAT,
	made_in_africa VARCHAR,
	site_origine VARCHAR,
	note_article  FLOAT,
	categorie_article VARCHAR,
	pays_origine_article VARCHAR,
	date_article DATE,
	CONSTRAINT pk_id_article PRIMARY KEY (id_article)
);

DROP TABLE IF EXISTS site CASCADE;
CREATE TABLE site(
	id_site INT,
	nom_site VARCHAR,
	url_site VARCHAR,
	type_site VARCHAR,
	pays_hebergement_site VARCHAR,
	CONSTRAINT pk_id_site PRIMARY KEY (id_site)
);

DROP TABLE IF EXISTS pays CASCADE;
CREATE TABLE pays(
	nom_pays VARCHAR,
	PIB_pays FLOAT,
	population_pays FLOAT,
	taux_demographique_pays FLOAT,
	taux_croissance_pays FLOAT,
	inflation_pays FLOAT,
	part_exportation_intra_pays FLOAT,
	exportation_intra_pays FLOAT,
	CONSTRAINT pk_nom_pays PRIMARY KEY (nom_pays)
);

DROP TABLE IF EXISTS compteur CASCADE; 
CREATE TABLE compteur(
	id_compteur INT,
	nom_compteur VARCHAR,
	compte INT,
	
	CONSTRAINT pk_id_compteur PRIMARY KEY (id_compteur)
);

DROP TABLE IF EXISTS maque_made_in_africa CASCADE; 
CREATE TABLE maque_made_in_africa(
	id_marque INT,
	nom_marque VARCHAR,
	production_en_afrique VARCHAR,
	categorie_marque VARCHAR,
	pays_de_production VARCHAR,
	
	CONSTRAINT pk_id_marque PRIMARY KEY (id_marque)
);


DROP TABLE IF EXISTS nn_dresseur_pokemon CASCADE;
CREATE TABLE  nn_dresseur_pokemon(
	id_poke INT,
	id_dresseur INT,
	CONSTRAINT pk_poke_dresseur PRIMARY KEY(id_poke, id_dresseur),
	CONSTRAINT fk_poke_adverse FOREIGN KEY (id_poke) REFERENCES pokemon (id_poke),
	CONSTRAINT fk_dresseur_pokemon FOREIGN KEY (id_dresseur) REFERENCES dresseur(id_dresseur)
);

