from scholarly import scholarly
import json

AUTHOR_ID = 'E5-emBEAAAAJ'

def fetch_data():
    author = scholarly.search_author_id(AUTHOR_ID)
    scholarly.fill(author, sections=['counts', 'publications'])
    
    data = {
        "total_citations": author.get("citedby", 0),
        "publications": {}
    }
    
    for pub in author['publications']:
        title = pub['bib'].get('title', '')
        citations = pub.get('num_citations', 0)
        data["publications"][title] = citations
        
    with open('citations_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    fetch_data()
