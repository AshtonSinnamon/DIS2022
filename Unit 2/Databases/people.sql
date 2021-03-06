select name, age, sex
from members
where sex = 'm'
and age > 50
order by name;

select name, age, sex, likes
from members
where likes = 'dancing'
order by 3 asc, 1 asc;

select name, sex, likes
from members
where likes = 'politics';

select name, likes, dislikes
from members
where likes = dislikes;

select name, age, sex
from members
where age between 20 and 40
and sex = 'f';

select name
from members
where name like 'a%';

select name
from members
where name like '_a%';

select *
from members
where likes like '%ing';

select *
from members
where likes = 'football' or likes = 'golf';

select * 
from members
where likes in ('football','golf')
order by earns  desc