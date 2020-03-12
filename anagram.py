import tkinter as tk


class Anagram():
    def __init__(self, str1, str2):
        self.str1 = str1.strip()
        self.str2 = str2.strip()

    def is_anagram(self):
        str1_list = list(self.str1)
        str2_list = list(self.str2)

        if sorted(str1_list) == sorted(str2_list):
            print('True', str1_list, str2_list)
            return 'Is anagram'
        else:
            print('False', str1_list, str2_list)
            return 'Is not anagram'




if __name__ == '__main__':

    master = tk.Tk()
    master.geometry('500x500')

    def make_inputs():
        tk.Label(master, text="word 1").grid(row=0, column=0)
        tk.Label(master, text="word 2").grid(row=0, column=2)


    def make_entry():
        e1 = tk.Entry(master)
        e2 = tk.Entry(master)
        e1.grid(row=0, column=1)
        e2.grid(row=0, column=3)
        return e1, e2


    def make_display(string1, string2):
        anagram = Anagram(string1, string2)
        tk.Label(master, text=anagram.is_anagram()).grid(row=3, column=1)


    def make_button(entry_object_1, entry_object_2):
        button = tk.Button(master, text='Show', command=lambda: make_display(entry_object_1.get(), entry_object_2.get()))
        button.grid(row=3, column=2, sticky=tk.W, pady=4)


    make_inputs()
    t, k = make_entry()
    make_button(t, k)
    master.mainloop()