import tkinter as tk
from tkinter import messagebox
import csv
from PIL import Image, ImageTk  
from translations import UI_STRINGS

class SwiftShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Swift Shop - Multilingual Market")
        
        # Geometry Definitions matching Figma blueprints
        self.root.geometry("600x650")
        self.root.resizable(False, False)  
        self.root.configure(bg="#F5F5F5") 
        
        # Application Runtime States
        self.current_language = "English"
        self.product_list = []      
        self.cart_items = []  # Tracks user selections
        
        # UI Component Window Frames
        self.home_frame = None
        self.market_frame = None
        self.cart_frame = None  # Required Third View
        
        self.load_csv_inventory()
        self.create_home_screen()

    # --- MEMBER 1: CREATE HOME SCREEN VIEW ---
    def create_home_screen(self):
        """Generates the main welcome multi-tiered landing frame."""
        self.clear_all_frames()
            
        self.home_frame = tk.Frame(self.root, bg="#F5F5F5")
        self.home_frame.pack(fill="both", expand=True)
        
        title_label = tk.Label(self.home_frame, text="🛒 SWIFT SHOP", font=("Arial", 26, "bold"), fg="#2E7D32", bg="#F5F5F5")
        title_label.pack(pady=(50, 5))
        
        subtitle_label = tk.Label(self.home_frame, text="Select Your Language to Start Shopping", font=("Arial", 11), fg="#616161", bg="#F5F5F5")
        subtitle_label.pack(pady=(0, 35))
        
        grid_frame = tk.Frame(self.home_frame, bg="#F5F5F5")
        grid_frame.pack(pady=10)
        
        btn_styles = {
            "font": ("Arial", 11, "bold"), "bg": "#FFFFFF", "fg": "#2E7D32",
            "activebackground": "#2E7D32", "activeforeground": "#FFFFFF",
            "width": 18, "height": 2, "bd": 1, "relief": "solid"
        }
        
        tk.Button(grid_frame, text="ENGLISH", **btn_styles, command=lambda: self.initialize_market_view("English")).grid(row=0, column=0, padx=15, pady=12)
        tk.Button(grid_frame, text="YORUBA", **btn_styles, command=lambda: self.initialize_market_view("Yoruba")).grid(row=0, column=1, padx=15, pady=12)
        tk.Button(grid_frame, text="IGBO", **btn_styles, command=lambda: self.initialize_market_view("Igbo")).grid(row=1, column=0, padx=15, pady=12)
        tk.Button(grid_frame, text="HAUSA", **btn_styles, command=lambda: self.initialize_market_view("Hausa")).grid(row=1, column=1, padx=15, pady=12)
        
        pid_btn = tk.Button(grid_frame, text="PIDGIN", font=("Arial", 11, "bold"), bg="#FFFFFF", fg="#2E7D32", activebackground="#2E7D32", activeforeground="#FFFFFF", width=40, height=2, bd=1, relief="solid", command=lambda: self.initialize_market_view("Pidgin"))
        pid_btn.grid(row=2, column=0, columnspan=2, pady=15)
            
        start_guide = tk.Label(self.home_frame, text=UI_STRINGS["English"]["guide"], bg="#FFF9C4", fg="#5D4037", font=("Arial", 10, "italic"), bd=1, relief="solid", pady=8)
        start_guide.pack(side="bottom", fill="x")

  # --- MEMBER 2 & MEMBER 3: MAIN MARKET VIEW WITH SCROLLING GRID ---
    def create_market_screen(self):
        """Generates visual product catalog layout views with an integrated scrollbar."""
        self.clear_all_frames()
        
        self.market_frame = tk.Frame(self.root, bg="#F5F5F5")
        self.market_frame.pack(fill="both", expand=True)
        
        # 1. Mini top navigation selector ribbon
        mini_lang_frame = tk.Frame(self.market_frame, bg="#FFFFFF", bd=1, relief="groove")
        mini_lang_frame.pack(fill="x", padx=15, pady=5)
        
        for lang in ["English", "Yoruba", "Igbo", "Hausa", "Pidgin"]:
            btn_bg = "#2E7D32" if lang == self.current_language else "#F5F5F5"
            btn_fg = "#FFFFFF" if lang == self.current_language else "#212121"
            tk.Button(mini_lang_frame, text=lang, font=("Arial", 9, "bold"), bg=btn_bg, fg=btn_fg, width=9, command=lambda l=lang: self.change_language(l)).pack(side="left", padx=6, pady=5)
            
        self.welcome_label = tk.Label(self.market_frame, text=UI_STRINGS.get(self.current_language, UI_STRINGS["English"]).get("welcome", "Welcome"), font=("Arial", 14, "bold"), fg="#2E7D32", bg="#F5F5F5")
        self.welcome_label.pack(pady=4)
        
        self.title_label = tk.Label(self.market_frame, text=UI_STRINGS.get(self.current_language, UI_STRINGS["English"]).get("market_title", "Market"), font=("Arial", 11, "bold"), fg="#616161", bg="#F5F5F5")
        self.title_label.pack(pady=2)
        
        # 2. CREATE SCROLLABLE CANVAS STRUCTURE
        canvas_container = tk.Frame(self.market_frame, bg="#F5F5F5")
        canvas_container.pack(fill="both", expand=True, padx=15, pady=5)
        
        scrollbar = tk.Scrollbar(canvas_container, orient="vertical")
        scrollbar.pack(side="right", fill="y")
        
        # The Canvas acts as a view window over our scrollable area
        canvas = tk.Canvas(canvas_container, bg="#F5F5F5", yscrollcommand=scrollbar.set, highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)
        
        scrollbar.config(command=canvas.yview)
        
        # This interior frame holds the actual product item cards grid
        grid_container = tk.Frame(canvas, bg="#F5F5F5")
        
        # Bind the frame size configurations to update the canvas scrolling region bounds dynamically
        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        grid_container.bind("<Configure>", configure_scroll_region)
        
        # Center the grid frame smoothly inside the canvas area width
        canvas_frame_id = canvas.create_window((0, 0), window=grid_container, anchor="nw")
        
        def configure_canvas_width(event):
            canvas.itemconfig(canvas_frame_id, width=event.width)
        canvas.bind("<Configure>", configure_canvas_width)

        # Optional Mousewheel Support for effortless scrolling functionality
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # 3. POPULATE EVERY SINGLE PRODUCT FROM INVENTORY
        row_idx, col_idx = 0, 0
        
        for item in self.product_list:
            lang_column_key = f"{self.current_language}_Name"
            product_title = item.get(lang_column_key, item.get("English_Name", "Unknown Product"))
            price_value = item.get("Price_Naira", "0")
            
           # --- EXTENSIBLE IMAGE MAPPING LAYER ---
            english_name = item.get("English_Name", "").strip().lower()
            
            # 1. Eggs
            if "egg" in english_name:
                image_filename = "eggs.png"
                
            # 2. Fresh Pepper
            elif "fresh pepper" in english_name:
                image_filename = "fresh pepper.png"
                
            # 3. Brooms / Sweeper
            elif "broom" in english_name or "sweeper" in english_name:
                image_filename = "brooms.png"
                
            # 4. Tomatoes
            elif "tomato" in english_name:
                image_filename = "tomatoes.png"
                
            # 5. Palm Oil
            elif "palm oil" in english_name or "oil" in english_name:
                image_filename = "Oil.png"
                
            # 6. Smoked Fish
            elif "fish" in english_name:
                image_filename = "smokedfish.png"
                
            # 7. Onions
            elif "onion" in english_name:
                image_filename = "onions.png"
                
            # 8. Rice
            elif "rice" in english_name:
                image_filename = "rice.png"
                
            # 9. Soap
            elif "soap" in english_name:
                image_filename = "soap.png"
                
            # 10. Salt
            elif "salt" in english_name:
                image_filename = "salt.png"
                
            # 11. Sugar
            elif "sugar" in english_name:
                image_filename = "sugar.png"
                
            # 12. Pans
            elif "pan" in english_name:
                image_filename = "pans.png"
                
            # 13. Pots
            elif "pot" in english_name:
                image_filename = "pots.png"
                
            # 14. Toothpaste
            elif "toothpaste" in english_name or "tooth" in english_name:
                image_filename = "toothpaste.png"
                
            # 15. Bucket
            elif "bucket" in english_name:
                image_filename = "bucket.png"
                
            # 16. Chicken
            elif "chicken" in english_name:
                image_filename = "chicken.png"
                
            # 17. Long Pepper
            elif "long pepper" in english_name or "sombo" in english_name:
                image_filename = "modern long pepper.png"
                
            # 18. Milk
            elif "milk" in english_name:
                image_filename = "milk.png"
                
            # 19. Spaghetti
            elif "spaghetti" in english_name:
                image_filename = "spaghetti.png"
                
            # 20. Garri
            elif "garri" in english_name:
                image_filename = "garri.png"
                
            else:
                # Default safety fallback image asset configuration
                image_filename = "fresh pepper.png"
            
            card = tk.Frame(grid_container, bg="#FFFFFF", bd=1, relief="solid", padx=10, pady=8)
            card.grid(row=row_idx, column=col_idx, padx=12, pady=8, sticky="nsew")
            
            try:
                pil_image = Image.open(image_filename)
                pil_image = pil_image.resize((110, 85), Image.Resampling.LANCZOS)
                prod_img = ImageTk.PhotoImage(pil_image)
                img_lbl = tk.Label(card, image=prod_img, bg="#FFFFFF")
                img_lbl.image_ref = prod_img  
                img_lbl.pack(pady=(0, 4))
            except Exception:
                tk.Label(card, text="📦", font=("Arial", 22), bg="#FFFFFF").pack(pady=(12, 12))
            
            tk.Label(card, text=product_title, font=("Arial", 11, "bold"), bg="#FFFFFF", fg="#212121").pack(anchor="w")
            tk.Label(card, text=f"₦{price_value}", font=("Arial", 10, "bold"), bg="#FFFFFF", fg="#E53935").pack(anchor="w", pady=(1, 5))
            
            tk.Button(card, text="ADD TO BASKET", font=("Arial", 9, "bold"), bg="#2E7D32", fg="#FFFFFF", activebackground="#1B5E20", activeforeground="#FFFFFF", command=lambda name=product_title, price=price_value: self.add_to_basket(name, price)).pack(fill="x")
            
            col_idx += 1
            if col_idx > 1:
                col_idx = 0
                row_idx += 1
                
        grid_container.grid_columnconfigure(0, weight=1)
        grid_container.grid_columnconfigure(1, weight=1)

        # 4. Bottom controller bar navigation components
        nav_bar = tk.Frame(self.market_frame, bg="#FFFFFF", bd=1, relief="sunken")
        nav_bar.pack(side="bottom", fill="x")
        
        checkout_text = UI_STRINGS.get(self.current_language, UI_STRINGS["English"]).get("checkout", "Checkout")
        tk.Button(nav_bar, text=checkout_text, bg="#2E7D32", fg="white", font=("Arial", 10, "bold"), pady=5, command=self.create_cart_screen).pack(side="right", padx=20, pady=6)
        tk.Button(nav_bar, text="⬅ BACK TO HOME", font=("Arial", 9, "bold"), bg="#E0E0E0", command=self.return_to_home).pack(side="left", padx=20, pady=6)

        guide_text = UI_STRINGS.get(self.current_language, UI_STRINGS["English"]).get("guide", "Guide")
        self.guide_label = tk.Label(self.market_frame, text=guide_text, bg="#FFF9C4", fg="#5D4037", bd=1, relief="solid", anchor="w", font=("Arial", 10, "italic"), padx=12, pady=6)
        self.guide_label.pack(side="bottom", fill="x")


    # --- MEMBER 6: MANDATORY THIRD SCREEN (CART SUMMARY VIEW) ---
    def create_cart_screen(self):
        """Generates the third standalone checkout frame view to fulfill assignment criteria."""
        self.clear_all_frames()
        
        self.cart_frame = tk.Frame(self.root, bg="#F5F5F5")
        self.cart_frame.pack(fill="both", expand=True)
        
       # 1. Safely fetch the chosen language dictionary, fallback to English if missing entirely
        lang_dict = UI_STRINGS.get(self.current_language, UI_STRINGS.get("English", {}))
        
        # 2. Safely fetch the specific string, fallback to a hardcoded string if the key is missing
        basket_title_text = lang_dict.get("basket_title", "Shopping Basket Summary")
        
        tk.Label(self.cart_frame, text=basket_title_text, font=("Arial", 18, "bold"), fg="#2E7D32", bg="#F5F5F5").pack(pady=20)
        
        list_container = tk.Frame(self.cart_frame, bg="#FFFFFF", bd=1, relief="solid", padx=15, pady=15)
        list_container.pack(fill="both", expand=True, padx=30, pady=10)
        
        if not self.cart_items:
            empty_basket_text = lang_dict.get("empty_basket", "Your basket is currently empty.")
            tk.Label(list_container, text=empty_basket_text, font=("Arial", 12, "italic"), bg="#FFFFFF", fg="#757575").pack(pady=50)
        else:
            total_sum = 0
            for name, price in self.cart_items:
                item_row = tk.Frame(list_container, bg="#FFFFFF")
                item_row.pack(fill="x", pady=6)
                tk.Label(item_row, text=name, font=("Arial", 11), bg="#FFFFFF", fg="#212121").pack(side="left")
                tk.Label(item_row, text=f"₦{price}", font=("Arial", 11, "bold"), bg="#FFFFFF", fg="#E53935").pack(side="right")
                total_sum += int(price)
                
            # Divider line
            canvas_line = tk.Canvas(list_container, height=2, bg="#E0E0E0", highlightthickness=0)
            canvas_line.pack(fill="x", pady=15)
            
            total_row = tk.Frame(list_container, bg="#FFFFFF")
            total_row.pack(fill="x")
            tk.Label(total_row, text="TOTAL:", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#212121").pack(side="left")
            tk.Label(total_row, text=f"₦{total_sum}", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#E53935").pack(side="right")
            
        cart_nav_bar = tk.Frame(self.cart_frame, bg="#FFFFFF", bd=1, relief="sunken")
        cart_nav_bar.pack(side="bottom", fill="x")
        
        back_market_text = lang_dict.get("back_market", "⬅ BACK TO CATALOG")
        tk.Button(cart_nav_bar, text=back_market_text, font=("Arial", 9, "bold"), bg="#E0E0E0", command=self.create_market_screen).pack(side="left", padx=20, pady=12)
        tk.Button(cart_nav_bar, text="PLACE ORDER 🚀", font=("Arial", 9, "bold"), bg="#2E7D32", fg="white", command=self.trigger_order_finalization).pack(side="right", padx=20, pady=12)

    # --- MEMBER 4: SYSTEM INVENTORY EXTRACTOR ---
    def load_csv_inventory(self):
        """Pulls raw system inventory row assets from local storage tables."""
        self.product_list = []
        try:
            with open("swift_shop_inventory(2)(1).csv", mode="r", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)
                reader.fieldnames = [name.strip() for name in reader.fieldnames]
                for row in reader:
                    self.product_list.append(row)
        except FileNotFoundError:
            try:
                with open("swift_shop_inventory.csv", mode="r", encoding="utf-8-sig") as file:
                    reader = csv.DictReader(file)
                    reader.fieldnames = [name.strip() for name in reader.fieldnames]
                    for row in reader:
                        self.product_list.append(row)
            except FileNotFoundError:
                messagebox.showerror("File Missing", "Inventory data tables could not be opened.")

    # --- SHARED APP ROUTING UTILITIES ---
    def initialize_market_view(self, chosen_lang):
        self.current_language = chosen_lang
        self.create_market_screen()

    def return_to_home(self):
        self.create_home_screen()

    def add_to_basket(self, product_name, price):
        self.cart_items.append((product_name, price))
        alert_msg = f"{product_name} - " + UI_STRINGS[self.current_language]["item_added"]
        messagebox.showinfo("Basket Update", alert_msg)

    def trigger_order_finalization(self):
        messagebox.showinfo("Success", "Order successfully placed!")
        self.cart_items = []
        self.create_home_screen()

    def change_language(self, chosen_lang):
        """Updates the current active language state and refreshes the market screen."""
        self.current_language = chosen_lang
        self.create_market_screen()

    def clear_all_frames(self):
        """Helper to clear active frames safely out of the window frame container."""
        if self.home_frame: self.home_frame.pack_forget()
        if self.market_frame: self.market_frame.pack_forget()
        if self.cart_frame: self.cart_frame.pack_forget()

if __name__ == "__main__":
    main_window = tk.Tk()
    application_instance = SwiftShopApp(main_window)
    main_window.mainloop()
