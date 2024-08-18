"""
Implement an interface, which is meant to enable working with document.
Document can have draft, editing, review and finilized states.
"""

from dataclasses import dataclass
from typing import Protocol


class DocumentState(Protocol):
    def edit(self):
        ...
    
    def review(self):
        ...
    
    def finilize(self):
        ...


class DocumentContext(Protocol):
    content: list[str]

    def set_state(self, state: DocumentState) -> None:
        ...
    
    def edit(self):
        ...
    
    def review(self):
        ...
    
    def finilize(self):
        ...
    
    def show_content(self):
        ...


@dataclass
class Draft:
    document: DocumentContext

    def edit(self):
        print("editing content.")
        self.document.content.append("editing content.")
    
    def review(self):
        print("the document is now under review.")
        self.document.set_state(state=Reviewed(document=self.document))

    def finilize(self):
        print("you need to review document the document before finilizing.")


@dataclass
class Reviewed:
    document: DocumentContext

    def edit(self):
        print("the document is under review now, can not editing.")
    
    def review(self):
        print("the document is already reviewed.")

    def finilize(self):
        print("finilizing the document")
        self.document.set_state(state=Finilized(document=self.document))


@dataclass
class Finilized:
    document: DocumentContext

    def edit(self):
        print("the document is finilized, can not editing.")
    
    def review(self):
        print("the document is finilized, can not reviwing.")

    def finilize(self):
        print("the document is already finilized.")


class Document:
    def __init__(self) -> None:
        self.state: DocumentState = Draft(document=self)
        self.content: list[str] = []
    
    def set_state(self, state: DocumentState):
        self.state = state
    
    def edit(self):
        self.state.edit()
    
    def review(self):
        self.state.review()
    
    def finilize(self):
        self.state.finilize()
    
    def show_content(self):
        return " ".join(self.content)

def main():
    document = Document()
    document.edit()
    document.show_content()
    document.finilize()
    document.review()
    document.edit()
    document.finilize()


if __name__ == "__main__":
    main()
