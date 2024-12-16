SELECT animal_id, name, if(sex_upon_intake in('Neutered Male', 'Spayed Female'), 'O', 'X') as 중성화
from animal_ins