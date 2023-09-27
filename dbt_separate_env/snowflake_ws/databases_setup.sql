create or replace database prod; 

use database prod;
create or replace schema my_schema;
create or replace table prod.my_schema.table_1 (
    id integer,
    first_name varchar, 
    last_name varchar
); 
copy into prod.my_schema.table_1 (id, first_name, last_name)
from 's3://dbt-tutorial-public/jaffle_shop_customers.csv'
file_format = (
    type = 'CSV'
    field_delimiter = ','
    skip_header = 1
    );

-- clone as test database
create or replace database test clone prod;