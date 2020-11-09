--liquibase formatted sql

--changeset chedv:create-users
CREATE TABLE users (
    id SERIAL NOT NULL,
    email VARCHAR NOT NULL,
    username VARCHAR NOT NULL,
    password_hash VARCHAR(64) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (email),
    UNIQUE (username)
);

--rollback DROP TABLE users;