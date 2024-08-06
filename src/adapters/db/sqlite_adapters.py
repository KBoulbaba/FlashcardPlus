from typing import List, Optional, Self

from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine, select

from src.domains.models import Category, Certification, Flashcard
from src.domains.repositories import CategoryRepository, CertificationRepository, FlashcardRepository


class SqliteCertificationRepository(CertificationRepository):
    """
    SQLite implementation of CertificationRepository.

    This class provides methods to interact with SQLite database for certifications.

    Args:
        db_url: URL to connect to the SQLite database.

    Returns:
        For get_all: List of Certification objects.
        For get_by_name: Optional Certification object.
    """

    def __init__(self: Self, db_url: str):
        """
        SQLite implementation of CertificationRepository.

        This class provides methods to interact with SQLite database for certifications.

        Args:
            db_url: URL to connect to the SQLite database.

        Returns:
            For get_all: List of Certification objects.
            For get_by_name: Optional Certification object.
        """
        self.engine: Engine = create_engine(db_url)
        SQLModel.metadata.create_all(self.engine)

    def get_all(self: Self) -> List[Certification]:
        """
        Initialize the database engine.

        This function creates the database engine using the provided URL.

        Args:
            db_url: URL to connect to the database.
        """
        with Session(self.engine) as session:
            return session.exec(select(Certification)).all()

    def get_by_name(self: Self, name: str) -> Optional[Certification]:
        """
        Retrieve all certifications.

        This function fetches all certification records from the database.

        Returns:
            List of Certification objects.
        """
        with Session(self.engine) as session:
            return session.exec(select(Certification).where(Certification.name == name)).first()


class SqliteCategoryRepository(CategoryRepository):
    """
    Retrieve a certification by name.

    This function fetches a certification record from the database based on the provided name.

    Args:
        name: Name of the certification to retrieve.

    Returns:
        Optional Certification object.
    """

    def __init__(self: Self, db_url: str):
        """
        SQLite implementation of CategoryRepository.

        This class provides methods to interact with SQLite database for categories.

        Args:
            db_url: URL to connect to the SQLite database.

        Returns:
            For get_all_by_cert_id: List of Category objects.
            For get_by_name: Optional Category object.
        """

        self.engine: Engine = create_engine(db_url)
        SQLModel.metadata.create_all(self.engine)

    def get_all_by_cert_id(self: Self, cert_id: int) -> List[Category]:
        """
        Retrieve all categories by certification ID.

        This function fetches all category records from the database associated with a given certification ID.

        Args:
            cert_id: ID of the certification to retrieve categories for.

        Returns:
            List of Category objects.
        """
        with Session(self.engine) as session:
            return session.exec(select(Category).where(Category.cert_id == cert_id)).all()

    def get_by_name(self: Self, cert_id: int, name: str) -> Optional[Category]:
        """
        Retrieve a category by certification ID and name.

        This function fetches a category record from the database based on the provided certification ID and name.

        Args:
            cert_id: ID of the certification the category belongs to.
            name: Name of the category to retrieve.

        Returns:
            Optional Category object.
        """
        with Session(self.engine) as session:
            return session.exec(select(Category).where(Category.cert_id == cert_id, Category.name == name)).first()


class SqliteFlashcardRepository(FlashcardRepository):
    """
    Retrieve a category by certification ID and name.

    This function fetches a category record from the database based on the provided certification ID and name.

    Args:
        cert_id: ID of the certification the category belongs to.
        name: Name of the category to retrieve.

    Returns:
        Optional Category object.
    """

    def __init__(self: Self, db_url: str):
        """
        SQLite implementation of FlashcardRepository.

        This class provides methods to interact with SQLite database for flashcards.

        Args:
            db_url: URL to connect to the SQLite database.

        Returns:
            For get_all_by_cat_id: List of Flashcard objects.
        """
        self.engine: Engine = create_engine(db_url)
        SQLModel.metadata.create_all(self.engine)

    def get_all_by_cat_id(self, cat_id: int) -> List[Flashcard]:
        """
        Initialize the database engine.

        This function creates the database engine using the provided URL.

        Args:
            db_url: URL to connect to the database.
        """
        with Session(self.engine) as session:
            return session.exec(select(Flashcard).where(Flashcard.cat_id == cat_id)).all()
