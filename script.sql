create database tasks;
use tasks;

create table tasks (
id int auto_increment primary key,
description varchar(255) not null,
due_date date,
status ENUM('pending', 'completed') default 'pending'
);
