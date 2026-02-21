# Python Calculator

A modern Python calculator application with both command-line and graphical interfaces.

## Features

### 🖥️ Command-Line Calculator (`calculator.py`)
- Basic arithmetic operations: +, -, *, /
- Error handling for division by zero
- Interactive command-line interface
- Input validation

### 🎨 Graphical Calculator (`gui_calculator.py`)
- Modern GUI with tkinter
- Color-coded buttons for different operations
- Advanced functions: square root (√), power (^)
- Error handling with user-friendly messages
- Keyboard and mouse support

## Requirements

- Python 3.11.0 or higher
- tkinter (included with Python standard library)
- math module (included with Python standard library)

## Installation

1. Ensure you have Python 3.11+ installed:
   ```bash
   python --version
   ```

2. Upgrade pip to latest version:
   ```bash
   python -m pip install --upgrade pip
   ```

3. Install requirements (optional for development):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Calculator
```bash
cd calculator
python calculator.py
```

### Graphical Calculator
```bash
cd calculator
python gui_calculator.py
```

## Project Structure

```
calculator/
├── calculator.py      # Command-line version
├── gui_calculator.py  # Graphical version
├── requirements.txt   # Python version and dependencies
└── README.md         # This file
```

## Development

### Code Formatting
Use black for code formatting:
```bash
black *.py
```

### Linting
Use flake8 for linting:
```bash
flake8 *.py
```

### Testing
Run tests with pytest:
```bash
pytest
```

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for your changes
5. Submit a pull request