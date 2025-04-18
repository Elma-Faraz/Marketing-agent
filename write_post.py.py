from utils import final_output

user_guidelines = """
Coforge Brand Prompt Guide for Content Generation
LinkedIn Post Prompt Template

Write a LinkedIn post of 400-500 words for Coforge readers on the topic: "{insert topic here}".
Follow this structure:
- Hook (20–30 words): Start with a question or attention-grabbing statement.
- Introduction (50–100 words): Contextualize the topic within the industry/domain.
- Industry Trends: Provide 3–5 bullet points.
- Coforge's Point of View: 100–150 words of insights or unique perspectives.
- CTA (Call to Action): 25–50 words encouraging engagement.

Tone:  concise, and informative. Use SEO-rich keywords and include technical details if relevant.

SEO Blog Prompt Template

Write an SEO-friendly blog post of around 800-1000 words on the topic: "{insert topic here}". Focus on the latest advancements and their impact on the "{domain}" industry.

Structure:
- Introduction: Define topic and its relevance.
- Trends: Explore AI, ML, IoT, Blockchain, etc.
- Use Cases: Provide real-world examples, include Coforge solutions.
- Customer Experience: Highlight improvements due to technology.
- Disruptors: Mention startups and innovation.
- Challenges & Opportunities: Discuss key hurdles and benefits.
- Future Outlook: Predict future trends and technologies.
- CTA: Encourage readers to engage or contact Coforge.

Tone: Professional, informative, and aligned with Coforge’s brand. Use SEO-rich keywords and technical details.

Brand Voice Notes

- Objective: Set clear goals for the content.
- Target Audience: Coforge readers and professionals in relevant domains.
- Tone: Informative, confident, professional.
- Examples: Include case studies or statistics for credibility.
- Technicality: Adapt based on audience — beginner, intermediate, or advanced.
- SEO: Use relevant keywords to enhance visibility.
- Review: Proofread and ensure alignment with Coforge standards



Styling Guide
Title
•	Font: Century
•	Size: 16
•	Bold: Yes
•	Alignment: Center
•	Color: Blue
Heading 1
•	Font: Calibri
•	Size: 14
•	Bold: Yes
•	Alignment: Left
•	Color: Black
Heading 2
•	Font: Calibri
•	Size: 12
•	Italic: Yes
•	Alignment: Left
•	Color: Black
Paragraph
•	Font: Calibri
•	Size: 12
•	Alignment: Left
•	Spacing After: 6
•	Color: Black
Bullet
•	Font: Calibri
•	Size: 12
•	Alignment: Left
•	Color: Black
Hyperlink
•	Font: Calibri
•	Color: Blue
•	Underline: Yes
"""

user_inst = """
"Generate the content introducing TARA, Coforge’s AI-powered chatbot designed to assist employees with HR and IT-related queries. The post should highlight the key capabilities of TARA, including:
•	Providing information on HR policies
•	Helping employees apply for leaves and check attendance
•	Answering HR-related questions
•	Assisting with IT-related queries
•	Facilitating IT service request and incident management
•	Being available 24/7 for instant support
The tone should be professional yet engaging, emphasizing how TARA enhances the employee experience by making HR and IT support seamless and efficient. The post should encourage employees to explore TARA and share their experiences in the comments. Keep the length between 150-300 words and include relevant industry hashtags like #AI #HRTech #Chatbot #EmployeeExperience."*
"""
configs = {
        "length": "200 words",
        "tone": "Professional",
        "target_audience": "Tech Professionals",
        "technicality": "Intermediate",
        "content_type": "LinkedIn Post"
    }

output_path = "output_files/generated_post.docx"

results = final_output(user_guidelines, user_inst, configs, "testtt.docx", "English", True, "gen_image1.jpeg")

print(results)