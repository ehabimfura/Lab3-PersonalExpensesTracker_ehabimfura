---

# README.md  
**Lab 3: Personal Expenses Tracker (RWF)**  

---

## 📌 Project Overview  
This is a command‑line program in **Python** with a companion **shell script**.  
It tracks personal expenses in **Rwandan Francs (RWF)**, manages balance, and archives expense files.  

---

## 📂 Files in Repo  
- `expenses-tracker.py` → main Python program  
- `archive_expenses.sh` → shell script for archiving/search  
- `balance.txt` → starts at `0` (user adds money later)  
- `expenses_YYYY-MM-DD.txt` → expense files created by the program  

---

## ▶️ How to Run  

### 1. Start the Python program  
```bash
python3 expenses-tracker.py
```

### 2. Menu Options  
1. Check Remaining Balance  
2. View Expenses  
3. Add New Expense  
4. Exit  

---

## 🧾 Feature Details  

### Feature 1: Main Menu  
- Provides navigation to all features.  

### Feature 2: Check Remaining Balance  
- Reads current balance from `balance.txt`.  
- Displays a formatted report:  
  - Initial/Current Balance  
  - Total Expenses to Date  
  - Available Balance (`Balance - Total Expenses`)  
- Asks if user wants to add money.  
- If yes:  
  - Prompts for amount.  
  - Validates input (positive integer).  
  - Updates `balance.txt`.  
  - Confirms with **new available balance**.  

### Feature 3: Add New Expense  
- Shows available balance.  
- Prompts for date, item, and amount.  
- Validates input.  
- Saves expense in `expenses_YYYY-MM-DD.txt` with:  
  ```
  ID,Item,Amount,Timestamp
  ```  
- Updates report with remaining balance.  

### Feature 4: View Expenses  
- Search expenses by item name or amount.  
- Displays matching records with file name and timestamp.  

---

## 🛠️ Shell Script Usage  

### Archive a file  
```bash
./archive_expenses.sh 2025-11-19
```

### Search archived file  
```bash
./archive_expenses.sh search 2025-11-19
```

---

## 📝 Notes  
- **balance.txt starts at 0 RWF**.  
- User must add money before recording expenses.  
- All amounts are integers in RWF.  
- Works on Linux/macOS terminal.  

---

