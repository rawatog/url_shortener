from sqlalchemy.orm import Session
from . import models
import random, string

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def create_short_url(db: Session, original_url: str):
    # 1. Check if URL already exists
    existing = db.query(models.URL).filter(models.URL.original_url == original_url).first()
    if existing:
        return existing  # Return existing record

    # 2. Generate unique short_code
    while True:
        short_code = generate_short_code()
        if not db.query(models.URL).filter(models.URL.short_code == short_code).first():
            break

    db_url = models.URL(short_code=short_code, original_url=original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_original_url(db: Session, short_code: str):
    """
    Retrieve the original URL corresponding to a short code.
    Returns None if not found.
    """
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()