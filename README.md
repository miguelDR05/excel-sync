# 📊 Excelsync - Servicio de carga y conversión de Excel a SQL

**Excelsync** es un microservicio desarrollado con **FastAPI** que permite subir archivos Excel o Google Sheets y convertirlos en estructuras de base de datos SQL de forma automática o personalizada.

Este servicio es ideal para la carga masiva de datos estructurados, la construcción rápida de bases de datos a partir de hojas de cálculo y la integración en pipelines ETL u otros sistemas backend.

---

## 🚀 Características principales

- ✅ Soporte para archivos `.xlsx`, `.xls` y Google Sheets.
- 🔄 Conversión automática de hojas a tablas SQL.
- ⚙️ Configuración manual (custom) para:
  - Definir entidades
  - Rutas y relaciones entre tablas
  - Estructuras condicionales según datos
- 🔌 Integración con motores SQL como MySQL, PostgreSQL y SQL Server.
- 🧱 Arquitectura basada en **servicios** / **microservicios** con FastAPI.
- 🔐 Listo para integrarse con APIs RESTful y sistemas distribuidos.

---

## 🛠️ Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/) para validación de datos
- [SQLAlchemy](https://www.sqlalchemy.org/) para interacción con bases de datos
- [Pandas](https://pandas.pydata.org/) para procesamiento de hojas Excel
- [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/) (opcional) para Excel
- [Google Sheets API](https://developers.google.com/sheets/api) (opcional)

---

## ⚙️ Instalación rápida

```bash
https://github.com/miguelDR05/excel-sync.git
cd excel-sync
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
