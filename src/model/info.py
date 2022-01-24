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
                if len(att_val.strip()) < 2:
                    delattr(self, att)

    ### renames attributes of the object
    def reorder_attributes(self):
        i = 0
        for att in dir(self):
            if att.startswith('info'):
                self.__dict__['u_info%s'%i] = self.__dict__.pop(att)
                i+=1

    ### returns our object informations as a Dict
    ###@ return info: Dict
    def to_dict(self):
        self.clean_object()
        self.reorder_attributes()
        return self.__dict__
