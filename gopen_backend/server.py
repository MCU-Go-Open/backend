from fastapi import FastAPI
import uvicorn

import os,sys
sys.path.append(os.path.dirname(__file__))

from routers import tests,auth,comment,course


app = FastAPI()
app.include_router(tests.router,prefix="/test",tags=["test"])
app.include_router(course.router,prefix="/course",tags=["course"])
app.include_router(auth.router,prefix="/auth",tags=["auth"])
app.include_router(comment.router,prefix="/comment",tags=["comment"])

@app.get("/PING")
def ping() -> str:
   return "PONG"

if __name__ == "__main__":
   uvicorn.run(app, host='0.0.0.0', port=8080)
