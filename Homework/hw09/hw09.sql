create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
select name, size FROM dogs, sizes WHERE height > min AND height <= max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
select child FROM parents, dogs WHERE parent = name ORDER by -height;


-- Sentences about siblings that are the same size
with
  siblings as (
    select a.child, b.child from parents as a, parents as b
    WHERE a.parent = b.parent;
    )
with matching_siblings as (
    select a, b from siblings, size_of_dogs as a, siblings, size_of_dogs as b
    WHERE a.size = b.size;
  )
create table sentences as
select * FROM matching_siblings;



-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
with
  stack_recur(dogs, total, n) as (
    select name, height from dogs union);
    select dogs || ',' || name, total + height, n, height from dogs;
create table stacks as
select dogs, total from stack_recur;
  where n = 4 and total >= 170 order by total;


create table tallest as
select max(height), name from dogs group by height/10 having count(name) > 1;


-- All non-parent relations ordered by height difference
create table non_parents as
select "REPLACE THIS LINE WITH YOUR SOLUTION";


