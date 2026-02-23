## BMW Digital Paintshop

### Overview

The BMW Digital Paintshop is a desktop-based configuration application developed using Python and the PyQt6 framework. It provides a high-fidelity interface for users to customize the BMW M4 Competition Coupé, allowing for real-time selection of exterior paint finishes, wheel designs, and interior leather options. The application features a dark-themed, minimalist aesthetic consistent with modern luxury automotive digital interfaces.

---

### Technical Specifications

* **Core Framework**: PyQt6
* **Language**: Python 3.x
* **User Interface Components**: QMainWindow, QStackedWidget, QVBoxLayout, QHBoxLayout, QGridLayout
* **Graphics Handling**: QPixmap for high-resolution asset rendering

---

### Key Features

* **Interactive Customization**: Toggle between different configuration modules including Paint, Wheels, and Interior.
* **Dynamic Summary**: A final summary view that aggregates all user selections and calculates the total vehicle price.
* **Modern UI/UX**: Custom CSS-styled widgets providing a sleek, responsive design with hover effects and active state indicators.
* **Performance Metrics Display**: Real-time visibility of technical data such as acceleration, power output, and fuel consumption.

---

### Installation and Setup

#### Prerequisites

Ensure that Python 3.x is installed on your local machine. You will also need the PyQt6 library.

#### Dependency Installation

Install the required framework using the following command:

```bash
pip install PyQt6

```

#### Configuration

The application requires local image assets to function correctly. Ensure the following line in the script points to a valid image file on your system:

```python
pixmap = QPixmap(r"YOUR_FILE_PATH_HERE")

```

*Note: Use the 'r' prefix for Windows file paths to avoid unicode escape errors.*

#### Execution

Run the application from your terminal or IDE:

```bash
python bmw_configurator.py

```

---

### Project Structure

* **BMWConfigurator Class**: The main application controller handling window initialization and global state.
* **Navigation System**: Custom-built header for switching between configuration stacks.
* **Content Area**: A central hub that utilizes a QStackedWidget to transition between different customization panels without reloading the window.
* **Footer**: Contains regulatory information and technical data strings.

---

### License

This project is intended for educational and demonstration purposes. All rights to the BMW brand and associated imagery belong to BMW AG.

### Images of the interface

<img width="1919" height="1011" alt="Screenshot 2026-02-23 223500" src="https://github.com/user-attachments/assets/6f470f05-928a-4c5a-8778-770927f6ec34" />

<img width="646" height="304" alt="Screenshot 2026-02-23 223520" src="https://github.com/user-attachments/assets/94806a80-5070-4151-805a-ad5be8acbe49" />

<img width="631" height="314" alt="Screenshot 2026-02-23 223534" src="https://github.com/user-attachments/assets/5241a92a-4198-4a82-a469-ddd59435dca9" />

<img width="659" height="293" alt="Screenshot 2026-02-23 223551" src="https://github.com/user-attachments/assets/80c16d8a-aff0-471a-88f8-7941135cfb19" />


