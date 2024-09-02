from datetime import datetime
from typing import List
from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        manufacturing_dates = []
        expiration_dates = []
        companies = {}

        for inventory in self.inventories:
            for product in inventory.data:
                manufacturing_dates.append(product.manufacturing_date)
                if product.expiration_date > datetime.now().strftime(
                    "%Y-%m-%d"
                ):
                    expiration_dates.append(product.expiration_date)
                company_name = product.company_name
                companies[company_name] = companies.get(company_name, 0) + 1

        oldest_manufacturing_date = min(manufacturing_dates)
        closest_expiration_date = min(expiration_dates)

        largest_inventory = (
            max(companies, key=companies.get) if companies else None
        )

        return (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory}"
        )
