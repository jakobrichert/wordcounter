# Advanced Word Counter

A powerful text analysis web application built with Django that provides comprehensive statistics and insights about your text content.

![Django](https://img.shields.io/badge/Django-2.2.28-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Features

### Comprehensive Text Analysis
- **Word Count**: Total and unique word counts
- **Character Analysis**: Character counts with and without spaces
- **Sentence Detection**: Automatic sentence counting
- **Average Word Length**: Calculate text complexity
- **Reading Time Estimation**: Based on average reading speed (200 WPM)
- **Word Frequency Analysis**: See which words appear most often
- **Smart Processing**: Intelligently handles punctuation and capitalization

### Modern User Interface
- Beautiful gradient design with responsive layout
- Mobile-friendly interface
- Visual statistics cards with real-time data
- Color-coded word frequency rankings (gold, silver, bronze for top 3)
- Clean, intuitive user experience

## Screenshots

The application features:
- A clean home page with text input area
- Comprehensive results page with statistical cards
- Detailed word frequency analysis with visual indicators
- Fully responsive design that works on all devices

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/jakobrichert/wordcounter.git
cd wordcounter
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Navigate to the project directory:
```bash
cd wordcount-project
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Open your browser and navigate to:
```
http://127.0.0.1:8000
```

## Usage

1. **Enter Text**: Paste or type your text into the text area on the home page
2. **Analyze**: Click the "Analyze Text" button
3. **View Results**: See comprehensive statistics including:
   - Total word count and unique words
   - Character counts
   - Sentence count
   - Average word length
   - Estimated reading time
   - Detailed word frequency breakdown

## Use Cases

- **Writers**: Check article or essay length and readability
- **Students**: Verify assignment word requirements
- **Content Creators**: Analyze and optimize content
- **SEO Professionals**: Optimize content for search engines
- **Researchers**: Analyze text patterns and word usage

## Technology Stack

- **Backend**: Django 2.2.28 (Python web framework)
- **Frontend**: HTML5, CSS3
- **Text Processing**: Python regular expressions
- **Database**: SQLite (default Django database)

## Project Structure

```
wordcounter/
├── wordcount-project/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── wordcount/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── wsgi.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── count.html
│   │   └── about.html
│   └── static/
│       └── css/
│           └── style.css
├── requirements.txt
├── .gitignore
└── README.md
```

## Features in Detail

### Word Frequency Analysis
The application processes text to show how many times each word appears, sorted by frequency. The top 3 most common words are highlighted with special colors (gold, silver, bronze).

### Reading Time Estimation
Calculates estimated reading time based on an average reading speed of 200 words per minute, helpful for content creators and writers.

### Smart Text Processing
- Removes punctuation for accurate word counting
- Handles capitalization (treats "Word" and "word" as the same)
- Intelligently detects sentence boundaries
- Accurately counts characters with various formatting

## Privacy

Your privacy is important. All text analysis happens locally on the server in real-time. Text is not stored, logged, or transmitted anywhere.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Author

Jakob Richert

## Acknowledgments

Built with Django, the high-level Python web framework that encourages rapid development and clean, pragmatic design.

---

**Star this repo if you find it useful!**
