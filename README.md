<p align="center">
    <a href=""><img src="https://img.shields.io/pypi/l/ansicolortags.svg" /></a>
    <a href=""><img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" /></a>
    <a href=""><img src="https://badgen.net/github/commits/jonrosenblum/NFL-Analytics-Dashboard" /></a>
    <br>
    <a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-%2320232a?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>
    <a href="https://dash-bootstrap-components.opensource.faculty.ai/"><img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" /></a>
    <a href="https://plotly.com/dash/"><img src="https://img.shields.io/badge/dash-008DE4?style=for-the-badge&logo=dash&logoColor=white" /></a>
    <br>
    <a href=""><img src="https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter" /></a>

</p>

<h1 align="center"><b>NFL Statistics Dashboard</b></h1>
<h4 align="center">A web application built using Dash and Plotly for visualizing NFL player statistics. This dashboard allows users to explore passing, rushing, and receiving statistics for quarterbacks, running backs, and wide receivers. </h4>

<p align="center">
    <img src="" alt="Project Banner" width=60% height=60%/>
</p>

## Table of Contents

- [Introduction](#introduction)
- [Technical Requirements](#technical-requirements)
- [Project Structure](#project-structure)
- [Key Functionalities](#key-functionalities)
- [Project Objectives](#project-objectives)
- [Advanced Project Objectives](#advanced-project-objectives)
- [Repository Objectives](#repository-objectives)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The NFL Player Statistics Dashboard provides an interactive way to visualize player statistics from 2019 to 2022 for different positions: quarterbacks (QB), running backs (RB), and wide receivers (WR). Users can select specific players and view various statistics, including passing yards, touchdowns, interceptions, rushing yards, rush touchdowns, rushing attempts, receiving yards, receptions, and receiving touchdowns.

## Technical Requirements

To run the NFL Player Statistics Dashboard locally, you need the following:

- Python 3.7 or later
- Dash 1.21.0 or later
- Plotly 5.0.0 or later
- Pandas 1.1.0 or later

## Project Directory Hierarchy

Upon successful setup (see **Getting Started**), you should see the following project directory hierarchy.

```
nfl-player-stats-dashboard/
├── classes/
├── data/
│ └── nfl_offensive_stats.csv
├── notebooks/
│ └── .ipynb_checkpoints/
│ │     └── .eda-checkpoints.ipynb
│ └── nfl-investigative_analysis.ipynb
├── app.py
├── OBJECTIVES.md
├── Pipfile
└── README.md
```

- `classes/`: Directory containing OOP Objectives
- `data/`: Directory containing the dataset `nfl_offensive_stats.csv`.
- `app.py`: Main application file containing the Dash app code and callbacks.
- `OBJECTIVES.md`: Project documentation for future objectives and functionality
- `Pipfile` and `Pipfile.lock`: Files specifying project dependencies when using `pipenv`.
- `README.md`: Project documentation providing an overview, setup instructions, and other details.

## Key Functionalities

The NFL Player Statistics Dashboard offers the following functionalities:

- Choose a player's position: quarterbacks, running backs, or wide receivers.
- Select a specific player from the dropdown menu.
- Choose from various statistics for the selected player using radio items.
- View bar graphs illustrating the selected player's statistics over different game IDs.
- Compare player statistics and visualizations.

## **Project Objectives**

**~~Position-Specific Tabs~~**

- ~~Create tabs for each player position: QBs, RBs, and WRs.~~
- ~~Display a dropdown to select a player from the chosen position.~~
- ~~Display a radio button group to choose a specific statistic (e.g., yards, touchdowns) for the selected player.~~
- ~~Show a bar chart representing the chosen statistic for each game the player participated in.~~
- ~~Provide detailed statistics for a selected game upon clicking on a game in the bar chart.~~

**Export and Sharing Options:**

- Enable users to export selected data and visualizations for further analysis or sharing.
- Add buttons or links to export data as CSV or Excel files for offline analysis.
- Implement social media sharing buttons to allow users to share interesting insights or visualizations.
- Provide an option to generate and download high-resolution images of graphs and charts.

**Interactive Data Filters:**

- Allow users to filter and explore data based on specific criteria.
- Implement dropdown menus or input fields to filter data by season, team, or player attributes.
- Provide users with the ability to apply multiple filters simultaneously to refine their analysis.
- Update visualizations and statistics dynamically based on the selected filters.

**Customization and Personalization:**

- Allow users to customize the dashboard layout and content based on their preferences.
- Implement a dashboard settings panel that lets users choose the default view, preferred statistics, and visualizations.
- Provide options to rearrange and resize dashboard components to create a personalized layout.
- Allow users to save their customizations for future visits.

**Weekly Schedule Tab**

- Present the NFL game scheudle week by week
- Use a table or other visualization to display game details (opponents, dates, locations, etc.).
- Implement interactivity to explore game details and navigate between weeks.

## **Advanced Project Objectives**

**Performance Analysis by Position:**

- Provide users with insights into the performance of different positions (Quarterbacks, Running Backs, and Wide Receivers) over the seasons.
- Display key statistics such as passing yards, rushing yards, and receiving yards for each position.
- Allow users to select a specific player and view their detailed statistics.
- Show graphical representations (e.g., bar charts) of selected statistics for each position.

**Game Impact Analysis:**

- Enable users to analyze the impact of specific games on player performance, including touchdowns and yardage.
- Display game-by-game statistics for touchdowns, passing yards, and rushing yards for selected players.
- Allow users to click on a game in the graph to view detailed statistics for that game, including pass attempts, completions, and rushing attempts.
- Highlight exceptional game performances through color-coded visuals based on specified thresholds.

**Player Comparison and Trend Analysis:**

- Provide a platform for users to compare multiple players' statistics and observe performance trends over seasons.
- Enable users to select and compare statistics of two or more players simultaneously.
- Display line charts showing the trend of key statistics (e.g., passing yards, rushing touchdowns) over the seasons for the selected players.
- Allow users to customize the visualization by choosing different statistics and timeframes (seasons or years).

## **Repository Objectives**

- ~~Rename GitHub (**_NOT_** local) project name to something more expressive (e.g. `nfl-dashboard` -> `nfl-analytics-dashboard`).~~
- Upload project banner image to project repository.
  - Upload project banner image to assets subdirectory (e.g. `project-banner.png` -> `assets/project-banner.png`).
- ~~Hide `.ipynb_checkpoints/`, `.DS_Store`, and other unnecessary files/directories through better usage of `.gitignore`.~~
- ~~Compartmentalize project by including `eda.ipynb` in a subdirectory of your naming choice (e.g. `eda.ipynb` -> `notebooks/eda.ipynb`).~~
  - ~~You can also choose to rename your notebook file to something more explicit/descriptive (e.g. `eda.ipynb` -> `nfl-investigative-analysis.ipynb`).~~
- Add more badges!

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/jonrosenblum/nfl-player-stats-dashboard.git
```

2. Navigate to the project directory:

```bash
cd nfl-player-stats-dashboard
```

3. Install the required dependencies using pipenv:

```bash
pipenv install
```

4. Run the Dash app:

```bash
pipenv run python app.py
```

## Usage

1. Choose a position (Quarterbacks, Running Backs, or Wide Receivers) from the tabs.
2. Select a player from the dropdown menu.
3. Use the radio items to choose the desired statistic.
4. Observe the corresponding bar graph showing the player's statistics.

## Dependencies

The NFL Player Statistics Dashboard relies on the following libraries:

- Dash: A web application framework for building interactive web applications with Python.
- Plotly: A graphing library for creating interactive, publication-quality graphs.
- Pandas: A data manipulation library for data analysis and manipulation.

## Contributing

Contributions to the NFL Player Statistics Dashboard are welcome! If you encounter any issues, have feature suggestions, or would like to contribute code, please open an issue or pull request on the GitHub repository.

## License

MIT License

Copyright (c) 2023 Jon Rosenblum

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
