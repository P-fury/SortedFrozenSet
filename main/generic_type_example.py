# from typing import TypeAlias, TypeVar
#
# Book: TypeAlias = dict[str, str]
# Movie: TypeAlias = dict[str, int]
#
# T = TypeVar('T')
#
# book: Book = {
#     "author": "Henryk Sienkiewicz",
#     "title": "Ogniem i Mieczem"
# }
#
# movie: Movie = {
#     "author": 42,
#     "title": 42,
# }
#
#
# def get_author(obj: dict[str, T]) -> T:
#     return obj["author"]
#
#
# print(get_author(book))
# print(get_author(movie))
#
#
#
# b = get_author(book)
# m = get_author(movie)
#
#
#
# print(b.upper())
# print(m.upper())