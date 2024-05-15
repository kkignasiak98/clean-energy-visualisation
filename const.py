import plotly.express as px
# Geographic constants
CONTINENT_NAMES = ("World", 
                    "Europe",
                    "Africa",
                    "Asia Pacific",
                    "Australia",
                    "China",
                    "India",
                    "Middle East",
                    "North America",
                    "South America")
EUROPEAN_COUNTRIES = ("World", 
                            "Europe",
                            "Austria",
                            "Belarus",
                            "Belgium",
                            "Czechia",
                            "Denmark",
                            "Estonia",
                            "Finland",
                            "France",
                            "Greece",
                            "Hungary",
                            "Iceland",
                            "Ireland",
                            "Italy",
                            "Latvia",
                            "Lithuania",
                            "United Kingdom",
                            "Ukraine",
                            "Switzerland",
                            "Sweden",
                            "Portugal",
                            "Poland",
                            "Norway",
                            "Luxembourg",
                            "Bulgaria",
                            "Germany",
                            "Denmark",
                            "Spain",
                            "Albania",
                            "Bosnia and Herzegovina",
                            "Croatia",
                            "Cyprus",
                            "Kosovo",
                            "Malta",
                            "Moldova",
                            "Netherlands",
                            "Romania",
                            "Russia",
                            "Serbia",
                            "Slovakia")

# Visualisation

PLOT_FONT_DICT = dict(
    family="Arial",
    size=20,
    color='#000000'
)
PLOT_HEIGHT = 800
PLOT_WIDTH = 1400

PASTEL_PALETTE_MAIN = px.colors.qualitative.Pastel
SEQUENTIAL_PALETTE = px.colors.sequential.algae
PIE_COLORS =['mediumturquoise', 'gold', 'darkorange', 'lightgreen']
PIE_COLORS_DICT = dict(colors=PIE_COLORS, line=dict(color='#000000', width=2))
