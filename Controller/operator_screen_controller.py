from kivy.uix.gridlayout import chain
from kivy.uix.filechooser import error
import View
import View.OperatorScreen
import View.OperatorScreen.operator_screen
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
import decimal as PythonDecimal
from tabulate import tabulate


class OperatorScreenController:
    def __init__(self, model):
        self.model = model
        self.view = View.OperatorScreen.operator_screen.OperatorScreenView(
            controller=self, model=self.model
        )
        self.searched_product = []
        self.products_on_the_card = dict()
        self.recently_added_product_id = []  # this is use to help udate the produc_on_the_card when undo is press

    def get_view(self):
        return self.view

    def searchProduct(self, textbox, productNameLable, productPriceLable):
        """
        This function takes the product name or bar code as it value
        to search for the product
        """
        text = str(textbox.text)
        productNameLable.text = ""
        productNameLable.text_color = get_color_from_hex("5C5C5C")
        if text == "":
            textbox.error = True
            return
        else:
            self.searched_product.clear()
            product_searched = self.model.selectProduct(text)
            if str(product_searched) == "None":
                productNameLable.text = "No Product with that name or code"
                productNameLable.text_color = (1, 0, 0, 1)
                return
            else:
                self.searched_product.append(
                    product_searched
                )  # ==>[(5, '34332', 'gary', 5.0, 67.0, 8)]
                try:
                    productNameLable.text = str(self.searched_product[0][2])
                    productPriceLable.text = str(self.searched_product[0][4])
                except Exception as e:
                    pass

            # print(self.searched_product)

    def clearSearchedProduct(self, productNameLable, productPriceLable):
        self.productNameLable = productNameLable
        self.productPriceLable = productPriceLable
        """
        This function clear the product searched name and price on the user 
        interface.
        it also emptys product-search list variable 

        """
        self.productNameLable.text = ""
        self.productPriceLable.text = ""
        self.searched_product.clear()

    def addToCard(self, productNameLable, productPriceLable, recycleview):
        """It adds and at the same time updates the
        products_on_the_card variable

        """
        namelable = productNameLable
        pricelable = productPriceLable
        # it takes the product searched from the self.searched_product
        try:
            if len(self.searched_product) == 0:
                return
            else:
                prod = list(self.searched_product[0])
                # apdating the product quantity and multplying the
                # amount if it already exist
                product_to_add_id = str(prod[0])
                if product_to_add_id in (self.products_on_the_card.keys()):
                    # update that Product
                    product_to_update = self.products_on_the_card[
                        f"{product_to_add_id}"
                    ]
                    # updating the price
                    product_to_update[4] = (
                        f"{(PythonDecimal.Decimal(f'{product_to_update[4]}') + PythonDecimal.Decimal(f'{product_to_update[7]}'))}"
                    )
                    product_to_update[6] = f"{int(product_to_update[6]) + int(1)}"
                    updated_product = product_to_update
                    self.products_on_the_card[str(product_to_add_id)] = updated_product
                    recycleview.data = self.display_bill_data()
                    self.recently_added_product_id.append(str(prod[0]))

                else:
                    # add as a new product
                    "uding initial quantity value as 1"
                    prod.append("1")
                    prod.append(prod[4])  # unit price of the product
                    self.products_on_the_card[f"{prod[0]}"] = prod
                    recycleview.data = self.display_bill_data()
                    self.recently_added_product_id.append(str(prod[0]))
                    print(self.products_on_the_card)
                self.clearSearchedProduct(namelable, pricelable)
            print(self.products_on_the_card)
        except Exception as e:
            pass

    def display_bill_data(self):
        data_ = []
        if len(self.products_on_the_card) == 0:
            return data_
        else:
            for id_ in self.products_on_the_card.keys():
                item = self.products_on_the_card[f"{id_}"][2]
                amount = self.products_on_the_card[f"{id_}"][4]
                qt = self.products_on_the_card[f"{id_}"][6]
                unitprice = self.products_on_the_card[f"{id_}"][7]
                data_.append({"text": f"{item}"})
                data_.append({"text": f"{unitprice}"})
                data_.append({"text": f"{qt}"})
                data_.append({"text": f"{amount}"})

            return data_

    def undoButton(self, recycleview):
        # if the last product in the product to add to card chain
        # quantity value is more than one, reduce it and subtract the unit price from the amount
        # else we remove the entire product
        try:
            key_of_the_last_product = str(self.recently_added_product_id[-1])
            product_to_undo = self.products_on_the_card[key_of_the_last_product]
            if int(product_to_undo[6]) > 1:
                product_to_undo[6] = f"{int(product_to_undo[6]) - int(1)}"
                product_to_undo[4] = (
                    f"{(PythonDecimal.Decimal(f'{product_to_undo[4]}') - PythonDecimal.Decimal(f'{product_to_undo[7]}'))}"
                )
                self.products_on_the_card[key_of_the_last_product] = product_to_undo
                recycleview.data = self.display_bill_data()
                print(self.products_on_the_card)

            else:
                # delete the product
                del self.products_on_the_card[key_of_the_last_product]
                new_list = []
                for i in self.recently_added_product_id:
                    if i != key_of_the_last_product:
                        new_list.append(i)

                self.recently_added_product_id = new_list
                recycleview.data = self.display_bill_data()
            print(self.products_on_the_card)

        except IndexError as e:
            pass

    def finiliseButton(self, checbox):
        isgeneratebill = checbox.active
        for purchased_prod in self.products_on_the_card:
            print(purchased_prod)

        # if isgeneratebill:
        #     productPurchaseTable = tabulate(
        #         listOpProducts_,
        #         headers=["Item", "Unit Price", "Qt", "amount"],
        #         floatfmt=".2f",
        #     )

        #     ...
        # else:
        #     ...

        # print(checbox.active)

    # ==========================================================================
