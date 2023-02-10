from typing import List

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from src.mutants.domain.mutant import Mutant
from src.mutants.infrastructure.validate_dna import has_number
from src.building_blocks.errors import APIErrorMessage

router = APIRouter()

@router.post("/mutant",
             responses={400: {"model": APIErrorMessage}, 500: {"model": APIErrorMessage}})
async def validate_mutant(request: Request, dna: List[str]) -> JSONResponse:
    #VALIDADOR QUE DNA SEA ARRAY DE STR
    if not isinstance(dna,list) or has_number(dna):
        return JSONResponse(content={'msg':'Oops!, value is not a valid list', 'type': 'type_error.list'}, status_code=status.HTTP_400_BAD_REQUEST)
    mutant = Mutant(dna)
    if not request.app.collection.find_one(mutant.id_):
        request.app.collection.insert_one(mutant)
    if mutant.is_mutant:
        return JSONResponse(content={"has_mutant": mutant.is_mutant}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={"has_mutant": mutant.is_mutant}, status_code=status.HTTP_403_FORBIDDEN)

@router.get('/stats',
            responses={400: {"model": APIErrorMessage}, 500: {"model": APIErrorMessage}})
async def get_stats(request: Request) -> JSONResponse:
    count_mutant_dna = request.app.collection.count_documents({'is_mutant': True})
    count_human_dna = request.app.collection.count_documents({'is_mutant': False})
    if not count_human_dna:
        #count_human_dna are validated, so as not to generate a division by 0 exception
        count_human_dna = 1
    return JSONResponse(
        content={'count_mutant_dna':count_mutant_dna,
                 'count_human_dna':count_human_dna,
                 'ratio':count_mutant_dna / count_human_dna},
        status_code=status.HTTP_200_OK
    )
