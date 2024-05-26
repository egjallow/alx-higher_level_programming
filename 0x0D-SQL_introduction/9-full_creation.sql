-- list create a second table and insert into it
CREATE TABLE if NOT EXISTS second_table(
	id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	score INT NOT NULL);

INSERT INTO second_table VALUES(1, 'John', 10);
INSERT INTO second_table VALUES(2, 'Alex', 3);
INSERT INTO second_table VALUES(3, 'Bob', 14);
INSERT INTO second_table VALUES(4, 'George', 8);
