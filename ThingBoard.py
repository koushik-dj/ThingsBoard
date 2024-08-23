from fastapi import FastAPI
import httpx
from pydantic import BaseModel

app = FastAPI()

class Temp(BaseModel):
    temperature: int

@app.post('/monitortemp')
async def monitortemp(temp: Temp):
    payload = {"temperature": temp.temperature}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://thingsboard.cloud/api/v1/7QJzklmW14FN7YTaREvb/telemetry",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

    return {"status_code": response.status_code, "response_text": response.text}

# @app.post('/device-connectivity/{deviceId}')
# def deviceCon(deiceId:int):
#     async with httpx.AsyncClient() as client:
#         response=await client.post(
#             ""
#         )