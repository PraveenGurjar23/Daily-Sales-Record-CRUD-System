#sales_record.py

class SalesRecord:
    """Represents a single daily sales entry."""
    
    def __init__(self, record_id, date, item_name, quantity, unit_price):
        self.id = record_id
        self.date = date
        self.item_name = item_name
        self.quantity = quantity
        self.unit_price = unit_price
        # Calculated field
        self.total_amount = self.quantity * self.unit_price

    def to_csv_row(self):
        """Returns a list of data fields suitable for writing to a CSV file."""
        return [
            str(self.id), self.date, self.item_name, 
            str(self.quantity), str(self.unit_price), 
            str(self.total_amount)
        ]

    def __str__(self):
        """String representation for display."""
        return (
            f"ID: {self.id} | Date: {self.date} | Item: {self.item_name} "
            f"| Qty: {self.quantity} | Price: ${self.unit_price:.2f} "
            f"| Total: ${self.total_amount:.2f}"
        )