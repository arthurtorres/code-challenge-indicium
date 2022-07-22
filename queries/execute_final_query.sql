SELECT DISTINCT 
od.order_id,	
od.product_id,
od.unit_price,
od.quantity,	
od.discount,
o.customer_id,
o.employee_id,
o.order_date,
o.required_date,
o.shipped_date,
o.ship_via,
o.freight,
o.ship_name,
o.ship_address,
o.ship_city,
o.ship_region,
o.ship_postal_code,
o.ship_country

from db.order_details as od
INNER JOIN db.orders  as o
WHERE od.order_id =o.order_id