class Info:
    def __init__(self, header, link, **kwargs):
        self.header = header
        self.link = link

    ### add new attribute to the object
    ### attribute must start by "info"
    ### @param key: str
    ### @param value: any
    def add_new_attribute(self, key, value, filter):
        if filter:
            att_exists = False
            for att in dir(self):
                if att.startswith('info'):
                    if getattr(self, att) == value:
                        att_exists = True
                        break
                    
            if not att_exists:
                setattr(self, key, value)
        else:
            setattr(self, key, value)
    
    ### removes useless attributes of size < 2
    def clean_object(self):
        for att in dir(self):
            if att.startswith('info'):
                att_val = getattr(self, att)
                if len(att_val) < 4:
                    print(att_val)
                    delattr(self, att)

    ### returns our object informations as a Dict
    ###@ return info: Dict
    def to_dict(self):
        self.clean_object()
        return self.__dict__
