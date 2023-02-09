from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from src.mutants.domain.mutant import Mutant
from src.building_blocks.errors import APIErrorMessage

router = APIRouter()

@router.post("/mutant")
async def validate_mutant(request: Request, dna: dict) -> JSONResponse:
    #VALIDADOR QUE DNA SEA ARRAY DE STR
    mutant = Mutant(dna)
    if not request.app.collection.find_one(mutant.id_):
        request.app.collection.insert_one(mutant)
    if mutant.is_mutant:
        return JSONResponse(content={"has_mutant": mutant.is_mutant}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={"has_mutant": mutant.is_mutant}, status_code=status.HTTP_403_FORBIDDEN)
