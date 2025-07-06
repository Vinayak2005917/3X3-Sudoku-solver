import streamlit as st
import numpy as np
import pandas as pd
import random

#title
st.title("3X3 SUDOKU SOLVER")


# Function to generate a random 3x3 Sudoku grid
if 'grid_values' not in st.session_state:
    grid_values = [[1,2,3], [1,2,3], [1,2,3]]

    def check():
        if grid_values[0][0]+grid_values[0][1]+grid_values[0][2] == 6 and \
             grid_values[1][0]+grid_values[1][1]+grid_values[1][2] == 6 and \
             grid_values[2][0]+grid_values[2][1]+grid_values[2][2] == 6 and \
             grid_values[0][0]+grid_values[1][0]+grid_values[2][0] == 6 and \
             grid_values[0][1]+grid_values[1][1]+grid_values[2][1] == 6 and \
             grid_values[0][2]+grid_values[1][2]+grid_values[2][2] == 6 and \
             grid_values[0][0]+grid_values[1][1]+grid_values[2][2] == 6 and \
             grid_values[0][2]+grid_values[1][1]+grid_values[2][0] == 6:
              return True

    while(check() != True):
        r1, c1 = random.randint(0, 2), random.randint(0, 2)
        r2, c2 = random.randint(0, 2), random.randint(0, 2)
        grid_values[r1][c1], grid_values[r2][c2] = grid_values[r2][c2], grid_values[r1][c1]

    #removing 3 random values
    for _ in range(3):
        r, c = random.randint(0, 2), random.randint(0, 2)
        grid_values[r][c] = "-"

    st.session_state.grid_values = grid_values

grid_values = st.session_state.grid_values


# Generate HTML cells to display the Sudoku grid
cells_html = ""
for rows in grid_values:
    for val in rows:
        cells_html += f'<div class="sudoku-cell">{val}</div>'

html = f"""
<style>
.sudoku-grid {{
    display: grid;
    grid-template-columns: repeat(3, 100px);
    grid-template-rows: repeat(3, 100px);
    gap: 10px;
    justify-content: center;
    margin-top: 50px;
}}

.sudoku-cell {{
    width: 100px;
    height: 100px;
    background-color: #3c4963;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid black;
    border-radius: 10px;
    font-size: 32px;
    color: white;
}}
</style>

<div class="sudoku-grid">
    {cells_html}
</div>
"""

st.markdown(html, unsafe_allow_html=True)

def solve_grid():
    for i in range(3):
        row = st.session_state.grid_values[i]
        if row.count("-") == 1:  # one missing value
            val = 6
            for k in row:
                if k != "-":
                    val -= k
            idx = row.index("-")
            row[idx] = val
        elif row.count("-") == 2:  # two missing values
            present = set(k for k in row if k != "-")
            missing = [n for n in [1, 2, 3] if n not in present]
            idxs = [idx for idx, v in enumerate(row) if v == "-"]
            if len(idxs) == 2:
                row[idxs[0]] = missing[0]
                row[idxs[1]] = missing[1]

col1, col2, col3 = st.columns([1, 2, 1])

with col3:
    st.button("Solve", on_click=solve_grid)