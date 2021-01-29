from flask_sqlalchemy import SQLAlchemy
from database_setup import Restaurant, MenuItem


class DBAccess:
    def __init__(self, database: SQLAlchemy):
        self.db = database

    def getRestaurant(self, restaurantId: int) -> Restaurant:
        return self.db.session.query(Restaurant) \
            .filter_by(id=restaurantId).first()

    def getMenuItem(self, menuId: int) -> MenuItem:
        return self.db.session.query(MenuItem).filter_by(id=menuId).first()

    def getRestaurants(self, ):
        return self.db.session.query(Restaurant).order_by(Restaurant.name)

    def getMenuItems(self, restaurantId: int):
        return self.db.session.query(MenuItem).filter_by(
            restaurant_id=restaurantId
            )

    def createNewRestaurant(self, name: str):
        newRestaurant = Restaurant(
            name=name)
        self.db.session.add(newRestaurant)
        self.db.session.commit()

    def createNewMenuItem(self, restaurantId: int, name: str):
        newMenuItem = MenuItem(
            name=name,
            restaurant_id=self.getRestaurant(restaurantId).id
            )
        self.db.session.add(newMenuItem)
        self.db.session.commit()

    def renameRestaurant(self, restaurantId: int, name: str):
        restaurant = self.getRestaurant(restaurantId)
        restaurant.name = name
        self.db.session.commit()

    def editMenuItem(self, menuId: int, name: str):
        menuItem = self.getMenuItem(menuId=menuId)
        menuItem.name = name
        self.db.session.commit()

    def deleteRestaurant(self, restaurantId: int):
        self.db.session.delete(self.getRestaurant(restaurantId))
        self.db.session.commit()

    def deleteMenuItem(self, menuId: int):
        self.db.session.delete(self.getMenuItem(menuId=menuId))
        self.db.session.commit()
