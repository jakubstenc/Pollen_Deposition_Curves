import pandas as pd
import os
import matplotlib.pyplot as plt
from IPython.display import display, Image, HTML

def process_payload(flat_data_table):
    """
    Processes a flat list of data dictionaries:
    1. Creates a Pandas DataFrame.
    2. Displays the table.
    3. Verifies and plots figures.
    """

    if not flat_data_table:
        print("No data to process.")
        return

    # a) Create DataFrame
    df = pd.DataFrame(flat_data_table)

    # b) Reorder columns for readability
    preferred_order = [
        'bibtex_nick', 'Species', 'time_point_h', 'variable', 'value',
        'variation_value', 'variation_type', 'series_name', 'source_figure',
        'Family', 'breeding_system', 'total_longevity', 'ovule_number', 'pollen_number',
        'image_path', 'methods_notes'
    ]
    # Get existing columns and reorder, appending any new ones at the end
    cols = [c for c in preferred_order if c in df.columns] + [c for c in df.columns if c not in preferred_order]
    df = df[cols]

    # cExport to CSV
    csv_dir = "data/csv"
    os.makedirs(csv_dir, exist_ok=True)
    
    if 'bibtex_nick' in df.columns and not df.empty:
        nick = df['bibtex_nick'].iloc[0]
        # Sanitize filename just in case
        safe_nick = "".join([c for c in nick if c.isalnum() or c in ('-','_')])
        csv_path = os.path.join(csv_dir, f"{safe_nick}.csv")
        df.to_csv(csv_path, index=False)
        print(f"**💾 Data exported to:** `{csv_path}`")
    
    # c) Display the Main Table
    print("### 📄 Extracted Data Table (Ready for Spreadsheet)")
    # Use HTML display for scrolling support, as reflected in the user's snippet
    print("<div style='max-height: 400px; overflow: auto;'>" + df.to_html(index=False) + "</div>")

    # d) Image & Plot Verification Loop
    # print("\n<hr>")
    print("### 🖼️ Figure Verification")

    if 'image_path' in df.columns and 'source_figure' in df.columns:
        unique_images = df[['image_path', 'source_figure']].drop_duplicates()

        for _, img_row in unique_images.iterrows():
            path = img_row['image_path']
            fig_name = img_row['source_figure']

            print(f"\n#### Source: {fig_name} ({path})")

            # Check if image exists
            if os.path.exists(path):
                try:
                    import matplotlib.image as mpimg
                    img = mpimg.imread(path)
                    
                    # Create plot for reconstruction
                    # Filter by both path AND figure name to handle multi-panel images
                    fig_data = df[(df['image_path'] == path) & (df['source_figure'] == fig_name)]
                    
                    # Setup figure: Left = Image, Right = Plot
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
                    
                    # Left: Image
                    ax1.imshow(img)
                    ax1.set_title(f"Source: {fig_name}")
                    ax1.axis('off')
                    
                    # Right: Plot
                    # Get unique series
                    if 'series_name' in fig_data.columns:
                        series_list = fig_data['series_name'].unique()
                        for series in series_list:
                            s_data = fig_data[fig_data['series_name'] == series].sort_values('time_point_h')
                            
                            x = s_data['time_point_h']
                            y = s_data['value']
                            yerr = s_data['variation_value'] if 'variation_value' in s_data.columns else None
                            
                            ax2.errorbar(x, y, yerr=yerr, fmt='-o', label=series, capsize=3)
                        
                        ax2.legend()
                    else:
                        # No series, just plot all
                        s_data = fig_data.sort_values('time_point_h')
                        ax2.plot(s_data['time_point_h'], s_data['value'], '-o')

                    variable_label = fig_data['variable'].iloc[0] if 'variable' in fig_data.columns else "Value"
                    ax2.set_ylabel(variable_label)
                    ax2.set_xlabel("Time (h)")
                    ax2.set_title(f"Reconstruction: {fig_name}")
                    ax2.grid(True, linestyle='--', alpha=0.7)
                    
                    plt.tight_layout()
                    plt.show()

                except Exception as e:
                    print(f"Could not create verification plot: {e}")

            else:
                print(f"❌ Error: Image not found at path: {path}")
                print("Please check that your local folder structure matches the 'bibtex_nick' exactly (case-sensitive).")
    else:
        print("Skipping visualization: 'image_path' or 'source_figure' columns missing.")

    print("\n✅ Process Complete.")
