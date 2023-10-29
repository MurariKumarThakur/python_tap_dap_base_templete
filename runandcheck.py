from driverFactory.DriverFactory import DriverFactory
from utils.ConfigReader import ConfigReader

# Get the config property file path
# config_path = FilePath.get_config_property_file_path()
# print(config_path)

# Create an instance of ConfigReader


config_reader = ConfigReader()

# Get the properties from the instance
properties = config_reader.get_properties()

# Access specific properties
print(properties.get('General', 'browser'))

# DriverFactory.initialize_browser(properties.get('General', 'browser'))
