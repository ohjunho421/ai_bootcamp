SELECT 
    animal_ins.name, 
    animal_ins.datetime
FROM 
    animal_ins
LEFT JOIN 
    animal_outs
ON 
    animal_ins.animal_id = animal_outs.animal_id
WHERE 
    animal_outs.animal_id IS NULL
ORDER BY 
    animal_ins.datetime
LIMIT 3