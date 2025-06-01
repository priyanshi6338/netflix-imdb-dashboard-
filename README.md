# 🎬 Netflix IMDb Dashboard with Power BI

## 📌 Project Objective
Analyze and visualize Netflix content using IMDb ratings and metadata to uncover trends in content type, certifications, votes, and runtime. This interactive dashboard helps understand the distribution and performance of movies and TV shows over time.

---

## 📊 Dashboard Overview

### 💡 KPIs / Cards
- **Total IMDb Votes**: `123M+`
- **Average IMDb Score**: `6.53`
- **Content Breakdown**: Movies vs. Shows

### 🧁 Donut Chart
- **Content Type Distribution**
  - Movies: 60.3%
  - Shows: 39.7%

### 🪪 Bar Charts
- **Top Age Certifications by Title Count**
- **Average Runtime by Age Certification**

### 🕰️ Column Chart
- **Average IMDb Score by Decade**

### 🔘 Scatter Plot
- **IMDb Score vs IMDb Votes**
  - **Bubble Size** = Runtime (min)

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `netflix_imdb_cleaned.csv` | Cleaned dataset ready for Power BI |
| `netflix_analysis.py` | Python code for data cleaning and transformation |
| `Netflix_Imdb_Dashboard.pbix` | Power BI dashboard file |
| `README.md` | Project description and details |

---

## 🧹 Data Cleaning Highlights (Python)
- Removed rows with missing IMDb scores and runtime
- Converted columns to correct types (e.g., `release_year`, `runtime`)
- Created decade column for grouped analysis
- Exported cleaned data for visualization in Power BI

---

## 📦 Tools & Technologies
- **Python**: Pandas, NumPy
- **Power BI**: Dashboard and visualizations
- **GitHub**: Version control and hosting
- Dataset: [Kaggle – Netflix IMDb Scores](https://www.kaggle.com/datasets/thedevastator/netflix-imdb-scores)

---

## 📌 Key Insights
- Content with `PG-13` and `R` ratings tends to have longer runtimes.
- Most titles fall under specific certifications like `TV-MA`, `PG`, and `Unrated`.
- IMDb scores have remained relatively steady across decades.
- Movies have received more votes on average compared to shows.

---

## 👩‍💻 Author

**Priyanshi Dadhich**  
B.Tech CSE (AIML), VIT Bhopal  
GitHub: [@priyanshi6338](https://github.com/priyanshi6338)  


---

⭐ If you found this project helpful, feel free to **star** it and check out more of my work!
