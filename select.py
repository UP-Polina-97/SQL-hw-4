select * from album where year_of_release = '2018';

select * from collection where year_of_release between '2018' and '2020';

select * from song where name like '%%my%%';

select * from song where duration > '3';

select name, duration from song where duration = (select max (duration) from song);

select * from artist  where name not like '% %';