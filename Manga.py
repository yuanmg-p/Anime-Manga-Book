class Manga:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"


class MangaLibrary:
    def __init__(self):
        self.mangas = []

    def add_manga(self, manga):
        self.mangas.append(manga)

    def list_mangas(self):
        if not self.mangas:
            print("No manga in the library.")
        else:
            print("Manga in the library:")
            for manga in self.mangas:
                print(manga)

    def search_by_title(self, title):
        found_mangas = [manga for manga in self.mangas if manga.title.lower() == title.lower()]
        if found_mangas:
            print("Manga found with matching title:")
            for manga in found_mangas:
                print(manga)
        else:
            print("No manga found with matching title.")

    def search_by_author(self, author):
        found_mangas = [manga for manga in self.mangas if manga.author.lower() == author.lower()]
        if found_mangas:
            print("Manga found with matching author:")
            for manga in found_mangas:
                print(manga)
        else:
            print("No manga found with matching author.")


# Example usage
if __name__ == "__main__":
    manga_library = MangaLibrary()

    # Adding mangas to the library
    manga1 = Manga("Naruto", "Masashi Kishimoto", "Shonen")
    manga2 = Manga("One Piece", "Eiichiro Oda", "Shonen")
    manga3 = Manga("Death Note", "Tsugumi Ohba", "Mystery")

    manga_library.add_manga(manga1)
    manga_library.add_manga(manga2)
    manga_library.add_manga(manga3)

    # Listing all mangas
    manga_library.list_mangas()

    # Searching mangas by title
    manga_library.search_by_title("One Piece")

    # Searching mangas by author
    manga_library.search_by_author("Tsugumi Ohba")
