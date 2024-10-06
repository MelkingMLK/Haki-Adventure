import xml.etree.ElementTree as ET


class SettingsManager:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    def get_current_resolution(self):
        resolution = self.root.find('resolution').get('current')
        return resolution

    def get_current_master_volume(self):
        master_volume = self.root.find('masterVolume').get('current')
        return int(master_volume)

    def get_current_effects_volume(self):
        effects_volume = self.root.find('effectsVolume').get('current')
        return int(effects_volume)

    def update_resolution(self, new_resolution):
        self.root.find('resolution').set('current', new_resolution)
        self.tree.write('settings.xml')  # Salva le modifiche

    def update_master_volume(self, new_volume):
        self.root.find('masterVolume').set('current', str(new_volume))
        self.tree.write('settings.xml')  # Salva le modifiche

    def update_effects_volume(self, new_volume):
        self.root.find('effectsVolume').set('current', str(new_volume))
        self.tree.write('settings.xml')  # Salva le modifiche