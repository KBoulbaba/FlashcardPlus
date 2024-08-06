from abc import ABC, abstractmethod
from typing import List, Optional, Self

from src.domains.models import Category, Certification, Flashcard


class CertificationRepository(ABC):
    """
    Abstract base class for Certification repositories.

    This class defines abstract methods to retrieve all certifications and to retrieve a certification by name.

    Args:
        self: Instance of the CertificationRepository.

    Returns:
        For get_all: List of Certification objects.
        For get_by_name: Optional Certification object.

    """

    @abstractmethod
    def get_all(self: Self) -> List[Certification]:
        """
        Retrieve all certifications.

        This abstract method defines the behavior to retrieve all certifications.

        Returns:
            List of Certification objects.
        """
        return []

    @abstractmethod
    def get_by_name(self: Self, name: str) -> Optional[Certification]:
        """
        Retrieve a certification by name.

        This abstract method defines the behavior to retrieve a certification by its name.

        Args:
            name: Name of the certification to retrieve.

        Returns:
            Optional Certification object.
        """


class CategoryRepository(ABC):
    """
    Retrieve a certification by name.

    This abstract method defines the behavior to retrieve a certification by its name.

    Args:
        name: Name of the certification to retrieve.

    Returns:
        Optional Certification object.
    """

    @abstractmethod
    def get_all_by_cert_id(self: Self, cert_id: int) -> List[Category]:
        """
        Retrieve a certification by name.

        This abstract method defines the behavior to retrieve a certification by its name.

        Args:
            name: Name of the certification to retrieve.

        Returns:
            Optional Certification object.
        """
        return []

    @abstractmethod
    def get_by_name(self: Self, cert_id: int, name: str) -> Optional[Category]:
        """
        Retrieve a category by certification ID and name.

        This abstract method defines the behavior to retrieve a category by its certification ID and name.

        Args:
            cert_id: ID of the certification the category belongs to.
            name: Name of the category to retrieve.

        Returns:
            Optional Category object.
        """


class FlashcardRepository(ABC):
    """
    Retrieve all flashcards by category ID.

    This abstract method defines the behavior to retrieve all flashcards associated with a given category ID.

    Args:
        cat_id: ID of the category to retrieve flashcards for.

    Returns:
        List of Flashcard objects.
    """

    @abstractmethod
    def get_all_by_cat_id(self: Self, cat_id: int) -> List[Flashcard]:
        """
        Retrieve all flashcards by category ID.

        This abstract method defines the behavior to retrieve all flashcards associated with a given category ID.

        Args:
            cat_id: ID of the category to retrieve flashcards for.

        Returns:
            List of Flashcard objects.
        """
        return []
