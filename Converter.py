print("Sensitivity Converter")

def main():
    mode = int(input("1. SoundSpace > Rhythia\n2. Rhythia > SoundSpace\n\n > "))
    if mode == 1:
        dpi = int(input("Mouse DPI\n> "))
        sens = float(input("SoundSpace (Roblox) Sens\n> "))
        print("Rhythia Sensitivity")
        print(round(((sens)*1.9689), 3))
        input()

    if mode == 2:
        dpi = int(input("Mouse DPI\n> "))
        sens = float(input("Rhythia Sens\n> "))
        print("SoundSpace Sensitivity")
        print(round(((sens)/1.9689), 2))
        input()

if __name__ == '__main__':
    main()
