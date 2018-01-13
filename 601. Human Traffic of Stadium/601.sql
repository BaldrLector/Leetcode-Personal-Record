SELECT t.*
from stadium t
    left JOIN stadium p1 on t.id-1=p1.id
    left JOIN stadium p2 on t.id-2=p2.id
    left JOIN stadium n1 on t.id+1=n1.id
    left join stadium n2 on t.id+2=n2.id
WHERE (t.people>=100 and p1.people>=100 and p2.people>=100)
    or (t.people>=100 and n1.people>=100 and n2.people>=100)
    or (t.people>=100 and n1.people>=100 and p1.people>=100)
ORDER BY id;