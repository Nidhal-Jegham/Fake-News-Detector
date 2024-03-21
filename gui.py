import customtkinter as ctk
import tkinter as tk
import pickle as pickle
import pandas as pd
from nltk.stem.porter import PorterStemmer
import re 
import nltk
from nltk.corpus import stopwords


def insert_random_text():
    # Select a random row from the DataFrame
    random_row = df.sample()
    # Get the text from the selected row
    random_text = random_row['text'].values[0]  # Assuming 'text' is the column name
    # Insert the random text into the entry field
    entry.delete(0, ctk.END)  # Clear any existing text in the entry field
    entry.insert(0, random_text)




load_model = pickle.load(open('rfc_model.sav', 'rb'))
df= pd.read_csv('manual_testing.csv')


testing_news=''
def manual_testing(news):
    testing_news = {"text":[news]}
    new_df = pd.DataFrame(testing_news)

    return new_df


port_stemmer= PorterStemmer()

nltk.download('stopwords')

def stemmer(content):
    stemmed_content=re.sub('[^a-zA-Z]',' ', content)
    stemmed_content= stemmed_content.lower()
    stemmed_content= stemmed_content.split()
    stemmed_content= [port_stemmer.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content= ' '.join(stemmed_content)
    return stemmed_content

def reuters_removal(text):
    reuters_text=''
    reuters_text= text.split()
    reuters_text= [word for word in reuters_text if not word=="(Reuters)"]
    reuters_text= " ".join(reuters_text)
    return reuters_text

def man_testing(news):
    news_df= manual_testing(news)
    news_df['text']=news_df['text'].apply(stemmer)
    news_df= news_df['text']
    prediction= load_model.predict(news_df)
    result_label.configure( text="These News are ")
    result_label_2.configure(text=prediction[0])
    if prediction[0]=='True':
        result_label_2.configure(text_color='green')
    else:
        result_label_2.configure(text_color='#990000')
    return prediction

def perform_manual_testing():
    # Get the text from the entry field
    text = entry.get()
    # Call the manual_testing function with the text
    result = man_testing(text)

root = ctk.CTk()
root.geometry("2800 x 1480")  
root.title("Fake News Detector")

bg_color = "#660606" 
fg_color = "#000000"  
button_color = "#800000"  

font_size = 14


# Add title label
title_label = ctk.CTkLabel(master=root, text="Fake News Detector", font=ctk.CTkFont(family="Helvetica", size=60, weight='bold'), 
                         text_color='#990000', fg_color='transparent') 
title_label.pack(pady=(50, 0))  # Adjusted padding

# Create input field
entry = ctk.CTkEntry(master=root, width=700, height=50, bg_color=bg_color, 
                     corner_radius=4, font=ctk.CTkFont(family="Helvetica", size=16),placeholder_text="Let's fact check News...",
                     justify="left")
entry.pack(padx=20, pady=(10,10), expand=True)  # Adjusted padding

# Create buttons
button_frame = ctk.CTkFrame(master=root, fg_color='transparent')  # Frame for buttons with dark background
button_frame.pack(pady=(10, 20))  # Adjusted padding

random_button = ctk.CTkButton(master=button_frame, text='Random News', width=150, height=40, fg_color=button_color,  hover_color='#ad0909',
                              corner_radius=4, font=ctk.CTkFont(family="Arial", size=20), command=insert_random_text)
random_button.pack(side="left", padx=10)

check_button = ctk.CTkButton(master=button_frame, text='Fact-Check', width=150, height=40, hover_color='#ad0909',
                             fg_color=button_color,  corner_radius=4, font=ctk.CTkFont(family="Arial", size=20), command=perform_manual_testing)
check_button.pack(side="left", padx=10)

# Create a label to display the result
result_frame = ctk.CTkFrame(master=root, fg_color='transparent', width=360)
result_frame.pack(pady=(0, 80))  # Adjusted padding
result_label = ctk.CTkLabel(result_frame, text="", font=ctk.CTkFont(family="Helvetica", size=24,), text_color='white', fg_color='transparent')
result_label.pack(side="left")
result_label_2 = ctk.CTkLabel(result_frame, text='', font=ctk.CTkFont(family="Helvetica", size=24, weight='bold'), 
                              text_color='#990000', fg_color='transparent')
result_label_2.pack(side="right")




root.mainloop()
