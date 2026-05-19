# Swift Shop: Easy Multi-Language Market App

## 📌 Project Overview
**Swift Shop** is an assistive desktop e-commerce application developed in Python using the Tkinter Graphic User Interface (GUI) framework. 

This app is designed to help local market traders (like market women selling pepper and vegetables) sell their goods digitally, even if they cannot read or speak English.

---

## 🛑 The Problem & Our Solution
### The Problem:
Many local market women and traders in Nigeria do not know how to read or write in English. Because almost all modern e-commerce websites and apps are entirely in English, these local traders are locked out. They cannot use technology to reach more customers, which limits how much money they can make in an already crowded marketplace.

### Our Solution:
**Swift Shop** removes the English language barrier completely! The app has **5 language buttons**: English, Yoruba, Igbo, Hausa, and Pidgin. 

When a trader clicks any of these buttons, **every single word on the screen changes instantly** to that chosen language. This includes the titles, the help instructions, and the names of the products (like changing "Fresh Pepper" to "Ata Rodo" or "Ose Oyibo"). This makes the app incredibly easy for any local vendor to use.

---

## 👥 Group 9: Traceable Team Matrix & Task Allocation
To ensure engineering transparency, responsibilities are distinct and mapped cleanly to specific code repositories and documentation branches:

| Name / GitHub Handle | Core Team Role | Primary Traceable Contribution & Deliverable Artifacts |
| :--- | :--- | :--- |
| *Olamiju Oluwasemilore* | **Project Manager & Git Lead** | Systems architecture coordination, GitHub repository maintenance, code conflict resolution/merging, final evaluation abstract documentation. |
| *gameboyzuky* | **UI/UX Designer** | High-fidelity screen wireframe architecture mapping in Figma, multi-dialect typography constraint validation layouts, documentation of asset branches via `figma_design_links.md`. |
| *Oladeji Ouwasayomi* | **Data Architect** | Data schema engineering, creation and structural maintenance of the multi-column translation dataset matrix file `swift_shop_inventory.csv`. |
| *Ndiwe Brian* | **Frontend UI Architect** | Base object-oriented Tkinter graphical layout programming (`main.py`), frame allocations, button grids, and internal dynamic reference array setups. |
| *Ezeani Christabel* | **Localization Engineer** | Algorithmic layout mapping routines, development of the `change_language()` live execution array parser block within the main application runtime class loop. |
| *Durojaiye Muhammad* | **Translation Engineer** | Contextual translation dictionary research, development and deployment of the structural nested Python dictionary array module `translations.py`. |

---

## 🛠️ System Architecture & Component Mapping
The software pipeline runs sequentially through isolated object-oriented structures:
1. **The Database (`swift_shop_inventory.csv`):** Houses localized indexing structures for inventories (Fresh Pepper, Onions, Palm Oil, etc.) matching multi-language product entry strings to persistent float price structures.
2. **The Translation Dictionary (`translations.py`):** Holds a nested structural Python dictionary variable (`UI_STRINGS`) managing text translations for universal banners, buttons, error messages, and guide prompts.
3. **The Core UI Engine (`main.py`):** Spawns a dedicated $600 \times 650$ pixel runtime layout display canvas processing multi-directional functional triggers.
   * **Persistent Information Element:** Includes a continuous tutorial guidance prompt locked to the base screen boundary rows, ensuring non-technical accessibility that automatically morphs to match selected language models.

---

## 🚀 Execution & Deployment Instructions
To run the fully localized e-commerce experience locally on an evaluation environment:

### Prerequisites
Ensure your local development computer environment contains Python 3 installed. The UI engine relies exclusively on native built-in system components, meaning no exterior third-party library setup is required.

### Execution Routine
1. Clone the master repository branch files down into an isolated system folder:
   ```bash
   git clone [https://github.com/Priscagold/COS102-GROUP9.git](https://github.com/Priscagold/COS102-GROUP9.git)
   cd COS102-GROUP9
