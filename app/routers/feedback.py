from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/feedback",
    tags=['Feedback']
)


@router.get("/", response_model=List[schemas.FeedbackOut])
def get_feedbacks(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    feedbacks = db.query(models.Feedback).all()
    return feedbacks


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Feedback)
def create_feedbacks(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    new_feedback = models.Feedback(**feedback.dict())
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)



    return new_feedback


@router.get("/{id}", response_model=schemas.FeedbackOut)
def get_feedback(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):


    feedback = db.query(models.Feedback).first()

    if not feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"feedback with id: {id} was not found")

    return feedback


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_feedback(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    feedback_query = db.query(models.Feedback).filter(models.Feedback.id == id)

    Feedback = feedback_query.first()

    if Feedback == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"feedback with id: {id} does not exist")

    if 5 != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    feedback_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


