"""
Module containing the barcode symbol mappings and dictionary operations.
"""

# Valid barcode symbols
VALID_SYMBOLS = {'𝄂', '𝄃', '𝄀', '𝄄', '𝄅'}

# Dictionary mapping letters to unique symbol sequences
BARCODE_DICT = {
    'A': '𝄂𝄂𝄂', 'B': '𝄂𝄂𝄃', 'C': '𝄂𝄂𝄀', 'D': '𝄂𝄃𝄂', 'E': '𝄂𝄃𝄃',
    'F': '𝄂𝄃𝄀', 'G': '𝄂𝄀𝄂', 'H': '𝄂𝄀𝄃', 'I': '𝄂𝄀𝄀', 'J': '𝄃𝄂𝄂',
    'K': '𝄃𝄂𝄃', 'L': '𝄃𝄂𝄀', 'M': '𝄃𝄃𝄂', 'N': '𝄃𝄃𝄃', 'O': '𝄃𝄃𝄀',
    'P': '𝄃𝄀𝄂', 'Q': '𝄃𝄀𝄃', 'R': '𝄃𝄀𝄀', 'S': '𝄀𝄂𝄂', 'T': '𝄀𝄂𝄃',
    'U': '𝄀𝄂𝄀', 'V': '𝄀𝄃𝄂', 'W': '𝄀𝄃𝄃', 'X': '𝄀𝄃𝄀', 'Y': '𝄀𝄀𝄂',
    'Z': '𝄀𝄀𝄃', ' ': '𝄅'  # Space character
}

# Create reverse dictionary for decoding
REVERSE_DICT = {value: key for key, value in BARCODE_DICT.items()}

# Set of all valid sequences
VALID_SEQUENCES = set(BARCODE_DICT.values())

def is_valid_sequence(sequence):
    """
    Check if a sequence is valid.
    
    Args:
        sequence (str): Barcode sequence to validate
        
    Returns:
        bool: True if sequence is valid, False otherwise
    """
    return sequence in VALID_SEQUENCES

def is_valid_symbol(symbol):
    """
    Check if a symbol is valid.
    
    Args:
        symbol (str): Symbol to validate
        
    Returns:
        bool: True if symbol is valid, False otherwise
    """
    return symbol in VALID_SYMBOLS