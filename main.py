import tkinter as tk
from tkinter import messagebox
import csv
from PIL import Image, ImageTk  # <--- Added to handle JPG/JPEG and other formats safely

# --- MEMBER 6 INTEGRATED DICTIONARY ASSET FRAMEWORK ---
UI_STRINGS = {
    "English": {
        "welcome": "Welcome to Swift Shop",
        "market_title": "Marketplace / Product Catalog",
        "checkout": "Proceed to Checkout",
        "item_added": "Item successfully added to your market basket!",
        "guide": "Guide: Click any language button to translate the entire page. Click a product to buy it."
    },
    "Yoruba": {
        "welcome": "Kábọ̀ sí Swift Shop",
        "market_title": "Ojú-Oge Ọjà / Àwọn Ọjà Wa",
        "checkout": "Sísanwó / Parí Ìrajà",
        "item_added": "A ti fi ọjà sínú agbọ̀n tìrẹ lọ́nà àṣeyọrí!",
        "guide": "Ìtọ́sọ́nà: Tẹ bọ́tìnì èdè kankan láti yí gbogbo ojú-ewé padà. Tẹ ọjà kan láti rà á."
    },
    "Igbo": {
        "welcome": "Nnọọ na Swift Shop",
        "market_title": "Ebe Ngosipụta Ngwaahịa / Katọlọgụ",
        "checkout": "Gaa n'Ebe Ịkwụ Ụgwọ",
        "item_added": "Agbakwunyere ihe a nke ọma na nkata ahịa gị!",
        "guide": "Ntuziaka: Pịa bọtịnụ asụsụ ọ bụla ka ị sụgharịa ibe ahụ dum. Pịa ngwaahịa ka ị zụọ ya."
    },
    "Hausa": {
        "welcome": "Barka da zuwa Swift Shop",
        "market_title": "Dandalin Kasuwa / Kayayyakinmu",
        "checkout": "Ci gaba da Biyan Kuɗi",
        "item_added": "An yi nasarar ƙara kaya a rariyar sayayya taka!",
        "guide": "Jagora: Danna kowane bọtini na yare don fassara dukkan shafin. Danna samfur don saya."
    },
    "Pidgin": {
        "welcome": "Welcome to Swift Shop",
        "market_title": "Market Area / All Beta Market",
        "checkout": "Go Pay Money for Counter",
        "item_added": "Market don enter your basket smoothly!",
        "guide": "Guide: Touch any language button to change all the words. Click the market item to buy am."
    }
}

class SwiftShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Swift Shop - Multilingual Market")
        
        # STRICT PM CONSTRAINTS: Hardcoded window limits matching Figma geometry definitions
        self.root.geometry("600x650")
        self.root.resizable(False, False)  # Keeps layouts from expanding automatically
        self.root.configure(bg="#F5F5F5") 
        
        # Internal Runtime State Framework Tracking
        self.current_language = "English"
        self.product_list = []      # Dynamic array capturing parsed rows from swift_shop_inventory(2)(1)_1_1.csv
        self.product_buttons = []   # Maps tracking tuples containing active widgets and row metrics
        
        # Global UI State Element Frames
        self.home_frame = None
        self.market_frame = None
        
        # Pre-load dataset records prior to execution
        self.load_csv_inventory()
        
        # Open to screen 1 landing module matching Member 2's specifications
        self.create_home_screen()

    # --- SCREEN 1: NEW FIGMA HOME SCREEN (2x2 GRID + BASE CENTERED PIDGIN) ---
    def create_home_screen(self):
        """Generates Member 2's welcome choice grid layout view."""
        if self.market_frame:
            self.market_frame.pack_forget()
            
        self.home_frame = tk.Frame(self.root, bg="#F5F5F5")
        self.home_frame.pack(fill="both", expand=True)
        
        # 1. App Identity Header Labels
        title_label = tk.Label(self.home_frame, text="🛒 SWIFT SHOP", font=("Arial", 26, "bold"), fg="#2E7D32", bg="#F5F5F5")
        title_label.pack(pady=(50, 5))
        
        subtitle_label = tk.Label(self.home_frame, text="Select Your Language to Start Shopping", font=("Arial", 11), fg="#616161", bg="#F5F5F5")
        subtitle_label.pack(pady=(0, 35))
        
        # 2. Layout Grid Matrix Block Setup
        grid_frame = tk.Frame(self.home_frame, bg="#F5F5F5")
        grid_frame.pack(pady=10)
        
        btn_styles = {
            "font": ("Arial", 11, "bold"),
            "bg": "#FFFFFF",
            "fg": "#2E7D32",
            "activebackground": "#2E7D32",
            "activeforeground": "#FFFFFF",
            "width": 18,
            "height": 2,
            "bd": 1,
            "relief": "solid"
        }
        
        # Row Block 1: English & Yoruba
        tk.Button(grid_frame, text="ENGLISH", **btn_styles, command=lambda: self.initialize_market_view("English")).grid(row=0, column=0, padx=15, pady=12)
        tk.Button(grid_frame, text="YORUBA", **btn_styles, command=lambda: self.initialize_market_view("Yoruba")).grid(row=0, column=1, padx=15, pady=12)
        
        # Row Block 2: Igbo & Hausa
        tk.Button(grid_frame, text="IGBO", **btn_styles, command=lambda: self.initialize_market_view("Igbo")).grid(row=1, column=0, padx=15, pady=12)
        tk.Button(grid_frame, text="HAUSA", **btn_styles, command=lambda: self.initialize_market_view("Hausa")).grid(row=1, column=1, padx=15, pady=12)
        
        # Row Block 3: Lower Centered Wide Pidgin Toggle Layout Component
        pid_btn = tk.Button(
            grid_frame, 
            text="PIDGIN", 
            font=("Arial", 11, "bold"), 
            bg="#FFFFFF", 
            fg="#2E7D32", 
            activebackground="#2E7D32",
            activeforeground="#FFFFFF",
            width=40, 
            height=2,
            bd=1,
            relief="solid",
            command=lambda: self.initialize_market_view("Pidgin")
        )
        pid_btn.grid(row=2, column=0, columnspan=2, pady=15)
            
        # 3. Base Informational Help Row Banner UI
        start_guide = tk.Label(self.home_frame, text=UI_STRINGS["English"]["guide"], bg="#FFF9C4", fg="#5D4037", font=("Arial", 10, "italic"), bd=1, relief="solid", pady=8)
        start_guide.pack(side="bottom", fill="x")

    # --- SCREEN 2: DYNAMIC TWO-COLUMN ITEM CATALOG MARKETPLACE ---
    def create_market_screen(self):
        """Generates visual elements utilizing data matrix records."""
        self.market_frame = tk.Frame(self.root, bg="#F5F5F5")
        self.market_frame.pack(fill="both", expand=True)
        
        # 1. Top Core Navigation Mini Language Bar Switch Ribbon Array
        mini_lang_frame = tk.Frame(self.market_frame, bg="#FFFFFF", bd=1, relief="groove")
        mini_lang_frame.pack(fill="x", padx=15, pady=5)
        
        languages = ["English", "Yoruba", "Igbo", "Hausa", "Pidgin"]
        for lang in languages:
            btn_bg = "#2E7D32" if lang == self.current_language else "#F5F5F5"
            btn_fg = "#FFFFFF" if lang == self.current_language else "#212121"
            
            btn = tk.Button(
                mini_lang_frame, 
                text=lang, 
                font=("Arial", 9, "bold"), 
                bg=btn_bg, 
                fg=btn_fg,
                width=9,
                command=lambda l=lang: self.change_language(l)
            )
            btn.pack(side="left", padx=6, pady=5)
            
        # 2. Localization Dynamic App Title Banner Fields
        self.welcome_label = tk.Label(self.market_frame, text=UI_STRINGS[self.current_language]["welcome"], font=("Arial", 14, "bold"), fg="#2E7D32", bg="#F5F5F5")
        self.welcome_label.pack(pady=4)
        
        self.title_label = tk.Label(self.market_frame, text=UI_STRINGS[self.current_language]["market_title"], font=("Arial", 11, "bold"), fg="#616161", bg="#F5F5F5")
        self.title_label.pack(pady=2)
        
        # 3. Two-Column Marketplace Layout Card Area Panel
        grid_container = tk.Frame(self.market_frame, bg="#F5F5F5")
        grid_container.pack(fill="both", expand=True, padx=20, pady=5)
        
        self.product_buttons = []
        row_idx, col_idx = 0, 0
        
        for item in self.product_list:
            # Safely fetch localization headers, falling back onto English if blank
            lang_column_key = f"{self.current_language}_Name"
            product_title = item.get(lang_column_key, item.get("English_Name", "Unknown Product"))
            price_value = item.get("Price_Naira", "0")
            image_filename = item.get("Image_File", "")
            
            # Individual Product Box Visual Frames Block
            card = tk.Frame(grid_container, bg="#FFFFFF", bd=1, relief="solid", padx=10, pady=8)
            card.grid(row=row_idx, column=col_idx, padx=12, pady=8, sticky="nsew")
            
            # Updated Image Handling Layer (Utilizes Pillow to ensure .jpg / .png compliance)
            try:
                pil_image = Image.open(image_filename)
                # Optional: Uncomment the line below if you ever want to strictly auto-resize images to fit the Figma boxes
                # pil_image = pil_image.resize((100, 100), Image.Resampling.LANCZOS)
                prod_img = ImageTk.PhotoImage(pil_image)
                
                img_lbl = tk.Label(card, image=prod_img, bg="#FFFFFF")
                img_lbl.image_ref = prod_img  # Essential link variable preventing memory disposal
                img_lbl.pack(pady=(0, 4))
            except Exception:
                # Automatic emoji symbol container deployment if system assets are missing
                fallback_lbl = tk.Label(card, text="📦", font=("Arial", 22), bg="#FFFFFF")
                fallback_lbl.pack(pady=(2, 4))
            
            name_lbl = tk.Label(card, text=product_title, font=("Arial", 11, "bold"), bg="#FFFFFF", fg="#212121")
            name_lbl.pack(anchor="w")
            
            price_lbl = tk.Label(card, text=f"₦{price_value}", font=("Arial", 10, "bold"), bg="#FFFFFF", fg="#E53935")
            price_lbl.pack(anchor="w", pady=(1, 5))
            
            buy_btn = tk.Button(
                card, 
                text="ADD TO BASKET", 
                font=("Arial", 9, "bold"), 
                bg="#2E7D32", 
                fg="#FFFFFF", 
                activebackground="#1B5E20",
                activeforeground="#FFFFFF",
                command=lambda name=product_title: self.trigger_purchase_notification(name)
            )
            buy_btn.pack(fill="x")
            
            # Map elements inside state tracking arrays for Member 5 context switching
            self.product_buttons.append((buy_btn, item))
            
            # Hard toggle indices to maintain a strict two-column threshold spacing limit
            col_idx += 1
            if col_idx > 1:
                col_idx = 0
                row_idx += 1
                
            if row_idx > 2:  # Cut layout early to perfectly respect structural window limits
                break
                
        grid_container.grid_columnconfigure(0, weight=1)
        grid_container.grid_columnconfigure(1, weight=1)

        # 4. Global Lower Navigation Controller Panel Segment
        nav_bar = tk.Frame(self.market_frame, bg="#FFFFFF", bd=1, relief="sunken")
        nav_bar.pack(side="bottom", fill="x")
        
        self.checkout_btn = tk.Button(nav_bar, text=UI_STRINGS[self.current_language]["checkout"], bg="#2E7D32", fg="white", font=("Arial", 10, "bold"), pady=5, command=self.trigger_checkout_panel)
        self.checkout_btn.pack(side="right", padx=20, pady=6)
        
        home_nav_btn = tk.Button(nav_bar, text="⬅ BACK TO HOME", font=("Arial", 9, "bold"), bg="#E0E0E0", command=self.return_to_home)
        home_nav_btn.pack(side="left", padx=20, pady=6)

        # 5. Persistent On-Screen Localized Technical Guide Banner Block
        self.guide_text = tk.StringVar(value=UI_STRINGS[self.current_language]["guide"])
        self.guide_label = tk.Label(self.market_frame, textvariable=self.guide_text, bg="#FFF9C4", fg="#5D4037", bd=1, relief="solid", anchor="w", font=("Arial", 10, "italic"), padx=12, pady=6)
        self.guide_label.pack(side="bottom", fill="x")

    # --- INPUT PIPELINE & NAVIGATION ROUTE CONTROLLERS ---
    def load_csv_inventory(self):
        """Pulls text metrics from swift_shop_inventory(2)(1).csv using utf-8-sig to clear hidden Excel bits."""
        try:
            with open("swift_shop_inventory(2)(1).csv", mode="r", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)
                reader.fieldnames = [name.strip() for name in reader.fieldnames]
                for row in reader:
                    self.product_list.append(row)
        except FileNotFoundError:
            messagebox.showerror("Critical File Error", "System cannot detect database resource 'swift_shop_inventory(2)(1).csv'!")

    def initialize_market_view(self, chosen_lang):
        """Clears landing screen objects to route the application window context directly onto the marketplace."""
        self.current_language = chosen_lang
        if self.home_frame:
            self.home_frame.pack_forget()
        self.create_market_screen()

    def return_to_home(self):
        """Clears active display grids to reverse directions smoothly back to main selection layout."""
        if self.market_frame:
            self.market_frame.pack_forget()
        self.create_home_screen()

    def trigger_purchase_notification(self, product_name):
        """Launches an overlay announcement using translated configurations."""
        alert_msg = f"{product_name} - " + UI_STRINGS[self.current_language]["item_added"]
        messagebox.showinfo("Basket Update", alert_msg)
        
    def trigger_checkout_panel(self):
        messagebox.showinfo("Swift Shop Checkout", "Checkout workflow layer active.")

    # --- LOGIC HOOK SHELL FOR MEMBER 5 IMPLEMENTATION ---
    def change_language(self, selected_lang):
        """
        This routine shell handles switching text strings.
        Member 5 will overwrite this to translate widget configs without reloading frames.
        """
        self.current_language = selected_lang
        if self.market_frame:
            self.market_frame.pack_forget()
            self.create_market_screen()

if __name__ == "__main__":
    main_window = tk.Tk()
    application_instance = SwiftShopApp(main_window)
    main_window.mainloop()
