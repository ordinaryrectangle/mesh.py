from __future__ import annotations
from .utils import MISSING, get_missable

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Any
    from pydantic import BaseModel, TypeAdapter
    from .client import Client

__ALL__ = ['Subsystem'] 

class Subsystem:
    BASE_URL: str | None = None
    HEADERS: dict | None = None
    def _validate(self, endpoint: str, model: type[BaseModel] | TypeAdapter, method='get', json: Any = MISSING, base_url: str | None | type[MISSING] = MISSING, headers=HEADERS, **kwargs):
        return self._client._validate(endpoint, model, method, json, get_missable(base_url, self.BASE_URL) or '', headers=headers, **kwargs)

    def __init__(self, client, base_url = None):
        if base_url is not None:
            self.BASE_URL = base_url # pyright:ignore[reportConstantRedefinition]
        self._client: Client = client