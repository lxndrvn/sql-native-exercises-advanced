/*
Write an SQL file here, which changes the schools table's schema with the followings:
- adds an address field (varchar), without the NOT NULL constraint
- modifies the 'name' column's name to 'code'
*/
ALTER TABLE schools
    ADD address VARCHAR(250);
ALTER TABLE schools
    RENAME name TO code;