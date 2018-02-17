class Sales:

    ''' Represents one sale of an item at an art show'''

    NO_ID = None

    def __init__(self, saleitemid, salequantity, saletotal, showid, update_ind, id=NO_ID):
        '''a new sales item has no ID'''
        self.id = id
        self.saleItemId = saleitemid
        self.saleQuantity = salequantity
        self.saleTotal = saletotal
        self.showId = showid
        self.update_ind = update_ind

    def set_id(self, id):
        self.id = id

    def __str__(self):

        id_str = '(no id)' if self.id is None else self.id

        template = 'id: {} Sale ItemId: {} Sale Quantity: {} Sale Total: {} ShowId: {} Update Ind: {}'
        return template.format(id_str, self.saleItemId, self.saleQuantity, self.saleTotal, self.showId, self.update_ind)

    def __repr__(self):
        return 'id: {} Sale ItemId: {} Sale Quantity: {} Sale Total: {} ShowId: {} Update Ind: {}' \
            .format(self.id, self.saleItemId, self.saleQuantity, self.saleTotal, self.showId, self.update_ind)

    def __eq__(self, other):
        if isinstance(other, Sales):
            return self.id == other.id and self.saleItemId == other.saleItemId and \
                   self.saleQuantity == other.saleQuantity and self.saleTotal == other.saleTotal and \
                   self.showId == other.showId

    def __ne__(self, other):
        return not self == other
