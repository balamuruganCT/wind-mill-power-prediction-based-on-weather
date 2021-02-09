import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
from numpy.random import seed
from scipy.stats import pearsonr
from tkinter import messagebox
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn.utils._weight_vector
model_lr = LinearRegression()
def root_destroy():
    root.quit()
seed(123)
file_path = "https://drive.google.com/uc?export=download&id=1_yRWosrRMuhWK9sdJ2j-yiqa_oY1YVjr"
dataset = pd.read_csv(file_path)
var_1 = dataset['power_generation (unit)']
'''Gui for the linear regression model or power prediction method'''
root = Tk()
root.title("POWER PREDICTION APPLICATION")
root.geometry("1500x1500")
root.config(bg = 'powder blue')
L2 = Label(root,fg = 'black',text = "To find correlation ",font = ('Helvetica',16))
L2.place(x = 100,y = 40,anchor = 'center')
ttk.Label(root, text = "Select field  :", font = ("Helvetica", 12)).place(x = 70, y = 100, anchor= 'center')
n = tk.StringVar()
n.set('select here...')
choosing_variable = ttk.Combobox(root, width = 27, textvariable = n,font = ("Helvetica", 12))
choosing_variable.place(x=280, y=100, anchor='center')
choosing_variable['values'] = ('Temperature (C)',
                          'Apparent Temperature (C)',
                          'Humidity',
                          'Wind Speed  (km/h)',
                          'Wind  Bearing  (degrees)',
                          'Visibility (km)',
                          'Cloud Cover',
                          'Pressure (millibars)')
B2 = Button(root,text='OK', fg = 'black',font = ("Helvetica", 12,'bold'), command=lambda :correrlation_func())
B2.place(x =435,y = 80)
def correrlation_func():
    some = choosing_variable.get()
    string_var = str(some)
    try:
        var_2 = dataset[string_var]
        T2 = Text(root, width=10, height=2, fg='black', font=('Helvetica', 15))
        T2.place(x=420,y=160, anchor='center')
        corr, _ = pearsonr(var_1, var_2)
        T2.insert(END,'correlation: %.3f' % corr)
        if (corr > 0.9):
            l2 = tk.Label(root, text='Efficient Variable', width=20,font=('Helvetica', 14))
            l2.place(x=90, y=145)
        elif (corr >= 0.5 and corr < 0.9):
            l2 = tk.Label(root, text='Moderate', width=20,font=('Helvetica', 14))
            l2.place(x=90, y=145)
        else:
            l2 = tk.Label(root, text='Not efficient', width=20,font=('Helvetica', 14))
            l2.place(x=90, y=145)
    except BaseException as e:
        messagebox.showinfo("ALERT MESSAGE!!!", e)
L0 = Label(root,fg = 'black',text = "WIND MILL",font = ('Helvetica',16,"bold"))
L0.place(x = 650,y = 10,anchor = 'center')
L1 = Label(root,fg = 'black',text = "POWER PREDICTION ",font = ('Helvetica',22,"bold"))
L1.place(x = 650,y = 40,anchor = 'center')
B1 = Button(root,padx=8,pady=4,bd=16,fg="black",font=('arial',12,'bold'),width=10,text="EXIT",bg="powder blue",command = root_destroy)
B1.place(x = 1150,y = 20)
L2 = Label(root,fg = 'black', text = "Output Console", font = ('Helvetica',18))
L2.place(x = 1000,y = 70,anchor = 'center')
T1 = Text(root,bd= 16,width = 50,height = 25,fg = 'black',bg='powder blue',font = ('Courier',15,'bold'))
T1.place(x = 1000,y = 400,anchor='center')
L3 = Label(root,fg = 'black',text = "Select field for training a data",font = ('Helvetica',16))
L3.place(x = 150,y = 210,anchor = 'center')
ttk.Label(root, text = "Select field  :", font = ("Helvetica", 12)).place(x = 70, y = 260, anchor= 'center')
n_2 = tk.StringVar()
n_2.set('Select here...')
choosing_variable_2 = ttk.Combobox(root, width = 27, textvariable = n_2,font = ("Helvetica", 12))
choosing_variable_2.place(x=270, y=260, anchor='center')
# Adding combobox drop down list
choosing_variable_2['values'] = ('Temperature (C)',
                          'Apparent Temperature (C)',
                          'Humidity',
                          'Wind Speed  (km/h)',
                          'Wind  Bearing  (degrees)',
                          'Visibility (km)',
                          'Cloud Cover',
                          'Pressure (millibars)')
