import openai
import os
from dotenv import load_dotenv

# Load your OpenAI key from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_report(vuln_type, scope, steps, impact, fix):
    prompt = f"""
You're an experienced bug bounty hunter. Create a professional bug report.

Vulnerability Type: {vuln_type}
Scope/Asset: {scope}
Steps to Reproduce: {steps}
Impact: {impact}
Suggested Fix: {fix}

Format the output:

**Title:**  
[Concise title]

**Summary:**  
[What is the issue? Why is it important?]

**Steps to Reproduce:**  
[List clearly]

**Impact:**  
[Explain consequences]

**Remediation:**  
[Fix suggestion]
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
