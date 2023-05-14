import os
import tkinter
from tkinter import filedialog, messagebox

import customtkinter
from PIL import Image
from pytube import YouTube

def ytVideoQuality(link):

    yt = YouTube(link)

    # Obtener todas las opciones de calidad de video optimas disponibles en formato mp4
    video_options = yt.streams.filter(type="video", file_extension="mp4",  progressive=True)

    # View video-quiality options
    videoQuality = []
    for i, stream in enumerate(video_options):
        videoQuality.append(stream.resolution)

    return videoQuality


def dowloadVideo(link, video_resolution, download_path):

    # link
    yt = YouTube(link)

    # resolución seleccionada
    stream = yt.streams.filter(res=video_resolution, file_extension="mp4").first()
    stream.download(output_path=download_path)

    # Descarga Exitosa
    messagebox.showinfo("Yt-Download", "Descarga Exitosa!!!")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window appearance
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        # configure window title
        self.title("YT-CodeDownload by-MauroPepa.py")

        # configure window size
        self.geometry(f"{400}x{450}")
        self.resizable(False, False)

        # create canvas
        self.frame = customtkinter.CTkFrame(master=self, corner_radius=30)
        self.frame.pack(fill="both", expand=True)
        self.frame.place(relx=0.07, rely=0.07, relwidth=0.87, relheight=0.87)

        # TEXT-LABEL
        self.label = customtkinter.CTkLabel(master=self.frame, text="YT-DOWNLOAD", font=("Arial Black", 24, "underline"))
        self.label.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)

        # load image qr ---> GITHUB/PEPAXD
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "youtube-download.png")),
                                                       size=(300, 250))
        self.home_frame_large_image_label = customtkinter.CTkLabel(master=self.frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.place(relx=0.5, rely=0.46, anchor=tkinter.CENTER)

        def linkYoutube(event=None):  # Se agrega el parámetro event
            ytLink = self.entry.get()
            QualityVideo = ytVideoQuality(ytLink)

            def click_button():
                # Obtener la ruta de descarga del usuario
                download_path = filedialog.askdirectory()

                # Obtener la opción de calidad de video seleccionada
                video_resolution = self.appearance_mode_optionemenu.get()

                # Descargar el video en la calidad seleccionada
                dowloadVideo(ytLink, video_resolution, download_path)


            # create button QR-GENERATOR
            self.main_button = customtkinter.CTkButton(master=self.frame, command=click_button, fg_color="transparent",
                                                       text="DOWNLOAD", border_width=2,
                                                       text_color=("gray10", "#DCE4EE"))
            self.main_button.place(relx=0.25, rely=0.92, anchor=tkinter.CENTER)

            # MENU OPTION QUALITY
            self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame, width=170, values=QualityVideo)
            self.appearance_mode_optionemenu.set(max(QualityVideo))
            self.appearance_mode_optionemenu.place(relx=0.71, rely=0.92, anchor=tkinter.CENTER)

        # create entry link-qr
        self.entry = customtkinter.CTkEntry(self.frame, placeholder_text="Add YT-link and press enter", width=320)
        self.entry.place(relx=0.5, rely=0.83, anchor=tkinter.CENTER)

        # Enlazar la función linkYoutube con el evento KeyRelease
        self.entry.bind("<Return>", linkYoutube)



if __name__ == "__main__":
    app = App()
    app.mainloop()