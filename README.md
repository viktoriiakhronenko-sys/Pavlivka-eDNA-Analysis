# eDNA Biodiversity Visualization Script

This script processes merged MegaBLAST and BOLD datasets to visualize species diversity from environmental DNA (eDNA) samples.

## Features
1. **Taxonomic Pie Chart**: Generates a `.png` file showing the percentage distribution of Phyla.
2. **Krona Plot Export**: Generates a `.txt` file formatted for KronaTools to create interactive hierarchical charts.



## Requirements
- Python 3.x
- Pandas
- Matplotlib

## Usage
1. Place your `Final_eDNA_Report_Pavlivka.csv` in the script directory.
2. Run the script:
   ```bash
   python visualize_edna.py
