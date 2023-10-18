SQL Query Optimization README.md
Overview
In the random.sql file, we have a slow query due to joining three un-indexed tables. This leads to a nested for loop, and if the tables are approximately the same size, it results in a time complexity of O(N³).

In the random_indexed.sql file, we improve the query speed by introducing indexes to the tables.

Your task is to run all three SQL files to observe the performance differences and understand the underlying mechanisms.

Instructions
Running the Scripts: Execute the following files to check the query execution time:

random.sql
random_indexed.sql
random_cover_indexed.sql (Note: The content for this file has not been provided)
Pseudo Code Explanation: After understanding the query optimization with indexes, write pseudo code to explain the fast query execution process.

Big-O Notation Analysis:

Provide an estimate of the asymptotic scaling behavior in big-O notation for the improved query.
Specify the asymptotic scaling behavior for creating an index.
Observations
The query in random.sql performs a nested join between three tables without any indexes. This can be very inefficient, especially when the tables have large amounts of data.

The query in random_indexed.sql introduces indexes on columns that are used in the join operations (x of TEST2 and y of TEST3). By using indexes, the database can quickly locate rows that match the join condition, making the join operation much faster.

Things to Note
SQLite's query planner is intelligent enough to generate temporary indices in certain cases. Even with this automatic indexing, it is usually faster than a naive table scan. For a clearer understanding, we've turned off automatic indexing using the PRAGMA automatic_index=off command.

Conclusion
Indexes can drastically improve query performance, especially in operations that involve joins, filters, and sorts. However, it's essential to strike a balance. While indexes speed up read operations, they can slow down write operations because the database needs to update the index when data changes. Always analyze the specific requirements and test different approaches to determine the optimal configuration.