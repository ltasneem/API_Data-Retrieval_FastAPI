from sqlalchemy import literal_column, select, or_
#import model classes
from models.personnel.GL_PersonProfile import *
from models.personnel.PersonProfileRequest import *
from models.personnel.PersonProfileResponse import *

#populate PersonProfile query based on request column values or flag values
def populate_PersonProfile_query(GL_PersonProfile_cls: GL_PersonProfile_cls):
  query = (select (GL_PersonProfile_cls))

## using flags
# try: 
#  query = query.join(cls, cls.DimSK == cls1.DimSK) 
# can use or_ for columns
# query.filter(cls.DimSK.in_(list))
# query = query.orderby(cls.DimSK)
# if DimSK is not None query=query.filter(literal_column("DimSK") == req.DimSK)
# excapt AttributeError:
#  pass
  query = query.distinct()
  return query
