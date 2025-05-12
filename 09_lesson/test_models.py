import pytest
from models import Base, SessionLocal, Subject


# Настройка подключения к тестовой базе данных
@pytest.fixture(scope='module')
def setup_database():
    # Создание таблиц перед запуском тестов
    Base.metadata.create_all(bind=SessionLocal().bind)
    yield
    # Удаление таблиц после завершения всех тестов
    Base.metadata.drop_all(bind=SessionLocal().bind)


@pytest.fixture()
def db_session(setup_database):
    # Создание новой сессии для каждого теста
    session = SessionLocal()
    yield session
    session.rollback()  # Откат изменений после каждого теста
    session.close()


def test_add_subject(db_session):
    subject_title = "Physics"
    new_subject = Subject(subject_title=subject_title)

    db_session.add(new_subject)
    db_session.commit()

    assert new_subject.subject_id is not None  # Проверяем, что ID был присвоен


def test_update_subject(db_session):
    old_title = "Physics"
    new_title = "Chemistry"

    subject = (db_session.query(Subject)
               .filter(Subject.subject_title == old_title).first())

    if subject:
        subject.subject_title = new_title
        db_session.commit()

        updated_subject = (db_session.query(Subject)
                           .filter(Subject.subject_title == new_title).first())
        # Проверяем, что предмет был обновлён
        assert updated_subject is not None


def test_delete_subject(db_session):
    subject_title = "Chemistry"

    subject = (db_session.query(Subject)
               .filter(Subject.subject_title == subject_title).first())

    if subject:
        db_session.delete(subject)
        db_session.commit()

        deleted_subject = (db_session.query(Subject)
                           .filter(Subject.subject_title == subject_title).first())
        # Проверяем, что предмет был удалён
        assert deleted_subject is None


if __name__ == "__main__":
    pytest.main()
