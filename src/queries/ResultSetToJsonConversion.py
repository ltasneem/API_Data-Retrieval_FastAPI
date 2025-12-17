def personProfileJsonConversion(personProfileList : list):
  personProfileJsonList = []
  for obj in personProfileList:
    personProfileJsonList.append({
      'PersonId' : obj.PersonId
    })
  return personProfileJsonList
