import argparse
import csv
from pathlib import Path
from typing import List

from sqlmodel import Session, create_engine

from src.adapters.db.sqlite_adapters import (
    SqliteCategoryRepository,
    SqliteCertificationRepository,
    SqliteFlashcardRepository,
)
from src.domains.models import Category, Certification, Flashcard


def load_data(db_url: str, resources_path: str):
    """
    Retrieve all flashcards by category ID.

    This function fetches all flashcard records from the database associated with a given category ID.

    Args:
        cat_id: ID of the category to retrieve flashcards for.

    Returns:
        List of Flashcard objects.
    """

    engine = create_engine(db_url)
    cert_repo = SqliteCertificationRepository(db_url)
    cat_repo = SqliteCategoryRepository(db_url)
    SqliteFlashcardRepository(db_url)

    with Session(engine) as session:
        resources_dir = Path(resources_path)
        process_cert_dirs(resources_dir, session, cert_repo, cat_repo)


def process_cert_dirs(resources_dir, session, cert_repo, cat_repo):
    """
    Process certification directories.

    This function iterates over directories, extracts certification data, and populates the database with certifications and categories.

    Args:
        resources_dir: Directory containing certification directories.
        session: Database session.
        cert_repo: Certification repository.
        cat_repo: Category repository.

    Returns:
        None.
    """
    for cert_dir in resources_dir.iterdir():
        if cert_dir.is_dir() and cert_dir.name != "corrections":
            cert_name: str = cert_dir.name

            cert: List[Certification] = cert_repo.get_by_name(cert_name)
            if not cert:
                cert = Certification(name=cert_name)
                session.add(cert)
                session.commit()

            cert_id: int = cert.id

            process_csv_files(cert_dir, session, cert_id, cat_repo)


def process_csv_files(cert_dir, session, cert_id, cat_repo):
    """
    Process certification directories.

    This function iterates over directories, extracts certification data, and populates the database with certifications and categories.

    Args:
        resources_dir: Directory containing certification directories.
        session: Database session.
        cert_repo: Certification repository.
        cat_repo: Category repository.

    Returns:
        None.
    """
    for file_path in cert_dir.glob("*.csv"):
        cat_name: str = file_path.stem

        cat: Category | None = cat_repo.get_by_name(cert_id, cat_name)
        if not cat:
            cat = Category(cert_id=cert_id, name=cat_name)
            session.add(cat)
            session.commit()

        cat_id: int = cat.id

        with file_path.open(newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2:
                    question, answer = row[0], row[1]
                    flashcard = Flashcard(cat_id=cat_id, question=question, answer=answer)
                    session.add(flashcard)
            session.commit()


def main():
    parser = argparse.ArgumentParser(description="Load flashcard data from CSV files into the database.")
    parser.add_argument("db_url", help="URL of the SQLite database")
    parser.add_argument("resources_path", help="Path to the directory containing the certification folders")

    args = parser.parse_args()
    load_data(args.db_url, args.resources_path)


if __name__ == "__main__":
    main()
