import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import re

def get_amazon_reviews(url, max_reviews=30):
    headers = {"User-Agent": UserAgent().random}
    reviews = []

    for page in range(1, 5):  # First 4 pages
        page_url = f"{url}/ref=cm_cr_getr_d_paging_btm_next_{page}?pageNumber={page}"
        res = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(res.content, "html.parser")

        review_blocks = soup.select("div[data-hook='review']")
        for block in review_blocks:
            text = block.select_one("span[data-hook='review-body']")
            if text:
                review = text.get_text(strip=True)
                reviews.append(review)
                if len(reviews) >= max_reviews:
                    return reviews
    return reviews

def filter_genuine_reviews(reviews):
    # Simple heuristic: longer, specific reviews are more likely genuine
    return [r for r in reviews if len(r.split()) > 12 and not re.search(r"scam|fake|worst|duplicate", r.lower())]

def summarize_reviews(reviews, num_sentences=3):
    text = " ".join(reviews)
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

if __name__ == "__main__":
    amazon_url = input("Enter full Amazon product URL (e.g. https://www.amazon.in/dp/B0C7JQ5YJ4): ").strip()
    print("Fetching and analyzing reviews...")

    all_reviews = get_amazon_reviews(amazon_url)
    genuine_reviews = filter_genuine_reviews(all_reviews)

    if not genuine_reviews:
        print("No genuine-looking reviews found.")
    else:
        summary = summarize_reviews(genuine_reviews)
        print("\nSummary of Genuine Reviews:")
        print(summary)
