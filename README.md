# NFL Player Statistics Dashboard

## Introduction/Summary

The NFL Player Statistics Dashboard is a web application built using the Dash framework that allows users to visualize and analyze offensive statistics of NFL players for the years 2019-2022. The dashboard provides insights into passing, rushing, and receiving performance for quarterbacks, running backs, and wide receivers.

## Technical Requirements

- Python 3.7+
- `pip` package manager

## Project Structure

The project's directory structure is as follows:

nfl-dashboard/
├── app.py
├── data/
│ ├── nfl_offensive_stats.csv
├── requirements.txt
├── README.md
└── assets/
├── styles.css

- `app.py`: The main script that initializes the Dash app and defines the layout and callbacks.
- `data/`: Directory containing CSV data file(s).
- `requirements.txt`: List of required Python packages and their versions.
- `README.md`: This file, providing project documentation and instructions.
- `assets/`: Directory for additional static files such as stylesheets (`styles.css`).

## Key Functionalities

The dashboard provides the following functionalities:

- View passing statistics (yards, touchdowns, interceptions) for quarterbacks.
- View rushing statistics (yards, touchdowns, attempts) for running backs.
- View receiving statistics (yards, receptions, touchdowns) for wide receivers.
- Filter and visualize data based on player selection and specific statistics.
- Tabbed layout for easy navigation between different player positions.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/nfl-dashboard.git`
2. Navigate to the project directory: `cd nfl-dashboard`
3. Install required packages: `pip install -r requirements.txt`
4. Run the app: `python app.py`
5. Open a web browser and go to `http://127.0.0.1:8050` to access the dashboard.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
