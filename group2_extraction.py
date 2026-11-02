import re
import json
import os

# Creates a sample file with test data
def create_sample_file():
    data = """
    FROM: rimzino@gmail.com
    MESSAGE: I am looking for a new laptop.
    Brand: Dell.
    Price is around $1200.
    
    FROM: imanesahib@gmail.com
    MESSAGE: The new phone is great.
    Brand: Samsung.
    I paid $800 for it!
    
    SPAM: fake.user@bad-domain.net sent a virus link.
    Brand: Unknown.
    Price: $0.
    """
    
    file = open("social_media_data.txt", "w")
    file.write(data)
    file.close()
    print("--- File 'social_media_data.txt' has been created ---")

# Main extraction function
def run_extraction_algorithm():
    if not os.path.exists("social_media_data.txt"):
        create_sample_file()
    
    f = open("social_media_data.txt", "r")
    text_content = f.read()
    f.close()

    print("\n--- STARTING DATA EXTRACTION ---")

    # Extract emails
    print("Scanning for emails...")
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    found_emails = re.findall(email_regex, text_content)
    print(f" -> Found {len(found_emails)} emails.")

    # Extract prices
    print("Scanning for prices...")
    price_regex = r'\$\d+'
    found_prices = re.findall(price_regex, text_content)
    print(f" -> Found {len(found_prices)} prices.")

    # Extract brands
    print("Scanning for brands...")
    brand_regex = r'Brand:\s*(\w+)'
    found_brands = re.findall(brand_regex, text_content)
    print(f" -> Found {len(found_brands)} brands.")

    # Classify and save the data
    print("\n--- CLASSIFYING DATA ---")
    
    output_data = {
        "HIGH_SECURITY": {
            "description": "User personal data (Emails)",
            "data": found_emails
        },
        "LOW_SECURITY": {
            "description": "Public commercial data (Prices & Brands)",
            "data": {
                "prices_list": found_prices,
                "brands_list": found_brands
            }
        }
    }

    save_file = open("classified_results.json", "w")
    json.dump(output_data, save_file, indent=4)
    save_file.close()
    
    print("Success! Data saved to 'classified_results.json'")

# Run the script
if __name__ == "__main__":
    run_extraction_algorithm()