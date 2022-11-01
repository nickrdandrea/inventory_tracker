from sqlalchemy.exc import SQLAlchemyError

from app import db

class CoreDao:

    @staticmethod
    def safe_commit() -> bool:
        try:
            db.session.commit()
            return True
        except SQLAlchemyError as error:
            db.session.rollback()
            return False
