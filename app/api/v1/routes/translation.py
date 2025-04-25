
from fastapi import APIRouter, File, UploadFile , HTTPException , status
from fastapi.responses import FileResponse

from app.core.law_translate import LawTranslator

router = APIRouter()

SUPPORTED_EXTENSIONS = {".docx"}


@router.get("/get-dictionary/{lng}")
async def get_lng_dictionary(
    lng: str
) -> dict:
    
    try:
        return LawTranslator().fetch_dictionary(lng=lng)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY , detail=f"{e}")

@router.post("/add-to-dictionary" , status_code=status.HTTP_201_CREATED)
async def add_word_translation(
    src_lng: str,
    word: str,
    translation: str,
):

    LawTranslator().add_to_dictionary(
        word=word,
        translation=translation,
        src_lng=src_lng,
    )

    return dict(
        word=word,
        translation=translation,
        src_lng=src_lng
    )

@router.post("/document-translation")
async def translate_document(
    document: UploadFile = File(...),
) -> FileResponse:
    filename = document.filename
    extension = filename[filename.rfind("."):].lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{extension}'. Only the following file types are supported: {', '.join(SUPPORTED_EXTENSIONS)}"
        )

    translated_document = await LawTranslator().translate_document(document)
    return translated_document
    