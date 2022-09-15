import invoiceReporter
import pdfConverter
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 

class InvoiceReportApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 2
        self.window.add_widget(Image("icon.png"))

        return self.window

if __name__ == "__main__":
    InvoiceReportApp().run()


#invoiceReporter.report(pdfConverter.importReport(), pdfConverter.importInvoices())