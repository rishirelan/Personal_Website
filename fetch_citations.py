from scholarly import scholarly, ProxyGenerator
import json
import sys

AUTHOR_ID = 'E5-emBEAAAAJ'

def fetch_data():
    try:
        print("Setting up proxies...")
        pg = ProxyGenerator()
        # Use FreeProxies to avoid datacenter blocks
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        
        print("Fetching data from Google Scholar...")
        author = scholarly.search_author_id(AUTHOR_ID)
        scholarly.fill(author, sections=['counts', 'publications'])
        
        data = {
            "total_citations": author.get("citedby", 0),
            "publications": {}
        }
        
        for pub in author.get('publications', []):
            title = pub['bib'].get('title', '')
            citations = pub.get('num_citations', 0)
            if title:
                data["publications"][title] = citations
                
        with open('citations_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        print("Successfully updated citations_data.json")
        
    except Exception as e:
        print(f"Error fetching data: {e}")
        # Print more detail about the error if possible
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    fetch_data()
