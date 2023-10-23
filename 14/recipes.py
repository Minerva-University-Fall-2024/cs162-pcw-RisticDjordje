import sqlalchemy 
from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 

engine = create_engine('sqlite:///recipe_database.db')
Base = declarative_base() 

# Users table
class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    
    recipes = relationship('Recipe', back_populates='user') # One-to-Many relationship with Recipes

    def __repr__(self):
        return "<User(user_id={}, username='{}', email='{}')>".format(self.user_id, self.username, self.email)

# Recipes table
class Recipe(Base):
    __tablename__ = 'recipes'
    
    recipe_id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    
    user = relationship('User', back_populates='recipes') # Many-to-One relationship with User
    ingredients = relationship('Ingredient', secondary='recipe_ingredients', back_populates='recipes') # Many-to-Many relationship with Ingredients

    def __repr__(self):
        return "<Recipe(recipe_id={}, title='{}', description='{}', user_id={})>".format(self.recipe_id, self.title, self.description, self.user_id)

# Ingredients table
class Ingredient(Base):
    __tablename__ = 'ingredients'
    
    ingredient_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    
    recipes = relationship('Recipe', secondary='recipe_ingredients', back_populates='ingredients') # Many-to-Many relationship with Recipes

    def __repr__(self):
        return "<Ingredient(ingredient_id={}, name='{}')>".format(self.ingredient_id, self.name)

# RecipeIngredients table
recipe_ingredients_association = Table('recipe_ingredients', Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.recipe_id'), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredients.ingredient_id'), primary_key=True)
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Populate tables
session.add(User(username='chef1', email='chef1@example.com'))
session.add(User(username='user2', email='user2@example.com'))
session.commit()

spaghetti = Recipe(title='Spaghetti Carbonara', description='Classic Italian pasta dish.', user_id=1)
stirfry = Recipe(title='Chicken Stir-Fry', description='Quick and healthy stir-fry recipe.', user_id=1)
veggie_burger = Recipe(title='Veggie Burger', description='Vegetarian burger with a twist.', user_id=2)
session.add_all([spaghetti, stirfry, veggie_burger])

ingredients = ['Spaghetti', 'Eggs', 'Bacon', 'Chicken', 'Broccoli', 'Black Beans']
for ingredient in ingredients:
    session.add(Ingredient(name=ingredient))
session.commit()

spaghetti.ingredients.append(session.query(Ingredient).filter_by(name='Spaghetti').first())
spaghetti.ingredients.append(session.query(Ingredient).filter_by(name='Eggs').first())
spaghetti.ingredients.append(session.query(Ingredient).filter_by(name='Bacon').first())

stirfry.ingredients.append(session.query(Ingredient).filter_by(name='Chicken').first())
stirfry.ingredients.append(session.query(Ingredient).filter_by(name='Broccoli').first())

veggie_burger.ingredients.append(session.query(Ingredient).filter_by(name='Black Beans').first())

session.commit()

print(session.query(Recipe).all())
print(session.query(Ingredient).all())
