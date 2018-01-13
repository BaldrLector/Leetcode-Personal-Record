
SELECT *
from cinema c
WHERE (
    c.id%2=1 AND c.description not like "boring" 
)
ORDER BY c.rating DESC