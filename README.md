# TestTask
 FinSTC Software LLC
 - 1)GET запросы:
   - http://localhost:5000//TestTask/api/v1.0/salesmen - все продавцы
   - http://localhost:5000//TestTask/api/v1.0/cars/1 - мышины по ID
 - 2)POST запрос:
   - http://localhost:5000//TestTask/api/v1.0/cars + json {"brand":"mazda"} - добовляет машину в список
 - 3)DELETE запрос:
   - http://localhost:5000//TestTask/api/v1.0/salesmen/1 - удалить продавца с ID 1
 - 4)PUT запрос:
   - http://localhost:5000//TestTask/api/v1.0/cars/1 + json {"brand":"mazda","sold":true} - машина с ID 1 переназвать и пометить как проданую
