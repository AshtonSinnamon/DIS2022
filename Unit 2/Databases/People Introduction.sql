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


