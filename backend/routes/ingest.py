from fastapi import APIRouter, UploadFile, File, HTTPException
import pdfplumber

router = APIRouter()

@router.post("/ingest")
async def ingest_file(file: UploadFile = File(...)):

    if file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="PDF ingestion is currently disabled.")
    
    try:
        with pdfplumber.open(file.file) as pdf:
            text = ""
            for page in pdf.page:
                text += page.extract_text() + ""

        return {"filename": file.filename, "content": text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the file: {str(e)}")