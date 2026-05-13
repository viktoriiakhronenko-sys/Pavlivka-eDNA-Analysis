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
## 📈 Ecological Diversity Analysis (Mlyn Station)

Beyond simple identification, we performed a mathematical analysis of the ecosystem's health using diversity indices. These metrics account for both the number of species and how evenly individuals are distributed among them.

### Biodiversity Metrics
![Diversity Analysis](ecolog.ind.pavlivka.png)

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Species Richness** | [65] | Total number of unique species found |
| **Shannon Index (H)** | [1.819] | Measures uncertainty; higher values mean higher stability |
| **Simpson's Index (1-D)** | [0.740] | Probability that two random individuals belong to different species |

### Scientific Conclusion
A value of 1.819 is significantly high for freshwater ecosystems (typically ranging between 1.5 and 3.5). This indicates a very high species richness and a well-balanced community at the Mlyn station. The ecosystem is complex enough to be resilient against external environmental pressures.
The score of 0.740 (close to the maximum of 1.0) means there is a 74% chance that two random organisms from your sample will be different species. This proves that the Pavlivka River at this point is not dominated by a single "pollution-tolerant" species, which is a key indicator of a clean and healthy environment.
Conclusion: The combination of a high Shannon Index and a near-perfect Simpson Index confirms that the Pavlivka station serves as a biodiversity hotspot. The data suggests minimal anthropogenic stress and a high capacity for self-regulation within the aquatic community.

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
