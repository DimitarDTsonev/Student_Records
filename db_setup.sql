CREATE DATABASE student_records;
USE student_records;
CREATE TABLE students (
  id              INT AUTO_INCREMENT PRIMARY KEY,
  faculty_number  VARCHAR(10) UNIQUE NOT NULL,
  first_name      VARCHAR(100) NOT NULL,
  last_name       VARCHAR(100) NOT NULL,
  email           VARCHAR(120) UNIQUE NOT NULL
  address         VARCHAR(255) NOT NULL,
  city            VARCHAR(100) NOT NULL,
  state           VARCHAR(100) NOT NULL,
  phone           VARCHAR(20)  UNIQUE NOT NULL;
);