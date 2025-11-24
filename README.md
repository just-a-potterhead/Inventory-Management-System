# Inventory Management System
---

## 📦 Overview

The **Inventory Management System** is a lightweight, command-line Python application that helps users manage product inventory using a simple CSV-based database. The program supports adding new items, updating stock, and viewing all available products along with their pricing.

This project is perfect for beginners learning file handling, Python functions, and CSV manipulation.

---

## 🚀 Features

* Add new inventory items
* Update stock quantities
* Display all remaining items
* Auto-create CSV database if missing
* Simple and easy-to-use CLI menus

---

## 📁 Project Structure

```
project_folder/
│
├── main.py            # Python script (your source code)
├── inventory.csv      # Auto-generated inventory database
└── README.md          # Documentation file
```

---

## 🧠 How It Works

1. The program starts by ensuring `inventory.csv` exists.
2. A menu-driven interface allows users to:

   * **Insert** items
   * **Update** quantity
   * **View** inventory
   * **Exit** the program
3. New items are appended to the CSV file.
4. Updating items rewrites the entire CSV with modified values.
5. All inventory records are displayed in a human-readable format.

---

## 📜 Functions Breakdown

### **1. `project()` — View Inventory**

Reads and prints all inventory items with name, brand, quantity, and cost.

### **2. `write(inventory)` — Add New Entry**

Appends a new row (item name, brand, stock, cost) to the CSV file.

### **3. `insert()` — Insert Item**

Takes user input, validates stock and cost, and writes data to the CSV.

### **4. `stockextend()` — Modify Quantity**

Handles updating an existing item's stock value.

### **5. `update()` — Update Existing Item**

Searches for an item and updates its stock using `stockextend()`.

### **6. `menu()` / `choice()` — UI Navigation**

Provides interactive menu and handles user selection.

---

## 🔮 Future Enhancements

* Add search and filter options
* Prevent duplicate entries
* GUI version using Tkinter or PyQt
* Low-stock alerts and analytics
* Support for deleting items
* Data visualization using charts
* Integration with databases (SQLite / MongoDB)

---

## 🛠️ Requirements

* Python 3.x
* No external packages required (uses only built-in `csv` and `time`)

---

## 📥 Installation

```bash
git clone https://github.com/your-username/inventory-management-system.git
cd inventory-management-system
python3 main.py
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Acknowledgements

* Built using Python's CSV handling capabilities
* Designed as a beginner-friendly project to understand file operations

---

Thank you for using the **Inventory Management System**! 🚀
