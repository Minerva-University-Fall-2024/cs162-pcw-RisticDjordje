# Database Schema and Queries Explanation

This README provides an in-depth explanation of the SQL code provided for a database schema and queries related to a Recipe Recommendation and Meal Planning App. The code includes table creation, data insertion, and several SQL queries. The README will walk you through each part of the code and its purpose.

## Database Schema

### Users Table
The `Users` table stores information about app users. It includes the following columns:
- `user_id`: An integer representing the unique user ID (Primary Key).
- `username`: Text field for the user's username.
- `email`: Text field for the user's email address.

### Recipes Table
The `Recipes` table stores information about recipes. It includes the following columns:
- `recipe_id`: An integer representing the unique recipe ID (Primary Key).
- `title`: Text field for the recipe title.
- `description`: Text field for the recipe description.
- `user_id`: Integer representing the user who created the recipe (Foreign Key referencing `Users` table).

### Ingredients Table
The `Ingredients` table stores information about individual ingredients used in recipes. It includes the following columns:
- `ingredient_id`: An integer representing the unique ingredient ID (Primary Key).
- `name`: Text field for the ingredient name.

### RecipeIngredients Table
The `RecipeIngredients` table establishes a many-to-many relationship between recipes and ingredients. It includes the following columns:
- `recipe_id`: Integer representing the recipe (Foreign Key referencing `Recipes` table).
- `ingredient_id`: Integer representing the ingredient (Foreign Key referencing `Ingredients` table).

## Data Insertion

- Data is inserted into the `Users`, `Recipes`, `Ingredients`, and `RecipeIngredients` tables to populate the database with sample information. Users, recipes, and ingredients are added with relevant data.

## SQL Queries

### Query 1: Get all recipes
This query retrieves all records from the `Recipes` table. It provides a list of all recipes stored in the database.

### Query 2: Get all ingredients
This query retrieves all records from the `Ingredients` table. It provides a list of all ingredients available in the database.

### Query 3: Get all ingredients for a recipe with a given id
This query retrieves all ingredients associated with a specific recipe ID. It joins the `Ingredients` and `RecipeIngredients` tables to find ingredients for a given recipe.

### Query 4: Which recipes contain eggs as an ingredient?
This query finds all recipes that include "Eggs" as an ingredient. It involves joining the `Recipes`, `RecipeIngredients`, and `Ingredients` tables to filter recipes containing eggs.

### Query 5: What are the ingredients in the "Veggie Burger" recipe?
This query lists all ingredients for the "Veggie Burger" recipe. It joins the `Ingredients`, `RecipeIngredients`, and `Recipes` tables to identify the ingredients for the specified recipe title.

### Query 6: How many recipes does chef1 have?
This query counts the number of recipes created by a specific user (in this case, "chef1" with user ID 1). It counts the rows in the `Recipes` table where the `user_id` matches the given user's ID.