B4 = Button(root,text='TRAIN', fg = 'black',font = ("Helvetica", 12,'bold'), command=lambda :some_2())
B4.place(x =435 ,y = 240)
def some_2():
    some_2 = choosing_variable_2.get()
    string_var_2 = str(some_2)
    try:
        x = dataset['power_generation (unit)']
        y = dataset[string_var_2]
        X = x.values.reshape(len(x), 1)
        Y = y.values.reshape(len(y), 1)
        train_x, test_x = train_test_split(X, test_size=0.30, random_state=4)
        train_y, test_y = train_test_split(Y, test_size=0.30, random_state=4)
        model_lr.fit(train_x, train_y, )
        coeff = model_lr.coef_
        intercept = model_lr.intercept_
        T1.insert(END, "\n" "\n" "co-efficient : %f" % (coeff))
        T1.insert(END, "\n""\n" "Intercept : %f" % (intercept))
        messagebox.showinfo("SUCCESSFULL INFORMATION",message="Data Training successfull")
        L5 = Label(root, fg='black', text="Visualize Trained Data", font=('Helvetica', 16))
        L5.place(x=270, y=325, anchor='center')
        B5 = Button(root, text='SHOW', fg='black', font=("Helvetica", 12, 'bold'), command=lambda: visulize())
        B5.place(x=435, y=305)
        def visulize():
            plt.scatter(train_x, train_y, color="red")
            plt.plot(train_x, model_lr.predict(train_x), color="green")
            plt.title("power_generation (unit) vs " + string_var_2)
            plt.xlabel("power_generation (unit)")
            plt.ylabel(string_var_2)
            plt.show()
    except BaseException as e:
        messagebox.showinfo("ALERT MESSAGE!!!",e)
pos_data = len(dataset) - 1
val_test = (dataset.iloc[pos_data])
L3 = Label(root,fg = 'black',text = "Select test field for prediction ",font = ('Helvetica',16))
L3.place(x = 150,y = 400,anchor = 'center')
ttk.Label(root, text = "Select field  :", font = ("Helvetica", 12)).place(x = 70, y = 450, anchor= 'center')
n_1 = tk.StringVar()
n_1.set('select here...')
choosing_variable_1 = ttk.Combobox(root, width = 27, textvariable = n_1,font = ("Helvetica", 12))
choosing_variable_1.place(x=270, y=450, anchor='center')
choosing_variable_1['values'] = ('Temperature (C)',
                          'Apparent Temperature (C)',
                          'Humidity',
                          'Wind Speed  (km/h)',
                          'Wind  Bearing  (degrees)',
                          'Visibility (km)',
                          'Cloud Cover',
                          'Pressure (millibars)')
B3 = Button(root,text='PREDICT', fg = 'black',font = ("Helvetica", 12,'bold'), command=lambda :prediction_func())
B3.place(x =435 ,y = 430)
def prediction_func():
    some_1 = choosing_variable_1.get()
    string_var_1 = str(some_1)
    try:
        testing_var = val_test[string_var_1]
        testing_var_reshape = testing_var.reshape(1, 1)
        predicted_val = model_lr.predict(testing_var_reshape)
        T1.insert(END, "\n""\n""Testing Variable:" + " " + string_var_1)
        T1.insert(END, "\n" "Testing Value: %f" % testing_var)
        T1.insert(END,"\n" "Expected power: %f"%(predicted_val)+ " " + "units/second")
        T1.insert(END, "\n""\t""(until weather change)")
        L6 = Label(root, fg='black', text="Visualize Trained Data", font=('Helvetica', 16))
        L6.place(x=270, y=520, anchor='center')
        B6 = Button(root, text='SHOW', fg='black', font=("Helvetica", 12, 'bold'), command=lambda: visulize_predicted())
        B6.place(x=435, y=505)
        def visulize_predicted():
            plt.scatter(predicted_val,testing_var_reshape,color="red")
            plt.plot(predicted_val,model_lr.predict(predicted_val), color="green")
            plt.title("power_generation (unit) vs " + string_var_1)
            plt.xlabel(string_var_1)
            plt.ylabel("power_generation (unit)")
            plt.show()
    except BaseException as e:
        messagebox.showinfo("ALERT MESSAGE!!!", e)
T1.insert(END,"\t" "Output based on selected variables")
root.mainloop()
