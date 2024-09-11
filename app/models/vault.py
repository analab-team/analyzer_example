from pydantic import BaseModel


class Vault(BaseModel):
    max_request_size: int
    max_output_size: int
