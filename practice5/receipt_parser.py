import re
import json


def parse_receipt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Extract prices
    prices = re.findall(r"\d+\s?\d*,\d{2}", text)

    # 2. Extract product names
    product_pattern = r"\d+\.\n(.+)"
    products = re.findall(product_pattern, text)

    # 3. Total amount
    total_match = re.search(r"ИТОГО:\s*\n?\s*([\d\s,]+)", text)
    total = total_match.group(1) if total_match else None

    # 4. Date and time
    datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}", text)
    datetime = datetime_match.group(0) if datetime_match else None

    # 5. Payment method
    payment_match = re.search(r"Банковская карта", text)
    payment = "Bank Card" if payment_match else "Unknown"

    data = {
        "products": products,
        "prices": prices,
        "total": total,
        "datetime": datetime,
        "payment_method": payment
    }

    return data


def main():
    data = parse_receipt("raw.txt")

    print("Products:")
    for p in data["products"]:
        print("-", p)

    print("\nPrices:", data["prices"])
    print("Total:", data["total"])
    print("DateTime:", data["datetime"])
    print("Payment:", data["payment_method"])

    print("\nJSON Output:")
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()