--liquibase formatted sql

--changeset chedv:create-sessions
CREATE TABLE sessions (
    id SERIAL NOT NULL,
    user_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES users (id)
);

--rollback DROP TABLE sessions;