from scholarly import scholarly
import json
import os

# Your Google Scholar ID from your URL
AUTHOR_ID = 'E5-emBEAAAAJ'

def fetch_data():
    try:
        # Fetch the author profile and fill in the publications
        author = scholarly.search_author_id(AUTHOR_ID)
        scholarly.fill(author, sections=['counts', 'publications'])
        
        data = {
            "total_citations": author.get("citedby", 0),
            "publications": {}
        }
        
        # Extract citations for each paper
        for pub in author['publications']:
            title = pub['bib'].get('title', '')
            citations = pub.get('num_citations', 0)
            if title:
                data["publications"][title] = citations
                
        # Save to a JSON file
        with open('citations_data.json', 'w') as f:
            json.dump(data, f, indent=4)
            
        print("Successfully updated citations_data.json")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_data()