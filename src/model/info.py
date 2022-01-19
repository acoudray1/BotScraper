from typing import Dict


class Info:
    def __init__(self, header, link, **kwargs) -> None:
        self.header = header
        self.link = link

    ### add new attribute to the object
    ### attribute must start by "info"
    ### @param key: str
    ### @param value: any
    def add_new_attribute(self, key, value) -> None:
        setattr(self, key, value)

    ### returns our object informations as a Dict
    ###@ return info: Dict
    def to_dict(self) -> Dict:
        return self.__dict__
