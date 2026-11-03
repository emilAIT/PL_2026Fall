from collections import defaultdict

class Listing:
    def __init__(self, make, price, year):
        self.make = make
        self.price = price
        self.year = year
    
class EventBus:
    def __init__(self):
        self.subscribers = defaultdict(list)
    
    def subscribe(self, event, observer):
        self.subscribers[event].append(observer)
    
    def unsubscribe(self, event, observer):
        self.subscribers[event].remove(observer)

    def publish(self, event, listing):
        for i in self.subscribers[event]:
            i.update(event, listing)


class Observer:
    def update(self, event, listing):
        pass


class SavedSearches(Observer):
    def __init__(self, user, make, price_from, price_to):
        self.user = user
        self.make = make
        self.price_from = price_from
        self.price_to = price_to

    def update(self, event, listing):
        if self.make == listing.make and self.price_from <= listing.price <= self.price_to:
            print(f'sending notifaction to {self.user} on {self.make} which matched {listing.make}, {listing.price}')

class PriceDrop(Observer):
    def __init__(self, user, make):
        self.user = user
        self.make = make

    def update(self, event, listing):
        if self.make == listing.make:
            print(f'price change notification email: {self.user} price changed for {listing.make} to {listing.price}')

class TelegramNofication(Observer):
    pass


eventbus = EventBus()

akyl = SavedSearches('emil','bmw', 5000, 8000)
iskender = SavedSearches('iskender', 'toyota', 1000, 5000)
altynai = SavedSearches('altynai', 'audi', 10000, 20000)

begimai = PriceDrop('begimai', 'byd')
sultan = PriceDrop('sultan', 'hyundai')

eventbus.subscribe('saved_search', akyl)
eventbus.subscribe('saved_search', iskender)
eventbus.subscribe('saved_search', altynai)
eventbus.subscribe('price_change', begimai)
eventbus.subscribe('price_change', sultan)


listing1 = Listing('bmw', 1998, 3000)
listing2 = Listing('toyta', 2000, 15000)
listing3 = Listing('byd', 20000)