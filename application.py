from fastapi import FastAPI, Request
#from fastapi.responses import FileResponse
from datetime import datetime
# from dotenv import load_dotenv
# import psycopg2
import os


# load_dotenv()
# conn_str = os.getenv("CONN_STR")

application = FastAPI()


# @application.get("/track/{email_id}.png")
# async def track_email(email_id: str, request: Request):
#     ip = request.client.host
#     user_agent = request.headers.get("user-agent", "unknown")
#     timestamp = datetime.utcnow()

#     conn = psycopg2.connect(conn_str)
#     cur = conn.cursor()
#     cur.execute("""
#         INSERT INTO email_tracking (email_id, ip_address, user_agent, timestamp)
#         VALUES (%s, %s, %s, %s)
#     """, (email_id, ip, user_agent, timestamp))
#     conn.commit()
#     cur.close()
#     conn.close()

#     return FileResponse("pixel.png", media_type="image/png")


@application.get("/")
async def root():
    return {"message": "Email tracking service 2 is running."}


#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run("application:application", host="0.0.0.0", port=5000, reload=True)# dev
    #uvicorn.run(application, host="0.0.0.0", port=5000)# prod


