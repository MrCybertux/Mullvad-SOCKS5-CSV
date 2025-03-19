import csv

# Mapping of ISO codes to full country names
country_name_mapping = {
    "al": "Albania",
    "at": "Austria",
    "au": "Australia",
    "be": "Belgium",
    "bg": "Bulgaria",
    "br": "Brazil",
    "ca": "Canada",
    "ch": "Switzerland",
    "cl": "Chile",
    "co": "Colombia",
    "cy": "Cyprus",
    "cz": "Czech Republic",
    "de": "Germany",
    "dk": "Denmark",
    "ee": "Estonia",
    "es": "Spain",
    "fi": "Finland",
    "fr": "France",
    "gb": "United Kingdom",
    "gr": "Greece",
    "hk": "Hong Kong",
    "hr": "Croatia",
    "hu": "Hungary",
    "id": "Indonesia",
    "ie": "Ireland",
    "il": "Israel",
    "it": "Italy",
    "jp": "Japan",
    "mx": "Mexico",
    "my": "Malaysia",
    "ng": "Nigeria",
    "nl": "Netherlands",
    "no": "Norway",
    "nz": "New Zealand",
    "pe": "Peru",
    "ph": "Philippines",
    "pl": "Poland",
    "pt": "Portugal",
    "ro": "Romania",
    "rs": "Serbia",
    "se": "Sweden",
    "sg": "Singapore",
    "si": "Slovenia",
    "sk": "Slovakia",
    "th": "Thailand",
    "tr": "Turkey",
    "ua": "Ukraine",
    "us": "United States",
    "za": "South Africa"
}

# Mapping of countries to continents
continent_mapping = {
    "Albania": "Europe",
    "Austria": "Europe",
    "Australia": "Oceania",
    "Belgium": "Europe",
    "Bulgaria": "Europe",
    "Brazil": "South America",
    "Canada": "North America",
    "Switzerland": "Europe",
    "Chile": "South America",
    "Colombia": "South America",
    "Cyprus": "Europe",
    "Czech Republic": "Europe",
    "Germany": "Europe",
    "Denmark": "Europe",
    "Estonia": "Europe",
    "Spain": "Europe",
    "Finland": "Europe",
    "France": "Europe",
    "United Kingdom": "Europe",
    "Greece": "Europe",
    "Hong Kong": "Asia",
    "Croatia": "Europe",
    "Hungary": "Europe",
    "Indonesia": "Asia",
    "Ireland": "Europe",
    "Israel": "Asia",
    "Italy": "Europe",
    "Japan": "Asia",
    "Mexico": "North America",
    "Malaysia": "Asia",
    "Nigeria": "Africa",
    "Netherlands": "Europe",
    "Norway": "Europe",
    "New Zealand": "Oceania",
    "Peru": "South America",
    "Philippines": "Asia",
    "Poland": "Europe",
    "Portugal": "Europe",
    "Romania": "Europe",
    "Serbia": "Europe",
    "Sweden": "Europe",
    "Singapore": "Asia",
    "Slovenia": "Europe",
    "Slovakia": "Europe",
    "Thailand": "Asia",
    "Turkey": "Asia",
    "Ukraine": "Europe",
    "United States": "North America",
    "South Africa": "Africa"
}

# Input and output files
input_file = "mullvad_hostnames.csv"
output_file = "mullvad_hostnames_with_full_names_and_continents.csv"

# Read the CSV, replace ISO codes with full names and add continent column
with open(input_file, "r", newline="") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header with the new column "Continent"
    header = next(reader)
    writer.writerow(header + ["Continent"])

    # Process each row
    for row in reader:
        country_code = row[0]
        hostname = row[1]
        
        # Get the full country name using the country code
        country_name = country_name_mapping.get(country_code, country_code)  # Fallback on code if name not found
        
        # Get the continent using the country name
        continent = continent_mapping.get(country_name, "Unknown")  # Fallback to "Unknown" if continent is not found
        
        # Write the row with the country name and continent
        writer.writerow([country_name, hostname, continent])

print(f"New CSV file created: {output_file}")

