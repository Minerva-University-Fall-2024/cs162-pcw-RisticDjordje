import React from "react";


export default function Home(){
    return(
        <>
        <main>
        <section class="board">
          <div class="column">
            <h2>To Do</h2>
            <ul class="task-list">
              <li>Task 1</li>
              <li>Task 2</li>
            </ul>
          </div>

          <div class="column">
            <h2>In Progress</h2>
            <ul class="task-list">
              <li>Task 3</li>
            </ul>
          </div>

          <div class="column">
            <h2>Review</h2>
            <ul class="task-list">
              <li>Task 4</li>
            </ul>
          </div>

          <div class="column">
            <h2>Testing</h2>
            <ul class="task-list">
              <li>Task 5</li>
            </ul>
          </div>

          <div class="column">
            <h2>Done</h2>
            <ul class="task-list">
              <li>Task 6</li>
            </ul>
          </div>
        </section>
      </main>

      <footer>
        <p>© Djordje Ristic | 2023</p>
      </footer>   
        </>
    )
}