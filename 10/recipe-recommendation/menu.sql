-- Users table
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);

-- Recipes table
CREATE TABLE Recipes (
    recipe_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Ingredients table
CREATE TABLE Ingredients (
    ingredient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL                                                                                                                                                   
);

-- RecipeIngredients table (many-to-many relationship)
CREATE TABLE RecipeIngredients (
    recipe_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
);


-- Users
INSERT INTO Users (username, email) VALUES
    ('chef1', 'chef1@example.com'),
    ('user2', 'user2@example.com');

-- Recipes
INSERT INTO Recipes (title, description, user_id) VALUES
    ('Spaghetti Carbonara', 'Classic Italian pasta dish.', 1),
    ('Chicken Stir-Fry', 'Quick and healthy stir-fry recipe.', 1),
    ('Veggie Burger', 'Vegetarian burger with a twist.', 2);

-- Ingredients
INSERT INTO Ingredients (name) VALUES
    ('Spaghetti'),
    ('Eggs'),
    ('Bacon'),
    ('Chicken'),
    ('Broccoli'),
    ('Black Beans');

-- RecipeIngredients
INSERT INTO RecipeIngredients (recipe_id, ingredient_id) VALUES
    (1, 1), (1, 2), (1, 3),
    (2, 4), (2, 5),
    (3, 6);


-- Query 1: Get all recipes
SELECT * FROM Recipes;

-- Query 2: Get all ingredients
SELECT * FROM Ingredients;

-- Query 3: Get all ingredients for a recipe with a given id
SELECT * FROM Ingredients
    JOIN RecipeIngredients USING (ingredient_id)
    WHERE recipe_id = 1;

-- Query 4: Which recipes contain eggs as an ingredient??
SELECT DISTINCT r.title
FROM Recipes r
    JOIN RecipeIngredients ri ON r.recipe_id = ri.recipe_id
    JOIN Ingredients i ON ri.ingredient_id = i.ingredient_id
    WHERE i.name = 'Eggs';

-- Query 5: What are the ingredients in the "Veggie Burger" recipe?
SELECT i.name
FROM Ingredients i
    JOIN RecipeIngredients ri ON i.ingredient_id = ri.ingredient_id
    JOIN Recipes r ON ri.recipe_id = r.recipe_id
    WHERE r.title = 'Veggie Burger';

-- Query 6: How many recipes does chef1 have?
SELECT COUNT(*) 
FROM Recipes 
WHERE user_id = 1;
