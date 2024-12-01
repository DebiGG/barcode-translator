"""
Main module for the barcode translation program.
"""
from encoder import encode_text, EncodingError
from decoder import decode_barcode, DecodingError
import sys

def get_user_choice():
    """Get and validate user menu choice."""
    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice in {'1', '2', '3'}:
                return choice
            print("Invalid choice. Please enter 1, 2, or 3.")
        except (EOFError, KeyboardInterrupt):
            return '3'  # Exit gracefully on Ctrl+C or Ctrl+D

def get_user_input(prompt):
    """Get user input with error handling."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        return None

def display_menu():
    """Display the main menu."""
    print("\nBarcode Translator")
    print("1. Encode text to barcode")
    print("2. Decode barcode to text")
    print("3. Exit")

def continue_prompt():
    """Prompt user to continue."""
    try:
        input("\nPress Enter to continue...")
    except (EOFError, KeyboardInterrupt):
        pass

def handle_encoding(text):
    """Handle text encoding with error handling."""
    try:
        if text:
            barcode = encode_text(text)
            print("\nEncoded barcode:")
            print(barcode)
        return True
    except EncodingError as e:
        print(f"\nEncoding error: {str(e)}")
        return False
    except Exception as e:
        print(f"\nUnexpected error during encoding: {str(e)}")
        return False

def handle_decoding(barcode):
    """Handle barcode decoding with error handling."""
    try:
        if barcode:
            text = decode_barcode(barcode)
            print("\nDecoded text:")
            print(text)
        return True
    except DecodingError as e:
        print(f"\nDecoding error: {str(e)}")
        return False
    except Exception as e:
        print(f"\nUnexpected error during decoding: {str(e)}")
        return False

def main():
    """Main program loop."""
    while True:
        try:
            display_menu()
            choice = get_user_choice()
            
            if choice == '1':
                text = get_user_input("Enter text to encode: ")
                if handle_encoding(text):
                    continue_prompt()
                
            elif choice == '2':
                barcode = get_user_input("Enter barcode to decode: ")
                if handle_decoding(barcode):
                    continue_prompt()
                
            elif choice == '3':
                print("\nGoodbye!")
                sys.exit(0)
        
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            continue_prompt()

if __name__ == "__main__":
    main()