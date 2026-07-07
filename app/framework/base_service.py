"""
AADHINI ERP Enterprise
Base Service

Common business service for all ERP modules.
"""


class BaseService:

    def __init__(self, repository):
        self.repository = repository

    # ---------------------------------------------------------
    # Read
    # ---------------------------------------------------------

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, record_id):
        return self.repository.get_by_id(record_id)

    def count(self):
        return self.repository.count()

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    def delete(self, record_id):
        self.repository.delete_by_id(record_id)

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate_required(self, value, field_name):

        if value is None:
            raise ValueError(f"{field_name} is required.")

        if isinstance(value, str) and not value.strip():
            raise ValueError(f"{field_name} is required.")

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def success(self, message):

        return {
            "status": True,
            "message": message
        }

    def failure(self, message):

        return {
            "status": False,
            "message": message
        }