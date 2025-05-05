import tkinter as tk
from tkinter import *

def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def on_find_click():
    input_text = entry.get()
    try:
        # Convert input to list of ints
        nums = [int(x.strip()) for x in input_text.split(",")]

        # Check for duplicates
        if len(nums) != len(set(nums)):
            raise ValueError("Input contains duplicates.", fg="yellow")

        # Check range
        if any(x < 0 or x > len(nums) for x in nums):
            raise ValueError(f"Numbers must be between 0 and {len(nums)}.", fg="yellow")

        missing = find_missing_number(nums)
        result_label.config(text=f"🎯 Missing number is: {missing}", fg="green")

    except ValueError as ve:
        result_label.config(text=f"❌ Error: {ve}", fg="red")
    except:
        result_label.config(text="❌ Invalid input. Use format like 3,0,1", fg="red")

# GUI setup
root = tk.Tk()
root.title("Missing Number Game 🎯")
root.geometry("900x500")

bgImage = PhotoImage(file="bgheart.png")
bgLabel = Label(root, image=bgImage)
bgLabel.place(relheight=1, relwidth=1)

bgLabel = PhotoImage(file="label.png")
tk.Label(root, text="Enter numbers \n(example. 3,0,1):",
         font=("Courier", 16),
         image=bgLabel,
         compound="center",
         width=400, height=50).pack(pady=20)

entry = tk.Entry(root, width=40,
                 borderwidth= 0,
                 font=("Courier", 16))
entry.pack(pady=10, ipady=10)

buttonMissingNumber = PhotoImage(file="button.png")
buttonPhoto = buttonMissingNumber.subsample(5,5)
tk.Button(root, 
          image = buttonPhoto,
          height= 200,
          width= 200,
          command=on_find_click).pack(pady=30)

result_label = tk.Label(root, text="", font=("Courier", 18))
result_label.pack(pady=20)

root.mainloop()
