# Pavlivka River eDNA Biodiversity Analysis

This project focuses on analyzing environmental DNA (eDNA) samples from the Pavlivka River. The goal is to identify species diversity and ecosystem health using metabarcoding data processed through MegaBLAST and BOLD systems.

## 📊 Visualizations

Below are the results of the taxonomic analysis. These charts were generated using Python (Pandas & Matplotlib) based on the processed eDNA datasets.

### 1. General Taxonomic Composition (Main Groups)
This pie chart displays the dominant Phyla found in the river. To maintain clarity, all groups representing less than 2% of the total diversity are grouped into the **"Others"** category.

![Taxonomic Pie Chart](main_composition.png)

### 2. Rare Biosphere (Minority Taxa)
This bar chart provides a detailed look at the species and groups that make up the "Others" category (less than 2% of the total sample). Identifying these rare taxa is crucial for understanding the full biodiversity of the ecosystem.

![Minority Bar Chart](minority_details.png)

---

## 🛠 Tools Used

- **Galaxy Europe**: For primary sequence processing and taxonomic assignment.
- **Python 3.x**: For data cleaning and visualization.
- **Google Colab**: Used as the primary environment for executing visualization scripts.
- **GitHub Copilot**: Assisted in optimizing the visualization code and data grouping logic.

---

## 📂 Project Structure

- `Final_eDNA_Report_Pavlivka.csv`: The complete merged dataset containing BLAST and BOLD results.
- `visualize_edna.py`: Python script used to generate the charts.
- `main_composition.png`: High-resolution pie chart image.
- `minority_details.png`: Detailed bar chart of rare taxa.

---

## 🚀 How to Run the Script

If you want to reproduce these visualizations:

1. Clone this repository.
2. Ensure you have `pandas` and `matplotlib` installed:
   ```bash
   pip install pandas matplotlib
