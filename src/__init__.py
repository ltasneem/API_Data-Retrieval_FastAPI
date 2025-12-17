import azure.functions as func
import memory_profiler
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import *
from fastapi import Body, Request, FastAPI
import fastapi
import time
import json
import pandas as pd
from fastapi_pagination import paginate, Page, add_pagination

from datetime import datetime, timedelta
from sqlalchemy.orm import clear_mappers

from models.request.*
from models.response.*
from core_common.*
from queries.ResultSetToJsonConversion import *
from query_builder import *
from payloadToRequestConversion import *


#instantiate memory profiler
profiler_logstream = memory_profiler.LogFile("memory_logs", True)

#call fastapi
app = fastapi.FastAPI(title="Azure Function to test DB data", debug=True, docs_url=None)

@app.post("/pprequests", name = "Get PersonProfile Data", response_model=Page[PersonProfileResponse])
async def personprofilerequests(code:str, payload: Any = Body(None)):
  payloadconverted = json.dumps(payload)
  request = personProfileToRequestConversion(payloadconverted)

  conn = engine.connect()
  map_personnel_personprofile(request,conn)

  personprofileResult = list[PersonProfileResponse] = personProfileQuery(request, conn)

  return paginate(PersonProfileResponseResult)

add_pagination(app)
