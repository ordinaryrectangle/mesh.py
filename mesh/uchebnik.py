from __future__ import annotations

from pydantic import TypeAdapter
from typing import List

from .subsystem import Subsystem
from .models import (
    ProfileInfo,
    Sessions,
    UserInfo,
    DnevnikConfig,
    Role,
)

class Uchebnik(Subsystem):
    BASE_URL = 'https://uchebnik.mos.ru/'

    # def get_profile(self) -> ProfileInfo:
    #     return self._validate('api/family/web/v1/profile', ProfileInfo)
    
    # def get_user_info(self) -> UserInfo:
    #     return self._validate('v1/oauth/userinfo', UserInfo)
    
    # def __init__(self, client):
    #     super().__init__(client)
    #     self.config: DnevnikConfig = self._validate('diary/mfConfig/config.json', DnevnikConfig)
    #     self.sessions: Sessions = self._validate('api/ej/acl/v1/sessions', Sessions, 'post', self._client._auth_data)
    #     self.roles = self._validate('v1/roles/allGlobal/', TypeAdapter(List[Role]))