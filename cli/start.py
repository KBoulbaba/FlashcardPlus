from src.adapters.db.sqlite_adapters import (
    SqliteCategoryRepository,
    SqliteCertificationRepository,
    SqliteFlashcardRepository,
)
from src.adapters.ui.tk_adapters import TkinterUI
from src.application.db_service import DbService
from src.application.flashcard_service import FlashcardService


def main():
    db_url = "sqlite:///flashcards.db"
    cert_repo = SqliteCertificationRepository(db_url)
    cat_repo = SqliteCategoryRepository(db_url)
    flashcard_repo = SqliteFlashcardRepository(db_url)

    db_service = DbService(cert_repo, cat_repo, flashcard_repo)
    print(db_service.cert_repo.get_all())
    flashcard_service = FlashcardService(flashcard_repo)

    ui = TkinterUI(flashcard_service, db_service)
    ui.run()


if __name__ == "__main__":
    main()
