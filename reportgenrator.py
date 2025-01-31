import pandas as pd
from fpdf import FPDF

# Step 1: Read Data from a File
def read_data(file_path):
    # Assuming the file is a CSV, you can modify this to read other formats
    data = pd.read_csv(file_path)
    return data

# Step 2: Analyze Data
def analyze_data(data):
    # Example analysis: Calculate mean, max, min, etc.
    analysis_results = {
        'mean': data.mean(),
        'max': data.max(),
        'min': data.min(),
        'std_dev': data.std()
    }
    return analysis_results

# Step 3: Generate PDF Report
def generate_pdf_report(analysis_results, output_file='report.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add a title
    pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align='C')

    # Add analysis results
    pdf.ln(10)
    pdf.set_font("Arial", size=10)

    for key, value in analysis_results.items():
        # Convert Series to string and remove dtype information
        if isinstance(value, pd.Series):
            value_str = value.to_string(index=False)  # Exclude the index
        else:
            value_str = str(value)
        
        pdf.cell(200, 10, txt=f"{key}: {value_str}", ln=True)

    # Save the PDF
    pdf.output(output_file)

# Main Function
def main():
    # File path to the data file
    file_path = 'Python\data.csv'  # Change this to your file path

    # Step 1: Read Data
    data = read_data(file_path)

    # Step 2: Analyze Data
    analysis_results = analyze_data(data)

    # Step 3: Generate PDF Report
    generate_pdf_report(analysis_results)

    print(f"PDF report generated successfully: report.pdf")

if __name__ == "__main__":
    main()