import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load your joined dataset
# Replace 'final_report.csv' with your actual filename
df = pd.read_csv('Final_eDNA_Report_Pavlivka.csv')

# --- PART 1: TAXONOMIC COMPOSITION (PIE CHART) ---
def generate_pie_chart(data):
    # Group by Phylum and count occurrences
    tax_counts = data['Phylum'].value_counts()
    
    plt.figure(figsize=(10, 8))
    tax_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='Set3')
    plt.title('Taxonomic Composition by Phylum (eDNA Pavlovka)')
    plt.ylabel('')  # Remove default ylabel
    plt.tight_layout()
    plt.savefig('taxonomic_pie_chart.png')
    print("✓ Pie chart saved as 'taxonomic_pie_chart.png'")

# --- PART 2: KRONA PLOT PREPARATION ---
def generate_krona_data(data):
    # Krona requires a specific format: [Count] [Level 1] [Level 2] ... [Level N]
    # We will use 'Hits_Count' as the magnitude
    krona_columns = ['Hits_Count', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'BOLD_Species']
    
    # Fill NaN values to avoid errors in visualization
    krona_df = data[krona_columns].fillna('Unclassified')
    
    # Save as a tab-separated file for Krona Tools or online upload
    krona_df.to_csv('krona_input.txt', sep='\t', index=False, header=False)
    print("✓ Data for Krona saved as 'krona_input.txt'")
    print("Note: Upload 'krona_input.txt' to KronaTools or use Galaxy Krona Pie Chart tool.")

# Run functions
if __name__ == "__main__":
    generate_pie_chart(df)
    generate_krona_data(df)
