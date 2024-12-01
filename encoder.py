"""
Module for encoding text into barcode symbols.
"""
from barcode_dictionary import BARCODE_DICT, is_valid_symbol

class EncodingError(Exception):
    """Custom exception for encoding errors."""
    pass

def validate_input(text):
    """
    Validate input text before encoding.
    
    Args:
        text (str): Input text to validate
        
    Returns:
        str: Validated text
        
    Raises:
        EncodingError: If text contains invalid characters
    """
    if not text:
        raise EncodingError("Input text cannot be empty")
    return text.upper()

def encode_text(text):
    """
    Convert text to barcode symbols with validation.
    
    Args:
        text (str): Input text to encode
        
    Returns:
        str: Encoded barcode sequence
        
    Raises:
        EncodingError: If encoding fails
    """
    try:
        text = validate_input(text)
        encoded_chars = []
        
        for char in text:
            if char in BARCODE_DICT:
                sequence = BARCODE_DICT[char]
                # Verify each symbol in the sequence
                if all(is_valid_symbol(symbol) for symbol in sequence):
                    encoded_chars.append(sequence)
                else:
                    raise EncodingError(f"Invalid symbol sequence for character: {char}")
            else:
                encoded_chars.append('?')
        
        # Join with separator, ensuring no double separators
        result = '𝄄'.join(filter(None, encoded_chars))
        return result if result else '?'
        
    except Exception as e:
        raise EncodingError(f"Encoding failed: {str(e)}")