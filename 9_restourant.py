

class Restourant():
    ''' new car'''

    def __init__(self, name, cuisine):

        self.rest_name = name.title()
        self.cuisine_type = cuisine.title()
        self.number_surved = 0

    def describe_restourant(self):

        print(f'the restaurant name : {self.rest_name} serve cuisiene type: {self.cuisine_type}')

    def set_num_served(self, num):

        self.number_surved = num
        print(f'number served: {self.number_surved}')

    def increment_number_served(self, increment):

        self.number_surved += increment
        print(f'number served: {self.number_surved}')


class IceCreamStand(Restourant):

    def __init__(self,name, cuisine='ice_cream'):
        super().__init__(name, cuisine)
        self.flavors = []


    def list_of_flavors(self):
        print(f"today we fave the following fvalors:")
        # print(self.flavors)
        for i in self.flavors:
            print(f"-{i}")



rest = Restourant('Ako', 'italian')
rest.describe_restourant()

rest.set_num_served(45)
rest.increment_number_served(7)

list_icecream = ['a','b','c']
ice_restourant = IceCreamStand('Big_iwo' )
ice_restourant.flavors = list_icecream
ice_restourant.describe_restourant()
ice_restourant.list_of_flavors()





