import tkinter as tk
from tkinter import messagebox
from sklearn.tree import DecisionTreeClassifier

X = [[8,7,1],[3,4,5],[7,6,2],[2,3,6],[6,7,3]]
y = ['Fresh','Spoiled','Fresh','Spoiled','Fresh']

model = DecisionTreeClassifier()
model.fit(X,y)

def predict_freshness():
    color=int(color_entry.get())
    firmness=int(firmness_entry.get())
    days=int(days_entry.get())
    prediction=model.predict([[color,firmness,days]])[0]
    messagebox.showinfo("Prediction",f"The produce is likely: {prediction}")

root=tk.Tk()
root.title("Grocery Freshness Predictor")
tk.Label(root,text="Color (1-10):").pack()
color_entry=tk.Entry(root); color_entry.pack()
tk.Label(root,text="Firmness (1-10):").pack()
firmness_entry=tk.Entry(root); firmness_entry.pack()
tk.Label(root,text="Days Since Purchase:").pack()
days_entry=tk.Entry(root); days_entry.pack()
tk.Button(root,text="Predict",command=predict_freshness).pack()
root.mainloop()
