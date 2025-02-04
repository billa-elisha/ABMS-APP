from View.base_screen import BaseScreen
from kivy.properties import ObjectProperty
import decimal as PythonDecimal


class OperatorScreenView(BaseScreen):
    bill_data = ObjectProperty()
    productName = ObjectProperty()
    productPrice = ObjectProperty()
    product_to_search_name = ObjectProperty()
    # product_to_search_code = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)

        self.listOfProductToBill = {}
        self.receipt_bill_list = []

    # def display_bill_data(self,listofbillproducts):
    #     listOfProductToBill= listofbillproducts
    #     data_ = []
    #     for data in listOfProductToBill.keys():
    #         item = listOfProductToBill[f"{data}"][2]
    #         amount = listOfProductToBill[f"{data}"][4]
    #         qt = listOfProductToBill[f"{data}"][6]
    #         unitprice = listOfProductToBill[f"{data}"][0]
    #         data_.append({"text": f"{item}"})
    #         data_.append({"text": f"{amount}"})
    #         data_.append({"text": f"{qt}"})
    #         data_.append({"text": f"{unitprice}"})
    #     return data_

    def searchProductByName(self):
        product_to_search_name = f"{self.product_to_search_name.text}"
        product_to_search_code = f"{self.product_to_search_code.text}"
        if product_to_search_name == "":
            self.product_to_search_name.error = True
            return
        else:
            product_ = self.controller.searchProductByNameOrCode(
                product_to_search_name, product_to_search_code
            )
            ProductToBill = self.controller.searchedProductToAddToBill(
                product_,
                self.productName,
                self.productPrice,
            )
            self.controller.billing_data(ProductToBill, self.listOfProductToBill)

    def searchProductByCode(self):
        product_to_search_name = f"{self.product_to_search_name.text}"
        product_to_search_code = f"{self.product_to_search_code.text}"
        if product_to_search_code == "":
            self.product_to_search_code.error = True
            return
        else:
            product_ = self.controller.searchProductByNameOrCode(
                product_to_search_name, product_to_search_code
            )
            ProductToBill = self.controller.searchedProductToAddToBill(
                product_,
                self.productName,
                self.productPrice,
            )
            self.controller.billing_data(ProductToBill, self.listOfProductToBill)

    def addTocard(self):
        if self.productName.text == "":
            pass
        else:
            if self.productName.text == "No product found":
                pass
            else:
                # name of the product to add to the bill
                name = (self.productName.text).strip()
                # trying to see if product aready exist in the list of products searched
                for pl in self.listOfProductToBill.values():
                    if name in pl:
                        # checking for the presence of the product in the receipt_bill_list
                        if str(pl[0]) in self.receipt_bill_list:
                            pass
                        else:
                            self.receipt_bill_list.append(str(pl[0]))

                # displaying the bill data on the bill section
                self.bill_data.data = self.controller.display_bill_data(
                    self.listOfProductToBill, self.receipt_bill_list
                )

        self.productName.text = ""
        self.productPrice.text = ""
        # print(self.receipt_bill_list)

    def clearButton(self):
        self.controller.clear(self.productName, self.productPrice)

    def generatate_bill(self):
        bi = []
        for id in self.receipt_bill_list:
            bi.append(self.listOfProductToBill[id])
        print(bi)
