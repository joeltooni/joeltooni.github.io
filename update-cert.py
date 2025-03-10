import json

cert_file = "certifications.json"

def add_certification():
    name = input("Enter Certification Name: ")
    issuer = input("Enter Issuer: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    link = input("Enter Certificate Link: ")

    try:
        with open(cert_file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"certifications": []}

    data["certifications"].append({
        "name": name,
        "issuer": issuer,
        "date": date,
        "link": link
    })

    with open(cert_file, "w") as f:
        json.dump(data, f, indent=4)

    print("Certification added successfully!")

if __name__ == "__main__":
    add_certification()
