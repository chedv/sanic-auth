--liquibase formatted sql

--changeset create.sessions:1
CREATE TABLE sessions (
    id SERIAL NOT NULL,
    user_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES users (id)
);
