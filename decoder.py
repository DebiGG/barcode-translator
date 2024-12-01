"""
Module for decoding barcode symbols back to text.
"""
from barcode_dictionary import REVERSE_DICT, is_valid_sequence, is_valid_symbol

class DecodingError(Exception):
    """Custom exception for decoding errors."""
    pass

def validate_barcode(barcode):
    """
    Validate barcode sequence before decoding.
    
    Args:
        barcode (str): Barcode sequence to validate
        
    Returns:
        str: Validated barcode sequence
        
    Raises:
        DecodingError: If barcode is invalid
    """
    if not barcode:
        raise DecodingError("Barcode sequence cannot be empty")
    
    # Check for valid symbols
    if not all(char in {'𝄂', '𝄃', '𝄀', '𝄄', '𝄅'} or char.isspace() for char in barcode):
        raise DecodingError("Barcode contains invalid symbols")
    
    return barcode.strip()

def decode_barcode(barcode):
    """
    Convert barcode symbols back to text with validation.
    
    Args:
        barcode (str): Input barcode sequence
        
    Returns:
        str: Decoded text
        
    Raises:
        DecodingError: If decoding fails
    """
    try:
        barcode = validate_barcode(barcode)
        decoded_chars = []
        
        # Split the barcode sequence by the separator
        sequences = [seq.strip() for seq in barcode.split('𝄄') if seq.strip()]
        
        for sequence in sequences:
            # Verify the sequence is complete and valid
            if is_valid_sequence(sequence):
                decoded_chars.append(REVERSE_DICT[sequence])
            else:
                # Check if it's a space character
                if sequence == '𝄅':
                    decoded_chars.append(' ')
                else:
                    decoded_chars.append('?')
        
        result = ''.join(decoded_chars)
        return result if result else '?'
        
    except Exception as e:
        raise DecodingError(f"Decoding failed: {str(e)}")