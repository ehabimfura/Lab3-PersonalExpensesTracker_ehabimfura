Got it 👍 — here’s a **simple student‑friendly README.md** with only the necessary info.  

---

# README.md  
**Lab 3: Personal Expenses Tracker (RWF)**  

---

## Project Overview  
This is a command‑line program in **Python** with a companion **shell script**.  
It tracks personal expenses in **Rwandan Francs (RWF)**, manages balance, and archives expense files.  

---

## Files in Repo  
- `expenses-tracker.py` → main Python program  
- `archive_expenses.sh` → shell script for archiving/search  
- `balance.txt` → starting balance (integer, e.g. `10000`)  
- `expenses_YYYY-MM-DD.txt` → expense files created by the program  

---

## How to Run  

### 1. Start the Python program  
```bash
python3 expenses-tracker.py
```

### 2. Menu Options  
1. Check Remaining Balance  
2. View Expenses  
3. Add New Expense  
4. Exit  

### 3. Example  
```
Available Balance: 10000 RWF
Enter date (YYYY-MM-DD): 2025-11-19
Enter item name: Transport
Enter amount (RWF): 500
Expense saved! Remaining balance: 9500 RWF
```

---

## Shell Script Usage  

### Archive a file  
```bash
./archive_expenses.sh 2025-11-19
```

### Search archived file  
```bash
./archive_expenses.sh search 2025-11-19
```

---

## Notes  
- All amounts are integers in **RWF**.  
- Expense files follow the format:  
  ```
  ID,Item,Amount,Timestamp
  ```  
- Always test on Linux/macOS terminal.  

