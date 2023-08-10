## Things To Do

### **Basic Objectives**

1. **Customization and Personalization:** Allow users to customize the dashboard layout and content based on their preferences.
   - Implement a dashboard settings panel that lets users choose the default view, preferred statistics, and visualizations.
   - Provide options to rearrange and resize dashboard components to create a personalized layout.
   - Allow users to save their customizations for future visits.

<br>

2. **Data Insights and Highlights:** Automatically generate insights and highlights based on data analysis.
   - Implement a feature that identifies exceptional player performances (e.g., record-breaking games) and displays them prominently.
   - Use natural language processing to generate textual summaries or highlights for selected players or games.
   - Provide tooltips or pop-ups that explain statistical terms and concepts to assist users in understanding the data.

<br>

3. **Export and Sharing Options:** Enable users to export selected data and visualizations for further analysis or sharing.
   - Add buttons or links to export data as CSV or Excel files for offline analysis.
   - Implement social media sharing buttons to allow users to share interesting insights or visualizations.
   - Provide an option to generate and download high-resolution images of graphs and charts.

<br>

4. **Interactive Data Filters:** Allow users to filter and explore data based on specific criteria.

   - Implement dropdown menus or input fields to filter data by season, team, or player attributes.
   - Provide users with the ability to apply multiple filters simultaneously to refine their analysis.
   - Update visualizations and statistics dynamically based on the selected filters.

<br>

5. **Enhanced Styling and Branding:** Improve the visual appeal of the dashboard by applying consistent styling, branding, and layout.
   - Implement a consistent color scheme and typography throughout the dashboard.
   - Add a logo or header image that represents the theme of the dashboard.
   - Use responsive design principles to ensure the dashboard looks good on various devices.

### **Repo Objectives**

- ~~Rename GitHub (**_NOT_** local) project name to something more expressive (e.g. `nfl-dashboard` -> `nfl-analytics-dashboard`).~~
- Upload project banner image to project repository.
  - Upload project banner image to assets subdirectory (e.g. `project-banner.png` -> `assets/project-banner.png`).
- ~~Hide `.ipynb_checkpoints/`, `.DS_Store`, and other unnecessary files/directories through better usage of `.gitignore`.~~
- ~~Compartmentalize project by including `eda.ipynb` in a subdirectory of your naming choice (e.g. `eda.ipynb` -> `notebooks/eda.ipynb`).~~
  - ~~You can also choose to rename your notebook file to something more explicit/descriptive (e.g. `eda.ipynb` -> `nfl-investigative-analysis.ipynb`).~~
- Add more badges!

### **Advanced/Stretch Objectives**

1. **Performance Analysis by Position:** Provide users with insights into the performance of different positions (Quarterbacks, Running Backs, and Wide Receivers) over the seasons.
   - Display key statistics such as passing yards, rushing yards, and receiving yards for each position.
   - Allow users to select a specific player and view their detailed statistics.
   - Show graphical representations (e.g., bar charts) of selected statistics for each position.

<br>

2. **Game Impact Analysis:** Enable users to analyze the impact of specific games on player performance, including touchdowns and yardage.
   - Display game-by-game statistics for touchdowns, passing yards, and rushing yards for selected players.
   - Allow users to click on a game in the graph to view detailed statistics for that game, including pass attempts, completions, and rushing attempts.
   - Highlight exceptional game performances through color-coded visuals based on specified thresholds.

<br>

3. **Player Comparison and Trend Analysis:** Provide a platform for users to compare multiple players' statistics and observe performance trends over seasons.
   - Enable users to select and compare statistics of two or more players simultaneously.
   - Display line charts showing the trend of key statistics (e.g., passing yards, rushing touchdowns) over the seasons for the selected players.
   - Allow users to customize the visualization by choosing different statistics and timeframes (seasons or years).
