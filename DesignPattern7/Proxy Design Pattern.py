from abc import ABC, abstractmethod
from typing import List

class DocumentStorage(ABC):
    @abstractmethod
    def upload_document(self, document: dict, user_credentials: dict) -> bool:
        pass

    @abstractmethod
    def download_document(self, document_id: str, user_credentials: dict) -> dict:
        pass

    @abstractmethod
    def edit_document(self, document_id: str, new_content: str, user_credentials: dict) -> bool:
        pass

    @abstractmethod
    def search_documents(self, query: str, user_credentials: dict) -> List[dict]:
        pass

class RealDocumentStorage(DocumentStorage):
    def upload_document(self, document: dict, user_credentials: dict) -> bool:
        # Загрузка документа
        print(f"Document uploaded: {document}")
        return True

    def download_document(self, document_id: str, user_credentials: dict) -> dict:
        # Скачивание документа
        return {"id": document_id, "content": "Document content"}

    def edit_document(self, document_id: str, new_content: str, user_credentials: dict) -> bool:
        # Редактирование документа
        print(f"Document {document_id} edited with new content: {new_content}")
        return True

    def search_documents(self, query: str, user_credentials: dict) -> List[dict]:
        # Поиск документов
        return [{"id": "1", "content": "Document 1"}, {"id": "2", "content": "Document 2"}]

# Прокси для системы хранения документов
class DocumentStorageProxy(DocumentStorage):
    def __init__(self, real_document_storage: DocumentStorage):
        self.real_document_storage = real_document_storage

    def upload_document(self, document: dict, user_credentials: dict) -> bool:
        if self.authenticate(user_credentials) and self.authorize(user_credentials):
            self.log_action("Upload document", user_credentials)
            return self.real_document_storage.upload_document(document, user_credentials)
        else:
            print("Failed to upload document: authentication or authorization failed.")
            return False

    def download_document(self, document_id: str, user_credentials: dict) -> dict:
        if self.authenticate(user_credentials) and self.authorize(user_credentials):
            self.log_action("Download document", user_credentials)
            return self.real_document_storage.download_document(document_id, user_credentials)
        else:
            print("Failed to download document: authentication or authorization failed.")
            return {}

    def edit_document(self, document_id: str, new_content: str, user_credentials: dict) -> bool:
        # Заглушка для метода edit_document
        pass

    def search_documents(self, query: str, user_credentials: dict) -> List[dict]:
        # Заглушка для метода search_documents
        pass

    def authenticate(self, user_credentials: dict) -> bool:
        # Простая проверка наличия учетных данных
        return user_credentials.get("username") and user_credentials.get("password")

    def authorize(self, user_credentials: dict) -> bool:
        # Простая проверка наличия роли
        return user_credentials.get("role") == "admin"

    def log_action(self, action: str, user_credentials: dict):
        # Простая запись в консоль
        print(f"Action '{action}' logged for user {user_credentials.get('username')}")


if __name__ == "__main__":
    real_storage = RealDocumentStorage()
    proxy_storage = DocumentStorageProxy(real_storage)

    # Пример загрузки документа
    document_to_upload = {"id": "123", "content": "Document content"}
    credentials = {"username": "admin", "password": "admin_password", "role": "admin"}
    upload_success = proxy_storage.upload_document(document_to_upload, credentials)
    if upload_success:
        print("Document uploaded successfully.")
    else:
        print("Failed to upload document.")

    # Пример скачивания документа
    document = proxy_storage.download_document("123", credentials)
    print("Downloaded document:", document)
