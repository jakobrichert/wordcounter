"""
Views for word counter application.
Provides text analysis including word count, character count, and frequency analysis.
"""
from django.shortcuts import render
import operator
import re


def home(request):
    """Render the home page with text input form."""
    return render(request, 'home.html')


def about(request):
    """Render the about page."""
    return render(request, 'about.html')


def count(request):
    """
    Process submitted text and return detailed word analysis.

    Analyzes:
    - Total word count
    - Individual word frequencies
    - Character count (with and without spaces)
    - Sentence count
    - Average word length
    - Reading time estimate
    """
    fulltext = request.GET.get('fulltext', '')

    # Basic counts
    wordlist = fulltext.split()
    word_count = len(wordlist)

    # Character counts
    char_count_with_spaces = len(fulltext)
    char_count_no_spaces = len(fulltext.replace(' ', '').replace('\n', '').replace('\t', ''))

    # Sentence count (approximate)
    sentence_count = len(re.findall(r'[.!?]+', fulltext)) or 1

    # Average word length
    avg_word_length = round(sum(len(word) for word in wordlist) / word_count, 2) if word_count > 0 else 0

    # Reading time (average reading speed: 200 words per minute)
    reading_time_minutes = round(word_count / 200, 1) if word_count > 0 else 0

    # Word frequency analysis
    word_frequency = {}
    for word in wordlist:
        # Clean and normalize words
        cleaned_word = re.sub(r'[^\w\s]', '', word.lower())
        if cleaned_word:  # Only count non-empty words
            if cleaned_word in word_frequency:
                word_frequency[cleaned_word] += 1
            else:
                word_frequency[cleaned_word] = 1

    # Sort words by frequency (descending)
    sorted_words = sorted(word_frequency.items(), key=operator.itemgetter(1), reverse=True)

    # Get unique word count
    unique_word_count = len(word_frequency)

    context = {
        'fulltext': fulltext,
        'count': word_count,
        'sortedwords': sorted_words,
        'char_with_spaces': char_count_with_spaces,
        'char_no_spaces': char_count_no_spaces,
        'sentence_count': sentence_count,
        'unique_words': unique_word_count,
        'avg_word_length': avg_word_length,
        'reading_time': reading_time_minutes,
    }

    return render(request, 'count.html', context)
