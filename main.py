from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class BudgetApp(App):
    def build(self):
        self.total_budget = 0.0
        self.total_spent = 0.0
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # হেডার
        header = Label(text="Smart Pocket Budget", font_size='22sp', size_hint_y=None, height=40)
        main_layout.add_widget(header)
        
        # বাজেট ইনপুট
        self.budget_input = TextInput(hint_text="Enter Total Budget (Tk)", input_filter='float', multiline=False, size_hint_y=None, height=45)
        main_layout.add_widget(self.budget_input)
        
        set_btn = Button(text="Set Budget", background_color=(0.2, 0.6, 1, 1), size_hint_y=None, height=45)
        set_btn.bind(on_press=self.set_budget)
        main_layout.add_widget(set_btn)
        
        # স্ট্যাটাস লেবেল
        self.status_label = Label(text="Budget: 0 Tk | Spent: 0 Tk | Remaining: 0 Tk", font_size='14sp', size_hint_y=None, height=40)
        main_layout.add_widget(self.status_label)
        
        # আইটেম ও দাম ইনপুট
        item_layout = BoxLayout(size_hint_y=None, height=45, spacing=5)
        self.item_name = TextInput(hint_text="Item Name", multiline=False)
        self.item_price = TextInput(hint_text="Price", input_filter='float', multiline=False)
        item_layout.add_widget(self.item_name)
        item_layout.add_widget(self.item_price)
        main_layout.add_widget(item_layout)
        
        add_btn = Button(text="Add Item", background_color=(0.2, 0.7, 0.3, 1), size_hint_y=None, height=45)
        add_btn.bind(on_press=self.add_item)
        main_layout.add_widget(add_btn)
        
        # তালিকা দেখানোর স্ক্রোল ভিউ
        self.scroll = ScrollView()
        self.item_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.item_list.bind(minimum_height=self.item_list.setter('height'))
        self.scroll.add_widget(self.item_list)
        main_layout.add_widget(self.scroll)
        
        return main_layout

    def set_budget(self, instance):
        if self.budget_input.text:
            self.total_budget = float(self.budget_input.text)
            self.update_status()

    def add_item(self, instance):
        name = self.item_name.text.strip()
        price_text = self.item_price.text.strip()
        
        if name and price_text:
            price = float(price_text)
            self.total_spent += price
            
            entry = Label(text=f"- {name}: {price} Tk", font_size='15sp', size_hint_y=None, height=35, halign='left')
            self.item_list.add_widget(entry)
            
            self.item_name.text = ""
            self.item_price.text = ""
            self.update_status()

    def update_status(self):
        remaining = self.total_budget - self.total_spent
        if remaining < 0:
            msg = f"OVER BUDGET! Spent: {self.total_spent} Tk | Extra: {abs(remaining)} Tk"
        else:
            msg = f"Budget: {self.total_budget} Tk | Spent: {self.total_spent} Tk | Left: {remaining} Tk"
        self.status_label.text = msg

if __name__ == "__main__":
    BudgetApp().run()
