# Import necessary standard libraries (limited set available)
import collections
import string
import re
import requests 
from bs4 import BeautifulSoup

def get_html_from_url(url):

  url = "https://guyguzman.com/"  # Example URL for demonstration
  try:
      response = requests.get(url, timeout=10, headers={'User-Agent': 'KeywordExtractorBot/1.0'})
      response.raise_for_status()  # Raise an exception for bad status codes
      return response.text
  except requests.exceptions.RequestException as e:
      print(f"Error fetching URL {url}: {e}")
      return None


def extract_text_from_html(html_content):

  soup = BeautifulSoup(html_content, 'html.parser')
  
  # Extract title
  title_tag = soup.find('title')
  title_text = title_tag.string if title_tag else ""
  
  # Extract meta description
  meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
  description_text = meta_desc_tag['content'] if meta_desc_tag else ""
  
  # Extract body text (simple version, could be refined)
  # Remove script and style elements
  for script_or_style in soup(["script", "style"]):
      script_or_style.decompose()
  body_text = soup.get_text(separator=' ', strip=True)
  
  print(f"\n--- Extracted Text ---\nTitle: {title_text}\nDescription: {description_text}\nBody Snippet: {body_text[:200]}...")  
  return title_text, description_text, body_text

def preprocess_text(text):
    """
    Performs basic text preprocessing: lowercase, remove punctuation, tokenize.
    Advanced steps like stopword removal and lemmatization require NLP libraries.
    """
    if not text:
        return []

    # Lowercase
    text = text.lower()

    # Remove punctuation (using string.punctuation)
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove numbers (optional, depending on use case)
    text = re.sub(r'\d+', '', text)

    # Tokenize (simple split by space)
    tokens = text.split()

    # --- Placeholder: Stopword removal and Lemmatization ---
    # In a real scenario:
    # nltk.download('stopwords', quiet=True)
    # nltk.download('punkt', quiet=True)
    # nltk.download('wordnet', quiet=True)
    # stop_words = set(stopwords.words('english')) # Assuming English
    # lemmatizer = WordNetLemmatizer()
    # tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and len(word) > 1] # Also remove single chars
    print("--- Placeholder: Stopword removal & Lemmatization would happen here (requires NLTK/SpaCy) ---")
    # Simple filter for demo purposes (remove very short words)
    tokens = [word for word in tokens if len(word) > 2]

    return tokens

def get_term_frequencies(tokens):
    """Calculates the frequency of each token."""
    return collections.Counter(tokens)

def extract_top_keywords(url, top_n=10):

    html = get_html_from_url(url)
    if not html:
        print("Failed to retrieve HTML.")
        return []

    title, description, body = extract_text_from_html(html)

    full_text = (title + ' ') * 3 + (description + ' ') * 2 + body
    tokens = preprocess_text(full_text)
    print(f"\nTokens after basic preprocessing: {tokens[:30]}...") 
    term_freqs = get_term_frequencies(tokens)

    most_common_keywords = term_freqs.most_common(top_n)

    print(f"\nTop {top_n} keywords based on frequency (conceptual):")
    for keyword, freq in most_common_keywords:
      print(f"- {keyword} (Frequency: {freq})")

    return [keyword for keyword, freq in most_common_keywords]

# --- Example Usage ---
target_url = "http://example.com/news/ai-advancements" # Replace with a real URL if running locally
top_keywords = extract_top_keywords(target_url, top_n=10)

print("\nFinal Top 10 Keywords:", top_keywords)