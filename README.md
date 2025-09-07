# 🎬 IMDb Top 100 Movies Web Scraper

This project demonstrates **web scraping with Python** to collect information about the Top 1000 movies on IMDb.
It extracts movie details such as name, release year, duration, rating, metascore, votes, and gross earnings, then saves them into an **Excel file**.

---

## 🚀 Features

* Scrapes IMDb's *Top 1000 Movies* page.
* Extracts the following data:

  * 🎥 Movie Title
  * 📅 Release Year
  * ⏱️ Runtime (minutes)
  * ⭐ IMDb Rating
  * 📝 Metascore
  * 🗳️ Number of Votes
  * 💰 Gross Collection
* Stores the results in a **Pandas DataFrame**.
* Exports the dataset into an **Excel file (Top\_100\_IMDB\_Movies.xlsx)**.

---

## 🛠️ Requirements

Install the required libraries before running the script:

```bash
pip install requests beautifulsoup4 pandas numpy openpyxl
```

---

## 📂 How It Works

1. The script sends an HTTP request to IMDb's *Top 1000 Movies* page.
2. Parses the HTML content using **BeautifulSoup**.
3. Extracts relevant movie information.
4. Saves the collected data into an Excel file.

---

## ▶️ Usage

Run the script with:

```bash
python imdb_scraper.py
```

After execution, the results will be available in:

```
Top_100_IMDB_Movies.xlsx
```

---

## 📊 Example Output

| Movie Title     | Year | Runtime | IMDb Rating | Metascore | Votes     | Gross         |
| --------------- | ---- | ------- | ----------- | --------- | --------- | ------------- |
| Avatar          | 2009 | 162     | 7.8         | 83        | 1,200,000 | \$760,507,625 |
| The Dark Knight | 2008 | 152     | 9.0         | 84        | 2,500,000 | \$534,858,444 |
| Inception       | 2010 | 148     | 8.8         | 74        | 2,300,000 | \$292,576,195 |

---

## 📎 Related Projects

If you are interested in movie-based projects, check out my other repository:
👉 [Movie Recommendation System](https://github.com/begumsara/movieRecommendationSystem/tree/main)

---

## 📜 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute this project.
