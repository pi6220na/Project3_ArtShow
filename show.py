class Show:
    ''' Represents one show of an art show collection'''

    NO_ID = None

    def __init__(self, showname, showlocation, showdate, update_ind, id=NO_ID):
        '''a new show has no ID'''
        self.id = id
        self.showName = showname
        self.showLocation = showlocation
        self.showDate = showdate
        self.update_ind = update_ind


    def set_id(self, id):
        self.id = id

    def __str__(self):
        id_str = '(no id)' if self.id is None else self.id

        template = 'id: {} Show Name: {} Show Location: {} Show Date: {} Update Ind: {}'
        return template.format(id_str, self.showName, self.showLocation, self.showDate, self.update_ind)

    def __repr__(self):
        return 'id: {} Show Name: {} Show Location: {} Show Date: {} Update Ind: {}' \
            .format(self.id, self.showName, self.showLocation, self.showDate, self.update_ind)

    def __eq__(self, other):
        if isinstance(other, Show):
            return self.id == other.id and self.showName == other.showName and \
                   self.showLocation == other.showLocation and self.showDate == other.showDate

    def __ne__(self, other):
        return not self == other
