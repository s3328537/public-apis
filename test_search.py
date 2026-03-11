from search_api import search_public_apis
import json

print("Test 1: Search for 'dog' without category")
res1 = search_public_apis("dog")
print(json.dumps(res1, indent=2))

print("\nTest 2: Search for 'cat' with category 'Animals'")
res2 = search_public_apis("cat", "Animals")
print(json.dumps(res2, indent=2))

print("\nTest 3: Limit 10")
res3 = search_public_apis("a")
print(len(res3))
