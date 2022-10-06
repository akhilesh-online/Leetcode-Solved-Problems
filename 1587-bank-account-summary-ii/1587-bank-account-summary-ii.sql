# Write your MySQL query statement below
select Users.name, SUM(Transactions.amount) as balance 
from Users LEFT Join Transactions on Users.account=Transactions.account
group by Transactions.account
having balance > 10000