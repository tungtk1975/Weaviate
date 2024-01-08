import weaviate

# Weaviate instance details
weaviate_url = "http://localhost:8080"
client = weaviate.Client(url=weaviate_url)

# Define the class name
class_name = "Document"

# GraphQL query as a string
graphql_query = f"""
{{
  Get {{
    {class_name} {{
      text
      filename
    }}
  }}
}}
"""

# Function to perform the query and print results
def query_weaviate():
    try:
        results = client.query.raw(graphql_query)
        for result in results["data"]["Get"][class_name]:
            print("Filename:", result["filename"])
            print("-------------")
            print("Content:", result["text"])
            print("-------------")
    except Exception as e:
        print("Error during query:", e)

# Run the query function
query_weaviate()
