import openai

# Setup your OpenAI API key
openai.api_key = 'your_openai_api_key_here'

def parse_content_and_recommend(content):
    """
    Parse the given content and generate recommendations.
    
    Parameters:
    - content (str): The text of the article or promotion.
    
    Returns:
    - str: Recommendations for agents and customers.
    """
    
    try:
        prompt = ("Given the following article or promotion content, "
                  "provide recommendations for both agents and customers:\n\n"
                  f"{content}\n\n"
                  "Recommendations:")
        
        response = openai.Completion.create(
            engine='text-davinci-003',  # Consider using the latest and most capable model
            prompt=prompt,
            max_tokens=150,  # You might need to adjust based on expected output length
            n=1,
            stop=None,
            temperature=0.5  # Lower for more deterministic output
        )
        
        recommendations = response.choices[0].text.strip()
        return recommendations
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Failed to generate recommendations."

# Example content
content = """
Promotion: Get 20% off on all electronics this weekend. This summer, upgrade your gadgets 
with our special discount. Offer is valid from Friday 8 PM to Sunday midnight. 
"""

recommendations = parse_content_and_recommend(content)
print("Generated Recommendations:\n", recommendations)
