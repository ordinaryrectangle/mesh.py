from __future__ import annotations
import json
from pydantic import TypeAdapter
from requests import Session
import curlify
from typing import List, TYPE_CHECKING

from .dnevnik import Dnevnik
from .models import (
    MetricEntry,
    Role,
    SubsystemInfo,
    TestInfo,
)
from .utils import MISSING

__ALL__ = ['Client']

if TYPE_CHECKING:
    from typing import Any
    from pydantic import BaseModel, TypeAdapter

class Client:
    @property
    def _auth_data(self):
        return {'auth_token': self._token}

    def _validate(self, endpoint: str, model: type[BaseModel] | TypeAdapter, method='get', json: Any = MISSING, base_url: str = '', **kwargs):
        r = self._session.request(method, base_url + endpoint, json=json if json is not MISSING else (self._auth_data if method == 'post' else None), **kwargs)
        if r.status_code != 200:
            content = r.content
            try: content = content.decode()
            except: pass
            raise RuntimeError('status code invalid', r.status_code, content)
        if 'exam/rest/secure' in endpoint:
            print(curlify.to_curl(r.request))
            print(endpoint, r.content.decode())
        return getattr(model, 'model_validate_json' if hasattr(model, 'model_validate_json') else 'validate_json') \
            (r.content)

    def __init__(self, token):
        self._session = Session()
        self._token = token
        self._session.cookies.set('aupd_token', token)
        self._session.headers['Accept'] = 'application/json, text/plain, */*'
        self._session.headers['X-mes-subsystem'] = 'familyweb'
        self._session.headers['Authorization'] = f'Bearer {token}'

        self.dnevnik = Dnevnik(self)
        self.subsystems = self.dnevnik._validate('v1/allSubsystems/', TypeAdapter(List[SubsystemInfo]))
        self.metric = self.dnevnik._validate('api/notifications/events/v1/notification/event/type/metric', TypeAdapter(List[MetricEntry]), headers={'X-mes-subsystem': 'headerweb'})

    def get_test_info(self, test_id):
        # URL could be more flexible and use more config but that's for later
        profile = self.dnevnik.get_profile().profile
        if profile is None:
            raise RuntimeError('Profile is none, cant get test info')
        headers = {
            'User-Id': str(profile.user_id),
            'Profile-Id': str(profile.id),
            'Profile': json.dumps({
                'id': str(profile.id),
                'type': getattr(profile.type, 'value', 'student'),
                # too lazy to do these two, so hardcoded rn:
                'x-mes-globalRoleId': '1',
                'organizationIds': '[]',
            }),
            'Authorization': f'Bearer {self.dnevnik.sessions.authentication_token}',
        }
        return self._validate(f'/webtests/exam/rest/secure/challenge/{test_id}/info', TestInfo, base_url=self.config.library_stand_url, headers=headers)