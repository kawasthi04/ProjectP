from fastapi import APIRouter, Header, HTTPException
import requests
from app.config import settings

router = APIRouter()

@router.get("/verify")
def verify_user(authorization: str = Header(...)):
    """Verify Clerk JWT"""
    headers = {"Authorization": authorization}
    r = requests.get(f"{settings.CLERK_API_URL}/v1/users/me", headers=headers)
    if r.status_code != 200:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return r.json()
