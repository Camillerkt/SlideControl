import os
import platform
from pynput.keyboard import Key, Controller


# Non fonctionnel sur Linux


class Slide:
    def __init__(self, opsys, ppt_file_name, ppt_path):
        self.opsys = opsys
        self.ppt_file_name = ppt_file_name
        self.ppt_path = ppt_path

    def createCopy(self):
        first_path = self.ppt_path + self.ppt_file_name + '.pptx'
        final_path = self.ppt_path + self.ppt_file_name + '.pps'
        if self.opsys == 'Darwin':  # Darwin = Mac
            os.system("cp -R {} {}".format(first_path, final_path))
        elif self.opsys == 'Linux':
            os.system("cp {} {}".format(first_path, final_path))
        elif self.opsys == 'Windows':
            os.system("copy {} {}".format(first_path, final_path))
        else:
            print('Malheureusement, votre système d\'exploitation n\'est pas reconnu')

    def openFile(self):
        path = self.ppt_path + self.ppt_file_name + '.pps'
        if self.opsys == 'Darwin':
            os.system("open {}".format(path))
        elif self.opsys == 'Linux':
            print('Malheureusement, pour l\'instant, le système d\'exploitation Linux que vous utilisez n\'est pas adapaté au programme.')
        elif self.opsys == 'Windows':
            os.system("start {}".format(path))
        else:
            print('Malheureusement, votre système d\'exploitation n\'est pas reconnu')

    def nextAndPrevious(self, action):
        keyboard = Controller()
        if action == 'next':
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        elif action == 'previous':
            keyboard.press(Key.left)
            keyboard.release(Key.left)


def Main():
    # système d'exploitation, nom du fichier, destination du fichier
    file_name = input(
        '- Veuillez vous assurer d\'être en possession d\'une connexion Internet sur votre appareil\n- Veuillez indiquer le nom du fichier de présentation. \n (ex: presentation)\n L\'extension de fichier .pptx n\'est pas à spécifier \n Les espaces, et caractères spéciaux ne sont pas tolérés \n>> ')
    slide = Slide(platform.system(), file_name, 'slides/')
    slide.createCopy()
    slide.openFile()


if __name__ == '__main__':
    Main()
