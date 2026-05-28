
import requests
import tkinter as tk
from tkinter import messagebox

window= tk.Tk()
window.title("Weather app")
window.geometry("500x500")
FONT=("Arial",10,"bold",)


city = ""
current_temperature = "Veri Yok"
current_pressure = "Veri Yok"
current_humidity = "Veri Yok"
weather_description = "Veri Yok"




welcome= tk.Label( text="WELCOME TO WEATHER APP",font=("Arial",20,"bold",),fg="black",bg="yellow" )
welcome.config(padx=10, pady=10)
welcome.pack()

def first_page():
    global current_temperature, current_pressure, current_humidity, weather_description


    enter_city_label= tk.Label(text="Enter City",font=FONT,fg="black",bg="light blue")
    enter_city_label.place(x=210,y=100)

    city_entry= tk.Entry(width=20)
    city_entry.place(x=180,y=130)


    def button_clicked():
        global city, current_temperature, current_pressure, current_humidity,weather_description
        city= city_entry.get().strip()

        if city == "":
            print("Lütfen bir şehir adı girin!")
            return






        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid="YOUR API KEY"&units=metric'

        try:
                response = requests.get(url)
                last = response.json()

                if last.get("cod") != "404":
                    x = last["main"]
                    current_temperature = f"{x['temp']} °C"
                    current_pressure = f"{x['pressure']} hPa"
                    current_humidity = f"%{x['humidity']}"
                    z = last["weather"]
                    weather_description = z[0]["description"].capitalize()

                    enter_city_label.place_forget()
                    city_entry.place_forget()
                    city_button.place_forget()
                    my_listbox.place(x=190, y=100)
                    print(f"Şehir Seçildi: {city}")
                else:
                    print("Şehir bulunamadı! Lütfen yazımı kontrol edin.")

        except requests.exceptions.RequestException:
            print("İnternet bağlantısı hatası!")



    city_button = tk.Button(text="Next", command=button_clicked)
    city_button.place(x=330, y=125)


    def listbox_clicked(event):
        selection = my_listbox.curselection()

        if selection:
            secilen_eleman = my_listbox.get(selection[0])

            
            answer_message = {
                "Temperature": f"Sıcaklık: {current_temperature}",
                "pressure": f"Basınç: {current_pressure}",
                "Humidity": f"Nem: {current_humidity}",
                "Description": f"Durum: {weather_description}"
            }

            print(answer_message.get(secilen_eleman, "Bilinmeyen Seçim"))

    my_listbox= tk.Listbox(width=15)
    my_listbox.place_forget()
    element_list= ["Temperature","pressure","Humidity","Description"]
    for i in range(len(element_list)):
        my_listbox.insert(i,element_list[i])

    my_listbox.bind("<<ListboxSelect>>",listbox_clicked)



first_page()

window.mainloop()

