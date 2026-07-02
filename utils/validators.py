from typing import Optional


class TextValidator:
    """Text validation utilities."""
    
    @staticmethod
    def is_valid_name(name: str) -> bool:
        """Validate user name."""
        if not name or len(name) < 2 or len(name) > 50:
            return False
        return name.replace(" ", "").isalpha()
    
    @staticmethod
    def is_valid_class(class_level: str) -> bool:
        """Validate class level."""
        valid_classes = [f"{i}-sinf" for i in range(1, 12)]
        return class_level in valid_classes
    
    @staticmethod
    def normalize_text(text: str) -> str:
        """Normalize text input."""
        return text.strip().lower()
