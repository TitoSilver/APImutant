import uvicorn

from fastapi import FastAPI
#from fastapi.openapi.utils import get_openapi
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from src.mutants.controller import router as mutant_router
from src.building_blocks.db import get_mongo_database
from src.building_blocks.errors import APIErrorMessage, DomainError, RepositoryError, ResourceNotFound

from src.mutants.infrastructure.db_connection import DBMuntant

app = FastAPI()
app.include_router(mutant_router)

@app.exception_handler(DomainError)
async def domain_error_handler(request: Request, exc: DomainError) -> JSONResponse:
    error_msg = APIErrorMessage(type=exc.__class__.__name__, message=f"Oops! {exc}")
    return JSONResponse(
        status_code=400,
        content=error_msg.dict(),
    )

@app.on_event("startup")
def startup_db_client():
    app.database = get_mongo_database()
    app.collection = DBMuntant(app.database)
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.database.close()

@app.exception_handler(ResourceNotFound)
async def resource_not_found_handler(request: Request, exc: ResourceNotFound) -> JSONResponse:
    error_msg = APIErrorMessage(type=exc.__class__.__name__, message=str(exc))
    return JSONResponse(status_code=404, content=error_msg.dict())


@app.exception_handler(RepositoryError)
async def repository_error_handler(request: Request, exc: RepositoryError) -> JSONResponse:
    error_msg = APIErrorMessage(
        type=exc.__class__.__name__, message="Oops! Something went wrong, please try again later..."
    )
    return JSONResponse(
        status_code=500,
        content=error_msg.dict(),
    )


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
