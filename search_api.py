import json
import os

def search_public_apis(keyword: str, category: str = None) -> list:
    """
    Search the public_apis.json database for APIs.

    :param keyword: A keyword to search for in the API name or Description.
    :param category: Optional category to filter by.
    :return: A list of up to 10 matching API objects.
    """
    # Load the JSON database
    # Assuming public_apis.json is in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'public_apis.json')

    if not os.path.exists(json_path):
        return []

    with open(json_path, 'r', encoding='utf-8') as f:
        apis = json.load(f)

    keyword_lower = keyword.lower()
    category_lower = category.lower() if category else None

    results = []

    for api in apis:
        # Check category match if category is provided
        if category_lower and api.get('Category', '').lower() != category_lower:
            continue

        # Check keyword match in API name or Description
        api_name = api.get('API', '').lower()
        api_desc = api.get('Description', '').lower()

        if keyword_lower in api_name or keyword_lower in api_desc:
            results.append(api)

            # Stop if we hit the limit of 10
            if len(results) >= 10:
                break

    return results
