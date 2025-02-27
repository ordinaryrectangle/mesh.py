from __future__ import annotations

class MISSING:
    pass
    # def __eq__(self, value: object, /):
    #     return isinstance(value, MISSING)
    
    # def __ne__(self, value: object, /) -> bool:
    #     return not self.__eq__(value)

def get_missable(obj: str | MISSING, default):
    return default if obj == MISSING else obj