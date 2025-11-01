from serpapi import GoogleSearch
import matplotlib.pyplot as plt

API_KEY = "eb71788a2b3035cd005b8de32a7c4ef7a6b0f1403661a878015d1d6020e24efe"
KEYWORDS = ["gachagua", "ruto"]


def get_google_count(keyword):
    params = {
        "engine": "google",
        "q": keyword,
        "gl": "ke",  # Kenya region
        "api_key": API_KEY,
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    count = results.get("search_information", {}).get("total_results")
    if count is not None:
        return int(count)
    else:
        print(f"Could not get count for '{keyword}'")
        return None


def plot_pie_chart(counts):
    labels = []
    sizes = []
    for key, value in counts.items():
        if value is not None:
            labels.append(key)
            sizes.append(value)

    if not sizes:
        print("No data to plot pie chart.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=['#66b3ff','#ff9999'])
    plt.title("Search Result Count Distribution (gachagua vs ruto)")
    plt.axis("equal")  # Equal aspect ratio for circular pie
    plt.show()


def main():
    print("Fetching counts for keywords...")
    counts = {}
    for kw in KEYWORDS:
        count = get_google_count(kw)
        counts[kw] = count
        print(f"{kw}: {count}")

    plot_pie_chart(counts)


if __name__ == "__main__":
    main()
