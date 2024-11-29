# Write your MySQL query statement below
select customer_id, count(customer_id) as count_no_trans from
(select customer_id from
Visits where visit_id not in 
(select visit_id from Transactions )
)as t2
group by customer_id;