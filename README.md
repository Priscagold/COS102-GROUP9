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

| Name | Core Team Role | Primary Traceable Contribution & Deliverable Artifacts |
| :--- | :--- | :--- |
| *Olamiju Oluwasemilore* | **Project Manager,Translation Engineer & Git Lead** | Systems architecture coordination, GitHub repository maintenance, code conflict resolution/merging, final evaluation abstract documentation.Contextual translation dictionary research, development and deployment of the structural nested Python dictionary array module `translations.py`. |
| *Onyekonwu Chizuroke* | **UI/UX Designer** | High-fidelity screen wireframe architecture mapping in Figma, multi-dialect typography constraint validation layouts, documentation of asset branches via `figma_design_links.md`. |
| *Oladeji Ouwasayomi* | **Data Architect** | Data schema engineering, creation and structural maintenance of the multi-column translation dataset matrix file `swift_shop_inventory.csv`. |
| *Ndiwe Brian* | **Frontend UI Architect** | Base object-oriented Tkinter graphical layout programming (`main.py`), frame allocations, button grids, and internal dynamic reference array setups. |
| *Ezeani Christabel* | **Localization Engineer** | Algorithmic layout mapping routines, development of the `change_language()` live execution array parser block within the main application runtime class loop. |

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
Ensure your local development computer environment contains Python 3 and Pillow installed. The UI engine relies exclusively on native built-in system components, meaning no exterior third-party library setup is required.

### Execution Routine
1. Clone the master repository branch files down into an isolated system folder:
   ```bash
   git clone [https://github.com/Priscagold/COS102-GROUP9.git](https://github.com/Priscagold/COS102-GROUP9.git)
   cd COS102-GROUP9

### TESTING & DEBUGGING
During the development of this project, several rounds of testing were carried out to ensure that the application functioned properly and provided a smooth user experience for both market women and customers. The testing process focused on usability, language translation flow, navigation, responsiveness, and overall system performance.

KEY ISSUES ENCOUNTERED AND FIXES APPLIED
1. Language Selection Not Updating Properly
  ISSUE: User experienced problems where the selected language did not immediately reflect accross all screens of the application.
  CAUSE: The language state was not being shared properly between components.
  FIX APPLIED: Global state management and proper prop handling were implemented to ensure that the selected language updated consistently throughout the app.

2. Navigation Errors Between Screens
   ISSUE: Some users were redirected to incorrect pages or experienced blank screens during navigation.
   CAUSE: Incorrect routing paths and missing screen configurations.
   FIX APPLIED: Navigation routes were reviewed, corrected, and tested repeatedly to ensure seamless movement between screens.

3. Translation And Communication Delays
   ISSUE: Messages and translated content occasionally loaded slowly, affecting communication between buyers and sellers.
   CAUSE: Inefficient handling of API requests and asynchronous operations.
   FIX APPLIED: Request handling was optimized, loading states were added, and unnecessary re-renders were reduced to improve performance.

4. UI Responsiveness On Different Devices
   ISSUE: Certain components appeared misaligned on smaller mobile screens.
   CAUSE: Fixed width and height values in some sections of the interface.
   FIX APPLIED: Responsive styling techniques such as Flexbox and percentage based sizing were implemented to ensure compatibility across different screen sizes.

5. Button And Validation Errors
   ISSUE: Some buttons failed to respond correctly when required input fields were empty.
   CAUSE: Missing validation checks in forms.
   FIX APPLIED: Input validation logic was introduced to prevent incomplete submissions and provide feedback messages to users.

TESTING APPROACHES USED
. Functional Testing
. User Interface Testing
. Navigation Testing
. Responsiveness Testing
. Manual User Testing
. Error and Bug tracking

OUTCOME
After debugging and testing cycles, the application became more stable, responsiveness, and user-friendly. The fixes implemented improved communication between customers and market women, enhanced accessibility through language selection features and ensured smoother interaction across the platform.
