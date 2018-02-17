class Items:

    ''' Represents items for sale at an art show'''

    NO_ID = None

    def __init__(self, itemType, itemName, itemArtistId, update_ind, id=NO_ID):
        '''a new item has no ID'''
        self.id = id
        self.itemType = itemType
        self.itemName = itemName
        self.itemArtistId = itemArtistId
        self.update_ind = update_ind

    def set_id(self, id):
        self.id = id

    def __str__(self):

        id_str = '(no id)' if self.id is None else self.id

        template = 'id: {} Item Type: {} Item Name: {} Item Artist Id: {} Update Ind: {}'
        return template.format(id_str, self.itemType, self.itemName, self.itemArtistId, self.update_ind)

    def __repr__(self):
        return 'id: {} Item Type: {} Item Name: {} Item Artist Id: {} Update Ind: {}' \
            .format(self.id, self.itemType, self.itemName, self.itemArtistId, self.update_ind)

    def __eq__(self, other):
        if isinstance(other, Items):
            return self.id == other.id and self.itemType == other.itemType and self.itemName == other.itemName and \
                self.itemArtistId == other.itemArtistId

    def __ne__(self, other):
        return not self == other

