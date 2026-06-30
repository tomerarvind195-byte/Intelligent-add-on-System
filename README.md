# 🧠 Intelligent Add-on System — AI-Based Product Recommendation

> A Python-based intelligent recommendation system that suggests relevant products to users based on their preferences and interaction history — powered by AI logic and keyword matching.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![AI](https://img.shields.io/badge/AI-Recommendation%20Engine-purple?style=flat)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=flat&logo=windowsterminal)
![Type](https://img.shields.io/badge/Type-Recommendation%20System-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

---

## 📸 Demo

> _

```
================================================
     Intelligent Add-on Recommendation System __
================================================

Welcome! Let me help you find the best products.

Enter your interests (e.g. gaming, coding, music): coding

Analyzing your preferences...

🎯 Top Recommendations for You:
─────────────────────────────────────────────
  1. Mechanical Keyboard        ⭐ 98% Match
     Category: Accessories | Price: ₹2,499
     "Perfect for coders who type for long hours"

  2. Dual Monitor Setup         ⭐ 94% Match
     Category: Hardware | Price: ₹8,999
     "Boost your productivity with dual screens"

  3. VS Code Premium Extensions ⭐ 91% Match
     Category: Software | Price: ₹499
     "Must-have extensions for every developer"
─────────────────────────────────────────────
Would you like more recommendations? (yes/no):
```

---

## 📋 About The Project

An **AI-based intelligent product recommendation system** built in Python that analyzes user preferences and suggests the most relevant products using keyword matching, preference scoring, and rule-based filtering logic.

Inspired by real-world recommendation engines used in e-commerce platforms like Amazon and Flipkart — built from scratch without heavy ML frameworks.

**Key Highlights:**
- Analyzes user input to detect preferences and interests
- Scores and ranks products based on relevance to user profile
- Handles 5+ product categories with 20+ products in the dataset
- Intelligent filtering — eliminates irrelevant products automatically
- Continuous session — refine recommendations based on feedback

---

## ✨ Features

- ✅ AI-powered product scoring & ranking engine
- ✅ Keyword-based preference detection from user input
- ✅ 5+ product categories (Electronics, Accessories, Software, Books, Tools)
- ✅ Match percentage shown for each recommendation
- ✅ Feedback loop — user can refine results in same session
- ✅ Handles unknown inputs with smart fallback suggestions
- ✅ 100% pure Python — no external ML libraries needed

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| Core Libraries | `random`, `os`, `re`, `collections` |
| Algorithm | Keyword matching + weighted scoring |
| Data Storage | Python dictionaries / lists |
| Interface | Command Line (CLI) |
| Version Control | Git & GitHub |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/tomerarvind195-byte/intelligent-addon-system.git
cd intelligent-addon-system

# 2. Run the system
python main.py
```

No `pip install` needed — pure Python only!

---

## 🧠 How the Recommendation Engine Works

```
User enters preferences (text input)
            │
            ▼
    Keyword Extraction
  (detect interest tags from input)
            │
            ▼
    Preference Scoring
  (match keywords against product tags)
            │
            ▼
    Weighted Ranking
  (score each product 0–100%)
            │
            ▼
    Filter & Sort
  (remove low-score products, sort by match %)
            │
            ▼
  Top Recommendations displayed to user
            │
            ▼
  User Feedback → Refine Results (optional)
```

---

## 📦 Product Categories

| Category | Examples |
|----------|---------|
| Electronics | Laptop, Headphones, Smartwatch |
| Accessories | Keyboard, Mouse, Monitor |
| Software | IDE Extensions, Antivirus, Design Tools |
| Books | Python Programming, AI/ML, Web Dev |
| Tools | CLI Tools, Productivity Apps, Dev Tools |

---

## 💡 Core Algorithm

```python
def calculate_match_score(user_keywords, product_tags):
    """
    Score a product based on how many of its tags
    match the user's detected keywords.
    Returns a match percentage (0-100).
    """
    if not product_tags:
        return 0

    matches = sum(1 for tag in product_tags if tag in user_keywords)
    score = (matches / len(product_tags)) * 100
    return round(score, 2)


def get_recommendations(user_input, product_database, top_n=5):
    """
    Extract keywords from user input,
    score all products, return top N results.
    """
    user_keywords = extract_keywords(user_input)
    scored_products = []

    for product in product_database:
        score = calculate_match_score(user_keywords, product['tags'])
        if score > 0:
            scored_products.append({**product, 'match': score})

    scored_products.sort(key=lambda x: x['match'], reverse=True)
    return scored_products[:top_n]
```

---

## 📁 Project Structure

```
intelligent-addon-system/
│
├── main.py              # Entry point — run this
├── engine.py            # Recommendation engine & scoring logic
├── extractor.py         # Keyword extraction from user input
├── products.py          # Product database (categories + tags)
├── display.py           # Terminal UI & formatted output
├── README.md
└── requirements.txt
```

---

## 🔮 Future Improvements

- [ ] Add basic ML-based scoring (future learning goal)
- [ ] Connect to a product dataset via CSV or JSON file
- [ ] Build a web interface using Django
- [ ] Add user login to save preference history across sessions
- [ ] Improve keyword extraction using regex and string processing
- [ ] Expand product categories and improve scoring algorithm

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/ml-engine`)
3. Commit your changes (`git commit -m 'Add ML-based scoring engine'`)
4. Push and open a Pull Request

---

## 👨‍💻 Author

**Arvind Kumar**
3rd Year B.Tech IT Student | Aspiring Software Engineer

- 🌐 [LinkedIn](https://www.linkedin.com/in/arvind-kumar-399a60338)
- 💻 [GitHub](https://github.com/tomerarvind195-byte)
- 📧 tomerarvind195@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> ⭐ Agar helpful laga toh **star** zaroor karo!
