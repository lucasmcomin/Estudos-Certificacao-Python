import xml.etree.ElementTree as et
class ForecastXmlParser:

    def __init__(self, xml_file):

        self.tree = et.parse(xml_file)
        self.root = self.tree.getroot()

    
    def parse(self):
        convert = TemperatureConverter()
        for item in self.root:
            print(item[0].text, ":", item[1].text, "Celsius,", convert.convert_celsius_to_fahrenheit(int(item[1].text)), "Fahrenheit")


class TemperatureConverter:

    def convert_celsius_to_fahrenheit(self, temp_celsius):

        return round(9/5 * temp_celsius + 32, 1)
    



forecast = ForecastXmlParser("BD_FILES/forecast.xml")
forecast.parse()