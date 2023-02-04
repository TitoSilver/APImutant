from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse, Response


from src.mutants.domain.mutant import Mutant
from src.building_blocks.errors import APIErrorMessage
#from src.clients.application.client_service import ClientService

router = APIRouter()


@router.post("/mutant")
async def validate_mutant(dna: dict) -> JSONResponse:
    mutant = Mutant(dna)
    if mutant.has_mutant():
        return JSONResponse(content={"has_mutant": mutant.status}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={"has_mutant": mutant.status}, status_code=status.HTTP_403_FORBIDDEN)
