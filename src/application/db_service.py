from typing import List, Optional, Self

from src.domains.models import Category, Certification, Flashcard
from src.domains.repositories import CategoryRepository, CertificationRepository, FlashcardRepository


class DbService:
    """
    A service class for interacting with different repositories to retrieve certifications, categories, and flashcards.

    Methods:
    - get_certifications: Retrieves all certifications.
    - get_categories: Retrieves all categories for a given certification ID.
    - get_flashcards: Retrieves all flashcards for a given category ID.

    Args:
    - cert_repo: CertificationRepository instance for certification operations.
    - cat_repo: CategoryRepository instance for category operations.
    - flashcard_repo: FlashcardRepository instance for flashcard operations.

    Returns:
    - List of Certification objects for get_certifications.
    - List of Category objects for get_categories.
    - List of Flashcard objects for get_flashcards.
    """

    def __init__(
        self: Self,
        cert_repo: CertificationRepository,
        cat_repo: CategoryRepository,
        flashcard_repo: FlashcardRepository,
    ):
        """
        Initializes the DbService with instances of CertificationRepository, CategoryRepository, and FlashcardRepository.

        Args:
        - cert_repo: CertificationRepository instance for certification operations.
        - cat_repo: CategoryRepository instance for category operations.
        - flashcard_repo: FlashcardRepository instance for flashcard operations.
        """
        self.cert_repo = cert_repo
        self.cat_repo = cat_repo
        self.flashcard_repo = flashcard_repo

    def get_certifications(self: Self) -> List[Certification]:
        """
        Retrieves all certifications using the CertificationRepository instance.

        Returns:
        - List of Certification objects.
        """
        return self.cert_repo.get_all()

    def get_certification_by_name(self: Self, name: str) -> Certification | None:
        """
        Retrieves a certification by name using the CertificationRepository instance.

        Args:
        - name: String representing the name of the certification.

        Returns:
        - Certification object if found, else None.
        """
        return self.cert_repo.get_by_name(name)

    def get_categories(self: Self, cert_id: int) -> List[Category]:
        """
        Retrieves all categories for a given certification ID using the CategoryRepository instance.

        Args:
        - cert_id: Integer representing the certification ID.

        Returns:
        - List of Category objects.
        """
        self.categories = self.cat_repo.get_all_by_cert_id(cert_id)
        return self

    def get_by_name_category(self: Self, name: str) -> Optional[Category]:
        return next(iter(filter(lambda x: x.name == name, self.categories)), None)

    def get_flashcards(self, cat_id: int) -> List[Flashcard]:
        """
        Retrieves all flashcards for a given category ID using the FlashcardRepository instance.

        Args:
        - cat_id: Integer representing the category ID.

        Returns:
        - List of Flashcard objects.
        """
        return self.flashcard_repo.get_all_by_cat_id(cat_id)
