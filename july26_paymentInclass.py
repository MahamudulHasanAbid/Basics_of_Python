from abc import ABC, abstractmethod

# Abstraction
class payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Inheritance:
class bkashpayment(payment):
    def __init__(self, phone_number, initial_balance):
        self.phone_number = phone_number
        # Encapsulation
        self.__balance = initial_balance

    # For accessing encapsulated data (getter)
    def get_balance(self):
        return self.__balance
    
    def process_payment(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfull Transaction: {amount}, tk payment done. Current balance: {self.__balance} tk")
        else:
            print(f"Access denied. NO sufficient balance")
# ২. Inheritance: আরেকটি চাইল্ড ক্লাস
class RocketPayment(Payment):
    def __init__(self, account_id, initial_balance):
        self.account_id = account_id
        self.__balance = initial_balance

    def process_payment(self, amount):
        # রকেটে হয়তো পেমেন্টের নিয়ম একটু ভিন্ন (যেমন এক্সট্রা চার্জ)
        total_cost = amount + 2 # ২ টাকা ভ্যাট বা চার্জ
        if total_cost <= self.__balance:
            self.__balance -= total_cost
            print(f"রকেট সফল: {amount} টাকা পেমেন্ট হয়েছে (চার্জ ২ টাকা)। বর্তমান ব্যালেন্স: {self.__balance} টাকা।")
        else:
            print("রকেট ব্যর্থ: পর্যাপ্ত ব্যালেন্স নেই!")


# ৪. Polymorphism: এই ফাংশনটি জানেই না সে বিকাশ নাকি রকেট ব্যবহার করছে, সে শুধু পেমেন্ট প্রসেস করবে
def execute_transaction(payment_object, amount):
    # একই মেথড নাম (process_payment) ভিন্ন ভিন্ন ক্লাসে ভিন্নভাবে কাজ করছে
    payment_object.process_payment(amount)

# --- রান করার সেশন ---

# অবজেক্ট তৈরি
bkash = BkashPayment("01711122233", 500)
rocket = RocketPayment("12345-6", 1000)

print("--- পেমেন্ট শুরু ---")
# পলিমরফিজম টেস্ট: একই ফাংশনে ভিন্ন অবজেক্ট পাঠাচ্ছি
execute_transaction(bkash, 200)   # বিকাশের নিয়ম চলবে
execute_transaction(rocket, 200)  # রকেটের নিয়ম চলবে

print("\n--- এনক্যাপসুলেশন টেস্ট ---")
# নিচে কমেন্ট করা লাইনটি আনকমেন্ট করলে Error আসবে, কারণ __balance প্রাইভেট!
# print(bkash.__balance) 

# কিন্তু আমরা সিকিউর মেথড দিয়ে ব্যালেন্স দেখতে পারব:
print(f"বিকাশ অ্যাকাউন্টের ভেতরের ব্যালেন্স: {bkash.get_balance()} টাকা।")
