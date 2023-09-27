with customers as (

    select
        id as customer_id,
        first_name, 
        last_name

    from {{ source('customers', 'table_1') }}

)

select * from customers