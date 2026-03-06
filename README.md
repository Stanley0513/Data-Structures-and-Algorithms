# Data Structures & Algorithms 💻

這是我在大二的程式設計課程中與資料結構及演算法相關內容的 Python 實作紀錄。重點放在底層結構的刻劃、遞迴邏輯的運用，以及不同演算法與底層套件之間的效能評估。

## 📂 核心實作清單

### 1. 二元搜尋樹實作 - `BinarySearchTree.py`
* **技術：**
  * 不依賴外部套件，從零實作 BST 的節點物件與樹狀結構。
  * 包含節點插入 (Insert)、二元搜尋 (Search)、尋找極值 (Min/Max)，以及利用遞迴完成的中序走訪 (Inorder Traversal)。

### 2. 矩陣運算效能分析 - `Matrix-Multiplication-Performance.py`
* **技術：**
  * 實作傳統的三層巢狀迴圈來進行二維矩陣相乘。
  * 引入 `NumPy` 套件進行矩陣內積，並透過 `time` 模組進行精準的效能測量與對比。

### 3. 最大公因數 (GCD) 演算法對比 - `GCD-Algorithm-Analysis.py`
* **技術：**
  * 同時使用「遞迴」與「迴圈」兩種思維來解決同一個問題。
  * 透過效能計時器比較兩者在執行時間上的差異與優劣。

## 🛠 執行環境
* **語言：** Python 3
* **相依套件：** `numpy` (用於矩陣效能對比)
