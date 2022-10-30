import exo1.main as exo1
import exo2.main as exo2
import exo3.main as exo3
import exo4.main as exo4
import exo5.main as exo5


def main():
    numero = input("Quel exercice voulez-vous exécuter ? ")
    if numero == "1":
        exo1.main()
    elif numero == "2":
        exo2.main()
    elif numero == "3":
        exo3.main()
    elif numero == "4":
        exo4.main()
    elif numero == "5":
        exo5.main()
    else:
        print("L'exercice n'existe pas")


# -----------------------------------------------------------------

if __name__ == "__main__":
    main()
