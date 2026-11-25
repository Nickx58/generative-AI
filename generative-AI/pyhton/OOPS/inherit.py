class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai): # inheritence
    def add_spices(self):
        print("Adding elachi")

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("REgular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

shop = MasalaChai("Elachi")
shop.prepare()