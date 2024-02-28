create database nithish;

create table employee(empid int,empname varchar(100),salary int);

select * from employee;

select empid,empname from employee;

insert into employee values(1001,'azar1',10000);

insert into employee values(1002,'azar2',20000);

insert into employee values(1003,'azar3',10000);

insert into employee values(1004,'azar4',20000);

insert into employee values(1005,'azar5',10000);

insert into employee values(1003,'azar3',10000);

insert into employee values(1001,'azar1',10000);

select distinct empid from employee;

select distinct empname from employee;

select * from employee where empid=1001;

select * from employee where salary>=20000;

select * from employee;

select * from employee where empid=1001 and empname="azar1";

select * from employee where empid=1001 and empname="azar2";

select * from employee where empid=1001 or empname="azar2";

select * from employee where not empid=1001;

select *  from employee order by salary;

select *  from employee order by salary asc;

select *  from employee order by salary desc;

update employee set empname='shiek',salary='50000' where empid=1001;

select * from employee;

delete from employee where empid=1001;

select min(salary) as Minimum from employee;

select max(salary) as MaxSalary from employee;

select count(salary) as Count from employee;

select sum(salary) as SumofSalary from employee;

select Avg(salary) as AvgSalary from employee;

-- Like Operators

select * from employee;

create table customers(customerid integer,customername varchar(100),contactname varchar(80),city varchar(100),postalcode integer,country varchar(100));

insert into customers values(1,'azar','Maria','hyd',1234,'India');

insert into customers values(2,'yamuna','Hanna','bang',1235,'India');

insert into customers values(3,'jasmeen','simpsom','hyd',1245,'India');

insert into customers values(4,'mohan','kumar','tax',2345,'usa');

select * from customers;

select * from customers where customername like 'a%';

select * from customers where customername like '%a';


select * from employee where salary in(10000,30000);

select * from customers where city in('uk','hyd');

select * from customers where city not in('uk','hyd');

select * from customers where customerid between 1 and 3;

select * from customers where customerid not between 1 and 3;

select * from customers where customerid between 1 and 3 AND city in('uk','hyd');

create table Persons(ID int NOT NULL PRIMARY KEY,LastName varchar(255)NOT NULL,FirstName varchar(100),Age int);

insert into Persons values(103,'','mohamed',31);

insert into Persons values(102,'mohan','raja',31);

insert into Persons values(101,'azar','mohamed',31);

select * from Persons;

create table orders(Orderid int not null,ordernumber int not null,ID int,primary key (Orderid),foreign key(ID) references Persons(ID));

insert into orders values(201,1001,101);

insert into orders values(202,1002,102);

select * from orders;

alter table Persons drop primary key;

alter table Persons add primary key(id);

alter table Persons add constraint PK_Person primary key(id,lastname);

drop database testdb;

drop table tablename;

alter table persons add email varchar(100);

select * from persons;

alter table persons drop column email;

alter table Persons modify column email int;