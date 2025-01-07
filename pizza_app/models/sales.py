class Sales:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Sales, cls).__new__(cls)
            cls._instance.sales_data = []
        return cls._instance

    def record_sale(self, order):
        self.sales_data.append(order.calculate_total())

    def get_sales_report(self):
        return {
            "total_sales": sum(self.sales_data),
            "orders_count": len(self.sales_data)
        }