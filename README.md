<p align="center">
    <a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-%2320232a?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>
    <a href="https://dash-bootstrap-components.opensource.faculty.ai/"><img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" /></a>
    <a href="https://plotly.com/dash/"><img src="https://img.shields.io/badge/dash-008DE4?style=for-the-badge&logo=dash&logoColor=white" /></a>
     <a href=""><img src="https://img.shields.io/pypi/l/ansicolortags.svg" /></a>
    <a href=""><img src="https://img.shields.io/badge/any_text-you_like-blue" /></a>
    <a href=""><img src="https://img.shields.io/badge/any_text-you_like-blue" /></a>
    <a href=""><img src="https://img.shields.io/badge/any_text-you_like-blue" /></a>
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

- `data/`: Directory containing the dataset `nfl_offensive_stats.csv`.
- `app.py`: Main application file containing the Dash app code and callbacks.
- `Pipfile` and `Pipfile.lock`: Files specifying project dependencies when using `pipenv`.
- `README.md`: Project documentation providing an overview, setup instructions, and other details.

## Key Functionalities

The NFL Player Statistics Dashboard offers the following functionalities:

- Choose a player's position: quarterbacks, running backs, or wide receivers.
- Select a specific player from the dropdown menu.
- Choose from various statistics for the selected player using radio items.
- View bar graphs illustrating the selected player's statistics over different game IDs.

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

This project is licensed under the MIT License. See the LICENSE file for details.
