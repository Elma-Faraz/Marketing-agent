from docx.shared import RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH 

# Language name to ISO code mapping
LANGUAGE_NAME_TO_CODE = {
    "english": "en",
    "hindi": "hi",
    "french": "fr",
    "german": "de",
    "spanish": "es",
    "chinese": "zh-Hans",
    "japanese": "ja",
    "russian": "ru",
    "italian": "it",
    "arabic": "ar",
    "portuguese": "pt",
    "korean": "ko",
    "bengali": "bn",
    "tamil": "ta",
    "telugu": "te",
    "marathi": "mr",
    # Add more as needed
}

# Define default styles.  
default_styles = {  
    "Title": {  
        "alignment": WD_ALIGN_PARAGRAPH.CENTER,  
        "bold": True, 
        "italic":False,
        "spacing_after": 0,
        "spacing_before": 0,
        "line_spacing": 1.15,
        "size": 28,  
        "font_name": "Segoe UI",  
        "color": RGBColor(0, 78, 146)  
    },  
    "Heading 1": {  
        "alignment": WD_ALIGN_PARAGRAPH.LEFT,  
        "bold": True,
        "italic":False,  
        "size": 16, 
        "spacing_after": 0,
        "spacing_before": 0,
        "line_spacing": 1.15,
        "font_name": "Cambria (Body)",  
        "color": RGBColor(241, 88, 64),
    },  
    "Heading 2": {  
        "alignment": WD_ALIGN_PARAGRAPH.LEFT,  
        "bold": True,
        "italic":False,  
        "size": 13, 
        "spacing_after": 0,
        "spacing_before": 0,
        "line_spacing": 1.15,
        "font_name": "Cambria (Body)",  
        "color": RGBColor(241, 88, 64)  
    },  
    "Bullet": {  
        "size": 11, 
        "bold":False,
        "italic":False,
        "spacing_after": 0,
        "spacing_before": 0,
        "line_spacing": 1.15,
        "font_name": "Cambria (Body)",  
        "color": RGBColor(0, 0, 0)  
    },  
    "Hyperlink": {  
        "color": RGBColor(255, 192, 0),  
        "underline": True,
        "bold": False,
        "italic": True,
        "spacing_after": 0,
        "spacing_before": 0,
        "line_spacing": 1.15,
        "size": 11,
        "font_name": "Cambria (Body)"  
    },  
    "Paragraph": {  
        "alignment": WD_ALIGN_PARAGRAPH.JUSTIFY,  
        "spacing_after": 12,  
        "spacing_before": 0,
        "italic":False,
        "bold":False,
        "line_spacing": 1.15,
        "size": 11,  
        "font_name": "Cambria (Body)",  
        "color": RGBColor(0, 0, 0)  
    }  
}
    