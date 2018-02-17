class Artists:

    ''' Represents one artist who can sell art at a show'''

    NO_ID = None

    def __init__(self, firstName, lastName, update_ind, id=NO_ID):
        '''a new artist has no ID'''
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.update_ind = update_ind

    def set_id(self, id):
        self.id = id

    def __str__(self):

        id_str = '(no id)' if self.id == None else self.id

        template = 'id: {} First Name: {} Last Name: {} Update Ind: {}'
        return template.format(id_str, self.firstName, self.lastName, self.update_ind)

    def __repr__(self):
        return 'id: {} | First Name: {} | Last Name: {} | Update Ind: {}'\
            .format(self.id, self.firstName, self.lastName, self.update_ind)

    def __eq__(self, other):
        if isinstance(other, Artists):
            return self.id == other.id and self.firstName == other.firstName and self.lastName == other.lastName

    def __ne__(self, other):
        return not self == other
