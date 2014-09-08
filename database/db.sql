CREATE TABLE post (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    descr VARCHAR(1000) NOT NULL,
    link VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    PRIMARY KEY(id)
);
alter table post convert to character set utf8 COLLATE utf8_unicode_ci;

CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	f_name VARCHAR(100) NOT NULL,
	l_name VARCHAR(100) NOT NULL,
	PRIMARY KEY(id)
);
alter table post convert to character set utf8 COLLATE utf8_unicode_ci;