from fastapi import FastAPI   #which is the web framework we’re using to build your backend.
from backend.routes import ingest #importing the ingest router from the routes package.

print("✅ ingest route loaded successfully")
app = FastAPI() #This line creates the actual app — it’s like turning on the engine.
app.include_router(ingest.router)  #This line tells the app to use the routes defined in the ingest router. 

@app.get("/") #So when someone goes to https://your-app.onrender.com/, this function will run.
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}