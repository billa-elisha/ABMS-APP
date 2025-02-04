class OperatorScreenModel:
    def __init__(self, database):
        self.database = database
        self.selectProduct("4332")

    def fetchSearchedProduct(self, pName, pCode):
        """search by product name or product bar code"""
        pName = pName
        pCode = pCode
        try:
            db = self.database
            cur = db.cursor()

            if pName == "" and pCode == "":
                return
            elif pName != "" and pCode == "":
                # search by name
                cur.execute(f"SELECT * from products where product_name='{pName}';")
                product = cur.fetchone()
                return product
            elif pName == "" and pCode != "":
                # search by code
                cur.execute(
                    f"SELECT * from products where product_bar_code ='{pCode}';"
                )
                product = cur.fetchone()
                return product
        except Exception as e:
            pass

    def selectProduct(self, product_dentity):
        # This is the structure of the product table
        #      product_id INTEGER PRIMARY KEY,
        #      product_bar_code text NOT NULL,
        #      product_name text NOT NULL,
        #      product_cost_price real NOT NULL,
        #      product_selling_price real NOT NULL,
        #      product_quantity INTEGER NOT NULL
        """
        This function returns the product that is search for by
        the user.
        The product identity could be
        ** the name or
        ** the barcode
        It either returns the product in the form (5, '34332', 'gary', 5.0, 67.0, 8) or
        'None'
        """
        self.product_dentity = product_dentity
        try:
            db = self.database
            cursor = db.cursor()
            cursor.execute(
                f"SELECT * from products where product_name='{self.product_dentity}' or product_bar_code ='{self.product_dentity}' ;"
            )
            product = cursor.fetchone()
            return product
        except Exception as e:
            return None
