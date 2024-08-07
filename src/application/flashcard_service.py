from typing import List

from src.domains.models import Flashcard
from src.domains.repositories import FlashcardRepository


class FlashcardService:
    """
    A service class for managing flashcards, utilizing a FlashcardRepository for data operations.

    Methods:
    - get_flashcards: Retrieves all flashcards for a given category ID.

    """

    def __init__(self, flashcard_repo: FlashcardRepository):
        """
        Initializes the FlashcardService with a FlashcardRepository instance for managing flashcards.

        """
        self.flashcard_repo = flashcard_repo

    def get_flashcards(self, cat_id: int) -> List[Flashcard]:
        """
        Retrieves all flashcards for a given category ID using the associated FlashcardRepository.

        Args:
        - cat_id: Integer representing the category ID.

        Returns:
        - List of Flashcard objects.
        """
        return self.flashcard_repo.get_all_by_cat_id(cat_id)
