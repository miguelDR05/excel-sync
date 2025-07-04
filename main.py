from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import io

app = FastAPI(title="Service: Excel Importer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_excel(file: UploadFile = File(...)):
    contents = await file.read()
    excel_file = pd.read_excel(io.BytesIO(contents), sheet_name=None)  # lee todas las hojas
    preview = {}

    for sheet_name, df in excel_file.items():
        # Convertir inf y -inf en NaN
        df.replace([np.inf, -np.inf], np.nan, inplace=True)

        # Forzar todo a tipo objeto y reemplazar NaN por None
        cleaned_df = df.astype(object).where(pd.notnull(df), None)

        # Convertir a dict con valores válidos para JSON
        preview[sheet_name] = cleaned_df.head(5).to_dict(orient="records")

    return {"filename": file.filename, "sheets": preview}
